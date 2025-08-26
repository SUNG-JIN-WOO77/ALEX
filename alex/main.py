import asyncio
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from event import setup_handlers

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

class AlexBot:
    def __init__(self):
        self.app = Client(
            "alex_couples_bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN
        )
        
    async def start_bot(self):
        """Start the bot and setup handlers"""
        await self.app.start()
        setup_handlers(self.app)
        logger.info("✨ Alex Couples Bot is now online! 💕")
        
        # Keep the bot running
        await self.app.idle()
        
    async def stop_bot(self):
        """Stop the bot gracefully"""
        await self.app.stop()
        logger.info("Alex Couples Bot stopped.")

async def main():
    bot = AlexBot()
    try:
        await bot.start_bot()
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        await bot.stop_bot()

if __name__ == "__main__":
    asyncio.run(main())
