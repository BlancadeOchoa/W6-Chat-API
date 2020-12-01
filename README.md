# W6-Chat-API

The **goal of the project** was to **create an API** that would allow executing several requests to a database. As well as using **NLTK sentiment analysis**, a type of data mining to analyze a given text and extract conclusions from it .

- Create an API

- NLTK sentiment analysis


![Getting Started](pictures/goal.jpg)


# Create an API:
Firstly I used *Flask*, a framework that allowed me to build the API in Python. Secondly, I decided to use *MySQL* as the database to store the information requested and inserted through the API.

The initial endpoints given in the project were;

1. User endpoints

    - **(GET) /user/create/** --> Create a user and save into DB

2. Chat endpoints

    - **(GET) /chat/create** --> Create a conversation to load messages
    - **(GET) /chat/adduser** --> Add a user to a chat
    - **(GET or POST) /chat/addmessage** --> Add a message to the conversation. 
    - **(GET) /chat/list** --> Get all messages from chat_id
    - **(GET) /chat/sentiment** --> Analyze messages from chat_id. Use NLTK sentiment analysis package for this task
    
This means we had to create functions in order to fulfil these.

## Steps followed:

1. Create the scheme used in MySQL in order to later insert and extract information from it.
2. Create a file in VSC = *db_mYSQL_connection*, where the connection to the db and the functions that fulfil the queries are designed.
3. Create a new file = *endpoints*, where the routes that we will be using to call the API are generated.

To corroborate whether the queries work or not, I used a jupyter-notebook file called *w6_requests* where I execute every endpoint to later call the tables from the db and corroborate the API, its endpoints and functions work properly.


# NLTK sentiment analysis

The process of analyzing natural language and making sense of it falls under the field of Natural Language Processing (NLP). Sentiment analysis is a common NLP task, which involves classifying texts or parts of texts into a pre-defined sentiment. Therefore we use NLTK, a commonly used NLP library in Python, to analyze textual data.

Therefore, I created a jupyter-notebook file in wich with the messages extracted from a group chat, I used NLTK to analyze the overall sentiments.

# Challenges faced

![Getting Started](pictures/obstacle.png)

Many challenges were faced throughout the project, some of them where;
-  Understanding the project itself and how was I going to approach it.

- Learning about flask and how the framework works. 

- Creating multiple times the scheme in MySQL due to the need for making modifications as the project advanced.

- Introducing multiple parameters into a function to later call while executing the endpoints.

- Understanding how the NTLK endpoint works, rather than doing it separately in a jupyter-notebook file.



