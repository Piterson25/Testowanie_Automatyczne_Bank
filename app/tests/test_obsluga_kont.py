import unittest
import requests


class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "nick",
        "nazwisko": "cave",
        "pesel": "01292909876"
    }

    body_false = {
        "imie": "mike",
        "nazwisko": "baron",
        "pesel": "01292909876"
    }

    body2 = {
        "imie": "bob",
        "nazwisko": "marley"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_tworzenie_istniejacego_konta(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body_false)
        self.assertEqual(create_resp.status_code, 400)
        resp_body = create_resp.json()
        self.assertEqual(resp_body["error"], "Konto z tym peselem juz istnieje")

    def test_3_odczyt_konta(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_4_aktualizacja_konta(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=self.body2)
        self.assertEqual(put_resp.status_code, 200)
        resp_body = put_resp.json()
        self.assertEqual(resp_body["imie"], "bob")
        self.assertEqual(resp_body["nazwisko"], "marley")
        self.assertEqual(resp_body["pesel"], "01292909876")

    def test_5_usuniecie_konta(self):
        delete_resp = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(delete_resp.status_code, 200)

    def test_6_usuniecie_nieistniejacego_konta(self):
        delete_resp = requests.delete(self.url + f"/konta/delete/{self.body['pesel']}")
        self.assertEqual(delete_resp.status_code, 404)
