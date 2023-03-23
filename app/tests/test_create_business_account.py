import unittest
from unittest.mock import patch
from app.KontoFirmowe import KontoFirmowe


class TestCreateBusinessAccount(unittest.TestCase):
    nazwa = "Zakład Pogrzebowy A.S. Bytom"
    nip = "6262188083"

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=True)
    def test_tworzenie_konta_firmowego(self, mock):
        konto = KontoFirmowe(self.nazwa, self.nip)
        self.assertEqual(konto.nazwa, "Zakład Pogrzebowy A.S. Bytom", "Nazwa nie została zapisana!")
        self.assertEqual(konto.nip, "6262188083", "NIP nie został został zapisany!")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest zerowe!")

    @patch('app.KontoFirmowe.KontoFirmowe.request_do_api', return_value=False)
    def test_zly_nip(self, mock):
        konto = KontoFirmowe(self.nazwa, "12345")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "Zly NIP zostal zaakceptowany")
