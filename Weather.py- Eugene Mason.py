#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

import api_keys


from citipy import citipy


output_data_file = "output_data/cities.csv"


lat_range = (-90, 90)
lng_range = (-180, 180)
Generate Cities List
In [2]:

lat_lngs = []
cities = []


lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)


for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    
    city = city.replace(" ", "%20")
    
    
    if city not in cities:

        cities.append(city)


len(cities)
Out[2]:
606
Perform API Calls
In [3]:

api_key = api_keys.api_key


url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + api_key
In [4]:

city_name = []
cloudiness = []
country = []
date = []
humidity = []
lat = []
lng = []
max_temp = []
wind_speed = []


record = 1


print(f"Beginning Data Retrieval")
print(f"-------------------------------")


for city in cities:  
    

    try: 
        response = requests.get(f"{url}&q={city}").json() 
        city_name.append(response["name"])
        cloudiness.append(response["clouds"]["all"])
        country.append(response["sys"]["country"])
        date.append(response["dt"])
        humidity.append(response["main"]["humidity"])
        max_temp.append(response["main"]["temp_max"])
        lat.append(response["coord"]["lat"])
        lng.append(response["coord"]["lon"])
        wind_speed.append(response["wind"]["speed"])
        city_record = response["name"]
        print(f"Processing Record {record} | {city_record}")
        print(f"{url}&q={city}")
        
        
        record= record + 1
        
      
        time.sleep(1.01)
        
    
    except:
        print("City not found. Skipping...")
    continue
