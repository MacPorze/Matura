import csv

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

    print(results)

def rate_calculate(province, year):
    passed = results.province[province].years[year].gender["kobiety"].exam["zdało"] + \
             results.province[province].years[year].gender["mężczyźni"].exam["zdało"]
    tooked = results.province[province].years[year].gender["kobiety"].exam["przystąpiło"] + \
             results.province[province].years[year].gender["mężczyźni"].exam["przystąpiło"]
    rate = passed / tooked
    return rate


def average(province,first, last):
    sum = 0
    for i in range(last-first+1):
        print(i)
        sum = sum + results.province[province].years[str(first+i)].gender["kobiety"].exam["przystąpiło"] + results.province[province].years[str(first+i)].gender["mężczyźni"].exam["przystąpiło"]
    ave = sum/(last-first+1)
    return ave

def percentage(province):
    score = {}
    for x in results.province[province].years:
        rate = rate_calculate(province,x)
        score[x] = rate*100
    return score

def pass_rate(year):
    best_rate = 0
    for x in results.province:
        rate = rate_calculate(x, str(year))
        if rate > best_rate:
            best_rate = rate
            province = x

    return province

def regression():
    reg = {}
    for x in results.province:
        last_rate = 0
        for y in results.province[x].years:
            rate = rate_calculate(x,y)
            if rate < last_rate and x != "polska":
                reg[x] = (int(y)-1,y)
            last_rate = rate

    return reg

def compare(province1,province2):
    result = {}
    for y in results.province[province1].years:
        rate1 = rate_calculate(province1,y)
        rate2 = rate_calculate(province2,y)

        if rate1 > rate2:
            result[y] = province1
        elif rate1 < rate2:
            result[y] = province2
        else:
            result[y] = "The same"

    return result
print(compare("pomorskie","mazowieckie"))

