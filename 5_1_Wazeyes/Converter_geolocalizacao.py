from geopy.geocoders import Nominatim
from Funcoes.Funcoes_Endereco import *

endereco=carregarJSON("endereco.json")
enderStr=""
for strEnd in endereco["endereco"]:
    enderStr+=strEnd
    enderStr+=" "

geolocator=Nominatim(user_agent="wazeyes")
location=geolocator.geocode(enderStr)
print(location.address)
print((location.latitude, location.longitude))

coordenadas={
    "latitude": location.latitude,
    "longitude": location.longitude
}
salvarJSON("coordenadas.json", coordenadas)