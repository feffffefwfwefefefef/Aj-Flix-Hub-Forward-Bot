# bot developer @im_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28814392")
    API_HASH = environ.get("API_HASH", "38d09c28822aa20a56c43c4b492efba6")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8831047951:AAGxZYUXBM2cl0VvyObTvW8BxcC4VD93UQU") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7228509851').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://files.catbox.moe/uevfz8.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ramsaranhero1:EMVwKybGR1lBF5DZ@cluster0.tst47tx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ramsaranhero1")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003952418809'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/Aj_Flix_Hub") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    FORWARD_TASKS = {}
    
