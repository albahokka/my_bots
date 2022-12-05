import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["start"])
def repeat_all_messages(message):
    if str(message.chat.id)[0] == '-':
        bot.send_message(config.my_id, str(message.chat.id) + ' - id группы: '
                         + message.text)
    else:
        bot.send_message(config.my_id, str(message.chat.id) + ' - id человека: '
                         + message.text)

    if message.from_user.id == config.e_id:
        bot.send_message(message.chat.id, 'ты - человек-паук')
    else:
        pass

if __name__ == '__main__':
     bot.infinity_polling()
