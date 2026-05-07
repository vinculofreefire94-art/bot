import telebot
import time

from config import *
from utils import limpar_texto, similaridade
from storage import get_history, add_history, add_warning
from growth import add_ref
from scheduler import start_scheduler

bot = telebot.TeleBot(TOKEN)

# 🚀 inicia conteúdo automático (10h)
start_scheduler()


# ---------------- REF SYSTEM ----------------
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id != GRUPO_ID:
        return

    args = message.text.split()

    if len(args) > 1:
        try:
            ref_id = args[1].replace("ref_", "")
            total = add_ref(int(ref_id))

            bot.send_message(
                message.chat.id,
                f"""
━━━━━━━━━━━━━━
🚀 SISTEMA DE ENTRADA
━━━━━━━━━━━━━━

👤 Entrada validada por convite

📊 Total de convites do teu referenciador: {total}

⚔️ Status: ATIVO
━━━━━━━━━━━━━━
"""
            )
        except:
            pass

    else:
        bot.send_message(
            message.chat.id,
            """
━━━━━━━━━━━━━━
🧠 HOKAGE SYSTEM
━━━━━━━━━━━━━━

📊 Bem-vindo ao centro de inteligência.

⚔️ O sistema está ativo.
━━━━━━━━━━━━━━
"""
        )


# ---------------- MODERAÇÃO + INTELIGÊNCIA ----------------
@bot.message_handler(func=lambda message: True)
def handle(message):

    # 🔒 filtro de grupo
    if message.chat.id != GRUPO_ID:
        return

    if not message.text:
        return

    texto = limpar_texto(message.text)
    tempo = time.time()

    # ---------------- ANTI-DUPLICADO ----------------
    for msg in get_history():
        sim = similaridade(texto, msg["texto"])

        if sim > SIMILARIDADE_LIMITE:
            if tempo - msg["tempo"] < TEMPO_LIMITE:

                try:
                    bot.delete_message(message.chat.id, message.message_id)

                    warns = add_warning(message.from_user.id)

                    # ❌ REMOVIDO: Mensagem de aviso não será mais enviada
                    # O bot apenas deleta a mensagem silenciosamente

                    # 🔥 BAN AUTOMÁTICO
                    if warns >= MAX_WARNINGS:
                        bot.kick_chat_member(message.chat.id, message.from_user.id)

                except:
                    pass
                return

    add_history(texto)


# ---------------- LOOP ESTÁVEL ----------------
while True:
    try:
        print("🤖 Hokage System ativo...")
        bot.polling(non_stop=True, interval=1, timeout=20)

    except Exception as e:
        print("❌ Erro:", e)
        time.sleep(5)
