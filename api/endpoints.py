from api.app import app
from flask import Flask, jsonify
from flask import request
from helpers.db_MySQL_connection import get_table
from helpers.db_MySQL_connection import insert_user
from helpers.db_MySQL_connection import insert_chat 
from helpers.db_MySQL_connection import insert_user_to_chat
from helpers.db_MySQL_connection import insert_message_to_chat
from helpers.db_MySQL_connection import get_ONLYmessages_from_chat
from helpers.db_MySQL_connection import get_messages_from_chat
from bson import json_util


#Decorators
@app.route("/")
def hello_world():
    return {'Hello': 'World!'}
    
@app.route("/help")
def help():
    return {"welcome":"Welcome to my API"}

@app.route("/<name>")
def salute(name):
    return "Hello, {}!!!".format(name)
    
@app.route('/example', methods=['GET'])
def get_ex():
  return jsonify({'msg':'Is it working?'})


#EXAMPLE : CREO ENDPOINT A PARTIR DE MI PRIMERA QUERY DE MYSQL
@app.route('/sql/<name>')
def sql(name):
    return json_util.dumps(list(get_table(name)))

#USER ENDPOINTS : CREATE A USER
@app.route("/user/create/<name>")
def user_create(name):
    insert_user(name)
    return {'función':'usuario insertado'}

##CHAT ENDPOINTS : CREATE A CHAT
@app.route("/chat/create/<name>")
def chat_create(name):
    insert_chat(name)
    return {'función':'chat creado'}

##CHAT ENDPOINTS : ADD A USER TO A CHAT
@app.route("/chat/adduser/")
def chat_adduser():
    user_id = request.args.get("user")
    chat_id = request.args.get("chat")   
    
    if (user_id==None) or (chat_id==None):
        return {"error": "Insert user AND chat"}
    else:
        insert_user_to_chat(user_id, chat_id)
        return {'función':'usuario unido a chat'}

##CHAT ENDPOINTS : ADD A MESSAGE TO A CHAT
@app.route("/chat/addmessage/")
def chat_addmessage():
    user_id = request.args.get("user")
    chat_id = request.args.get("chat")   
    mssg = request.args.get("message")

    if (user_id==None) or (chat_id==None) or (mssg==None):
        return {"error": "Insert user AND chat AND message"}
    else:
        insert_message_to_chat(mssg, user_id, chat_id)
        return {'function':'message sent'}

##CHAT ENDPOINTS : GET ALL MSSG FORM A CHAT
@app.route("/chat/list/")
def chat_get_list_messages():
    
    chat_id = request.args.get("chat")   
    
    if (chat_id==None):
        return {"error": "Insert chat correctly"}
    else:
        get_messages_from_chat(chat_id)
        return {'function':'message extracted'}

@app.route("/chat/listONLY/")
def get_ONLYmessages():
    chat_id = request.args.get("chat")   
    return json_util.dumps(list(get_ONLYmessages_from_chat(chat_id)))


##SENTIMENT

