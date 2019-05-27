# -*- coding: utf-8 -*-
import csv
import sys
import io
import urllib.request as request
from db_service import Data, Service

global database_usage
database_usage = False

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

class Reader:
    def read_data(self, csv_file):  #reading data and inserting to database or object
        data = csv.reader(csv_file, delimiter=';')
        if database_usage:
            db_data = []
            service = Service()
            for row in data:
                if row[0] != "Terytorium":
                    db_data.append(Data(province=row[0].lower(), passed=row[1].lower(), gender=row[2].lower(),
                                        year=row[3], value=row[4]))
            service.write_db(db_data)
            return None
        else:
            results = Province()
            for row in data:
                if row[0] != "Terytorium":
                    results.province[row[0].lower()].years[row[3]].gender[row[2].lower()].exam[row[1].lower()] = int(row[4])
            return results

    def read_from_file(self):   #reading data from local csv file
        with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline='') as csv_file:
            return self.read_data(csv_file)

    def read_from_api(self):    #reading data from web api
        with request.urlopen(
                "https://www.dane.gov.pl/media/resources/20190520/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv") as response:
            bytes_data = io.BytesIO(response.read())
            csv_file = io.TextIOWrapper(bytes_data, encoding='windows-1250')
            return self.read_data(csv_file)

