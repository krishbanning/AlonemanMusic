#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "35776785"))
        self.API_HASH = getenv("API_HASH", "06ea86923bf5d34bf1572092ed6e3422)

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8774921393:AAFDqggJJkEkuAGSxdQjOWbBIZe4nQrmu80")
        self.MONGO_URL = getenv("MONGO_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003601301106"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7832349983"))
        
        self.SESSION1 = getenv("SESSION", "BQIh6REArTSBgv6Q1RTC1qw3sC5K9EMoEPJKibcxnmQw6BHl-krnarl2blmzXjNVL5pmMBoL9nsYC8hUtbr0Nuf5lBVqABOLGdqmbKHJIlHmMvalm5vUZkBRqXQzPfRohTHiSi9BrdtYMNXyQS9aAnzKGI4cfIORQdlNeZNmsKq8qjDudH04DFiJTzgF44uLQFve8ddfFT9eOmQjpCNkM0hZRGk8aI7z_MdBaeWcs2_YMpsoxFnEhs3gggQzPf2s8a-dNmHXHgYiq_DoZ1xtIpI8kZET_aLmFgh0OvhBFvP1j50n0TLdsovPR6lZ-eOjW2l_k4ThvLQdP-FiqGQ616xAdEjG4QAAAAHHwm12AA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Axynetwork")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Axychats")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY", "INFLEX68575028D")
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
