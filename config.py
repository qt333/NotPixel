from dotenv import load_dotenv
import os
load_dotenv()
# put yours
API_ID = os.getenv('API_ID')
API_HASH = os.getenv("API_HASH")

# =============[upgrades]================
# default is 5 level you can change it your self
PAINT_REWARD_MAX = 5 # max is 7
ENERGY_LIMIT_MAX = 5 # max is 6
RE_CHARGE_SPEED_MAX = 5 # max is 11

# ================[proxy]================
USE_PROXY = False # or put True if you want use it
# PROXIES = {
#     "http":"socks5://127.0.0.1",
#     "https":"socks5://127.0.0.1", # if you using socks4 or http only replace it with "socks5"
# }

#access to specific proxy by index
PROXIES = [
    "socks5://user:3243@127.0.0.1:8080",
    "socks5://127.0.0.1:8080"
]
