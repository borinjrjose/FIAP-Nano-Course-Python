from socket import *

servidor="127.0.0.1"
porta=43210
obj_socket=socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(1)
while True:
    print("Esperando conexão com o cliente.......")
    con, cliente=obj_socket.accept()
    print("Conectado com o cliente", cliente)
    while True:
        msg_recebida=str(con.recv(1024))
        print(cliente, "diz:", msg_recebida[2:-1])
        msg_enviada=bytes(input("Você diz: "), 'utf-8')
        con.send(msg_enviada)
        if msg_recebida[2:-1].upper()=="FIM":
            break
    con.close()
    print("Fim da conexão com o cliente", cliente)