import telebot

bot = telebot.TeleBot("6659548659:AAHlJqnQBAjJmgQQrPZOMLbw54VJKwoMAuc")
chat_id = -1001992227190   

@bot.message_handler(commands=["start"])
def privet(message):
    bot.send_message(message.chat.id, "Привет, если ты желаешь поделиться новостями, то пиши сюда, твоя новость будет перенаправлена к админам, которые рассмотрят твою новость")

@bot.message_handler(func=lambda message: True)
def peresilka(message):
    if message.chat.id != chat_id:
        if message.text:
            bot.forward_message(chat_id, message.chat.id, message.message_id)
        elif message.photo:
            bot.send_photo(chat_id, message.photo[-1].file_id)
        elif message.video:
            bot.send_video(chat_id, message.video.file_id)
        elif message.sticker:
            bot.send_sticker(chat_id, message.sticker.file_id)
        elif message.voice:
            bot.send_voice(chat_id, message.voice.file_id)
        elif message.video_note:
            bot.send_video_note(chat_id, message.video_note.file_id)

bot.polling()
