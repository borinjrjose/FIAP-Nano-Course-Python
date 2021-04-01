with open("economic-indicators.csv", "r") as boston:
    total2014=0
    maiorTransito=0
    mesMaiorTransito=""
    anoMaiorTransito=""
    anoEspecificado=input("Qual ano deseja saber o número de passageiros: ")
    totalEspecificado=0
    anoMediaDiaria=input("Qual ano deseja saber o mês com maior média da diária: ")
    mesMediaDiaria=""
    maiorMedia=0
    for linha in boston.readlines()[1:-1]:
        lista=linha.split(",")
        if lista[0]=="2014":
            total2014+=float(lista[3])
        
        if maiorTransito<float(lista[2]):
            maiorTransito=float(lista[2])
            anoMaiorTransito=lista[0]
            mesMaiorTransito=lista[1]
        
        if lista[0]==anoEspecificado:
            totalEspecificado+=float(lista[3])
        
        if lista[0]==anoMediaDiaria and maiorMedia<float(lista[5]):
            maiorMedia=float(lista[5])
            mesMediaDiaria=lista[1]

    print("Total de voos que partiram do aeroporto de Logan em 2014:", total2014)
    print("Data com o maior número de passageiros: " + mesMaiorTransito + "/" + anoMaiorTransito)
    print("No ano " + anoEspecificado + " passaram pelo aeroporto", totalEspecificado, "passageiros")
    print("No ano " + anoMediaDiaria + ", o mês com maior diária foi " + mesMediaDiaria)