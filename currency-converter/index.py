import json
import requests
import os


class app:
    options = {}

    with open("list.json", "r", encoding="utf-8") as f:
        options = json.loads(f.read())

    def __init__(self):
        os.system("cls")

        print("Conversor de moedas")

        v = input("Valor: ")

        for k, _ in self.options.items():
            print(k)

        f = input("Escolha uma das moedas acima da qual quer converter: ")

        for i in self.options[f]:
            print(i)

        t = input("Escolha uma das moedas acima para qual quer converter: ")

        res = self.converter(float(v), f, t)

        print(res)

    def converter(self, v, f, t):
        res = requests.get(f"https://economia.awesomeapi.com.br/last/{f}-{t}").json()[
            f"{f}{t}"
        ]

        cotação = (float(res["high"]) + float(res["low"])) / 2

        try:
            return "%.2f" % (float(v) * cotação)
        except:
            return "Valor inválido"


app()
