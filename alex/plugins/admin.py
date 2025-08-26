from pyrogram import filters
from pyrogram.types import Message
from modules.utils import is_admin, bot_stats
from modules.chatbot import toggle_chatbot
from config import OWNER_ID

def setup_admin_handlers(app):
    """Setup admin command handlers"""
    
    @app.on_message(filters.command("settings") & filters.user(OWNER_ID))
    async def settings_handler(client, message: Message):
        settings_text = """
⚙️ **Alex Bot Settings**

Current Configuration:
🤖 Chatbot: Enabled
💕 Romance Mode: Active  
🔞 NSFW Content: Restricted
👥 Group Features: Enabled

Use /toggle_chat to modify chatbot settings.
        """
        await message.reply_text(settings_text)
    
    @app.on_message(filters.command("toggle_chat"))
    async def toggle_chat_handler(client, message: Message):
        # Check if user is admin in group or bot owner
        if message.chat.type in ["group", "supergroup"]:
            member = await client.get_chat_member(message.chat.id, message.from_user.id)
            if member.status not in ["administrator", "creator"]:
                await message.reply_text("❌ Only admins can toggle chatbot settings!")
                return
        
        # Toggle chatbot
        new_status = await toggle_chatbot(message.chat.id, not CHATBOT_ENABLED)
        status_text = "enabled" if new_status else "disabled"
        
        await message.reply_text(f"🤖 Chatbot has been {status_text} for this chat!")
    
    @app.on_message(filters.command("stats") & filters.user(OWNER_ID))
    async def stats_handler(client, message: Message):
        stats_text = bot_stats.get_stats_text()
        await message.reply_text(stats_text)
    
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast_handler(client, message: Message):
        if len(message.command) < 2:
            await message.reply_text("Usage: /broadcast <message>")
            return
        
        broadcast_msg = message.text.split(None, 1)[1]
        # This would broadcast to all registered users/groups
        await message.reply_text(f"📢 Broadcasting message: {broadcast_msg}")
    
    @app.on_message(filters.command("ban"))
    async def ban_handler(client, message: Message):
        if message.chat.type not in ["group", "supergroup"]:
            await message.reply_text("❌ This command only works in groups!")
            return
        
        # Check admin status
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in ["administrator", "creator"] and message.from_user.id != OWNER_ID:
            await message.reply_text("❌ Only admins can use this command!")
            return
        
        if message.reply_to_message:
            user_to_ban = message.reply_to_message.from_user
            try:
                await client.ban_chat_member(message.chat.id, user_to_ban.id)
                await message.reply_text(f"🚫 {user_to_ban.mention} has been banned!")
            except Exception as e:
                await message.reply_text(f"❌ Failed to ban user: {e}")
        else:
            await message.reply_text("❌ Reply to a message to ban the user!")
