import asyncio
import random
import re
from datetime import datetime, timedelta
from pyrogram.types import Message

def is_admin(message: Message):
    """Check if user is admin"""
    from config import OWNER_ID
    return message.from_user.id == OWNER_ID

def get_user_mention(user):
    """Get user mention string"""
    if user.username:
        return f"@{user.username}"
    else:
        return f"[{user.first_name}](tg://user?id={user.id})"

def format_time_delta(td):
    """Format time delta to readable string"""
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    if days > 0:
        return f"{days} days, {hours} hours"
    elif hours > 0:
        return f"{hours} hours, {minutes} minutes"
    else:
        return f"{minutes} minutes"

def generate_heart_pattern():
    """Generate cute heart pattern"""
    hearts = ["💕", "💖", "💝", "💗", "💘", "💙", "💚", "💛", "🧡", "❤️"]
    pattern = ""
    for _ in range(3):
        pattern += random.choice(hearts)
    return pattern

async def typing_simulation(client, chat_id, duration=2):
    """Simulate typing for more natural feel"""
    await client.send_chat_action(chat_id, "typing")
    await asyncio.sleep(duration)

def clean_text(text):
    """Clean and format text"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_romantic_emoji():
    """Get random romantic emoji"""
    romantic_emojis = ["💕", "💖", "💝", "💗", "💘", "🌹", "💐", "😘", "🥰", "😍", "❤️"]
    return random.choice(romantic_emojis)

class Statistics:
    """Simple statistics tracker"""
    
    def __init__(self):
        self.stats = {
            'messages_sent': 0,
            'couples_registered': 0,
            'love_quotes_sent': 0,
            'games_played': 0,
            'start_time': datetime.now()
        }
    
    def increment(self, stat_name):
        """Increment a statistic"""
        if stat_name in self.stats:
            self.stats[stat_name] += 1
    
    def get_uptime(self):
        """Get bot uptime"""
        return datetime.now() - self.stats['start_time']
    
    def get_stats_text(self):
        """Get formatted statistics"""
        uptime = self.get_uptime()
        return f"""
📊 **Alex Bot Statistics**

⏰ Uptime: {format_time_delta(uptime)}
💌 Messages Sent: {self.stats['messages_sent']}
💕 Couples Registered: {self.stats['couples_registered']}  
🌹 Love Quotes Sent: {self.stats['love_quotes_sent']}
🎮 Games Played: {self.stats['games_played']}

💝 Spreading love since startup!
        """

# Global statistics instance
bot_stats = Statistics()

# Couple names generator
CUTE_COUPLE_NAMES = [
    "Lovebirds", "Sweethearts", "Darlings", "Honeykins", 
    "Cupcakes", "Butterflies", "Starlight", "Moonbeams",
    "Sunshine", "Rainbows", "Angels", "Precious"
]

def generate_couple_name():
    """Generate cute couple name"""
    return random.choice(CUTE_COUPLE_NAMES)
