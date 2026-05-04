import telebot
import time

from config import *
from utils import limpar_texto, similaridade
from storage import get_history, add_history, add_warning
from growth import add_ref
from scheduler import start_scheduler

bot = telebot.TeleBot(TOKEN)

start_scheduler()

# ---------------- REF SYSTEM ----------------
@bot.message_handler(commands=['start'])
def start(message):
    args = message.text.split()

    if len(args) > 1:
        ref_id = args[1].replace("ref_", "")
        try:
            total = add_ref(int(ref_id))
            bot.send_message(message.chat.id,
                f"🔥 Bem-vindo!\nConvites do teu referrer: {total}"
            )
        except:
            pass

# ---------------- MODERAÇÃO ----------------
@bot.message_handler(func=lambda message: True)
def handle(message):

    if message.chat.id != GRUPO_ID:
        return

    if not message.text:
        return

    texto = limpar_texto(message.text)
    tempo = time.time()

    # anti-duplicado
    for msg in get_history():
        sim = similaridade(texto, msg["texto"])

        if sim > SIMILARIDADE_LIMITE:
            if tempo - msg["tempo"] < TEMPO_LIMITE:

                try:
                    bot.delete_message(message.chat.id, message.message_id)

                    warns = add_warning(message.from_user.id)

                    bot.send_message(
                        message.chat.id,
                        f"⚠️ @{message.from_user.username} warning {warns}/{MAX_WARNINGS}"
                    )

                    if warns >= MAX_WARNINGS:
                        bot.kick_chat_member(message.chat.id, message.from_user.id)

                except:
                    pass
                return

    add_history(texto)

# ---------------- LOOP ----------------
while True:
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print(e)
        time.sleep(5)
