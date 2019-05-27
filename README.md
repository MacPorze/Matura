# Matura
## Aplikacja wyznaczaj¹ca statystyki egzaminu maturalnego
English version below

Jak uruchomiæ aplikacjê?
* Pobierz aplikacjê z portalu github:
[https://github.com/MacPorze/Matura.git](https://github.com/MacPorze/Matura.git)
* Zainstaluj Pythona 3.7 ze strony:
[https://www.python.org/](https://www.python.org/)
* Zainstaluj wymagane biblioteki
'sqlalchemy'

* Uruchom aplikacjê za pomoc¹ terminala:
'python matura.py [komenda] [argumenty]'

##### Dostêpne komendy:
* Wyznacz œredni¹ iloœæ osób bior¹cych udzia³ w egzaminie w danym województwie w danych latach:
'average [województwo] [rok pocz¹tkowy] [rok koñcowy]'
* Wyznacz procentow¹ zdawalnoœæ w danym województwie we wszystkich latach:
'percentage [województwo]'
* ZnajdŸ województwo z najlepsz¹ zdawalnoœci¹ w danym roku:
'pass_rate [rok]'
* ZnajdŸ województwa w których wyst¹pi³a regresja zdawalnoœci w kolejnych latach:
'regression'
* Wyznacz, które wojewodztwo mia³o lepsz¹ zdwalnoœæ we wszystkich latach:
'compare [województwo1] [województwo2]'
* P³eæ - p³eæ jest opcjonalna i mo¿na j¹ umieœciæ jako ostatni argument. Na przyk³ad:
' percentage [województwo] [p³eæ]'

Dostêpne województwa:
* Dolnoœl¹skie
* Kujawsko-pomorskie
* Lubelskie
* Lubuskie
* £ódzkie
* Ma³opolskie
* Mazowieckie
* Opolskie
* Podkarpackie
* Podlaskie
* Pomorskie
* Œl¹skie
* Œwiêtokrzyskie
* Warmiñsko-mazurskie
* Wielkopolskie
* Zachodniopomorskie

Dostêpne lata:
2010-2018

Dostêpne p³cie:
* Kobiety
* Mê¿czyŸni
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
* Dolnoœl¹skie
* Kujawsko-pomorskie
* Lubelskie
* Lubuskie
* £ódzkie
* Ma³opolskie
* Mazowieckie
* Opolskie
* Podkarpackie
* Podlaskie
* Pomorskie
* Œl¹skie
* Œwiêtokrzyskie
* Warmiñsko-mazurskie
* Wielkopolskie
* Zachodniopomorskie

Available years:
2010-2018

Available gender:
* Kobiety
* Mê¿czyŸni