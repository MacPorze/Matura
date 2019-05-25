# -*- coding: utf-8 -*-
import csv
import sys
import io
import urllib.request as request
from db_service import Data, read_db, write_db, create_db


class Province:
    def __init__(self):
        self.province = {
            "polska" : Year(),
            "dolnośląskie" : Year(),
            "kujawsko-pomorskie" : Year(),
            "lubelskie" : Year(),
            "lubuskie" : Year(),
            "łódzkie" : Year(),
            "małopolskie" : Year(),
            "mazowieckie" : Year(),
            "opolskie" : Year(),
            "podkarpackie" : Year(),
            "podlaskie" : Year(),
            "pomorskie" : Year(),
            "śląskie" : Year(),
            "świętokrzyskie" : Year(),
            "warmińsko-mazurskie" : Year(),
            "wielkopolskie" : Year(),
            "zachodniopomorskie" : Year(),
        }

class Exam:
    def __init__(self):
        self.exam = {
            "zdało" : 0,
            "przystąpiło" : 0,
        }

class Gender:
    def __init__(self):
        self.gender = {
            "kobiety" : Exam(),
            "mężczyźni" : Exam(),
        }

class Year:
    def __init__(self):
        self.years = {
            "2010" : Gender(),
            "2011" : Gender(),
            "2012" : Gender(),
            "2013" : Gender(),
            "2014" : Gender(),
            "2015" : Gender(),
            "2016" : Gender(),
            "2017" : Gender(),
            "2018" : Gender(),
        }

def read_data(csvfile):
    global results
    data = csv.reader(csvfile, delimiter=';')
    results = Province()
    db_data = []
    for row in data:
        if row[0] != "Terytorium":
            db_data.append(Data(province=row[0].lower(), passed=row[1].lower(), gender=row[2].lower(), year=row[3], value=row[4]))
            results.province[row[0].lower()].years[row[3]].gender[row[2].lower()].exam[row[1].lower()] = int(row[4])
    write_db(db_data)

def read_from_file():
    with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline='') as csvfile:
        read_data(csvfile)

def read_from_api():
    with request.urlopen(
            "https://www.dane.gov.pl/media/resources/20190520/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv") as response:
        bytes_data = io.BytesIO(response.read())
        csvfile = io.TextIOWrapper(bytes_data, encoding='windows-1250')
        read_data(csvfile)

def check_province(province):
    if province not in results.province:
        print("Nie ma takiego województwa jak: %s" % province)
        return False
    else: return True

def check_year(year):
    if year not in results.province["polska"].years:
        if year >= 2020:
            print("Przepraszamy ale nie posiadamy danych z przyszłości :(")
        else:
            print("Nie posiadamy danych z roku: %s" % year)
        return False
    else: return True

def check_gender(gender):
    if not (gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
        print("Nie ma takiej płci jak: %s" % gender)
        return False
    else: return True

class Tasks:
    def __init__(self):
        read_from_api()

    def __rate_calculate(self,province, year, gender):
        if gender == "brak":
            passed = results.province[province].years[year].gender["kobiety"].exam["zdało"] + \
                     results.province[province].years[year].gender["mężczyźni"].exam["zdało"]
            tooked = results.province[province].years[year].gender["kobiety"].exam["przystąpiło"] + \
                     results.province[province].years[year].gender["mężczyźni"].exam["przystąpiło"]
        else:
            passed = results.province[province].years[year].gender[gender].exam["zdało"]
            tooked = results.province[province].years[year].gender[gender].exam["przystąpiło"]
        rate = passed / tooked
        return rate

    def average(self,province, first, last, gender):
        sum = 0
        if check_province(province) and check_year(first) and check_year(last) and check_gender(gender):
            first = int(first)
            last = int(last)
            query = Data.year
            read_db(query,Data.province==province)
            if gender == "brak":
                for i in range(last-first+1):
                    sum = sum + results.province[province].years[str(first+i)].gender["kobiety"].exam["przystąpiło"] + results.province[province].years[str(first+i)].gender["mężczyźni"].exam["przystąpiło"]
            else:
                for i in range(last-first+1):
                    sum = sum + results.province[province].years[str(first+i)].gender[gender].exam["przystąpiło"]
            ave = sum/(last-first+1)
            return round(ave)
        else: return False

    def percentage(self,province, gender):
        if check_province(province) and check_gender(gender):
            score = {}
            for x in results.province[province].years:
                rate = self.__rate_calculate(province, x, gender)
                score[x] = round(rate*100)
            return score
        else: return False

    def pass_rate(self,year, gender):
        if check_year(year) and check_gender(gender):
            best_rate = 0
            for x in results.province:
                rate = self.__rate_calculate(x, str(year), gender)
                if rate > best_rate:
                    best_rate = rate
                    province = x

            return province
        else: return False

    def regression(self,gender):
        if check_gender(gender):
            reg = []
            for x in results.province:
                last_rate = 0
                for y in results.province[x].years:
                    rate = self.__rate_calculate(x, y, gender)
                    if rate < last_rate and x != "polska":
                        reg.append((x,int(y)-1,y))
                    last_rate = rate

            return reg
        else: return False

    def compare(self,province1, province2, gender):
        if check_province(province1) and check_province(province2) and check_gender(gender):
            result = {}
            for y in results.province[province1].years:
                rate1 = self.__rate_calculate(province1, y, gender)
                rate2 = self.__rate_calculate(province2, y, gender)

                if rate1 > rate2:
                    result[y] = province1
                elif rate1 < rate2:
                    result[y] = province2
                else:
                    result[y] = "The same"

            return result
        else: return False

def interface():
    try:
        argument = sys.argv[1]
    except:
        print("Brak wystarczającej liczby argumentów!")
        return None
    tasks = Tasks()

    if argument == "average":
        try:
            province = sys.argv[2]
            first = sys.argv[3]
            last = sys.argv[4]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[5]
        except:
            gender = "brak"

        if first <= last:
            result = tasks.average(province, first, last, gender)
        else:
            result = tasks.average(province, last, first, gender)

        if result:
            print("%s(%s-%s) - %s" % (province, first, last, result))

    elif argument == "percentage":
        try:
            province = sys.argv[2]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[3]
        except:
            gender = "brak"

        score = tasks.percentage(province,gender)
        if score:
            for x in score:
                print("%s - %s%s" % (x, score[x],u"\u0025"))

    elif argument == "pass_rate":
        try:
            year = sys.argv[2]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[3]
        except:
            gender = "brak"

        result = tasks.pass_rate(year, gender)
        if result:
            print("%s - %s" % (year, result))

    elif argument == "regression":
        try:
            gender = sys.argv[1]
        except:
            gender = "brak"

        result = tasks.regression(gender)
        if result:
            for x in result:
                print ("%s: %s -> %s" % (x[0],x[1],x[2]))

    elif argument == "compare":
        try:
            province1 = sys.argv[2]
            province2 = sys.argv[3]
        except:
            print ("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[4]
        except:
            gender = "brak"

        result = tasks.compare(province1, province2, gender)
        if result:
            for x in result:
                print("%s - %s" % (x, result[x]))

    else:
        "Niepoprawna komenda"

    return None

if __name__ == '__main__':
    interface()

