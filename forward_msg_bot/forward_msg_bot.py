"""Importing modules to create a bot"""
import config_msg_bot
import telebot

"""Token transfer to the bot from the module"""
bot = telebot.TeleBot(config_msg_bot.token)

"""Variation of the start of the bot"""
# @bot.message_handler(commands=['start'])
# def send_start(message):
#     bot.reply_to(message, 'Привет!')

"""Option to launch a bot with sending photos by link"""
photo_url = 'https://octobercinema.ru/wp-content/uploads/a/1/c/a1ce1f489c0b1c3153c266a92e391ea1.png'

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_photo(message.chat.id, photo=photo_url, caption='Привет!')

"""Option to launch a bot with sending photos via a local path"""
# photo_way = 'C:/Users/Albinus/Desktop/барахло/' \
#             '372027db4c3a56d8bf06741acc3b69f5.png'
# arg= 'rb'
#
# @bot.message_handler(commands=['start'])
# def send_start(message):
#     bot.send_photo(message.chat.id, photo=open(photo_way, arg),
#     caption='Привет!')

"""Setting the bot's response to the content in the form of text"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if str(message.chat.id)[0] != '-':
        bot.send_message(config_msg_bot.my_id,
                         str(message.chat.id) + ' - id человека: '
                         + message.text)
    else:
        bot.send_message(config_msg_bot.my_id, str(message.chat.id) +
                         ' - id группы: ' + message.text)

    if config_msg_bot.e_id == message.from_user.id:
        bot.send_message(message.chat.id, 'ты - человек-паук')
    else:
        pass


    # markup = types.ReplyKeyboardMarkup()
    # buttonA = types.KeyboardButton('A')
    # buttonB = types.KeyboardButton('B')
    # buttonC = types.KeyboardButton('C')
    #
    # markup.row(buttonA, buttonB)
    # markup.row(buttonC)
    #
    # bot.send_message(message.chat.id, 'It works!', reply_markup=markup)

"""Exclusion of stopping the bot in case of an error"""
if __name__ == '__main__':
    bot.infinity_polling()
