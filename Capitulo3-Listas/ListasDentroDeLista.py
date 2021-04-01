inventario=[]
resposta="S"
while resposta=="S":
    equipamento=[input("Nome: "),
                float(input("Valor: ")),
                int(input("Serial: ")),
                input("Departamento: ")]
    inventario.append(equipamento)
    resposta=input("Digite \"S\" para continuar: ").upper()

for equipamento in inventario:
    print("Nome.........:", equipamento[0])
    print("Valor........:", equipamento[1])
    print("Serial.......:", equipamento[2])
    print("Departamento.:", equipamento[3])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for equipamento in inventario:
    if equipamento[0]==busca:
        print("Valor..:", equipamento[1])
        print("Serial.:", equipamento[2])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for equipamento in inventario:
    if equipamento[0]==depreciacao:
        print("Valor antigo:", equipamento[1])
        equipamento[1]*=0.9
        print("Valor novo:", equipamento[1])

serial=int(input("Digite o serial do equipamento danificado: "))
for equipamento in inventario:
    if equipamento[2]==serial:
        inventario.remove(equipamento)

for equipamento in inventario:
    print("Nome.........:", equipamento[0])
    print("Valor........:", equipamento[1])
    print("Serial.......:", equipamento[2])
    print("Departamento.:", equipamento[3])

valores=[]
for equipamento in inventario:
    valores.append(equipamento[1])
if len(valores)>0:
    print("O equipamento mais caro custa:", max(valores))
    print("O equipamento mais barato custa:", min(valores))
    print("O total de equipamentos é de:", sum(valores))