import os
from webbrowser import get

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "qwertyuiopasdfghjklzxcvbnm"