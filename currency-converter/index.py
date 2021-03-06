import json
import requests
import os


class app:
    options = {}
    names = {}

    # Selecionando as moedas
    with open("list.json", "r", encoding="utf-8") as f:
        options = json.loads(f.read())

    # Selecionando os nomes das moedas
    with open("names.json", "r", encoding="utf-8") as f:
        names = json.loads(f.read())

    def __init__(self):
        os.system("cls")

        print("Conversor de moedas")

        # Listar moedas
        for k, _ in self.options.items():
            print(f"{self.names[k]}: {k}")

        # Receber moeda válida
        while True:
            f = input("Escolha uma das moedas acima da qual quer converter: ")

            if f in self.options:
                break
            else:
                print("Escolha uma moeda válida")

        # Listar moedas disponiveis
        for i in self.options[f]:
            print(f"{self.names[i]}: {i}")

        # Receber moeda para qual converter válida
        while True:
            t = input("Escolha uma das moedas acima para qual quer converter: ")

            if t in self.options[f]:
                break
            else:
                print("Escolha uma moeda válida")

        # Receber valor válido
        while True:
            v = input("Valor: ")

            try:
                float(v)

                break
            except:
                print("Escolha um valor válido")

        res = self.converter(float(v), f, t)

        print(res)

    def converter(self, v, f, t):
        """Converter moedas

        Args:
            v (float): Valor a converter
            f (string): Moeda que quer converter
            t (string): Moeda para qual converter

        Returns:
            float: Valor convertido
            string: Valor inválido
        """
        res = requests.get(f"https://economia.awesomeapi.com.br/last/{f}-{t}").json()[
            f"{f}{t}"
        ]

        cotação = (float(res["high"]) + float(res["low"])) / 2

        try:
            return "%.2f" % (float(v) * cotação)
        except:
            return "Valor inválido"


app()
