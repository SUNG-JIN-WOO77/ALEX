import random
import asyncio
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.chatbot import handle_chatbot
from modules.couples import *
from modules.media import *
from modules.utils import *
from plugins.admin import *
from plugins.fun import *
from plugins.romance import *
from config import *

def setup_handlers(app):
    """Setup all event handlers for the bot"""
    
    @app.on_message(filters.command("start"))
    async def start_handler(client, message: Message):
        user = message.from_user
        start_img = random.choice(START_IMAGES)
        
        welcome_text = f"""
🌹 **Welcome to Alex Couples Bot** 💕

Hey {user.mention}! I'm Alex, your romantic companion bot designed specially for couples! 

✨ **What I can do:**
💝 Send romantic messages and quotes
🎭 Fun couple games and activities  
🤖 AI-powered chatbot (powered by Gemini)
🖼️ Beautiful romantic images and stickers
🎵 Couple songs and entertainment
🔥 Spicy content for intimate moments
👥 Group management features

**Commands:**
/help - Show all commands
/couple - Couple features
/chat - Toggle AI chatbot
/romantic - Romantic content
/spicy - Adult content (18+)

Made with ❤️ for couples by {OWNER_USERNAME}
        """
        
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("💕 Couple Features", callback_data="couple_menu")],
            [InlineKeyboardButton("🤖 AI Chat", callback_data="ai_chat"),
             InlineKeyboardButton("🌹 Romance", callback_data="romance_menu")],
            [InlineKeyboardButton("📞 Support", url=SUPPORT_CHAT),
             InlineKeyboardButton("📢 Updates", url=UPDATES_CHANNEL)]
        ])
        
        await message.reply_photo(
            photo=start_img,
            caption=welcome_text,
            reply_markup=keyboard
        )
    
    @app.on_message(filters.command("help"))
    async def help_handler(client, message: Message):
        help_text = """
🔥 **Alex Couples Bot Commands** 💕

**🌹 Romance & Love:**
/quote - Random romantic quote
/love - Love calculator  
/kiss - Send a kiss
/hug - Send a warm hug
/propose - Romantic proposal
/date - Plan a date idea

**🎮 Fun & Games:**
/truth - Truth or dare
/compatibility - Check compatibility
/couple_game - Couple games
/riddle - Romantic riddles

**🤖 AI Features:**
/chat - Toggle AI chatbot
/ask - Ask AI anything
/poem - Generate love poem

**🔥 Spicy Content (18+):**
/hot - Hot images
/spicy - Spicy stickers
/nsfw - NSFW content
/roleplay - Role-play ideas

**👥 Group Features:**
/couple_register - Register as couple
/anniversary - Set anniversary
/relationship_status - Check status

**⚙️ Admin Commands:**
/settings - Bot settings
/toggle_chat - Enable/disable chatbot in group
/ban - Ban user (admin only)
/unban - Unban user (admin only)

**ℹ️ Info Commands:**
/ping - Check bot speed
/alive - Bot status  
/stats - Bot statistics
/about - About the bot

💝 **Made with love for couples!**
        """
        
        await message.reply_text(help_text)
    
    @app.on_message(filters.command("ping"))
    async def ping_handler(client, message: Message):
        ping_img = random.choice(PING_IMAGES)
        ping_text = "🏓 **Pong!** \n\n💕 Alex is online and ready to spread love!"
        
        await message.reply_photo(
            photo=ping_img,
            caption=ping_text
        )
    
    @app.on_message(filters.command("alive"))
    async def alive_handler(client, message: Message):
        alive_img = random.choice(ALIVE_IMAGES)
        alive_text = f"""
💖 **Alex is Alive & Loving!** 

🤖 Bot Status: **Online**
💕 Couples Served: **1000+**
🌹 Love Spread: **Infinite**
⚡ Response Time: **Lightning Fast**

Owner: {OWNER_USERNAME}
Version: v1.0.0
        """
        
        await message.reply_photo(
            photo=alive_img, 
            caption=alive_text
        )
    
    # Chatbot handler
    @app.on_message(filters.text & ~filters.command(["start", "help", "ping", "alive"]))
    async def message_handler(client, message: Message):
        # Check if message should be handled by chatbot
        if CHATBOT_ENABLED and message.text and not message.text.startswith('/'):
            await handle_chatbot(client, message)
    
    # Callback query handlers
    @app.on_callback_query()
    async def callback_handler(client, callback_query):
        data = callback_query.data
        
        if data == "couple_menu":
            text = """
💕 **Couple Features Menu**

Choose what you'd like to explore:
            """
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💝 Love Calculator", callback_data="love_calc")],
                [InlineKeyboardButton("🎮 Couple Games", callback_data="couple_games")],
                [InlineKeyboardButton("📅 Anniversary", callback_data="anniversary")],
                [InlineKeyboardButton("🔙 Back", callback_data="main_menu")]
            ])
            
            await callback_query.edit_message_text(text, reply_markup=keyboard)
        
        elif data == "romance_menu":
            text = """
🌹 **Romance Menu**

Select your romantic preference:
            """
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("💕 Love Quotes", callback_data="love_quotes")],
                [InlineKeyboardButton("🖼️ Romantic Images", callback_data="romantic_images")], 
                [InlineKeyboardButton("🎵 Love Songs", callback_data="love_songs")],
                [InlineKeyboardButton("🔙 Back", callback_data="main_menu")]
            ])
            
            await callback_query.edit_message_text(text, reply_markup=keyboard)

# Import specific command handlers
from plugins.romance import setup_romance_handlers
from plugins.fun import setup_fun_handlers  
from plugins.admin import setup_admin_handlers

# Setup plugin handlers
def setup_plugin_handlers(app):
    setup_romance_handlers(app)
    setup_fun_handlers(app)
    setup_admin_handlers(app)
