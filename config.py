import os


class Config(object):
    API_HASH = os.environ.get("API_HASH","29edd7420d528140c7a04bd47486886f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5638811601:AAEFjbHf8VzVx_0dBokFBJvu9amMKxKrVdE")
    TELEGRAM_API = os.environ["TELEGRAM_API", "3334521"]
    OWNER = os.environ.get("OWNER", "5079629749")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "aryan_kumar_1082")
    PASSWORD = os.environ.get("PASSWORD","1234")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aryan6969:Aryan6969@cluster0.krhmwhe.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1001789352719")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
