import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont


class TestAccountRegister(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "72345678912"

    @classmethod
    def setUpClass(cls):
        RejestrKont.add_account(Konto(cls.imie, cls.nazwisko, cls.pesel))

    def test_1_znajdz_konto(self):
        peselek = "72345678912"
        konto = RejestrKont.find_account(peselek)
        self.assertEqual(konto.pesel, peselek)

    def test_2_znajdz_nieistniejace_konto(self):
        peselek = "12345678910"
        konto = RejestrKont.find_account(peselek)
        self.assertEqual(konto, None)

    def test_3_dodawanie_drugiego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.add_account(konto)
        self.assertEqual(RejestrKont.accounts(), 2)

    def test_4_dodawanie_trzeciego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.add_account(konto)
        self.assertEqual(RejestrKont.accounts(), 3)

    def test_5_usuwanie_konta(self):
        usuniete = RejestrKont.delete(self.pesel)
        self.assertEqual(usuniete, True)

        RejestrKont.konta = []
        usuniete = RejestrKont.delete(self.pesel)
        self.assertIsNone(usuniete)


    @classmethod
    def tearDownClass(cls):
        RejestrKont.konta = []

