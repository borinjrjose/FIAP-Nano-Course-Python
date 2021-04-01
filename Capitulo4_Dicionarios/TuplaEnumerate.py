usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um email: ").lower())
    resp=input("Digite <S> para continuar: ").upper()

tuplas=list(enumerate(emails))
for chave in range(0, len(tuplas), 1):
    print("Email:", tuplas[chave][1])
    usuarios[tuplas[chave]]=[input("Digite o nome: "), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print("Usuário.:", chave[0])
    print("Email...:", chave[1])
    print("Nome....:", dado[0])
    print("Nível...:", dado[1])