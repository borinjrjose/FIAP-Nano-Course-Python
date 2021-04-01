with open("pagina.html", "w") as pagina:
    pagina.write("<html><body><h1>Questo è un test per una pagina WEB</h1>")
    pagina.write("<br/><h2>alcuni nomi inportanti per il progetto sono:</h2>")
    pagina.write("<h3>")
    nome=""
    while nome!="USCIRE":
        nome=input("Scrivi un nome oppure USCIRE: ").upper()
        if nome!="USCIRE":
            pagina.write("<br/>" + nome)
    pagina.write("</h3></body><html>")