import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

class TestNipValidation(unittest.TestCase):
    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=True)
    def test_1_prawidlowy_nip(self, mock):
        konto_firmowe = KontoFirmowe("Jakub", "4214214941")
        self.assertEqual(konto_firmowe.nip, "4214214941")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=None)
    def test_2_nieprawidlowy_nip(self, mock):
        konto_firmowe = KontoFirmowe("Arek", "0000000000")
        self.assertEqual(konto_firmowe.nip, "Pranie!")
