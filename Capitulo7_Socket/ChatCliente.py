from socket import *

servidor="127.0.0.1"
porta=43210
obj_socket=socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
print("Conectado com o servidor.")
while True:
    msg_enviada=bytes(input("Você diz: "), 'utf-8')
    obj_socket.send(msg_enviada)
    msg_recebida=str(obj_socket.recv(1024))
    print("Servidor diz:", msg_recebida[2:-1])

    if str(msg_enviada)[2:-1].upper()=="FIM":
        break
obj_socket.close()