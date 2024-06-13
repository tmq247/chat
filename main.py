import google.generativeai as genai
import telebot

# Your Telegram bot token
TOKEN = '6543379161:AAFRJFLuItZt-Ds_CdLVUcQU5tT0d7f4Yk0'

# Configure the generative AI API key
genai.configure(api_key="AIzaSyCCQesKko3O7P_J0SSbbE15Z3G6TIOc94s")

# Create a Telegram bot instance
bot = telebot.TeleBot(TOKEN)

# Handle /start, /help, and /hello commands
@bot.message_handler(commands=['start', 'help', 'hello'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Hello {name}! Ask me about anything")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_search_product(message):
    name = message.from_user.first_name
    msg = message.text
    
    # Check for empty message
    if msg == "":
        bot.reply_to(message, "Sorry, you mustn't write an empty message")
    
    try:
        bot.reply_to(message, f"Please wait a moment, {name}, before sending another message")
        
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat(history=[])

        response = chat.send_message(msg)
        print(response.text)
        
        bot.reply_to(message, response.text)
    
    except Exception as e:
        bot.reply_to(message, str(e))
        bot.reply_to(message, "Sorry, an error occurred while processing your request.")

# Start the bot's polling loop
if __name__ == "__main__":
    bot.polling()
