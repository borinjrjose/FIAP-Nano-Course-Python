nome = input("Digite o nome:")
idade = int(input("Digite a idade:"))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para a sala amarela!")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para a sala branca!")
else:
    print("Responda se há suspeita de doença infecto-contagiosa com SIM ou NAO!")

if idade >= 65:
    print("Paciente com prioridade!")
else:
    genero = input("Digite o gênero:").upper()
    if genero == "FEMININO" and idade >= 10:
        gravidez = input("Está grávida?").upper()
        if gravidez == "SIM":
            print("Paciente com prioridade!")
        else:
            print("Paciente sem prioridade!")
    else:
        print("Paciente sem prioridade!")
