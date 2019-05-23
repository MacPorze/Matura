import pytest
import matura as matura

class TestClass(object):
    def test_one(self):
        province = "pomorskie"
        first = 2013
        last = 2016
        assert matura.average(province,first,last,"brak") == 16103

    def test_two(self):
        province = "warmińsko-mazurskie"
        first = 2010
        last = 2018
        assert matura.average(province,first,last,"brak") == 11047

    def test_three(self):
        province = "wielkopolskie"
        first = 2012
        last = 2014
        gender = "kobiety"
        assert matura.average(province,first,last,gender) == 15801

    def test_four(self):
        province = "mazowieckie"
        first = 2016
        last = 2018
        gender = "mężczyźni"
        assert matura.average(province,first,last,gender) == 17238

    def test_five(self):
        province = "pomorskie"
        gender = "brak"
        result = {
            "2010": 82,
            "2011": 75,
            "2012": 80,
            "2013": 81,
            "2014": 71,
            "2015": 73,
            "2016": 79,
            "2017": 78,
            "2018": 77
        }
        assert matura.percentage(province,gender) == result

