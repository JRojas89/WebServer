Universidad Nacional de Costa Rica - II Proyecto - EIF212 Sistemas Operativos - I Ciclo 2022
  ------------------------------------------------------
    Para este proyecto se utilizo Python 3 y Flask para 
    la parte programada, XAMPP para la base de datos de 
    MySQL y Docker para crear la imagen
  ------------------------------------------------------

**- - ->> PARA CORRER LA APLICACION DEBE SEGUIR LOS SIGUIENTES PASOS <<- - -**

1. Descargar la imagen de docker --> https://hub.docker.com/r/jrojas89/projectso-una
2. Correr la imagen en el contenedor --> docker run --rm -p 80:5000 projectso-una:projectso-una
3. Abrir XAMPP iniciar los modulos Apache y MySQL
4. En XAMPP pulsar el boton [Admin] se abrira el navegador con phpMyAdmin
5. Crear una nueva base de datos llamada "bdtranslatorapi"
6. Ejecutar el script WebServer.py y detenerlo [Ctrl + C]
7. Volver a phpMyAdmin, abrir la base de datos y presionar el boton superior [SQL] y pegar los siguientes comandos:
  ------------------------------------------------------
    INSERT INTO en (pEs, pEn) VALUES ('Hola', 'Hello'), ('Adios', 'GoodBye'), ('Perro', 'Dog'), ('Gato', 'Cat');
    INSERT INTO ita (pEs, pIta) VALUES ('Hola', 'Ciao'), ('Adios', 'Arrivederci'), ('Perro', 'Cane'), ('Gato', 'Gatto');
    INSERT INTO fr (pEs, pFr) VALUES ('Hola', 'Salut'), ('Adios', 'Adieu'), ('Perro', 'Chien'), ('Gato', 'Chat');
  ------------------------------------------------------
8. Presionar el boton inferior [Continuar]
9. Ejecutar el script WebServer.py
10. Ejecutar el script Cliente.py y detenerlo [Ctrl + C]
    * (Para este paso tambien se puede utilizar Postman o copiar la solicitud HTTP directamente en el browser)
11. Aparecera un archivo llamado Archivo_log.txt con los datos de los clientes que enviaron las solicitudes HTTP

**- - ->> EJEMPLOS DE USO <<- - -**

* Se envia una solicitud http://127.0.0.1:5000/en/Hola --> Se recibe de respuesta: {"pEn": "Hello", "pEs": "Hola"}
* Se envia una solicitud http://127.0.0.1:5000/ita/Gato --> Se recibe de respuesta: {"pEs": "Gato", "pIta": "Gatto"}
* Se envia una solicitud http://127.0.0.1:5000/fr/Adios --> Se recibe de respuesta: {"pEs": "Adios", "pFr": "Adieu"}


**- - ->> IMPORTANTE <<- - -**

La solicitud HTTP tiene el siguiente formato http://127.0.0.1:5000/Language/Word --> Donde {Language} es el idioma al que se desea traducir la palabra el cual puede ser: en, ita, fr. Y {Word} es la palabra a traducir la cual puede ser: Hola, Adios, Perro, Gato

**NOTA: Se deben respetar las mayusculas y minusculas SIEMPRE.**