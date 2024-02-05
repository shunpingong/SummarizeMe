import google.generativeai as genai
import telebot

genai.configure(api_key="AIzaSyDm0q1l4WqjstZKJtot1Ps0UkdJv8BF9SA")

# Set up the model
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 500,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def handle_message(message):
    user_message = message.text
    
    # Check for empty message
    if user_message == "":
        bot.reply_to(message, "Sorry, you mustn't write an empty message")    
    try:
        prompt = [user_message]
        print("User's Input:", user_message)
        response = model.generate_content(prompt)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Sorry, an error occurred. Please try again")

bot = telebot.TeleBot("6855178474:AAHifutwhHodNZ2mgF5R_HG_65JuS9TXabM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "SummarizeMe: Ask me anything.")

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
  handle_message(message)

if __name__ == "__main__":
  while True:
    bot.polling()