Beginning Data Retrieval
-------------------------------
Processing Record 1 | Rikitea
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=rikitea
Processing Record 2 | Alofi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=alofi
Processing Record 3 | Puerto Leguizamo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=puerto%20leguizamo
Processing Record 4 | Hobart
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hobart
Processing Record 5 | Tiksi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tiksi
Processing Record 6 | Atuona
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=atuona
Processing Record 7 | Mataura
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mataura
Processing Record 8 | Punta Arenas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=punta%20arenas
Processing Record 9 | Marzuq
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=marzuq
Processing Record 10 | Octeville
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=octeville
Processing Record 11 | Solenzo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=solenzo
City not found. Skipping...
Processing Record 12 | Itarema
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=itarema
Processing Record 13 | Lorengau
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lorengau
Processing Record 14 | Albany
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=albany
City not found. Skipping...
Processing Record 15 | Yellowknife
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=yellowknife
Processing Record 16 | Bluff
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bluff
Processing Record 17 | Bida
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bida
Processing Record 18 | Hermanus
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hermanus
Processing Record 19 | Kununurra
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kununurra
Processing Record 20 | Marsa Matruh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=marsa%20matruh
Processing Record 21 | Kosonsoy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kosonsoy
Processing Record 22 | Sangar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sangar
Processing Record 23 | Goderich
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=goderich
Processing Record 24 | Port Alfred
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20alfred
Processing Record 25 | Arica
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=arica
Processing Record 26 | Gondanglegi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gondanglegi
City not found. Skipping...
Processing Record 27 | Itatskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=itatskiy
Processing Record 28 | Yar-Sale
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=yar-sale
Processing Record 29 | Lata
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lata
Processing Record 30 | Severo-Kurilsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=severo-kurilsk
Processing Record 31 | Cidreira
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cidreira
Processing Record 32 | Tlacotepec
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tlacotepec
Processing Record 33 | Dunedin
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dunedin
City not found. Skipping...
Processing Record 34 | Loa Janan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=loa%20janan
Processing Record 35 | Ushuaia
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ushuaia
Processing Record 36 | Upernavik
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=upernavik
Processing Record 37 | Byron Bay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=byron%20bay
Processing Record 38 | Daru
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=daru
Processing Record 39 | Cape Town
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cape%20town
Processing Record 40 | Vanavara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vanavara
Processing Record 41 | Pedernales
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pedernales
City not found. Skipping...
Processing Record 42 | Puerto Ayora
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=puerto%20ayora
Processing Record 43 | Ribeira Grande
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ribeira%20grande
Processing Record 44 | Mattru
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mattru
Processing Record 45 | Angoche
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=angoche
Processing Record 46 | Jamestown
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jamestown
Processing Record 47 | Ust-Kulom
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ust-kulom
Processing Record 48 | Kontagora
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kontagora
Processing Record 49 | Lebu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lebu
Processing Record 50 | Carnarvon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=carnarvon
Processing Record 51 | Hammerfest
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hammerfest
Processing Record 52 | Touros
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=touros
Processing Record 53 | Kaitangata
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kaitangata
Processing Record 54 | Gat
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gat
Processing Record 55 | Cabra
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cabra
Processing Record 56 | Herat
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=herat
Processing Record 57 | Parana
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=parana
Processing Record 58 | Saint-Pierre
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saint-pierre
Processing Record 59 | Kapaa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kapaa
Processing Record 60 | Ypsonas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ypsonas
Processing Record 61 | Shetpe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=shetpe
Processing Record 62 | Sitka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sitka
City not found. Skipping...
Processing Record 63 | Springdale
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=springdale
Processing Record 64 | New Norfolk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=new%20norfolk
Processing Record 65 | Pevek
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pevek
Processing Record 66 | Semey
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=semey
City not found. Skipping...
Processing Record 67 | Bambanglipuro
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bambanglipuro
Processing Record 68 | Enshi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=enshi
Processing Record 69 | East London
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=east%20london
Processing Record 70 | Butaritari
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=butaritari
Processing Record 71 | Copperas Cove
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=copperas%20cove
Processing Record 72 | Wanning
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=wanning
Processing Record 73 | Gisborne
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gisborne
Processing Record 74 | Kodiak
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kodiak
Processing Record 75 | Busselton
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=busselton
Processing Record 76 | Berlevag
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=berlevag
Processing Record 77 | Pacific Grove
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pacific%20grove
Processing Record 78 | Vysokogornyy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vysokogornyy
Processing Record 79 | Kiunga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kiunga
Processing Record 80 | Kirakira
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kirakira
Processing Record 81 | Baoro
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=baoro
Processing Record 82 | Mwinilunga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mwinilunga
Processing Record 83 | Pochutla
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pochutla
Processing Record 84 | Georgetown
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=georgetown
City not found. Skipping...
Processing Record 85 | Sao Joao da Barra
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sao%20joao%20da%20barra
Processing Record 86 | Dingle
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dingle
Processing Record 87 | Katsuura
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=katsuura
Processing Record 88 | Ucluelet
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ucluelet
City not found. Skipping...
Processing Record 89 | Cabo San Lucas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cabo%20san%20lucas
Processing Record 90 | Padang
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=padang
Processing Record 91 | Hualmay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hualmay
Processing Record 92 | Esperance
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=esperance
Processing Record 93 | Wundanyi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=wundanyi
Processing Record 94 | Haines Junction
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=haines%20junction
Processing Record 95 | Barrow
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=barrow
Processing Record 96 | Mahibadhoo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mahibadhoo
Processing Record 97 | Cururupu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cururupu
City not found. Skipping...
Processing Record 98 | Thompson
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=thompson
Processing Record 99 | Pontianak
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pontianak
Processing Record 100 | Iqaluit
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=iqaluit
Processing Record 101 | Maxixe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=maxixe
Processing Record 102 | Klaksvik
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=klaksvik
Processing Record 103 | Te Anau
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=te%20anau
Processing Record 104 | Riberalta
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=riberalta
Processing Record 105 | Khatanga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=khatanga
Processing Record 106 | Villefranche-sur-Saone
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=villefranche-sur-saone
Processing Record 107 | Barinas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=barinas
City not found. Skipping...
Processing Record 108 | Ozernovskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ozernovskiy
Processing Record 109 | Oksfjord
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=oksfjord
Processing Record 110 | Avarua
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=avarua
Processing Record 111 | San Patricio
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20patricio
Processing Record 112 | Victoria
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=victoria
Processing Record 113 | Tulum
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tulum
Processing Record 114 | Luderitz
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=luderitz
Processing Record 115 | Tuatapere
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tuatapere
Processing Record 116 | Ilulissat
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ilulissat
Processing Record 117 | Corn Island
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=corn%20island
City not found. Skipping...
City not found. Skipping...
Processing Record 118 | Talnakh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=talnakh
Processing Record 119 | Kidal
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kidal
Processing Record 120 | Magan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=magan
Processing Record 121 | Nushki
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nushki
Processing Record 122 | Provideniya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=provideniya
Processing Record 123 | Bredasdorp
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bredasdorp
Processing Record 124 | Joplin
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=joplin
Processing Record 125 | Qaanaaq
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=qaanaaq
Processing Record 126 | Moose Factory
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=moose%20factory
Processing Record 127 | Hilo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hilo
Processing Record 128 | Jacareacanga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jacareacanga
Processing Record 129 | Arraial do Cabo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=arraial%20do%20cabo
Processing Record 130 | Sobolevo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sobolevo
Processing Record 131 | Salalah
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=salalah
Processing Record 132 | Tuktoyaktuk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tuktoyaktuk
Processing Record 133 | Vaini
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vaini
Processing Record 134 | Geraldton
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=geraldton
Processing Record 135 | Terrasini
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=terrasini
Processing Record 136 | Boguchany
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=boguchany
Processing Record 137 | Belmonte
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=belmonte
Processing Record 138 | Leningradskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=leningradskiy
Processing Record 139 | Havre-Saint-Pierre
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=havre-saint-pierre
City not found. Skipping...
Processing Record 140 | Warren
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=warren
Processing Record 141 | Taoudenni
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=taoudenni
Processing Record 142 | Bara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bara
Processing Record 143 | Zaraza
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zaraza
Processing Record 144 | Manta
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=manta
City not found. Skipping...
Processing Record 145 | Garmsar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=garmsar
Processing Record 146 | Dongsheng
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dongsheng
Processing Record 147 | Pantai Remis
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pantai%20remis
Processing Record 148 | Collie
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=collie
Processing Record 149 | Namibe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=namibe
Processing Record 150 | Guerrero Negro
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=guerrero%20negro
City not found. Skipping...
Processing Record 151 | Westport
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=westport
Processing Record 152 | Nova Vicosa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nova%20vicosa
Processing Record 153 | Nacimiento
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nacimiento
Processing Record 154 | Walvis Bay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=walvis%20bay
Processing Record 155 | Dikson
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dikson
Processing Record 156 | Sakaiminato
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sakaiminato
Processing Record 157 | Paciran
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=paciran
Processing Record 158 | Kupino
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kupino
Processing Record 159 | Flin Flon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=flin%20flon
Processing Record 160 | Isangel
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=isangel
Processing Record 161 | Karratha
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=karratha
Processing Record 162 | Tautira
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tautira
Processing Record 163 | Jaisinghnagar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jaisinghnagar
Processing Record 164 | Uyuni
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=uyuni
Processing Record 165 | Airai
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=airai
Processing Record 166 | Lincoln
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lincoln
Processing Record 167 | Clyde River
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=clyde%20river
Processing Record 168 | Panama City
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=panama%20city
Processing Record 169 | Lingyuan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lingyuan
Processing Record 170 | Belyy Yar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=belyy%20yar
Processing Record 171 | Saint-Philippe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saint-philippe
City not found. Skipping...
Processing Record 172 | Dubbo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dubbo
Processing Record 173 | Waingapu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=waingapu
City not found. Skipping...
Processing Record 174 | Mocuba
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mocuba
City not found. Skipping...
Processing Record 175 | Runcu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=runcu
Processing Record 176 | Valreas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=valreas
City not found. Skipping...
Processing Record 177 | Bereda
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bereda
City not found. Skipping...
Processing Record 178 | Nueva Guinea
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nueva%20guinea
Processing Record 179 | Lagoa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lagoa
Processing Record 180 | La Ronge
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=la%20ronge
Processing Record 181 | Leh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=leh
Processing Record 182 | Nouadhibou
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nouadhibou
Processing Record 183 | College
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=college
Processing Record 184 | Cockburn Town
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cockburn%20town
Processing Record 185 | Mar del Plata
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mar%20del%20plata
City not found. Skipping...
City not found. Skipping...
Processing Record 186 | Morgan City
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=morgan%20city
Processing Record 187 | Vostok
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vostok
Processing Record 188 | San Cristobal
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20cristobal
Processing Record 189 | Krasnoborsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=krasnoborsk
Processing Record 190 | Talcahuano
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=talcahuano
Processing Record 191 | Aklavik
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=aklavik
Processing Record 192 | Becal
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=becal
City not found. Skipping...
Processing Record 193 | Laguna
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=laguna
Processing Record 194 | Vadinsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vadinsk
Processing Record 195 | Balabac
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=balabac
Processing Record 196 | Anloga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=anloga
Processing Record 197 | Tasiilaq
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tasiilaq
Processing Record 198 | Grindavik
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=grindavik
Processing Record 199 | Clinton
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=clinton
Processing Record 200 | Ivdel
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ivdel
Processing Record 201 | Shingu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=shingu
Processing Record 202 | Luoyang
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=luoyang
Processing Record 203 | Souillac
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=souillac
Processing Record 204 | Ron Phibun
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ron%20phibun
Processing Record 205 | Alvorada
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=alvorada
Processing Record 206 | Bilibino
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bilibino
Processing Record 207 | Bathsheba
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bathsheba
City not found. Skipping...
Processing Record 208 | Porbandar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=porbandar
Processing Record 209 | Calama
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=calama
Processing Record 210 | Norman Wells
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=norman%20wells
Processing Record 211 | Aleksandrovskoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=aleksandrovskoye
Processing Record 212 | Sundern
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sundern
City not found. Skipping...
Processing Record 213 | Kavieng
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kavieng
City not found. Skipping...
Processing Record 214 | Ahipara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ahipara
Processing Record 215 | Zyryanskoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zyryanskoye
Processing Record 216 | Ekhabi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ekhabi
Processing Record 217 | Sorland
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sorland
Processing Record 218 | Axim
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=axim
Processing Record 219 | Avera
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=avera
City not found. Skipping...
Processing Record 220 | Bambous Virieux
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bambous%20virieux
Processing Record 221 | Tsiroanomandidy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tsiroanomandidy
Processing Record 222 | Bayanday
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bayanday
Processing Record 223 | Pisco
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pisco
Processing Record 224 | Faanui
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=faanui
Processing Record 225 | Bethel
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bethel
Processing Record 226 | Hithadhoo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hithadhoo
Processing Record 227 | Elko
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=elko
Processing Record 228 | Nikolskoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nikolskoye
Processing Record 229 | Gerede
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gerede
Processing Record 230 | Lamar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lamar
Processing Record 231 | Tucuman
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tucuman
City not found. Skipping...
City not found. Skipping...
Processing Record 232 | Hokitika
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hokitika
Processing Record 233 | Ngunguru
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ngunguru
Processing Record 234 | Puyo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=puyo
City not found. Skipping...
Processing Record 235 | Lima
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lima
Processing Record 236 | San Ramon de la Nueva Oran
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20ramon%20de%20la%20nueva%20oran
Processing Record 237 | Hambantota
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hambantota
Processing Record 238 | Tromso
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tromso
Processing Record 239 | Tabou
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tabou
Processing Record 240 | Naze
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=naze
Processing Record 241 | Tiarei
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tiarei
Processing Record 242 | Sembakung
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sembakung
Processing Record 243 | Ancud
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ancud
Processing Record 244 | Lavrentiya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lavrentiya
Processing Record 245 | Valkeala
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=valkeala
City not found. Skipping...
Processing Record 246 | Hirara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hirara
Processing Record 247 | Polunochnoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=polunochnoye
City not found. Skipping...
Processing Record 248 | Aksarka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=aksarka
Processing Record 249 | Windhoek
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=windhoek
Processing Record 250 | Srednekolymsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=srednekolymsk
Processing Record 251 | Hanna
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hanna
Processing Record 252 | Viedma
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=viedma
Processing Record 253 | Taihe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=taihe
Processing Record 254 | Ushtobe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ushtobe
City not found. Skipping...
Processing Record 255 | Christchurch
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=christchurch
Processing Record 256 | Saint George
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saint%20george
Processing Record 257 | Seymchan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=seymchan
Processing Record 258 | Constantine
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=constantine
City not found. Skipping...
Processing Record 259 | La Mesa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=la%20mesa
Processing Record 260 | Castro
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=castro
Processing Record 261 | Vila
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vila
Processing Record 262 | Bainbridge
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bainbridge
Processing Record 263 | Saint-Francois
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saint-francois
Processing Record 264 | Khuzhir
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=khuzhir
Processing Record 265 | Nyurba
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nyurba
Processing Record 266 | Cuamba
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cuamba
Processing Record 267 | Mahebourg
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mahebourg
Processing Record 268 | Creston
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=creston
Processing Record 269 | Honningsvag
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=honningsvag
Processing Record 270 | Mehamn
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mehamn
Processing Record 271 | Cayenne
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cayenne
Processing Record 272 | Olinda
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=olinda
Processing Record 273 | San Vicente
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20vicente
Processing Record 274 | Valparaiso
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=valparaiso
Processing Record 275 | Port Blair
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20blair
Processing Record 276 | Acapulco
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=acapulco
Processing Record 277 | Kruisfontein
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kruisfontein
Processing Record 278 | Nanortalik
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nanortalik
Processing Record 279 | Evensk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=evensk
Processing Record 280 | Chuy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=chuy
Processing Record 281 | Adrar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=adrar
Processing Record 282 | Cordoba
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cordoba
Processing Record 283 | Sao Filipe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sao%20filipe
Processing Record 284 | Fabriano
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fabriano
Processing Record 285 | Nizhniy Kuranakh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nizhniy%20kuranakh
Processing Record 286 | Trairi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=trairi
Processing Record 287 | Saskylakh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saskylakh
Processing Record 288 | Rudnya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=rudnya
Processing Record 289 | Marsh Harbour
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=marsh%20harbour
Processing Record 290 | Balkanabat
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=balkanabat
Processing Record 291 | Whitehorse
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=whitehorse
Processing Record 292 | Lere
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lere
City not found. Skipping...
Processing Record 293 | Kosa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kosa
Processing Record 294 | Launceston
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=launceston
City not found. Skipping...
Processing Record 295 | Batagay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=batagay
Processing Record 296 | San Jeronimito
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20jeronimito
Processing Record 297 | Kassala
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kassala
Processing Record 298 | Namatanai
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=namatanai
Processing Record 299 | Barra do Garcas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=barra%20do%20garcas
Processing Record 300 | Ormara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ormara
Processing Record 301 | Margate
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=margate
City not found. Skipping...
Processing Record 302 | Huinan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=huinan
Processing Record 303 | Vigeland
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vigeland
Processing Record 304 | Constitucion
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=constitucion
Processing Record 305 | Hasaki
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hasaki
Processing Record 306 | Quesnel
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=quesnel
Processing Record 307 | Rio Gallegos
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=rio%20gallegos
Processing Record 308 | Champerico
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=champerico
Processing Record 309 | Pearl Lagoon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=laguna%20de%20perlas
Processing Record 310 | Shumskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=shumskiy
Processing Record 311 | Ahuimanu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ahuimanu
Processing Record 312 | Saldanha
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=saldanha
Processing Record 313 | Pangody
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pangody
Processing Record 314 | Oudtshoorn
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=oudtshoorn
Processing Record 315 | Chokurdakh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=chokurdakh
Processing Record 316 | Komsomolskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=komsomolskiy
Processing Record 317 | Bryant
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bryant
Processing Record 318 | Khandyga
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=khandyga
Processing Record 319 | Terra Santa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=terra%20santa
Processing Record 320 | La Grande
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=la%20grande
Processing Record 321 | Pitimbu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pitimbu
Processing Record 322 | Alekseyevsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=alekseyevsk
Processing Record 323 | Codrington
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=codrington
Processing Record 324 | Matagami
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=matagami
Processing Record 325 | Oranjemund
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=oranjemund
Processing Record 326 | Leshukonskoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=leshukonskoye
Processing Record 327 | Severnoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=severnoye
Processing Record 328 | Nishihara
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nishihara
Processing Record 329 | Havelock
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=havelock
Processing Record 330 | Narsaq
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=narsaq
City not found. Skipping...
Processing Record 331 | Henties Bay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=henties%20bay
Processing Record 332 | Nantucket
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nantucket
City not found. Skipping...
Processing Record 333 | Fairbanks
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fairbanks
Processing Record 334 | Praia da Vitoria
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=praia%20da%20vitoria
Processing Record 335 | Manyana
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=manyana
Processing Record 336 | Banyuwangi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=banyuwangi
Processing Record 337 | Paragominas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=paragominas
Processing Record 338 | Urrao
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=urrao
Processing Record 339 | Naron
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=naron
Processing Record 340 | North Bend
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=north%20bend
Processing Record 341 | Beian
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=beian
Processing Record 342 | Nadapuram
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nadapuram
Processing Record 343 | Aripuana
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=aripuana
Processing Record 344 | Sept-Iles
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sept-iles
Processing Record 345 | Vestmanna
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vestmanna
Processing Record 346 | Villa Carlos Paz
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=villa%20carlos%20paz
City not found. Skipping...
Processing Record 347 | Cherskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=cherskiy
City not found. Skipping...
City not found. Skipping...
Processing Record 348 | Broome
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=broome
Processing Record 349 | Stendal
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=stendal
Processing Record 350 | Lhokseumawe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lhokseumawe
Processing Record 351 | Ust-Maya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ust-maya
Processing Record 352 | Lompoc
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lompoc
Processing Record 353 | Hofn
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hofn
Processing Record 354 | Alta Floresta
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=alta%20floresta
Processing Record 355 | Copiapo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=copiapo
Processing Record 356 | Ponta do Sol
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ponta%20do%20sol
Processing Record 357 | Winton
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=winton
Processing Record 358 | Kampot
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kampot
Processing Record 359 | Longyearbyen
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=longyearbyen
City not found. Skipping...
City not found. Skipping...
Processing Record 360 | Zabaykalsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zabaykalsk
Processing Record 361 | The Valley
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=the%20valley
Processing Record 362 | Quatre Cocos
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=quatre%20cocos
Processing Record 363 | Kaihua
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kaihua
Processing Record 364 | Jinji
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jinji
Processing Record 365 | Sangin
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sangin
Processing Record 366 | Coquimbo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=coquimbo
Processing Record 367 | Talaya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=talaya
City not found. Skipping...
Processing Record 368 | Broken Hill
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=broken%20hill
Processing Record 369 | Zhangjiakou
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zhangjiakou
Processing Record 370 | Shahdadkot
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=shahdadkot
City not found. Skipping...
Processing Record 371 | Anshun
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=anshun
Processing Record 372 | Lucera
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lucera
Processing Record 373 | Aitape
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=aitape
Processing Record 374 | Kandrian
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kandrian
Processing Record 375 | Okato
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=okato
Processing Record 376 | Waddan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=waddan
Processing Record 377 | Anadyr
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=anadyr
Processing Record 378 | Torbay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=torbay
City not found. Skipping...
City not found. Skipping...
Processing Record 379 | Shimoda
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=shimoda
Processing Record 380 | Kudahuvadhoo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kudahuvadhoo
Processing Record 381 | Alexandria
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=alexandria
Processing Record 382 | Jinchang
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jinchang
Processing Record 383 | Santa Cruz
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=santa%20cruz
Processing Record 384 | Ola
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ola
Processing Record 385 | Horsham
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=horsham
Processing Record 386 | Troitsko-Pechorsk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=troitsko-pechorsk
Processing Record 387 | Kamenka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kamenka
Processing Record 388 | Palmer
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=palmer
Processing Record 389 | Bandarbeyla
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bandarbeyla
City not found. Skipping...
Processing Record 390 | Vila Velha
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vila%20velha
Processing Record 391 | Peniche
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=peniche
Processing Record 392 | Grants Pass
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=grants%20pass
Processing Record 393 | Mount Isa
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mount%20isa
Processing Record 394 | Hudson Bay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hudson%20bay
Processing Record 395 | Gaogou
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gaogou
Processing Record 396 | Peterborough
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=peterborough
Processing Record 397 | Tura
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tura
Processing Record 398 | Port Elizabeth
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20elizabeth
Processing Record 399 | Galveston
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=galveston
Processing Record 400 | Puerto Madero
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=puerto%20madero
Processing Record 401 | Teya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=teya
Processing Record 402 | Igarka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=igarka
Processing Record 403 | Jutai
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jutai
Processing Record 404 | Serebryansk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=serebryansk
Processing Record 405 | Fort Nelson
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fort%20nelson
Processing Record 406 | Sola
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sola
Processing Record 407 | Bowen
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bowen
Processing Record 408 | Muzhi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=muzhi
Processing Record 409 | Bansi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bansi
Processing Record 410 | Fallon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fallon
Processing Record 411 | Novoagansk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=novoagansk
Processing Record 412 | Najran
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=najran
Processing Record 413 | Mogadishu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mogadishu
Processing Record 414 | Tabuk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tabuk
Processing Record 415 | Sabang
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sabang
Processing Record 416 | Actopan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=actopan
Processing Record 417 | Monrovia
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=monrovia
Processing Record 418 | Wanlaweyn
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=wanlaweyn
Processing Record 419 | Fare
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fare
Processing Record 420 | Oyotun
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=oyotun
Processing Record 421 | Sao Gabriel da Cachoeira
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sao%20gabriel%20da%20cachoeira
City not found. Skipping...
City not found. Skipping...
Processing Record 422 | Lalmohan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lalmohan
Processing Record 423 | Tala
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tala
Processing Record 424 | Zliv
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zliv
Processing Record 425 | Resistencia
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=resistencia
City not found. Skipping...
Processing Record 426 | Dombarovskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dombarovskiy
Processing Record 427 | Tignere
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tignere
Processing Record 428 | Tsimlyansk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tsimlyansk
Processing Record 429 | Udachnyy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=udachnyy
Processing Record 430 | Nogliki
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nogliki
Processing Record 431 | Gusau
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gusau
Processing Record 432 | Ostrovnoy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ostrovnoy
Processing Record 433 | Wuwei
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=wuwei
Processing Record 434 | Naryan-Mar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=naryan-mar
Processing Record 435 | Bardejov
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bardejov
Processing Record 436 | Nurota
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nurota
Processing Record 437 | Lake Havasu City
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lake%20havasu%20city
Processing Record 438 | Verkhnyaya Inta
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=verkhnyaya%20inta
Processing Record 439 | Gerash
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gerash
Processing Record 440 | Opuwo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=opuwo
City not found. Skipping...
Processing Record 441 | Oktyabrskoye
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=oktyabrskoye
Processing Record 442 | Sergeyevka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sergeyevka
Processing Record 443 | Palana
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=palana
Processing Record 444 | Katherine
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=katherine
Processing Record 445 | Amarillo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=amarillo
Processing Record 446 | Kaman
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kaman
Processing Record 447 | Sinfra
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sinfra
City not found. Skipping...
Processing Record 448 | Fomboni
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=fomboni
Processing Record 449 | Novi Sanzhary
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=novi%20sanzhary
Processing Record 450 | Magdagachi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=magdagachi
Processing Record 451 | Barranca
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=barranca
Processing Record 452 | Neyshabur
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=neyshabur
Processing Record 453 | Arlit
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=arlit
Processing Record 454 | San Policarpo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20policarpo
Processing Record 455 | San Ramon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=san%20ramon
Processing Record 456 | Atambua
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=atambua
Processing Record 457 | Novikovo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=novikovo
Processing Record 458 | Umm Kaddadah
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=umm%20kaddadah
Processing Record 459 | Baruun-Urt
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=baruun-urt
Processing Record 460 | Traverse City
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=traverse%20city
Processing Record 461 | Port-Gentil
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port-gentil
Processing Record 462 | Port Shepstone
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20shepstone
City not found. Skipping...
City not found. Skipping...
Processing Record 463 | Novovorontsovka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=novovorontsovka
Processing Record 464 | Gondar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gondar
Processing Record 465 | Mumford
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mumford
Processing Record 466 | Nome
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nome
Processing Record 467 | Raudeberg
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=raudeberg
Processing Record 468 | Caravelas
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=caravelas
Processing Record 469 | Faya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=faya
Processing Record 470 | Pakxan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pakxan
Processing Record 471 | Kisangani
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kisangani
Processing Record 472 | Mount Gambier
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mount%20gambier
Processing Record 473 | Kavaratti
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kavaratti
Processing Record 474 | Nobres
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nobres
Processing Record 475 | Rabo de Peixe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=rabo%20de%20peixe
Processing Record 476 | Paamiut
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=paamiut
Processing Record 477 | Sioux Lookout
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=sioux%20lookout
Processing Record 478 | Manjacaze
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=manjacaze
Processing Record 479 | Bom Jesus
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bom%20jesus
Processing Record 480 | Banjar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=banjar
Processing Record 481 | Jonkoping
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=jonkoping
Processing Record 482 | Salinopolis
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=salinopolis
Processing Record 483 | Ankazobe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ankazobe
Processing Record 484 | Anori
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=anori
Processing Record 485 | Ailigandi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ailigandi
Processing Record 486 | Richards Bay
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=richards%20bay
Processing Record 487 | Ito
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ito
Processing Record 488 | Buta
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=buta
City not found. Skipping...
Processing Record 489 | Bundaberg
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bundaberg
Processing Record 490 | Harper
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=harper
Processing Record 491 | Nchelenge
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nchelenge
Processing Record 492 | Tessalit
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tessalit
Processing Record 493 | Yarada
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=yarada
Processing Record 494 | Vardo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vardo
Processing Record 495 | Tandil
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tandil
Processing Record 496 | Vestmannaeyjar
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=vestmannaeyjar
Processing Record 497 | Tual
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tual
Processing Record 498 | Novomykolayivka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=novomykolayivka
Processing Record 499 | Puerto Narino
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=puerto%20narino
City not found. Skipping...
Processing Record 500 | Esso
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=esso
Processing Record 501 | Gold Coast
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gold%20coast
Processing Record 502 | Lerwick
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=lerwick
Processing Record 503 | Worthington
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=worthington
Processing Record 504 | Nemuro
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nemuro
Processing Record 505 | Yarmouth
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=yarmouth
Processing Record 506 | Pittsburg
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pittsburg
City not found. Skipping...
Processing Record 507 | Ugoofaaru
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=ugoofaaru
Processing Record 508 | Antalaha
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=antalaha
Processing Record 509 | Nova Olinda do Norte
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=nova%20olinda%20do%20norte
Processing Record 510 | Gari
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=gari
City not found. Skipping...
Processing Record 511 | Kahului
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kahului
City not found. Skipping...
Processing Record 512 | Georgiyevka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=georgiyevka
Processing Record 513 | Mchinji
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mchinji
Processing Record 514 | Berdigestyakh
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=berdigestyakh
Processing Record 515 | Abengourou
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=abengourou
Processing Record 516 | Kroya
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kroya
Processing Record 517 | Port Hardy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20hardy
Processing Record 518 | Labuhan
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=labuhan
Processing Record 519 | Mandalgovi
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mandalgovi
Processing Record 520 | Kargasok
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kargasok
Processing Record 521 | Kasongo-Lunda
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kasongo-lunda
Processing Record 522 | Dudinka
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dudinka
Processing Record 523 | Big Rapids
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=big%20rapids
City not found. Skipping...
Processing Record 524 | Tres Rios
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=tres%20rios
Processing Record 525 | Requena
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=requena
Processing Record 526 | Zhigansk
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=zhigansk
Processing Record 527 | Coihaique
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=coihaique
Processing Record 528 | Marica
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=marica
Processing Record 529 | Hastings
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=hastings
Processing Record 530 | Inirida
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=inirida
Processing Record 531 | Chopda
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=chopda
Processing Record 532 | Pinega
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=pinega
Processing Record 533 | Kawalu
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kawalu
Processing Record 534 | Deputatskiy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=deputatskiy
Processing Record 535 | Bunol
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bunol
Processing Record 536 | Springfield
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=springfield
Processing Record 537 | Port Lincoln
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=port%20lincoln
Processing Record 538 | Torbat-e Jam
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=torbat-e%20jam
Processing Record 539 | Dong Xoai
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=dong%20xoai
Processing Record 540 | Mahon
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=mahon
Processing Record 541 | Bonthe
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=bonthe
Processing Record 542 | Kedrovyy
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=kedrovyy
Processing Record 543 | Thinadhoo
http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=f6f55705bfcd84b4da4d6829ad8c65d8&q=thinadhoo
In [5]:

