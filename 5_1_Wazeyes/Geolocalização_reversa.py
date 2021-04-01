from geopy.geocoders import Nominatim

geolocator=Nominatim(user_agent="wazeyes")
latitude=float(input("Digite a latitude: "))
longitude=float(input("Digite a longitude:"))

resultado=geolocator.reverse("f{latitude}, {longitude}")
if resultado.valid_address==True:
    print("Endereço completo.:", resultado)
    print("Número............:", resultado.street_number)
    print("CEP...............:", resultado.postal_code)