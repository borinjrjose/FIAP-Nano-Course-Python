nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade: "))
prioridade = "Não"
if idade >= 65:
    prioridade = "Sim"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)