import random
import asyncio
from datetime import datetime, timedelta

# Love quotes database
LOVE_QUOTES = [
    "Love is not about how many days, months, or years you have been together. It's about how much you love each other every single day. 💕",
    "In all the world, there is no heart for me like yours. In all the world, there is no love for you like mine. 💖",
    "You are my today and all of my tomorrows. 🌹",
    "I love you not only for what you are, but for what I am when I am with you. 💝",
    "The best thing to hold onto in life is each other. 🤗",
]

# Date ideas
DATE_IDEAS = [
    "🍷 Candlelit dinner at home with your favorite playlist",
    "🌅 Sunrise/sunset picnic in a beautiful location",
    "🎬 Movie marathon with your favorite romantic films",  
    "🍳 Cook a new recipe together",
    "🌟 Stargazing session with hot chocolate",
    "🎨 Paint and sip night at home",
    "🚗 Road trip to somewhere new",
    "🏖️ Beach day with a romantic walk"
]

# Relationship milestones
MILESTONES = {
    1: "First Month - The Honeymoon Phase 💕",
    3: "Three Months - Getting Serious 💖", 
    6: "Half Year - Deep Connection 💝",
    12: "One Year Anniversary - Forever Love 🎉",
    24: "Two Years - Unbreakable Bond 💍"
}

async def get_love_quote():
    """Get a random romantic quote"""
    return random.choice(LOVE_QUOTES)

async def get_date_idea():
    """Get a random date idea"""
    return random.choice(DATE_IDEAS)

async def calculate_love_percentage(name1, name2):
    """Calculate love compatibility (fun algorithm)"""
    # Simple hash-based calculation for consistency
    combined = (name1 + name2).lower()
    hash_val = sum(ord(c) for c in combined)
    percentage = (hash_val % 50) + 50  # Ensure 50-100% for positivity
    
    if percentage >= 90:
        message = "Perfect soulmates! 💕💕💕"
    elif percentage >= 80:
        message = "Incredible match! 💖💖"  
    elif percentage >= 70:
        message = "Great compatibility! 💝💝"
    elif percentage >= 60:
        message = "Good potential! 💕"
    else:
        message = "Keep working on it! 💪"
        
    return percentage, message

async def get_relationship_advice():
    """Get random relationship advice"""
    advice = [
        "Communication is key - talk openly about your feelings 💬",
        "Small gestures matter more than grand displays 💝",
        "Always make time for each other, no matter how busy 🕰️",
        "Surprise your partner with their favorite things 🎁", 
        "Never go to bed angry - resolve conflicts with love 😴",
        "Celebrate your differences - they make you stronger together 🌈"
    ]
    return random.choice(advice)

class CoupleDatabase:
    """Simple in-memory couple database (would use MongoDB in production)"""
    
    def __init__(self):
        self.couples = {}
        self.anniversaries = {}
    
    def register_couple(self, user1_id, user2_id, anniversary_date=None):
        """Register a couple"""
        couple_id = f"{min(user1_id, user2_id)}_{max(user1_id, user2_id)}"
        self.couples[couple_id] = {
            'user1': user1_id,
            'user2': user2_id, 
            'registered': datetime.now(),
            'anniversary': anniversary_date
        }
        return couple_id
    
    def get_couple_info(self, user_id):
        """Get couple information for a user"""
        for couple_id, info in self.couples.items():
            if user_id in [info['user1'], info['user2']]:
                return couple_id, info
        return None, None

# Global couple database instance
couple_db = CoupleDatabase()
