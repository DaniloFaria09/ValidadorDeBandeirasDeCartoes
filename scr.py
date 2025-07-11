import re

# Dicionário com as regras extraídas do CSV
REGRAS_BANDEIRAS = [
    {"bandeira": "Mastercard", "prefixos": ["51-55", "2221-2720"], "digitos": [16]},
    {"bandeira": "Visa", "prefixos": ["4"], "digitos": [13, 16]},
    {"bandeira": "American Express (Amex)", "prefixos": ["34", "37"], "digitos": [15]},
    {"bandeira": "Diners Club", "prefixos": ["300-305", "36", "38-39"], "digitos": [14]},
    {"bandeira": "Discover", "prefixos": ["6011", "622126-622925", "644-649", "65"], "digitos": [16]},
    {"bandeira": "EnRoute", "prefixos": ["2014", "2149"], "digitos": [15]},
    {"bandeira": "JCB", "prefixos": ["3528-3589"], "digitos": [16]},
    {"bandeira": "Voyager", "prefixos": ["8699"], "digitos": [15]},
    {"bandeira": "Hipercard", "prefixos": ["384100", "384140", "384160", "606282", "637095"], "digitos": list(range(13, 20))},
    {"bandeira": "Aura", "prefixos": ["50"], "digitos": [16]},
]

def verifica_bandeira(numero_cartao: str) -> str:
    numero_cartao = re.sub(r'\D', '', numero_cartao)
    tamanho = len(numero_cartao)
    for regra in REGRAS_BANDEIRAS:
        if tamanho not in regra["digitos"]:
            continue
        for prefixo in regra["prefixos"]:
            if '-' in prefixo:
                inicio, fim = prefixo.split('-')
                for tam in range(len(inicio), len(fim)+1):
                    prefixo_atual = numero_cartao[:tam]
                    if prefixo_atual.isdigit() and int(inicio) <= int(prefixo_atual) <= int(fim):
                        return regra["bandeira"]
            else:
                if numero_cartao.startswith(prefixo):
                    return regra["bandeira"]
    return "Bandeira desconhecida"

# Exemplos de uso:
print(verifica_bandeira("4555 5555 5555 4444"))  # Visa
print(verifica_bandeira("5555 5555 5555 4444"))  # Mastercard
print(verifica_bandeira("378282246310005"))      # American Express (Amex)
print(verifica_bandeira("6011111111111117"))     # Discover
