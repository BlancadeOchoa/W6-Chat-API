from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

user= 'root'
password = os.getenv('pass_mysql')

mysql_url = f'mysql+mysqldb://{user}:{password}@localhost'
engine = create_engine(mysql_url)
conn = engine.connect()


##EXAMPLE : GET CONTENT OF A TABLE
def get_table(name):
    query = f"SELECT * FROM {name};"
    res = conn.execute(query)
    return res


#USER: CREATE A NEW USER
# Insert a user into the database users
def insert_user(name):
    query = f"SELECT * FROM  w6_chat.User WHERE name='{name}';"
    res = list(conn.execute(query))
    if res == []:
        query = f'INSERT INTO w6_chat.User (name) VALUES ("{name}");'
        res = conn.execute(query)
    else:
        return ('This user already exists')

#insert_user('Adri') 

##CHAT : CREATE A CHAT (no user yet)
def insert_chat(name):
    query = f"SELECT * FROM  w6_chat.Chat WHERE chat_name='{name}';"
    res = list(conn.execute(query))
    if res == []:
        query = f'INSERT INTO w6_chat.Chat (chat_name) VALUES ("{name}");'
        res = conn.execute(query)
    else:
        return ('This chat already exists')

#insert_chat('Iron')

##CHAT : WITH A CREATED CHAT -----> INSERT USER
def insert_user_to_chat(user_id, chat_id):
    query = f"SELECT * FROM  w6_chat.Chat_has_User WHERE (User_idUser='{user_id}' AND Chat_idChat='{chat_id}');"
    res = list(conn.execute(query))
    if res == []:
        query = f'INSERT INTO w6_chat.Chat_has_User VALUES ({user_id},{chat_id});'
        res = conn.execute(query)
    else:
        return ('This user is already in the chat')

##CHAT : ADD A MESSAGE TO A CHAT
def insert_message_to_chat(mssg, user_id, chat_id):
    query = f'INSERT INTO w6_chat.Messages (messages_content, User_idUser, Chat_idChat) VALUES ("{mssg}",{user_id},{chat_id});'
    res = conn.execute(query)
    return ('Message inserted correctly')

##CHAT : GET ALL MSSG FORM A CHAT
def get_messages_from_chat(chat_id):
    query = f"SELECT * FROM w6_chat.Messages WHERE (Chat_idChat='{chat_id}');"
    res = list(conn.execute(query))
    return ('Messages have been extracted correctly')

## Return ONLY the messages
def get_ONLYmessages_from_chat(chat_id):
    query = f"SELECT messages_content FROM w6_chat.Messages WHERE (Chat_idChat='{chat_id}');"
    res = conn.execute(query)
    return res

##SENTIMENT


