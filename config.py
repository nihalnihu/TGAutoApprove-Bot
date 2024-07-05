import os
from os import getenv
from dotenv import load_dotenv

load_dotenv('sample.env')
#Necessary Variables 
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN") #Put your bot token here
CHANNEL = os.getenv("CHANNEL") #Your public channel username without @ for force subscription.
MONGO = os.getenv("MONGO") #Put mongo db url here
#Optional Variables
OWNER_ID = os.getenv("OWNER_ID")) #Go to and type /id and put that value here. 
FSUB = os.getenv("FSUB", True) #Set this True if you want to enable force subscription from users else set to False.
