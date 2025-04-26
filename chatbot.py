from textblob import TextBlob

def get_bot_response(user_input):
    blob = TextBlob(user_input)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.2:
        return "I'm really glad you're feeling positive! 😊"
    elif sentiment_score < -0.2:
        return "I'm sorry you're feeling down. Want to talk more about it?"
    else:
        return "Thanks for sharing. I'm here to listen."
