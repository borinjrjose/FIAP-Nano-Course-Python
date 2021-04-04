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
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")