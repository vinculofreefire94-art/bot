import telebot
import time

from config import *
from utils import limpar_texto, similaridade
from storage import historico, adicionar_historico, limpar_historico

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def analisar_mensagem(message):
    if message.chat.id != GRUPO_ID:
        return

    if not message.text:
        return

    texto = limpar_texto(message.text)
    tempo_atual = time.time()

    for msg in historico:
        sim = similaridade(texto, msg["texto"])

        if sim > SIMILARIDADE_LIMITE:
            if tempo_atual - msg["tempo"] < TEMPO_LIMITE:
                try:
                    bot.delete_message(message.chat.id, message.message_id)
                    bot.send_message(
                        message.chat.id,
                        f"⚠️ @{message.from_user.username}, mensagem duplicada."
                    )
                except:
                    pass
                return

    adicionar_historico(texto)
    limpar_historico(MAX_HISTORICO)


while True:
    try:
        bot.polling(non_stop=True, interval=1, timeout=20)
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(5)
