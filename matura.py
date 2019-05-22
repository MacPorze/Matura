import csv
import sys

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

with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline='') as csvfile:
    global results
    data = csv.reader(csvfile,delimiter=';')
    results = Province()
    for row in data:
        if row[0] != "Terytorium":
            results.province[row[0].lower()].years[row[3]].gender[row[2].lower()].exam[row[1].lower()] = int(row[4])

def rate_calculate(province, year, gender):
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

def average(province, first, last, gender):
    sum = 0
    if gender == "brak":
        for i in range(last-first+1):
            sum = sum + results.province[province].years[str(first+i)].gender["kobiety"].exam["przystąpiło"] + results.province[province].years[str(first+i)].gender["mężczyźni"].exam["przystąpiło"]
    else:
        for i in range(last-first+1):
            sum = sum + results.province[province].years[str(first+i)].gender[gender].exam["przystąpiło"]
    ave = sum/(last-first+1)
    return round(ave)

def percentage(province, gender):
    score = {}
    for x in results.province[province].years:
        rate = rate_calculate(province, x, gender)
        score[x] = round(rate*100)
    return score

def pass_rate(year, gender):
    best_rate = 0
    for x in results.province:
        rate = rate_calculate(x, str(year), gender)
        if rate > best_rate:
            best_rate = rate
            province = x

    return province

def regression(gender):
    reg = []
    for x in results.province:
        last_rate = 0
        for y in results.province[x].years:
            rate = rate_calculate(x, y, gender)
            if rate < last_rate and x != "polska":
                reg.append((x,int(y)-1,y))
            last_rate = rate

    return reg

def compare(province1, province2, gender):
    result = {}
    for y in results.province[province1].years:
        rate1 = rate_calculate(province1, y, gender)
        rate2 = rate_calculate(province2, y, gender)

        if rate1 > rate2:
            result[y] = province1
        elif rate1 < rate2:
            result[y] = province2
        else:
            result[y] = "The same"

    return result

def interface():
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

        try:
            gender = sys.argv[5]
        except:
            gender = None

        if province not in results.province:
            print("Nie ma takiego województwa jak: %s" % province)
        elif first not in results.province[province].years:
            if first >= 2020:
                print("Przepraszamy ale nie posiadamy danych z przyszłości :(")
            else:
                print("Nie posiadamy danych z roku: %s" % first)
        elif last not in results.province[province].years:
            if last >= 2020:
                print("Przepraszamy ale nie posiadamy danych z przyszłości :(")
            else:
                print("Nie posiadamy danych z roku: %s" % last)
        elif not(gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
        else:
            if first <= last:
                print("%s(%s-%s) - %s" % (province, first, last, average(province, int(first), int(last), gender)))
            else:
                print("%s(%s-%s) - %s" % (province, last, first, average(province, int(last), int(first), gender)))

    elif argument == "percentage":
        try:
            province = sys.argv[2]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[3]
        except:
            gender = None

        if province not in results.province:
            print("Nie ma takiego województwa jak: %s" % province)
        elif not (gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
        else:
            score = percentage(province,gender)
            for x in score:
                print("%s - %s" % (x, score[x]))

    elif argument == "pass_rate":
        try:
            year = sys.argv[2]
        except:
            print("Brak wystarczającej liczby argumentów!")
            return None

        try:
            gender = sys.argv[3]
        except:
            gender = None

        if year not in results.province["pomorskie"].years:
            if int(year) >= 2020:
                print ("Przepraszamy ale nie posiadamy danych z przyszłości :(")
            else:
                print ("Nie posiadamy danych z roku: %s" % year)
        elif not(gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
        else:
            print("%s - %s" % (year, pass_rate(year, gender)))

    elif argument == "regression":
        try:
            gender = sys.argv[1]
        except:
            gender = None

        if not(gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
        else:
            reg = regression(gender)
            for x in reg:
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

        if province1 not in results.province:
            print("Nie ma takiego województwa jak: %s" % province1)
        elif province2 not in results.province:
            print("Nie ma takiego województwa jak: %s" % province2)
        elif not(gender == "kobiety" or gender == "mężczyźni" or gender == "brak"):
            print("Nie ma takiej płci jak: %s" % gender)
        else:
            com = compare(province1, province2,gender)
            for x in com:
                print("%s - %s" % (x, com[x]))

    else:
        "Niepoprawna komenda"

    return None

if __name__ == '__main__':
    interface()

