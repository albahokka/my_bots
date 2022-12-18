"""Importing modules to create a bot"""
import config_gifanimeeeeebot
import telebot
import subprocess
import time

nmb = list(range(0, 10001))

def anime(a, b, m):
    subprocess.Popen([a, b, m])

def gifan(message):
    if len(str(message.text)) == 1:
        op = 'output_gif_' + '0000' + str(message.text) + '.gif'
    elif len(str(message.text)) == 2:
        op = 'output_gif_' + '000' + str(message.text) + '.gif'
    elif len(str(message.text)) == 3:
        op = 'output_gif_' + '00' + str(message.text) + '.gif'
    elif len(str(message.text)) == 4:
        op = 'output_gif_' + '0' + str(message.text) + '.gif'
    elif len(str(message.text)) == 5:
        op = 'output_gif_' + str(message.text) + '.gif'
    gif_way = 'C:/Users/Albinus/Desktop/python albinka/bots/gifanimeeeeebot/'\
              + op
    arg = 'rb'

    bot.send_animation(message.chat.id, animation=open(gif_way, arg))


"""Token transfer to the bot from the module"""
bot = telebot.TeleBot(config_gifanimeeeeebot.token)

"""Variation of the start of the bot"""
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.reply_to(message, 'Hello, send me any positive number!')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, '''
    To get a gif 🤗:
1. Enter any positive number
2. Wait a couple of seconds''')

"""Setting the bot's response to the content in the form of text"""
@bot.message_handler(content_types=["text"])
def number(message):
    for i in nmb:
        message.text = int(message.text)
        i = message.text
        if i > 0 and i < 10001:
            bot.reply_to(message, 'Good choice! One second...')
            i = str(i)
            anime('python', 'gififyThisAnimeDoesNotExist.py', i)
            time.sleep(30)
            gifan(message)
            break
        else:
            bot.send_message(message.chat.id, 'This is not an appropriate '
                                              'number... Try again.')
            break

"""Exclusion of stopping the bot in case of an error"""
if __name__ == '__main__':
    bot.infinity_polling()
