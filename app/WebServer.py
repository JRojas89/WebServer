import os
import time
import threading
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/bdtranslatorapi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
sem = threading.Semaphore()

#----------------------------- Tablas -----------------------------
#Creación de la tabla 'Ingles'
class en(db.Model):
    pEs = db.Column(db.String(50),primary_key = True)
    pEn = db.Column(db.String(50))

    def __init__(self,pEn):
        self.pEn = pEn

#Creación de la tabla 'Italiano'
class ita(db.Model):
    pEs = db.Column(db.String(50),primary_key = True)
    pIta = db.Column(db.String(50))

    def __init__(self,pIta):
        self.pIta = pIta

#Creación de la tabla 'Frances'
class fr(db.Model):
    pEs = db.Column(db.String(50),primary_key = True)
    pFr = db.Column(db.String(50))

    def __init__(self,pFr):
        self.pFr = pFr

db.create_all()

#----------------------------- Esquemas -----------------------------
#INGLES
class enSchema(ma.Schema):
    class Meta:
        fields = ('pEs','pEn')
en_schema = enSchema()

#ITALIANO
class itaSchema(ma.Schema):
    class Meta:
        fields = ('pEs','pIta')
ita_schema = itaSchema()

#FRANCES
class frSchema(ma.Schema):
    class Meta:
        fields = ('pEs','pFr')
fr_schema = frSchema()

#------------------------ Archivo log ----------------------------
def write_file_log(cadena):
    sem.acquire()
    file = open("app/Archivo_log.txt", "a")
    file.write(cadena)
    file.close()
    sem.release()

#--- Actualiza datetime ---
def datetime_update():
    date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return date_time

#------------------------------ GETS ------------------------------
#GET_Ingles
@app.route('/en/<palabra>',methods=['GET'])
def get_en_palabra(palabra):
    enPalabra = en.query.get(palabra)
    write_file_log("[" + datetime_update() + "] - - " + request.user_agent.string + " - " + str(request.method) + "/" + str(request.url) + "\n")
    return en_schema.jsonify(enPalabra)

#GET_Italiano
@app.route('/ita/<palabra>',methods=['GET'])
def get_ita_palabra(palabra):
    itaPalabra = ita.query.get(palabra)
    write_file_log("[" + datetime_update() + "] - - " + request.user_agent.string + " - " + str(request.method) + "/" + str(request.url) + "\n")
    return ita_schema.jsonify(itaPalabra)

#GET_Frances
@app.route('/fr/<palabra>',methods=['GET'])
def get_fr_palabra(palabra):
    frPalabra = fr.query.get(palabra)
    write_file_log("[" + datetime_update() + "] - - " + request.user_agent.string + " - " + str(request.method) + "/" + str(request.url) + "\n")
    return fr_schema.jsonify(frPalabra)


#------------------------- Inicio ---------------------------
@app.route("/",methods=['GET'])
def ping():
    return jsonify({"Mensaje" : "II Proyecto - EIF212 - Sistemas Operativos - I ciclo 2022"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)