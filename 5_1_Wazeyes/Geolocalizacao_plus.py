from geopy.geocoders import Nominatim

geolocator=Nominatim(user_agent="wazeyes")
endereco=input("Digite um endereço com número e cidade.\n"+
            "Exemplo: Avenida Paulista, 100 São Paulo: ")
resultado=geolocator.geocode(endereco)
print(resultado.latitude)
print(resultado.longitude)
if resultado.valid_address==True:
    print("Endereço completo.:", resultado)
    print("Coordenadas.......:", resultado.coordinates)
    print("Número............:", resultado.street_number)
    print("CEP...............:", resultado.postal_code)

print("Foi(ram) encontrado(s)", resultado.count, "endereco(s).")
for r in resultado:
    print("Cidade.....:", r.state)
    print("País.......:", r.country)
    print("Logradouro.:", r.route)
    print("########################")