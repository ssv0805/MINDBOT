
import random
from textblob import TextBlob
import re

# Simple conversation memory
conversation_history = []
user_emotional_state = None

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

# Enhanced keywords and patterns
ANXIETY_KEYWORDS = ['anxious', 'anxiety', 'worried', 'nervous', 'panic', 'stressed', 'overwhelmed', 'scared', 'fear']
DEPRESSION_KEYWORDS = ['sad', 'depressed', 'hopeless', 'empty', 'lonely', 'worthless', 'tired', 'exhausted', 'down']
ANGER_KEYWORDS = ['angry', 'furious', 'mad', 'frustrated', 'irritated', 'annoyed', 'upset', 'pissed']
GRATITUDE_KEYWORDS = ['grateful', 'thankful', 'blessed', 'appreciate', 'lucky', 'happy', 'joy']
CONFUSION_KEYWORDS = ['confused', 'lost', 'unsure', 'dont know', "don't know", 'uncertain', 'mixed feelings']
LONELINESS_KEYWORDS = ['lonely', 'alone', 'isolated', 'no one understands', 'nobody cares', 'by myself']
EXCITEMENT_KEYWORDS = ['excited', 'thrilled', 'pumped', 'can\'t wait', 'amazing', 'awesome', 'fantastic']
CRISIS_KEYWORDS = ['suicide', 'kill myself', 'end it all', 'not worth living', 'better off dead', 'hurt myself', 'self harm']

# Relationship and social keywords
RELATIONSHIP_KEYWORDS = ['friend', 'boyfriend', 'girlfriend', 'partner', 'family', 'mom', 'dad', 'sister', 'brother', 'crush', 'colleague']
CONFLICT_KEYWORDS = ['fight', 'argument', 'refused', 'rejected', 'ignored', 'betrayed', 'hurt me', 'disappointed', 'let me down']

def analyze_context(user_input):
    """Analyze the context and content of user input more deeply"""
    user_input_lower = user_input.lower()
    
    # Check for relationship conflicts first
    if any(keyword in user_input_lower for keyword in RELATIONSHIP_KEYWORDS) and any(keyword in user_input_lower for keyword in CONFLICT_KEYWORDS):
        return "relationship_conflict"
    
    # Check for refusal/rejection scenarios
    if "refused" in user_input_lower or "won't" in user_input_lower or "wouldn't" in user_input_lower:
        return "refusal_issue"
    
    # Check for help/support disappointment
    if ("help" in user_input_lower or "always" in user_input_lower) and ("but" in user_input_lower or "didn't like" in user_input_lower):
        return "disappointment_help"
    
    # Check for device sharing issues
    if ("laptop" in user_input_lower or "computer" in user_input_lower or "phone" in user_input_lower) and ("refused" in user_input_lower or "won't" in user_input_lower):
        return "device_sharing"
    
    if "password" in user_input_lower or "personal" in user_input_lower:
        return "privacy_boundary"
    
    return None

def get_contextual_response(context, user_input):
    """Get responses based on context analysis"""
    if context == "relationship_conflict":
        return "It sounds like you're having some difficulties with someone close to you. 💙 Relationship conflicts can be really painful. Would you like to talk about what happened and how it made you feel?"
    
    elif context == "refusal_issue":
        return "I understand that being refused or told 'no' can feel hurtful, especially from someone you trust. 🫂 Sometimes people have their own reasons for setting boundaries. How did this situation make you feel?"
    
    elif context == "disappointment_help":
        return "I can hear the disappointment in your words. 💙 It really hurts when we feel like we're always there for someone, but they don't reciprocate when we need something. Your feelings are completely valid - it's natural to feel let down when this happens. Sometimes people have different ways of showing care, or they might have boundaries we don't fully understand. What hurt you the most about this situation?"
    
    elif context == "device_sharing":
        return "I can understand feeling hurt when someone doesn't want to share their personal devices. 💻 Many people keep their devices private for security, personal reasons, or just comfort. It doesn't necessarily reflect how they feel about you as a friend. What's bothering you most about this situation?"
    
    elif context == "privacy_boundary":
        return "It can feel disappointing when someone won't share something personal with us. 💭 But everyone has a right to privacy and personal boundaries. Perhaps your friend has reasons for keeping their password private - it's actually a good security practice. How are you processing these feelings?"
    
    return None

