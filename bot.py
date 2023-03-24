import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
openai.api_key = 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

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот Паши. Чем могу помочь?")

def echo(update, context):
    question = update.message.text
    response = openai.Completion.create(
        engine="davinci", prompt=question, temperature=0.5, max_tokens=1024, n=1,stop=None,timeout=None,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def main():
    updater = Updater(token=os.environ["5828769239:AAG-5_kIhb0XzJp93CWOVlLm9IvpfpG-PjM"], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
