''' By MrXD | insta 8_wvu '''
import telebot

API_KEY = 'API_KEY'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message): 
  bot.send_message(message.chat.id, f'''ياهلا فيك يا {message.from_user.first_name}  نورت/ـي🤝🏾.
طريقة الاستخدام اكتب رقم الصفحه الي تبيه وتجيك.''', parse_mode='html')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  try:
    nam = int(message.text)

    url = f"https://quran.ksu.edu.sa/png_big/{nam}.png"

    bot.send_photo(message.chat.id, url)

  except ValueError:
    bot.send_message(message.chat.id,f"<strong>استخدم بس ارقام</strong>", parse_mode='html')
  
  except:
    bot.send_message(message.chat.id,f"<strong>الصفحه مو موجوده بس من 1 الى 604 :/</strong>", parse_mode='html')

bot.polling(none_stop=True)