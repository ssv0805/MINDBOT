from flask import Flask, render_template, request
from chatbot import get_bot_response
from datetime import datetime
from flask import send_file  



app = Flask(__name__)

# Function to save conversation to a file
def save_to_file(user_input, bot_response):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        file.write(f"{timestamp} You: {user_input}\n")
        file.write(f"{timestamp} MindBot: {bot_response}\n\n")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_reply():
    user_input = request.args.get("msg")

     # Safety check
    if not user_input:
        return "No message received."
    response = get_bot_response(user_input)

     # 🔥 Save the conversation
    save_to_file(user_input, response)

    return response

@app.route("/download")
def download_chat():
    return send_file("chat_history.txt", as_attachment=True)

    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
