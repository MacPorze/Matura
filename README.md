# Matura
## Aplikacja wyznaczaj�ca statystyki egzaminu maturalnego
English version below

Jak uruchomi� aplikacj�?
* Pobierz aplikacj� z portalu github:
[https://github.com/MacPorze/Matura.git](https://github.com/MacPorze/Matura.git)
* Zainstaluj Pythona 3.7 ze strony:
[https://www.python.org/](https://www.python.org/)
* Zainstaluj wymagane biblioteki
'sqlalchemy'

* Uruchom aplikacj� za pomoc� terminala:
'python matura.py [komenda] [argumenty]'

##### Dost�pne komendy:
* Wyznacz �redni� ilo�� os�b bior�cych udzia� w egzaminie w danym wojew�dztwie w danych latach:
'average [wojew�dztwo] [rok pocz�tkowy] [rok ko�cowy]'
* Wyznacz procentow� zdawalno�� w danym wojew�dztwie we wszystkich latach:
'percentage [wojew�dztwo]'
* Znajd� wojew�dztwo z najlepsz� zdawalno�ci� w danym roku:
'pass_rate [rok]'
* Znajd� wojew�dztwa w kt�rych wyst�pi�a regresja zdawalno�ci w kolejnych latach:
'regression'
* Wyznacz, kt�re wojewodztwo mia�o lepsz� zdwalno�� we wszystkich latach:
'compare [wojew�dztwo1] [wojew�dztwo2]'
* P�e� - p�e� jest opcjonalna i mo�na j� umie�ci� jako ostatni argument. Na przyk�ad:
' percentage [wojew�dztwo] [p�e�]'

Dost�pne wojew�dztwa:
* Dolno�l�skie
* Kujawsko-pomorskie
* Lubelskie
* Lubuskie
* ��dzkie
* Ma�opolskie
* Mazowieckie
* Opolskie
* Podkarpackie
* Podlaskie
* Pomorskie
* �l�skie
* �wi�tokrzyskie
* Warmi�sko-mazurskie
* Wielkopolskie
* Zachodniopomorskie

Dost�pne lata:
2010-2018

Dost�pne p�cie:
* Kobiety
* M�czy�ni
----------------------------------------------------------------------------------------------
# Matura
## Application wich give exams statistics

How to run application?
* Download application from github:
[https://github.com/MacPorze/Matura.git](https://github.com/MacPorze/Matura.git)
* Install Python 3.7 from page:
[https://www.python.org/](https://www.python.org/)
* Download required packages
'sqlalchemy'

* Run application using terminal
'python matura.py [command] [arguments]'

##### Aviable commands:
* calculate average number of people tooked part in exam
'average [province] [start year] [end year]'
* calculate percentage pass rate in every year in given province
'percentage [province]'
* search for province where was the best pass rate in given year
'pass_rate [year]'
* search for province where was regression in following years
'regression'
* compare wich province has better pass rate
'compare [province1] [province2]'
* gender - gender is optional and it can be put as a last argument. For example:
' percentage [province] [gender]'

Available provinces:
* Dolno�l�skie
* Kujawsko-pomorskie
* Lubelskie
* Lubuskie
* ��dzkie
* Ma�opolskie
* Mazowieckie
* Opolskie
* Podkarpackie
* Podlaskie
* Pomorskie
* �l�skie
* �wi�tokrzyskie
* Warmi�sko-mazurskie
* Wielkopolskie
* Zachodniopomorskie

Available years:
2010-2018

Available gender:
* Kobiety
* M�czy�ni