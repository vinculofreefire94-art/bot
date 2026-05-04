import time

historico = []
avisos = {}

def adicionar_historico(texto):
    historico.append({
        "texto": texto,
        "tempo": time.time()
    })

def limpar_historico(max_size):
    if len(historico) > max_size:
        historico.pop(0)

def adicionar_aviso(user_id):
    avisos[user_id] = avisos.get(user_id, 0) + 1
    return avisos[user_id]
