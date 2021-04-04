import serial
conexao=""
for porta in range(10):
    try:
        conexao=serial.Serial('/dev/ttyUSB'+str(porta), 115200)
        print("Conectado na prota", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    acao=input("Digite:\n"+
            "\t<L> - para ligar\n"+
            "\t<D> - para desligar: ").upper()
    while acao=="L" or acao=="D":
        if acao=="L":
            conexao.write(b'1')
        else:
            conexao.write(b'0')
        acao=input("Digite:\n"+
            "\t<L> - para ligar\n"+
            "\t<D> - para desligar: ").upper()
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")