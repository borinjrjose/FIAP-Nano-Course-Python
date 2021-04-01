acesso = input("Qual o seu nível de acesso?").upper()
if acesso == "ADM":
    genero = input("Qual o seu gênero?").upper()
    if genero == "MASCULINO":
        print("Olá administrador!")
    else:
        print("Olá administradora!")
elif acesso == "USR":
    genero = input("Qual o seu gênero?").upper()
    if genero == "MASCULINO":
        print("Olá usuário!")
    else:
        print("Olá usuária!")
elif acesso == "GUEST":
    print("Olá visitante!")
else:
    print("Olá desconhecido!")