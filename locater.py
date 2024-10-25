import phonenumbers
from phonenumbers import geocoder
import folium

Key = "29669e89e212423199949fab63f6dd2f"

print("Selamat datang di locater Telepon")
print("nomer telepon contoh +62xxxxxxxxxxx")
number = input("Masukkan nomer telepon : ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print("Lokasi Negara : ",number_location)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print("Service Provider : ",carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']["lat"]
lng = results[0]['geometry']["lng"]
print("Latitude : ",lat,"Longitude : ",lng)

map_location = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")