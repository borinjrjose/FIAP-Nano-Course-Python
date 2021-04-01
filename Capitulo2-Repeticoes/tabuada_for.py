tabuada = int(input("Qual tabuada quer ver?"))
print("Tabuada do", tabuada)
for numero in range(1, 11, 1):
    print("\t", numero, "x", tabuada, "=", numero*tabuada)