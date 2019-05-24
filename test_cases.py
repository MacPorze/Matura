import pytest
import matura as matura

class TestClass(object):
    def test_1(self):
        province = "pomorskie"
        first = 2013
        last = 2016
        assert matura.average(province,first,last,"brak") == 16103

    def test_2(self):
        province = "warmińsko-mazurskie"
        first = 2010
        last = 2018
        assert matura.average(province,first,last,"brak") == 11047

    def test_3(self):
        province = "wielkopolskie"
        first = 2012
        last = 2014
        gender = "kobiety"
        assert matura.average(province,first,last,gender) == 15801

    def test_4(self):
        province = "mazowieckie"
        first = 2016
        last = 2018
        gender = "mężczyźni"
        assert matura.average(province,first,last,gender) == 17238

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
        assert matura.percentage(province,gender) == result

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
        assert matura.percentage(province,gender) == result

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
        assert matura.percentage(province,gender) == result

    def test_8(self):
        year = "2010"
        gender = "brak"
        result = "kujawsko-pomorskie"
        assert matura.pass_rate(year,gender) == result

    def test_9(self):
        year = "2014"
        gender = "brak"
        result = "lubuskie"
        assert matura.pass_rate(year,gender) == result

    def test_10(self):
        year = "2016"
        gender = "kobiety"
        result = "małopolskie"
        assert matura.pass_rate(year,gender) == result

    def test_11(self):
        year = "2013"
        gender = "mężczyźni"
        result = "lubuskie"
        assert matura.pass_rate(year,gender) == result

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
        assert matura.compare(province1,province2,gender) == result

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
        assert matura.compare(province1,province2,gender) == result