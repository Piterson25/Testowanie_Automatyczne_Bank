import unittest
from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "72345678912"
    kod_rabatowy = "PROM_420"

    def test_tworzenie_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_pesel(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.pesel, self.pesel, "Pesel nie zostal zapisany")

    def test_pesel_zly(self):
        konto = Konto(self.imie, self.nazwisko, "111111")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!", "Pesel jest poprawny, a nie powinien byc")

    def test_kod_rabatowy_dobry(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kod_rabatowy)
        self.assertEqual(konto.saldo, 50, "Saldo sie nie doladowalo, osoba jest urodzona przed 1960")

    def test_kod_rabatowy_zly(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "POOM_000")
        self.assertEqual(konto.saldo, 0, "Saldo sie zwiekszylo bez uzycia kodu")

    def test_kod_rabatowy_brak(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.saldo, 0, "Saldo sie zwiekszylo bez uzycia kodu")

    def test_urodzone_po_1960(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, self.kod_rabatowy)
        self.assertEqual(konto.saldo, 50, "Kupon nie aktywowal sie dla osoby urodzonej po 1960")
