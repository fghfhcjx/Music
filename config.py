from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/79062c890920b080a302f.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/79062c890920b080a302f.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Yis35qS48To1MTM0")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ALM7NY")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1831414453").split()))


FAILED = "https://telegra.ph/file/79062c890920b080a302f.jpg"
