import time
import threading
import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

GRUPO_ID = -1003796977029

def enviar_conteudo():
    while True:
        try:
            bot.send_message(
                GRUPO_ID,
                "📊 Aula automática:\n\nRSI acima de 70 = sobrecompra\nRSI abaixo de 30 = sobrevenda"
            )
        except:
            pass

        time.sleep(36000)  # 10 horas

def start_scheduler():
    t = threading.Thread(target=enviar_conteudo)
    t.daemon = True
    t.start()
