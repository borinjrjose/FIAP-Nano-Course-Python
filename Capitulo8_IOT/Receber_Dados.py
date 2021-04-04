import serial
conexao=""
for porta in range(10):
    try:
        conexao=serial.Serial('/dev/ttyUSB'+str(porta), 115200)
        print("Conectado na porta:", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    while True:
        resposta=conexao.read()
        if resposta==b'1':
            print("LED ligado")
        else:
            print("LED desligado")
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")