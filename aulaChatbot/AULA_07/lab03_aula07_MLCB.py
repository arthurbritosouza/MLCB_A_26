# =====================================================================
# LAB 3: CHATBOT DE E-COMMERCE COM DECISION TREE
# =====================================================================

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

dados_treino = [
    ("Onde esta meu pedido e qual o rastreio", "rastrear_pedido"),
    ("Quero saber a localizacao da minha encomenda", "rastrear_pedido"),
    ("Quero cancelar minha compra e pedir reembolso", "cancelar_compra"),
    ("Preciso cancelar o pedido feito ontem", "cancelar_compra"),
    ("Qual o horario de atendimento da loja fisica", "fora_escopo")
]

stopwords = ["o", "a", "meu", "minha", "e", "da", "do"]

# 1. PRÉ-PROCESSAMENTO
def pré_processar(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()).strip()
    tokens = texto_limpo.split()

    # TODO 3.1: Filtre as stopwords da frase
    tokens_filtrados = [token for token in tokens if token not in stopwords]

    return " ".join(tokens_filtrados)

X_treino_limpo = [pré_processar(item[0]) for item in dados_treino]
y_treino = [item[1] for item in dados_treino]

# 2. VETORIZAÇÃO E TREINAMENTO (DECISION TREE)
vectorizer = TfidfVectorizer()
X_vetorizado = vectorizer.fit_transform(X_treino_limpo)

# TODO 3.2: Instancie o modelo DecisionTreeClassifier
modelo_tree = DecisionTreeClassifier(random_state=42)

# TODO 3.3: Treine o modelo com os dados vetorizados e os rótulos de treino
modelo_tree.fit(X_vetorizado, y_treino)

# 3. EXTRAÇÃO DE ENTIDADE (CÓDIGO DE RASTREIO BR)
def extrair_codigo_rastreio(texto):
    # Procura códigos de rastreio como 'BR123456789'
    match = re.search(r'BR\d{9}', texto, re.IGNORECASE)
    # TODO 3.4: Se encontrar, retorne o texto correspondente em maiúsculas (match.group(0).upper()). Se não, None.
    return match.group(0).upper() if match else None

# 4. PIPELINE NLU
def processar_ecommerce(mensagem_usuario, threshold=0.50):
    texto_p = pré_processar(mensagem_usuario)
    vetor_input = vectorizer.transform([texto_p])

    # DecisionTree também calcula probabilidades com base na pureza das folhas
    probas = modelo_tree.predict_proba(vetor_input)[0]

    maior_confianca = max(probas)
    intencao_prevista = str(modelo_tree.classes_[probas.argmax()])

    # TODO 3.5: Crie a verificação de segurança:
    # Se maior_confianca < threshold ou intencao == "fora_escopo":
    #     retorne o dicionário de FALLBACK
    # Senão:
    #     retorne o dicionário de SUCESSO com a intenção, confiança e código de rastreio extraído
    if maior_confianca < threshold or intencao_prevista == "fora_escopo":
        return {"status": "FALLBACK", "confianca": round(float(maior_confianca), 3),
                "resposta": "Nao entendi. Voce quer rastrear um pedido ou cancelar uma compra?"}
    else:
        return {"status": "SUCESSO", "intencao": intencao_prevista,
                "confianca": round(float(maior_confianca), 3),
                "rastreio": extrair_codigo_rastreio(mensagem_usuario)}

# --- TESTE 3 ---
if __name__ == "__main__":
    print(processar_ecommerce("Quero rastrear o pedido BR987654321"))
    for frase in [
        "Onde esta a minha encomenda br123456789",
        "Quero cancelar o pedido e pedir reembolso",
        "Qual o horario de atendimento",
        "banana azul",
    ]:
        print(f"{frase!r} -> {processar_ecommerce(frase)}")
