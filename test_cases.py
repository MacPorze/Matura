import pytest
from matura import Tasks, Validate

class TestClass(object):
    global tasks
    tasks = Tasks()
    global validate
    validate = Validate()

    def test_1(self):
        province = "pomorskie"
        first = "2013"
        last = "2016"
        assert tasks.average(province,first,last,"brak") == 16103

    def test_2(self):
        province = "warmińsko-mazurskie"
        first = "2010"
        last = "2018"
        assert tasks.average(province,first,last,"brak") == 11047

    def test_3(self):
        province = "wielkopolskie"
        first = "2012"
        last = "2014"
        gender = "kobiety"
        assert tasks.average(province,first,last,gender) == 15801

    def test_4(self):
        province = "mazowieckie"
        first = "2016"
        last = "2018"
        gender = "mężczyźni"
        assert tasks.average(province,first,last,gender) == 17238

    def test_5(self):
        province = "pomorskie"
        gender = "kobiety"
        result = {
            "2010": 82,
            "2011": 73,
            "2012": 80,
            "2013": 81,
            "2014": 71,
            "2015": 72,
            "2016": 79,
            "2017": 78,
            "2018": 77
        }
        assert tasks.percentage(province,gender) == result

    def test_6(self):
        province = "zachodniopomorskie"
        gender = "mężczyźni"
        result = {
            "2010": 81,
            "2011": 74,
            "2012": 78,
            "2013": 79,
            "2014": 68,
            "2015": 72,
            "2016": 77,
            "2017": 76,
            "2018": 78
        }
        assert tasks.percentage(province,gender) == result

    def test_7(self):
        province = "podkarpackie"
        gender = "brak"
        result = {
            "2010": 81,
            "2011": 75,
            "2012": 80,
            "2013": 81,
            "2014": 71,
            "2015": 75,
            "2016": 80,
            "2017": 78,
            "2018": 81
        }
        assert tasks.percentage(province,gender) == result

    def test_8(self):
        year = "2010"
        gender = "brak"
        result = "kujawsko-pomorskie"
        assert tasks.pass_rate(year,gender) == result

    def test_9(self):
        year = "2014"
        gender = "brak"
        result = "lubuskie"
        assert tasks.pass_rate(year,gender) == result

    def test_10(self):
        year = "2016"
        gender = "kobiety"
        result = "małopolskie"
        assert tasks.pass_rate(year,gender) == result

    def test_11(self):
        year = "2013"
        gender = "mężczyźni"
        result = "lubuskie"
        assert tasks.pass_rate(year,gender) == result

    def test_12(self):
        province1 = "dolnośląskie"
        province2 = "kujawsko-pomorskie"
        gender = "brak"
        result = {
            "2010": "kujawsko-pomorskie",
            "2011": "kujawsko-pomorskie",
            "2012": "kujawsko-pomorskie",
            "2013": "kujawsko-pomorskie",
            "2014": "kujawsko-pomorskie",
            "2015": "kujawsko-pomorskie",
            "2016": "kujawsko-pomorskie",
            "2017": "kujawsko-pomorskie",
            "2018": "kujawsko-pomorskie"
        }
        assert tasks.compare(province1,province2,gender) == result

    def test_13(self):
        province1 = "świętokrzyskie"
        province2 = "warmińsko-mazurskie"
        gender = "brak"
        result = {
            "2010": "warmińsko-mazurskie",
            "2011": "świętokrzyskie",
            "2012": "warmińsko-mazurskie",
            "2013": "warmińsko-mazurskie",
            "2014": "świętokrzyskie",
            "2015": "świętokrzyskie",
            "2016": "świętokrzyskie",
            "2017": "świętokrzyskie",
            "2018": "świętokrzyskie"
        }
        assert tasks.compare(province1,province2,gender) == result

    def test_14(self):
        province = "pomor567"
        first = "2013"
        last = "2016"
        assert tasks.average(province,first,last,"brak") == False

    def test_15(self):
        gender = "brak"
        assert tasks.regression(gender) == [('dolnośląskie', 2010, '2011'),
                                     ('dolnośląskie', 2013, '2014'),
                                     ('dolnośląskie', 2016, '2017'),
                                     ('kujawsko-pomorskie', 2010, '2011'),
                                     ('kujawsko-pomorskie', 2013, '2014'),
                                     ('kujawsko-pomorskie', 2016, '2017'),
                                     ('lubelskie', 2010, '2011'),
                                     ('lubelskie', 2013, '2014'),
                                     ('lubelskie', 2016, '2017'),
                                     ('lubuskie', 2010, '2011'),
                                     ('lubuskie', 2013, '2014'),
                                     ('lubuskie', 2016, '2017'),
                                     ('lubuskie', 2017, '2018'),
                                     ('łódzkie', 2010, '2011'),
                                     ('łódzkie', 2013, '2014'),
                                     ('łódzkie', 2016, '2017'),
                                     ('łódzkie', 2017, '2018'),
                                     ('małopolskie', 2010, '2011'),
                                     ('małopolskie', 2013, '2014'),
                                     ('mazowieckie', 2010, '2011'),
                                     ('mazowieckie', 2013, '2014'),
                                     ('mazowieckie', 2016, '2017'),
                                     ('opolskie', 2010, '2011'),
                                     ('opolskie', 2013, '2014'),
                                     ('opolskie', 2016, '2017'),
                                     ('podkarpackie', 2010, '2011'),
                                     ('podkarpackie', 2013, '2014'),
                                     ('podkarpackie', 2016, '2017'),
                                     ('podlaskie', 2010, '2011'),
                                     ('podlaskie', 2013, '2014'),
                                     ('podlaskie', 2016, '2017'),
                                     ('pomorskie', 2010, '2011'),
                                     ('pomorskie', 2013, '2014'),
                                     ('pomorskie', 2016, '2017'),
                                     ('pomorskie', 2017, '2018'),
                                     ('śląskie', 2010, '2011'),
                                     ('śląskie', 2013, '2014'),
                                     ('śląskie', 2016, '2017'),
                                     ('świętokrzyskie', 2010, '2011'),
                                     ('świętokrzyskie', 2013, '2014'),
                                     ('świętokrzyskie', 2016, '2017'),
                                     ('warmińsko-mazurskie', 2010, '2011'),
                                     ('warmińsko-mazurskie', 2013, '2014'),
                                     ('warmińsko-mazurskie', 2016, '2017'),
                                     ('wielkopolskie', 2010, '2011'),
                                     ('wielkopolskie', 2013, '2014'),
                                     ('wielkopolskie', 2016, '2017'),
                                     ('zachodniopomorskie', 2010, '2011'),
                                     ('zachodniopomorskie', 2013, '2014'),
                                     ('zachodniopomorskie', 2016, '2017')]

    def test_16(self):
        province = "pomorskie"
        assert validate.check_province(province) == True

    def test_17(self):
        province = "pomors"
        assert validate.check_province(province) == False

    def test_18(self):
        year = "2010"
        assert validate.check_year(year) == True

    def test_19(self):
        year = "2045"
        assert validate.check_year(year) == False

    def test_20(self):
        gender = "kobiety"
        assert validate.check_gender(gender) == True

    def test_21(self):
        gender = "meżczcz"
        assert validate.check_gender(gender) == False