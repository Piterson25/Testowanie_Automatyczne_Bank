# Testowanie Automatyczne Bank

🏦 Projekt Testowania Automatycznego Banku napisany w Pythonie z użyciem Flask, unittest, mock, requests, json. Testy były pisane przed implementacją kodu.

## 🛠️ Wykorzystane technologie
Projekt Testowania Automatycznego Banku został zrealizowany z wykorzystaniem następujących technologii:

* Python
* Flask
* unittest
* mock
* requests
* json

## 🚀 Uruchomienie
Aby uruchomić aplikację należy:
1. Uruchomić Flask: ```export FLASK_APP=app/api.py``` oraz ```python3 -m flask run```
2. Uruchomić testy: ```python3 -m unittest app/tests/test_obsluga_kont.py```
3. Zewnętrzne API: ```export BANK_APP_MF_URL="https://wl-api.mf.gov.pl/api/search/nip/"```

## 🎉 Funkcjonalności
Aplikacja służy do obsługi banku i umożliwia między innymi:
### Dodawanie kont
* Dodawanie kont firmowych i indywidualnych.

### Sprawdzanie różnych kryteriów
* Sprawdzanie stanu konta.
* Sprawdzanie historii transakcji.
* Sprawdzanie peselu i kodów rabatowych.

### Kontakt z zewnętrznym API
* Kontakt z API Ministerstwa Finansów w celu pobrania danych o firmie na podstawie numeru NIP.

### Wyświetlanie historii
* Wyświetlanie historii transakcji dla danego konta.

## 🧪 Testy
Projekt zawiera testy jednostkowe, integracyjne oraz akceptacyjne. Aby uruchomić testy należy użyć komend:

* ```python3 -m unittest```
* ```python3 -m coverage run -m unittest```
* ```python3 -m coverage report```
* ```python3 -m coverage html```

## Licencja
Projekt Testowania Automatycznego Banku objęty jest licencją MIT. Więcej informacji znajduje się w pliku [LICENSE](https://github.com/Piterson25/Testowanie_Automatyczne_Bank/blob/main/LICENSE).
