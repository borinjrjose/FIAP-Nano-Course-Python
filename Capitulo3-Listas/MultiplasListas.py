equipamentos=[]
valores=[]
seriais=[]
deptos=[]
resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    deptos.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos), 1):
    print("Equipamento..:", indice+1)
    print("Nome.........:", equipamentos[indice])
    print("Valor........:", valores[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.:", deptos[indice])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos), 1):
    if busca==equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Serial.:", seriais[indice])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos), 1):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo:", valores[indice])
        valores[indice]*=0.9
        print("Valor novo:", valores[indice])

eliminado=int(input("Digite o serial do equipamento danificado: "))
for indice in range(0, len(equipamentos), 1):
    if eliminado==seriais[indice]:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]
        del deptos[indice]
        break

for indice in range(0, len(equipamentos), 1):
    print("Equipamento..:", indice+1)
    print("Nome.........:", equipamentos[indice])
    print("Valor........:", valores[indice])
    print("Serial.......:", seriais[indice])
    print("Departamento.:", deptos[indice])