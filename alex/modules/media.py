import random
import aiohttp
import asyncio
from config import *

class MediaManager:
    def __init__(self):
        self.session = None
    
    async def get_session(self):
        """Get or create aiohttp session"""
        if not self.session:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def get_waifu_image(self, category="waifu"):
        """Get waifu/anime couple image"""
        try:
            session = await self.get_session()
            async with session.get(f"{WAIFU_API}/sfw/{category}") as response:
                data = await response.json()
                return data.get('url')
        except Exception as e:
            # Return fallback image
            return random.choice(START_IMAGES)
    
    async def get_romantic_image(self):
        """Get romantic couple image"""
        categories = ["waifu", "neko", "shinobu"]
        category = random.choice(categories)
        return await self.get_waifu_image(category)
    
    async def get_nsfw_content(self, category="blowjob"):
        """Get NSFW content (18+ only)"""
        try:
            session = await self.get_session()
            async with session.get(f"{WAIFU_API}/nsfw/{category}") as response:
                data = await response.json()
                return data.get('url')
        except Exception as e:
            return None
    
    def get_random_sticker(self, sticker_type="romantic"):
        """Get random sticker"""
        if sticker_type == "romantic":
            return random.choice(ROMANTIC_STICKERS)
        elif sticker_type == "nsfw":
            return random.choice(NSFW_STICKERS)
        else:
            return random.choice(ROMANTIC_STICKERS)
    
    def get_hot_image(self):
        """Get hot/spicy image"""
        return random.choice(HOT_IMAGES)
    
    async def close_session(self):
        """Close aiohttp session"""
        if self.session:
            await self.session.close()

# Global media manager instance
media_manager = MediaManager()

# Cute couple GIFs and images
COUPLE_GIFS = [
    "https://media.giphy.com/media/cute-couple-1.gif",
    "https://media.giphy.com/media/cute-couple-2.gif", 
    "https://media.giphy.com/media/romantic-couple.gif"
]

KISS_GIFS = [
    "https://media.giphy.com/media/kiss-1.gif",
    "https://media.giphy.com/media/kiss-2.gif"
]

HUG_GIFS = [
    "https://media.giphy.com/media/hug-1.gif", 
    "https://media.giphy.com/media/hug-2.gif"
]

async def get_couple_gif():
    """Get random couple GIF"""
    return random.choice(COUPLE_GIFS)

async def get_kiss_gif():
    """Get random kiss GIF"""  
    return random.choice(KISS_GIFS)

async def get_hug_gif():
    """Get random hug GIF"""
    return random.choice(HUG_GIFS)
