class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1270135977:AAGFxG_6gkpkLL9i9V-FBGpGrdLNLLGObKE"
    OWNER_ID = "973682688"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "@ShityBrainOfficial"
    DB_URL = 'postgres://alissadb:M@rvin2007@localhost:5432/alissadb'  # needed for any database modules
    MESSAGE_DUMP = -1001373984853 # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [973682688]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [123456789]
    WHITELIST_USERS = [973682688]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = None # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
