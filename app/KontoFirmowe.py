from app.Konto import Konto
from datetime import date
import requests
import os


class KontoFirmowe(Konto): # pragma: no cover
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.sprawdz_nip(nip)
        self.historia = []

    def sprawdz_nip(self, nip):
        if len(nip) == 10:
            if self.czy_nip_istnieje(nip) is None:
                self.nip = "Pranie!"
            else:
                self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

    def zaciagnij_kredyt(self, kwota):
        if -1775 in self.historia and self.saldo >= kwota * 2:
            self.zaksieguj_przelew_przychodzacy(kwota)
            return True
        return False

    @classmethod
    def czy_nip_istnieje(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        data = date.today()
        url = f"{gov_url}api/search/nip/{nip}?date={data}"
        return cls.request_do_api(url)

    @classmethod
    def request_do_api(cls, url):
        return requests.get(url).status_code == 200

    def wyslij_historie_na_maila(self, mail, smtp_connector):
        temat = f"Wyciąg z dnia {date.today()}"
        tresc = f"Historia konta firmowego: {self.historia}"
        return smtp_connector.wyslij(temat, tresc, mail)
