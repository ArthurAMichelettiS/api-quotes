
"""
Arthur Augusto Micheletti de Souza
081180004

Ao executar cria o arquivo com 30 citações
"""

import requests

try:
    resp = requests.get("https://quote-garden.herokuapp.com/api/v2/quotes?page=1&limit=30")
    quotes = resp.json()["quotes"]

    with open("quotes.tsv", "w") as txt:
        txt.write("\t".join(["id", "Citação", "Autor"]) + "\n")

        for qt in quotes:
            line = "\t".join(qt.values())
            txt.write(line + "\n")

        txt.close()
    print("Citações salvas com sucesso")
except:
    print("Erro ao conectar com API")