def get_bot_response(user_input):
    global conversation_history, user_emotional_state
    
    if not user_input or len(user_input.strip()) == 0:
        return "I'm here to listen. What's on your mind? 💙"
    
    # Add to conversation history
    conversation_history.append(user_input.lower())
    if len(conversation_history) > 10:  # Keep last 10 messages
        conversation_history.pop(0)
    
    user_input_lower = user_input.lower()
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity
    
    # Crisis detection - highest priority
    if any(keyword in user_input_lower for keyword in CRISIS_KEYWORDS):
        return "⚠️ I'm very concerned about you right now. Please reach out for immediate help:\n\n🆘 **Crisis Hotlines:**\n• National Suicide Prevention Lifeline: 988\n• Crisis Text Line: Text HOME to 741741\n• International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/\n\nYou matter, and there are people who want to help you through this. Please don't face this alone. 💙"
    
    # Track emotional state
    if any(keyword in user_input_lower for keyword in DEPRESSION_KEYWORDS):
        user_emotional_state = "sad"
    elif any(keyword in user_input_lower for keyword in ANXIETY_KEYWORDS):
        user_emotional_state = "anxious"
    elif any(keyword in user_input_lower for keyword in ANGER_KEYWORDS):
        user_emotional_state = "angry"
    
    # Analyze context first
    context = analyze_context(user_input)
    if context:
        contextual_response = get_contextual_response(context, user_input)
        if contextual_response:
            return contextual_response
    
    # Check for specific mental health keywords
    if any(keyword in user_input_lower for keyword in ANXIETY_KEYWORDS):
        return "I understand you're feeling anxious. 🌊 Try taking some deep breaths with me - in for 4, hold for 4, out for 4. Would you like to talk about what's making you feel this way?"
    
    if any(keyword in user_input_lower for keyword in DEPRESSION_KEYWORDS):
        return "I hear that you're going through a difficult time. 🌙 Your feelings are valid, and it's brave of you to reach out. Even small steps forward count. What's one small thing that brought you even a tiny bit of comfort today?"
    
    if any(keyword in user_input_lower for keyword in ANGER_KEYWORDS):
        return "It sounds like you're feeling really frustrated right now. 🔥 Anger can be a valid response to difficult situations. Would it help to talk about what triggered these feelings?"
    
    if any(keyword in user_input_lower for keyword in GRATITUDE_KEYWORDS):
        return "I love hearing about gratitude! 🌟 Focusing on what we're thankful for can be so powerful. What else has been bringing you joy lately?"
    
    if any(keyword in user_input_lower for keyword in CONFUSION_KEYWORDS):
        return "It sounds like you're feeling uncertain about something. 🤔 That's completely normal - life can be confusing sometimes. Would you like to talk through what's making you feel unsure?"
    
    if any(keyword in user_input_lower for keyword in LONELINESS_KEYWORDS):
        return "I hear that you're feeling lonely right now. 🫂 That can be really difficult to experience. Remember that feeling alone doesn't mean you are alone - I'm here with you. What's been making you feel this way?"
    
    if any(keyword in user_input_lower for keyword in EXCITEMENT_KEYWORDS):
        return "I can feel your excitement! ✨ That's wonderful! It's so great when something makes us feel energized and happy. What's got you feeling so excited?"
    
    # Better handling of short responses
    if user_input_lower in ['yes', 'yeah', 'yep', 'ok', 'okay']:
        return "I'm glad you're open to talking about it. 💙 Take your time - what would you like to share with me?"
    
    if user_input_lower in ['no', 'nah', 'not really']:
        return "That's perfectly okay. 🌸 Sometimes we need time to process things. I'm here whenever you feel ready to talk, or if you just want some company."
    
    # Greetings
    if any(greeting in user_input_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good evening']):
        return "Hello there! 👋 I'm MindBot, your mental health companion. I'm here to listen and support you. How are you feeling today?"
    
    # Goodbye
    if any(farewell in user_input_lower for farewell in ['bye', 'goodbye', 'see you', 'talk later']):
        return "Take care of yourself! 🌸 Remember, I'm always here when you need someone to talk to. You're stronger than you know! 💪"
    
    # Better response to vague negative feelings
    if user_input_lower in ['not great', 'bad', 'terrible', 'awful', 'horrible']:
        return "I'm sorry to hear you're not feeling great. 💙 That sounds difficult. Would you like to tell me more about what's going on? Sometimes talking about it can help lighten the load."
    
    # Default sentiment-based responses
    if sentiment_score > 0.2:
        return random.choice(POSITIVE_RESPONSES)
    elif sentiment_score < -0.2:
        return random.choice(NEGATIVE_RESPONSES)
    else:
        return random.choice(NEUTRAL_RESPONSES)
