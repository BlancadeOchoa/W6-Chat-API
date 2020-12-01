from flask import Flask
#Request allows to add methods to routes
#jsonify will encode python dictionaries into json strings

"""
from flask_sqlalchemy import SQLAlchemy #allows us to interact with the database
from flask_marshmallow import Marshmallow #serialization, esquema con el que interactuar
import os

"""
app = Flask(__name__)


# CONFIGURACION BASICA DE DONDE NOS ESTAMOS CONECTANDO

#Direccion de la base de datos = mysql + modulo de conexion : // direccion donde esta nuestra base de datos
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flaskmysql'

#Configuracion por defecto para que no de aviso al ejecutar
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#db = SQLAlchemy(app)
#ma = Marshmallow(app)

#definir que voy a guardar dentro de la base de datos
