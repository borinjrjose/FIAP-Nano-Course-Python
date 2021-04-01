def perguntar():
    return input("O que deseja realiza?\n"+
            "\t<I> - Para inserir um usuário\n"+
            "\t<P> - Para pesquisar um usuário\n"+
            "\t<E> - Para excluir um usuário\n"+
            "\t<L> - Para listar um usuário: ").upper()

def inserir(dicionario):
    login=input("Digite o login: ").upper()
    dicionario[login]=[input("Digite o nome: ").upper(),
                    input("Digite a última data de acesso: "),
                    input("Digite a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........:", lista[0])
        print("Último acesso..:", lista[1])
        print("Última estação.:", lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
        print("Objeto eliminado!")

def listar(dicionario):
    indice=1
    for chave, valor in dicionario.items():
        print("Objeto -", indice)
        print("Login:", chave)
        print("Dados:", valor)
        indice+=1