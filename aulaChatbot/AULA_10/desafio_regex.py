# =====================================================================
# DESAFIO "O FILTRO ANTI-DESPERDÍCIO" (Regex, sem IA no processamento)
# =====================================================================
import re

# Mensagem de teste que deve ser processada:
mensagem = "Atenção: estamos doando 35 lt de leite fresco que vence em 2 dias!"

# PADRÕES REGEX
# número (inteiro ou decimal com ponto/vírgula) + unidade (lt, litros, kg, quilos)
padrao_qtd = r'(\d+(?:[\.,]\d+)?)\s*(lt|litros?|kg|quilos?)\b'
# número + "dia" ou "dias"
padrao_dias = r'(\d+)\s*dias?\b'
# o alimento é a palavra que vem depois de "<qtd> <unidade> de"
padrao_alimento = r'\d+(?:[\.,]\d+)?\s*(?:lt|litros?|kg|quilos?)\s+de\s+(\w+)'


def filtro_anti_desperdicio(texto):
    qtd = re.search(padrao_qtd, texto, re.IGNORECASE)
    dias = re.search(padrao_dias, texto, re.IGNORECASE)
    alimento = re.search(padrao_alimento, texto, re.IGNORECASE)

    nome = alimento.group(1).capitalize() if alimento else "Não identificado"
    if qtd:
        quantidade = f"{float(qtd.group(1).replace(',', '.'))} {qtd.group(2).lower()}"
    else:
        quantidade = "Não identificada"

    # Perecível: vence em até 3 dias = urgência ALTA
    if dias is None:
        urgencia = "BAIXA (sem validade informada)"
    elif int(dias.group(1)) <= 3:
        urgencia = f"ALTA (Vence em {dias.group(1)} dias)"
    else:
        urgencia = f"NORMAL (Vence em {dias.group(1)} dias)"

    return f"Alimento: {nome} | Quantidade: {quantidade} | Urgência: {urgencia}"


# Saída esperada no print:
# Alimento: Leite | Quantidade: 35.0 lt | Urgência: ALTA (Vence em 2 dias)
print(filtro_anti_desperdicio(mensagem))

# Testes extras com mensagens bagunçadas
for extra in [
    "oi!! tenho 2,5 kg de arroz pra doar, vence em 10 dias",
    "DOANDO 12 litros de suco de uva, vence em 1 dias",
    "tenho comida sobrando",
]:
    print(f"{extra!r} -> {filtro_anti_desperdicio(extra)}")
