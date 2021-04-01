def preencherInventario(lista):
    resp="S"
    while resp=="S":
        equipamento=[input("Nome: "),
                    float(input("Valor: ")),
                    int(input("Serial: ")),
                    input("Departamento: ")]
        lista.append(equipamento)
        resp=input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for equipamento in lista:
        print("Nome.........:", equipamento[0])
        print("Valor........:", equipamento[1])
        print("Serial.......:", equipamento[2])
        print("Departamento.:", equipamento[3])

def localizarPorNome(lista):
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    for equipamento in lista:
        if busca==equipamento[0]:
            print("Valor..:", equipamento[1])
            print("Serial.:", equipamento[2])

def depreciarPorNome(lista, porc):
    depreciacao=input("Digite o nome do equipamento que será depreciado: ")
    for equipamento in lista:
        if depreciacao==equipamento[0]:
            print("Valor antigo:", equipamento[1])
            equipamento[1]*=(1-porc/100)
            print("Valor novo:", equipamento[1])

def excluirPorSerial(lista):
    serial=int(input("Digite o serial do equipamento danificado: "))
    for equipamento in lista:
        if serial==equipamento[2]:
            lista.remove(equipamento)
    return "Itens excluídos!"

def resumirValores(lista):
    valores=[]
    for equipamento in lista:
        valores.append(equipamento[1])
    if len(valores)>0:
        print("O equipamento mais caro custa:", max(valores))
        print("O equipamento mais barato custa:", min(valores))
        print("O total de equipamentos é de:", sum(valores))