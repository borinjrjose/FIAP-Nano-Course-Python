with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
    print("Tipo di variabile:", type(conteudo))
    print("Contenuto del file:", conteudo)