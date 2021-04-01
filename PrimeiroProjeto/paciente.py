nome = input("Qual o seu nome?\n")
idade = int(input("Qual a sua idade?\n"))
if idade >= 65:
    print("Paciente " + nome + " de", idade, "anos é prioritário!")
else:
    print("Paciente " + nome + " de", idade, "anos não é prioritário!")