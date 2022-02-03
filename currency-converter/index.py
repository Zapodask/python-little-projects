import requests
import os


class app:
    def __init__(self):
        os.system("cls")

        print("Conversor de moedas")

        value = input("Valor: ")

        res = self.converter(value)

        print(res)

    def converter(self, v):
        res = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()[
            "USDBRL"
        ]

        cotação = (float(res["high"]) + float(res["low"])) / 2

        try:
            return "%.2f" % (float(v) * cotação)
        except:
            return "Valor inválido"


app()
