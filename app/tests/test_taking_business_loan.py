import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe
from parameterized import parameterized


class TestTakingBusinessLoan(unittest.TestCase):
    nazwa = "Zakład Pogrzebowy A.S. Bytom"
    nip = "6262188083"

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def setUp(self, mock):
        self.kontoFirmowe = KontoFirmowe(self.nazwa, self.nip)

    @parameterized.expand([
        ([-1775, 2000, 50000], 52000, 10000, True, 62000),
        ([-1775, 4000], 4000, 2000, True, 6000),
        ([1000, 500], 1500, 500, False, 1500),
        ([-1775, 2000], 2000, 1700, False, 2000),
        ([], 500, 100, False, 500)
    ])
    def test_kredyt_firmowy(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.kontoFirmowe.historia = historia
        self.kontoFirmowe.saldo = saldo
        czy_przyznany = self.kontoFirmowe.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.kontoFirmowe.saldo, oczekiwane_saldo)
