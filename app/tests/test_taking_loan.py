import unittest
from ..Konto import Konto
from parameterized import parameterized


class TestTakingLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "72345678912"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([-100, 100, 0, 100, 600], 500, True, 500),
        ([-100000, 100, 100, 100, 600], 500, False, 0),
        ([], 1000, False, 0)
    ])
    def test_zaciaganie_kredytu(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)
