import os
import sys
from os import getenv
from dotenv import load_dotenv
from requests import get

load_dotenv()

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

HEROKU_API_KEY = os.environ.get("HEROKU_APIKEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
UPSTREAM_REPO_URL = os.environ.get("UPSTREAM_REPO_URL","https://github.com/jattpawan/evilbot")
