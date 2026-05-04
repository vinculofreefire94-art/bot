import time

historico = {}
warnings = {}

def add_history(texto):
    historico[len(historico)] = {
        "texto": texto,
        "tempo": time.time()
    }

def get_history():
    return list(historico.values())

def add_warning(user_id):
    warnings[user_id] = warnings.get(user_id, 0) + 1
    return warnings[user_id]
