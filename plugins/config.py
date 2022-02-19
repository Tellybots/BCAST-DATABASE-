import os

class Config(object):

    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}
