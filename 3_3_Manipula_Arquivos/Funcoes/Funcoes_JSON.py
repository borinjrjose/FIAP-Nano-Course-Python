import os
import json

def carregarInventario(arquivo):
    dicionario={}
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq:
            dicionario=json.load(arq)
    return dicionario

def perguntar():
    return int(input("Digite:\n"+
    "<1> para registrar ativo\n"+
    "<2> para exibir ativos armazenados: "))

def registrarAtivo(dicionario, arquivo):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ").upper()
        ]
        resp=input("Digite <S> para continuar: ").upper()
    with open(arquivo, "w") as arq:
        json.dump(dicionario, arq)
        print("JSON salvo!!!")

def exibirAtivos(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq:
            dicionario=json.load(arq)
            for valor in dicionario.values():
                print("Data.........:", valor[0])
                print("Descrição....:", valor[1])
                print("Departamento.:", valor[2], "\n")
    else:
        print("Erro: Arquivo não existe!!!")