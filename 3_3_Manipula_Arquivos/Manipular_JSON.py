from Funcoes.Funcoes_JSON import *

arquivo="inventario_json.json"
inventario=carregarInventario(arquivo)
opcao=perguntar()
while opcao>0 and opcao<3:
    if opcao==1:
        registrarAtivo(inventario, arquivo)
    elif opcao==2:
        exibirAtivos(arquivo)
    opcao=perguntar()