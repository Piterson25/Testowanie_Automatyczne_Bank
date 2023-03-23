from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.find_account(dane["pesel"]) is not None:
        return jsonify({"error": "Konto z tym peselem juz istnieje"}), 400
    else:
        konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
        RejestrKont.add_account(konto)
        return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f"Ilośc kont w rejestrze {RejestrKont.accounts()}", 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.find_account(pesel)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_konto(pesel):
    dane = request.get_json()
    print(f"Request o update konta z danymi: {dane}")
    konto = RejestrKont.find_account(pesel)
    print("konto znalezione")
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.saldo
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200


@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def delete(pesel):
    if RejestrKont.delete(pesel):
        return jsonify("Konto zostalo usuniete"), 200
    else:
        return jsonify("Nie ma takiego konta"), 404

