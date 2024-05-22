import telebot

import commands_texts as ct
import config
import phrases

bot = telebot.TeleBot(config.TOKEN)


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.chat.id, ct.Start[config.lang_short])


@bot.message_handler(commands=['language'])
def language_func(message):
    args = extract_arg(message.text.lower())
    if len(args) == 0:
        bot.send_message(message.chat.id, ct.Language_text[config.lang_short])
        return
    for lang in config.languages:
        if lang in args:
            config.lang_long = lang
            config.lang_short = config.languages_short[lang]
            bot.send_message(message.chat.id, ct.Language_changed[config.lang_short])
            return


@bot.message_handler(content_types=['text'])
def text_func(message):
    text = message.text.lower()
    phrases_list = phrases.checkall(text)
    if phrases_list is None:
        return
    for phrase in phrases_list:
        text_to_send = phrase.act()
        bot.send_message(message.chat.id, text_to_send)


bot.polling(none_stop=True)

