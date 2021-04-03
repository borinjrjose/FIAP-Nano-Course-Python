import os
import getpass
from ftplib import *

ftp_ativo=False
ftp=FTP(input("Digite o FTP que deseja se conectar: "))
usuario=input("Digite o usuário: ")
senha=getpass.getpass("Digite a senha: ")
ftp.login(usuario, senha)
ftp.set_pasv(ftp_ativo)
print("Conexão bem sucedida.\n"+
    "Diretório atual:", ftp.pwd(), "\n\n\n")

menu="1"
while menu=="1" or menu=="2" or menu=="3":
    menu=input("Escolha a opção desejada:\n"+
            "\t<1> - para listar arquivos\n"+
            "\t<2> - para definir um diretório\n"+
            "\t<3> - para baixar um arquivo: ")
    if menu=="1":
        print(ftp.dir())
    elif menu=="2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("Diretório corrente é:", ftp.pwd())
    elif menu=="3":
        tipo=input("Digite <B> para arquivo binário ou qualquer outra letra para arquivo ASCII: ").upper()
        if tipo=="B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem: "), escreverLinha)
        print("Arquivo baixado com sucesso!")
ftp.close()