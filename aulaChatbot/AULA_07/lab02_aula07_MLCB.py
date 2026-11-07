# =====================================================================
# LAB 2: TRIAGEM DE CHAMADOS COM NAIVE BAYES
# =====================================================================

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

dados_treino = [
    ("Urgente: o servidor caiu e a aplicacao esta fora", "incidente_critico"),
    ("Erro grave no banco de dados e sistema parou", "incidente_critico"),
    ("Como faco para alterar minha senha do e-mail", "duvida_suporte"),
    ("Qual o procedimento para solicitar novo mouse", "duvida_suporte"),
    ("Gostaria de saber o horario de funcionamento", "fora_escopo")
]

stopwords = ["o", "a", "e", "do", "da", "para", "de"]

# 1. PRÉ-PROCESSAMENTO
def pré_processar(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()).strip()
    tokens = texto_limpo.split()

    # TODO 2.1: Filtre as stopwords mantendo os tokens válidos
    tokens_filtrados = [token for token in tokens if token not in stopwords]

    return " ".join(tokens_filtrados)

X_treino_limpo = [pré_processar(item[0]) for item in dados_treino]
y_treino = [item[1] for item in dados_treino]

# 2. VETORIZAÇÃO E TREINAMENTO (NAIVE BAYES)
vectorizer = TfidfVectorizer()
X_vetorizado = vectorizer.fit_transform(X_treino_limpo)

# TODO 2.2: Instancie o modelo Naive Bayes (MultinomialNB)
modelo_nb = MultinomialNB()

# TODO 2.3: Treine o modelo com X_vetorizado e y_treino
modelo_nb.fit(X_vetorizado, y_treino)

# 3. EXTRAÇÃO DE ENTIDADE (CÓDIGO DE PROTOCOLO)
def extrair_protocolo(texto):
    # Procura um padrão de protocolo como 'INC-1234' ou 'INC1234'
    match = re.search(r'INC-?\d{4}', texto, re.IGNORECASE)
    # TODO 2.4: Retorne a string do protocolo encontrado (match.group(0)) em maiúsculas ou None
    return match.group(0).upper() if match else None

# 4. PIPELINE NLU
def processar_triagem(mensagem_usuario, threshold=0.60):
    texto_p = pré_processar(mensagem_usuario)
    vetor_input = vectorizer.transform([texto_p])

    # Naive Bayes também possui .predict_proba()
    probas = modelo_nb.predict_proba(vetor_input)[0]

    maior_confianca = max(probas)
    intencao_prevista = str(modelo_nb.classes_[probas.argmax()])

    # TODO 2.5: Retorne dicionário de FALLBACK se maior_confianca < threshold
    # Caso contrário, retorne SUCESSO com a intenção, confiança e o código do protocolo extraído
    if maior_confianca < threshold:
        return {"status": "FALLBACK", "confianca": round(float(maior_confianca), 3),
                "resposta": "Nao consegui classificar o chamado. Descreva o problema com mais detalhes."}
    else:
        return {"status": "SUCESSO", "intencao": intencao_prevista,
                "confianca": round(float(maior_confianca), 3),
                "protocolo": extrair_protocolo(mensagem_usuario)}

# --- TESTE 2 ---
if __name__ == "__main__":
    print(processar_triagem("Urgente: servidor caiu no protocolo INC-9982"))
    for frase in [
        "Erro grave no sistema, protocolo inc1234",
        "Como faco para solicitar novo mouse",
        "Qual o horario de funcionamento",
        "banana azul",
    ]:
        print(f"{frase!r} -> {processar_triagem(frase)}")

    # Com so 5 frases de treino o Naive Bayes nunca chega a 60%; com threshold 0.50 o protocolo aparece
    print("--- threshold 0.50 ---")
    print(processar_triagem("Urgente: servidor caiu no protocolo INC-9982", threshold=0.50))
    print(processar_triagem("Erro grave no sistema, protocolo inc1234", threshold=0.50))
