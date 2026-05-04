import re
import difflib

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"http\S+", "", texto)
    texto = re.sub(r"[^a-zA-Z0-9 ]", "", texto)
    return texto.strip()

def similaridade(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()
