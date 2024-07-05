from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN") #Put your bot token here
CHANNEL = getenv("CHANNEL") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID")) #Go to and type /id and put that value here. 
FSUB = bool(getenv("FSUB", True)) #Set this True if you want to enable force subscription from users else set to False.
