
import random
from textblob import TextBlob

# Enhanced response patterns
POSITIVE_RESPONSES = [
    "I'm really glad you're feeling positive! 😊 That's wonderful to hear!",
    "Your positive energy is contagious! ✨ Keep that spirit up!",
    "It sounds like things are going well for you! 🌟 What's been the highlight?",
    "I love hearing such positivity! 😄 Care to share what's making you happy?"
]

NEGATIVE_RESPONSES = [
    "I'm sorry you're feeling down. 💙 Want to talk more about what's bothering you?",
    "That sounds really tough. 🫂 I'm here to listen without judgment.",
    "I hear that you're struggling. 💚 Sometimes just talking about it can help.",
    "It's okay to feel this way. 🌙 Would you like to share what's on your mind?"
]

NEUTRAL_RESPONSES = [
    "Thanks for sharing that with me. 💭 I'm here to listen.",
    "I appreciate you opening up. 🤝 How has your day been overall?",
    "Thank you for trusting me with your thoughts. 💫 What's been on your mind lately?",
    "I'm here for you. 🌸 Is there anything specific you'd like to talk about?"
]

# Keywords for specific mental health topics
ANXIETY_KEYWORDS = ['anxious', 'anxiety', 'worried', 'nervous', 'panic', 'stressed', 'overwhelmed']
DEPRESSION_KEYWORDS = ['sad', 'depressed', 'hopeless', 'empty', 'lonely', 'worthless', 'tired']
ANGER_KEYWORDS = ['angry', 'furious', 'mad', 'frustrated', 'irritated', 'annoyed']
GRATITUDE_KEYWORDS = ['grateful', 'thankful', 'blessed', 'appreciate', 'lucky']

def get_bot_response(user_input):
    if not user_input or len(user_input.strip()) == 0:
        return "I'm here to listen. What's on your mind? 💙"
    
    user_input_lower = user_input.lower()
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity
    
    # Check for specific mental health keywords
    if any(keyword in user_input_lower for keyword in ANXIETY_KEYWORDS):
        return "I understand you're feeling anxious. 🌊 Try taking some deep breaths with me - in for 4, hold for 4, out for 4. Would you like to talk about what's making you feel this way?"
    
    if any(keyword in user_input_lower for keyword in DEPRESSION_KEYWORDS):
        return "I hear that you're going through a difficult time. 🌙 Your feelings are valid, and it's brave of you to reach out. Even small steps forward count. What's one small thing that brought you even a tiny bit of comfort today?"
    
    if any(keyword in user_input_lower for keyword in ANGER_KEYWORDS):
        return "It sounds like you're feeling really frustrated right now. 🔥 Anger can be a valid response to difficult situations. Would it help to talk about what triggered these feelings?"
    
    if any(keyword in user_input_lower for keyword in GRATITUDE_KEYWORDS):
        return "I love hearing about gratitude! 🌟 Focusing on what we're thankful for can be so powerful. What else has been bringing you joy lately?"
    
    # Greetings
    if any(greeting in user_input_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good evening']):
        return "Hello there! 👋 I'm MindBot, your mental health companion. I'm here to listen and support you. How are you feeling today?"
    
    # Goodbye
    if any(farewell in user_input_lower for farewell in ['bye', 'goodbye', 'see you', 'talk later']):
        return "Take care of yourself! 🌸 Remember, I'm always here when you need someone to talk to. You're stronger than you know! 💪"
    
    # Default sentiment-based responses
    if sentiment_score > 0.2:
        return random.choice(POSITIVE_RESPONSES)
    elif sentiment_score < -0.2:
        return random.choice(NEGATIVE_RESPONSES)
    else:
        return random.choice(NEUTRAL_RESPONSES)
