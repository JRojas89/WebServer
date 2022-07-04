import requests
import random

url = 'http://127.0.0.1:5000/'

#--------------------- Solicitud HTTP Ramdom ---------------------
#--- Idioma Ramdom ---
def ramdom_Lang():
    arrayLang = ["en/", "ita/", "fr/"]
    for i in range(len(arrayLang)):
        ramdomLang = random.choice(arrayLang)
        return ramdomLang

#--- Palabra Ramdom ---
def ramdom_Word():
    arrayWord = ["Hola", "Gato", "Perro", "Adios"]
    for i in range(len(arrayWord)):
        ramdomWord = random.choice(arrayWord)
        return ramdomWord

#--------------------- Enviar Solicitud HTTP ---------------------
def solicitudHTTP(fullURL):
    req = requests.get(fullURL)
    return req.json()

#---- Bucle de prueba para el mecanismo de sincronización ----
#--------------------- Crear Solicitudes ---------------------
while True:
    print(solicitudHTTP(url + ramdom_Lang() + ramdom_Word()))