class Validate:     #Class wich validates if given data is correct
    def __init__(self):
        self.province_pattern = Province()
        self.year_pattern = Year()
        self.gender_pattern = Gender()

    def check_province(self, province):     #check if given province is correct
        if province not in self.province_pattern.province:
            print("Nie ma takiego województwa jak: %s" % province)
            print("Dostępne województwa:")
            for x in self.province_pattern.province:
                print(x.capitalize())
            return False
        else: return True

    def check_year(self, year):     #check if given year is correct
        if year not in self.year_pattern.years:
            if int(year) >= 2020:
                print("Przepraszamy ale nie posiadamy danych z przyszłości :(")
            else:
                print("Nie posiadamy danych z roku: %s" % year)
            print("Dostępne lata:")
            for x in self.year_pattern.years:
                print(x)
            return False
        else: return True

    def check_gender(self, gender):     #check if given gender is correct
        if not (gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
            print("Dostępne płcie:")
            for x in self.gender_pattern.gender:
                print(x)
            return False
        else: return True

class Tasks:
    def __init__(self):
        self.validate = Validate()
        self.reader = Reader()
        self.results = Province()
        self.service = Service()
        if not database_usage:
            self.results = self.reader.read_from_api()

    def __rate_calculate(self,province, year, gender):      #private method wich calculates rate for given arguments
        passed = tooked = 0
        if gender == "brak":
            if database_usage:
                passed_value, tooked_value = self.service.read_db(2, province, year)
                for value, in passed_value:
                    passed += value
                for value, in tooked_value:
                    tooked += value
            else:
                passed = self.results.province[province].years[year].gender["kobiety"].exam["zdało"] + \
                         self.results.province[province].years[year].gender["mężczyźni"].exam["zdało"]
                tooked = self.results.province[province].years[year].gender["kobiety"].exam["przystąpiło"] + \
                         self.results.province[province].years[year].gender["mężczyźni"].exam["przystąpiło"]
        else:
            if database_usage:
                passed_value, tooked_value = self.service.read_db(2, province, year, gender)
                for value, in passed_value:
                    passed += value
                for value, in tooked_value:
                    tooked += value
            else:
                passed = self.results.province[province].years[year].gender[gender].exam["zdało"]
                tooked = self.results.province[province].years[year].gender[gender].exam["przystąpiło"]
        rate = passed / tooked
        return rate

    def average(self,province, first, last, gender):        #Method wich calculates average value of people toked exam in given province i given years range
        sum = 0
        if self.validate.check_province(province) and self.validate.check_year(first) and \
                self.validate.check_year(last) and self.validate.check_gender(gender):
            first = int(first)
            last = int(last)
            if gender == "brak":
                if database_usage:
                    for value, in self.service.read_db(1, province, first, last):
                        sum += value
                else:
                    for i in range(last-first+1):
                        sum += self.results.province[province].years[str(first+i)].gender["kobiety"].exam["przystąpiło"]\
                               + self.results.province[province].years[str(first+i)].gender["mężczyźni"].exam["przystąpiło"]
            else:
                if database_usage:
                    for value, in self.service.read_db(1,province, first, last, gender):
                        sum += value
                else:
                    for i in range(last-first+1):
                        sum += self.results.province[province].years[str(first+i)].gender[gender].exam["przystąpiło"]
            ave = sum/(last-first+1)
            return round(ave)
        else: return False

    def percentage(self, province, gender):     #Method wich calculate percentage of passed exams in given province
        if self.validate.check_province(province) and self.validate.check_gender(gender):
            result = {}
            for x in self.validate.year_pattern.years:
                rate = self.__rate_calculate(province, x, gender)
                result[x] = round(rate*100)
            return result
        else: return False

    def pass_rate(self, year, gender):      #Method wich search for province with best pass rate in given year
        if self.validate.check_year(year) and self.validate.check_gender(gender):
            best_rate = 0
            for x in self.validate.province_pattern.province:
                rate = self.__rate_calculate(x, str(year), gender)
                if rate > best_rate:
                    best_rate = rate
                    province = x

            return province
        else: return False

    def regression(self, gender):       #Method wich searchs for regression in following years
        if self.validate.check_gender(gender):
            reg = []
            for x in self.validate.province_pattern.province:
                last_rate = 0
                for y in self.validate.year_pattern.years:
                    rate = self.__rate_calculate(x, y, gender)
                    if rate < last_rate and x != "polska":
                        reg.append((x,int(y)-1,y))
                    last_rate = rate
            print(reg)
            return reg
        else: return False

    def compare(self, province1, province2, gender):        #Method wich compares results of two provinces
        if self.validate.check_province(province1) and self.validate.check_province(province2) and \
                self.validate.check_gender(gender):
            result = {}
            for y in self.validate.year_pattern.years:
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

    def get_gender(self):       #getting gender from terminal
        try:
            gender = sys.argv[5]
        except:
            gender = "brak"
        return gender

    def interface(self):        #Terminal interface
        try:
            argument = sys.argv[1]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        if argument == "average":
            try:
                province = sys.argv[2]
                first = sys.argv[3]
                last = sys.argv[4]
            except:
                print("Brak wystarczającej liczby argumentów!")
                return None

            gender = self.get_gender()

            if first <= last:
                result = self.average(province, first, last, gender)
            else:
                result = self.average(province, last, first, gender)

            if result:
                print("%s(%s-%s) - %s" % (province.capitalize(), first, last, result))

        elif argument == "percentage":
            try:
                province = sys.argv[2]
            except:
                print("Brak wystarczającej liczby argumentów!")
                return None

            gender = self.get_gender()

            score = self.percentage(province,gender)
            if score:
                for x in score:
                    print("%s - %s%s" % (x, score[x],u"\u0025"))

        elif argument == "pass_rate":
            try:
                year = sys.argv[2]
            except:
                print("Brak wystarczającej liczby argumentów!")
                return None

            gender = self.get_gender()

            result = self.pass_rate(year, gender)
            if result:
                print("%s - %s" % (year, result))

        elif argument == "regression":
            gender = self.get_gender()

            result = self.regression(gender)
            if result:
                for x in result:
                    print ("%s: %s -> %s" % (x[0].capitalize(),x[1],x[2]))

        elif argument == "compare":
            try:
                province1 = sys.argv[2]
                province2 = sys.argv[3]
            except:
                print ("Brak wystarczającej liczby argumentów!")
                return None

            gender = self.get_gender()

            result = self.compare(province1, province2, gender)
            if result:
                for x in result:
                    print("%s - %s" % (x.capitalize(), result[x]))

        elif argument == "download":
            try:
                source = sys.argv[2]
            except:
                print ("Brak wystarczającej liczby argumentów")
                return None

            if source == "file":
                self.reader.read_from_file()
            elif source == "api":
                self.reader.read_from_api()

        else:
            print("Niepoprawna komenda")

        return None

if __name__ == '__main__':
    tasks = Tasks()
    tasks.interface()

