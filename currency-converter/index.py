import requests


def convert(v):
    res = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL").json()[
        "USDBRL"
    ]

    cotação = (float(res["high"]) + float(res["low"])) / 2

    return v * cotação


value = input("Valor: ")

print(convert(float(value)))
