import csv

class Quantity:
    def __init__(self):
        self.quantity = 0
        self.province = {
            "dolnośląskie" : 0,
            "kujawsko-pomorskie" : 0,
            "lubelskie" : 0,
            "lubuskie" : 0,
            "łódzkie" : 0,
            "małopolskie" : 0,
            "mazowieckie" : 0,
            "opolskie" : 0,
            "podkarpackie" : 0,
            "podlaskie" : 0,
            "pomorskie" : 0,
            "śląskie" : 0,
            "świętokrzyskie" : 0,
            "warmińsko-mazurskie" : 0,
            "wielkopolskie" : 0,
            "zachodniopomorskie" : 0,
        }

class Gender:
    def __init__(self):
        self.exam = {
            "zdało" : Quantity(),
            "przystąpiło" : Quantity(),
        }



class Year:
    def __init__(self):
        self.gender = {
            "kobiety" : Gender(),
            "mężczyźni" : Gender(),
        }

class Results:
    def __init__(self):
        self.years = {
            "2010" : Year(),
            "2011" : Year(),
            "2012" : Year(),
            "2013" : Year(),
            "2014" : Year(),
            "2015" : Year(),
            "2016" : Year(),
            "2017" : Year(),
            "2018" : Year(),
        }

with open('Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv', newline='') as csvfile:
    data = csv.reader(csvfile,delimiter=';')
    results = Results()
    for row in data:
        if row[0] != "Terytorium":
            if row[0] == "Polska":
                results.years[row[3]].gender[row[2].lower()].exam[row[1].lower()].quantity = row[4]
            else:
                results.years[row[3]].gender[row[2].lower()].exam[row[1].lower()].province[row[0].lower()] = row[4]


