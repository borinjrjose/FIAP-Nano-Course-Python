nome = input("Digite o nome:")
idade = int(input("Digite a idade:"))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa?").upper()
if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para a sala amarela - com prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para a sala amarela - sem prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para a sala branca - com prioridade")
elif idade <= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para a sala branca - sem prioridade")
else:
    print("Responda se possui doença infecto-contagiosa com SIM ou NAO!")