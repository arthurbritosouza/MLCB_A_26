"""
MESAFARTAI - Extração de entidades com Regex
Arquivo: src/entities.py
Descrição: transforma o texto livre do chat em dados estruturados (alimento, quantidade em kg e validade).
"""

import re
from datetime import date, timedelta


class ExtratorEntidades:
    # número (aceita 2,5 ou 2.5) seguido de kg ou quilos
    padrao_massa = r'(\d+(?:[\.,]\d+)?)\s*(?:kg|quilos?)'
    # o alimento é a palavra depois de "<quantidade> kg de" (ou "caixas de", "litros de")
    padrao_alimento = r'\d+(?:[\.,]\d+)?\s*(?:kg|quilos?|caixas?|litros?|lt)\s+de\s+(\w+)'
    # validade: "em 2 dias" ou "vence em 2 dias"
    padrao_dias = r'(\d+)\s*dias?\b'

    def processar_texto(self, texto):
        """Devolve {'alimento', 'quantidade_kg', 'data_validade'}."""
        massa = re.search(self.padrao_massa, texto, re.IGNORECASE)
        quantidade_kg = float(massa.group(1).replace(',', '.')) if massa else 1.0

        alimento = re.search(self.padrao_alimento, texto, re.IGNORECASE)
        nome = alimento.group(1).capitalize() if alimento else "Alimento não identificado"

        hoje = date.today()
        dias = re.search(self.padrao_dias, texto, re.IGNORECASE)
        if dias:
            validade = (hoje + timedelta(days=int(dias.group(1)))).isoformat()
        elif re.search(r'\bamanh[ãa]\b', texto, re.IGNORECASE):
            validade = (hoje + timedelta(days=1)).isoformat()
        elif re.search(r'\bhoje\b', texto, re.IGNORECASE):
            validade = hoje.isoformat()
        else:
            validade = "Não informada"

        return {"alimento": nome, "quantidade_kg": quantidade_kg, "data_validade": validade}


# --- TESTE DO MÓDULO EM TEMPO DE EXECUÇÃO ---
if __name__ == "__main__":
    extrator = ExtratorEntidades()
    for frase in [
        "Olá! Tenho 25 kg de tomate para doar hoje perto do centro.",
        "Quero doar 15 kg de arroz que vencem amanhã",
        "Posso entregar 2,5 quilos de feijão, vence em 3 dias",
        "Tenho comida sobrando",
    ]:
        print(f"{frase!r}\n   -> {extrator.processar_texto(frase)}")