weatherpy_dict = {
    "City": city_name,
    "Cloudiness":cloudiness, 
    "Country":country,
    "Date":date, 
    "Humidity": humidity,
    "Lat":lat, 
    "Lng":lng, 
    "Max Temp": max_temp,
    "Wind Speed":wind_speed
}


weather_data = pd.DataFrame(weatherpy_dict)


weather_data.count()
Out[5]:
City          543
Cloudiness    543
Country       543
Date          543
Humidity      543
Lat           543
Lng           543
Max Temp      543
Wind Speed    543
dtype: int64
In [6]:

weather_data.to_csv('Output_CSV/weather_data.csv')


weather_data.head()
Out[6]:
City	Cloudiness	Country	Date	Humidity	Lat	Lng	Max Temp	Wind Speed
0	Rikitea	76	PF	1535161134	100	-23.12	-134.97	70.14	12.55
1	Alofi	90	NU	1535158800	74	-19.06	-169.92	78.80	8.05
2	Puerto Leguizamo	12	CO	1535161137	93	-0.19	-74.78	74.55	2.15
3	Hobart	0	AU	1535158800	54	-42.88	147.33	57.20	11.41
4	Tiksi	0	RU	1535161141	96	71.64	128.87	46.29	6.73
Latitude vs. Temperature Plot
In [7]:

plt.scatter(weather_data["Lat"], weather_data["Max Temp"], marker="o", s=10)


plt.title("City Latitude vs. Max Temperature")
plt.ylabel("Max. Temperature (F)")
plt.xlabel("Latitude")
plt.grid(True)


plt.savefig("Output_Plots/Max_Temp_vs_Latitude.png")


plt.show()

Latitude vs. Humidity Plot
In [8]:

plt.scatter(weather_data["Lat"], weather_data["Humidity"], marker="o", s=10)


plt.title("City Latitude vs. Humidity")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(True)


plt.savefig("Output_Plots/Humidity_vs_Latitude.png")


plt.show()

Latitude vs. Cloudiness Plot
In [9]:

plt.scatter(weather_data["Lat"], weather_data["Cloudiness"], marker="o", s=10)


plt.title("City Latitude vs. Cloudiness")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(True)


plt.savefig("Output_Plots/Cloudiness_vs_Latitude.png")


plt.show()

Latitude vs. Wind Speed Plot
In [10]:

plt.scatter(weather_data["Lat"], weather_data["Wind Speed"], marker="o", s=10)


plt.title("City Latitude vs. Wind Speed")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(True)


plt.savefig("Output_Plots/Wind_Speed_vs_Latitude.png")


plt.show()

