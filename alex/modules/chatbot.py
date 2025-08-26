import google.generativeai as genai
from config import GEMINI_API_KEY, CHATBOT_ENABLED
import asyncio
import random

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Couple-themed prompts
COUPLE_PROMPTS = [
    "You are Alex, a romantic AI assistant for couples. Respond with love and care.",
    "You are a relationship counselor AI who gives romantic advice to couples.",
    "You are a flirty, romantic chatbot designed to help couples express their love."
]

async def handle_chatbot(client, message):
    """Handle chatbot conversations"""
    if not CHATBOT_ENABLED:
        return
    
    try:
        # Add typing indicator
        await client.send_chat_action(message.chat.id, "typing")
        
        user_message = message.text
        user_name = message.from_user.first_name
        
        # Create romantic context
        prompt = f"""
{random.choice(COUPLE_PROMPTS)}
User name: {user_name}
User message: {user_message}

Respond in a romantic, caring way that's appropriate for couples. Use emojis and be warm and loving in your response.
"""
        
        # Generate response
        response = model.generate_content(prompt)
        ai_response = response.text
        
        # Add some romantic flair
        romantic_emojis = ["💕", "💖", "💝", "🌹", "💐", "😘", "🥰", "😍"]
        ai_response = f"{random.choice(romantic_emojis)} {ai_response} {random.choice(romantic_emojis)}"
        
        await message.reply_text(ai_response)
        
    except Exception as e:
        error_messages = [
            "Oops! My heart skipped a beat 💕 Try again!",
            "Sorry love, I got a bit flustered 😊 Can you repeat that?",
            "My romantic circuits are overloaded 💖 Give me a moment!"
        ]
        await message.reply_text(random.choice(error_messages))

async def toggle_chatbot(chat_id, status):
    """Toggle chatbot for specific chat"""
    # This would typically save to database
    global CHATBOT_ENABLED
    CHATBOT_ENABLED = status
    return status
