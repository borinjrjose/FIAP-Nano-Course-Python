import os
import json

def carregarJSON(arquivo):
    dicionario={}
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq:
            dicionario=json.load(arq)
    
    return dicionario

def salvarJSON(arquivo, dicionario):
    with open(arquivo, "w") as arq:
        json.dump(dicionario, arq)
        print("Arquivo salvo")