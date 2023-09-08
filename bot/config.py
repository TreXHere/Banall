import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", None)
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH' '72f11aec1dd3e5764554d477341a3d0b')
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID', '21364355'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
