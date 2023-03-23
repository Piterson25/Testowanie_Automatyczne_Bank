import unittest
from unittest.mock import patch
from app.KontoFirmowe import KontoFirmowe
from app.Konto import Konto


class TestAccounting(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678912"
    nazwa = "Zakład Pogrzebowy A.S. Bytom"
    nip = "6262188083"

    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 500 + 100, "Przelew nie dodal srodkow do konta")

    def test_przelew_wychodzacy_wystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 500 - 100, "Konto jest na minusie")

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def test_przelew_wychodzacy_niewystarczajace_srodki(self, mock):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(1000)
        self.assertEqual(konto.saldo, 500, "Konto jest na minusie")

    def test_seria_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(150)
        konto.zaksieguj_przelew_wychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(50)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 500 - 150 - 200 - 50 + 100, "Stan konta nie zgadza sie po serii przelewow")

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def test_seria_przelewow_firma(self, mock):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(150)
        konto.zaksieguj_przelew_wychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(50)
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 500 - 150 - 200 - 50 + 100, "Stan konta nie zgadza sie po serii przelewow")

    def test_przelew_ekspresowy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 500 - 200 - 1, "Stan konta nie zgadza sie po przelewie ekspresowym")

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def test_przelew_ekspresowy_firma(self, mock):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.saldo = 500
        konto.przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 500 - 200 - 5, "Stan konta firmy nie zgadza sie po przelewie ekspresowym")

    def test_przelew_ekspresowy_niewystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.przelew_ekspresowy(500)
        self.assertEqual(konto.saldo, 500 - 500 - 1, "Stan konta nie zgadza sie po przelewie ekspresowym")

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def test_przelew_ekspresowy_niewystarczajace_srodki_firma(self, mock):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.saldo = 500
        konto.przelew_ekspresowy(500)
        self.assertEqual(konto.saldo, 500 - 500 - 5, "Stan konta firmy nie zgadza sie po przelewie ekspresowym")
