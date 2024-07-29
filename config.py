from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "23255238")
    API_HASH = getenv("API_HASH", "009e3d8c1bdc89d5387cdd8fd182ec15")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "6898485942:AAHztBpjqvu2nNHPrynApKpAJxbhU33Dfrg")
    OWNER_ID = int(getenv("OWNER_ID", "7078181502")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Xeno_Kakarot")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "lolpagalokigc")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002009280180"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority",
    )
    DB_NAME = getenv("DB_NAME", "ExonRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", "postgres://oocekooc:W2w0GdYOHNwvqKh047VMGjhHq_Xlb2sS@hansken.db.elephantsql.com/oocekooc")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
