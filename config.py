from os import getenv
from dotenv import load_dotenv

#Necessary Variables 
API_ID = int(getenv("API_ID", "4640974"))
API_HASH = getenv("API_HASH", "75343828eb25bfb382cc04ae610b1522")
BOT_TOKEN = getenv("BOT_TOKEN", "7065287929:AAEz93hgi1nH9uynKWdwH_NS17YfnKbC6XY") #Put your bot token here
CHANNEL = getenv("CHANNEL", "TG_BotCreator") #Your public channel username without @ for force subscription.
MONGO = getenv("MONGO", "mongodb+srv://mergebot:mergebot@mergebot.q6kyhd4.mongodb.net/?retryWrites=true&w=majority") #Put mongo db url here
#Optional Variables
OWNER_ID = int(getenv("OWNER_ID", 1107626477)) #Go to @ThunderrXbot and type /id and put that value here. 
FSUB = bool(getenv("FSUB", True)) #Set this True if you want to enable force subscription from users else set to False.
