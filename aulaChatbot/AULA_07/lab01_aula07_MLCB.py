# =====================================================================
# LAB 1: NLU BANCÁRIO COM REGRESSÃO LOGÍSTICA
# =====================================================================

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

dados_treino = [
    # consultar_saldo
    ("Quero consultar meu saldo", "consultar_saldo"),
    ("Qual e o saldo da minha conta", "consultar_saldo"),
    ("Quanto dinheiro eu tenho na conta", "consultar_saldo"),
    ("Me mostra o saldo disponivel", "consultar_saldo"),
    ("Preciso ver o saldo do meu cartao", "consultar_saldo"),
    ("Pode informar o saldo atual", "consultar_saldo"),
    # fazer_pix
    ("Quero fazer um pix de 50 reais", "fazer_pix"),
    ("Preciso transferir dinheiro por pix", "fazer_pix"),
    ("Enviar pix para minha mae", "fazer_pix"),
    ("Como faco um pix para o joao", "fazer_pix"),
    ("Quero pagar uma conta com pix", "fazer_pix"),
    ("Vou mandar 100 reais por pix", "fazer_pix"),
    # fora_escopo
    ("Qual a previsao do tempo para amanha", "fora_escopo"),
    ("Quem ganhou o jogo de ontem", "fora_escopo"),
    ("Me conta uma piada engracada", "fora_escopo"),
    ("Qual a receita de bolo de cenoura", "fora_escopo"),
    ("Gosto de assistir filmes de ficcao", "fora_escopo"),
    ("Que horas sao agora", "fora_escopo"),
]

stopwords = ["o", "a", "os", "as", "um", "uma", "de", "da", "do", "meu", "minha", "me", "para", "por", "e", "eu", "na", "no", "pode"]

# 1. PRÉ-PROCESSAMENTO
def pré_processar(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()).strip()
    tokens = texto_limpo.split()

    # TODO 1.1: Filtre as stopwords da lista 'tokens' usando List Comprehension
    tokens_filtrados = [token for token in tokens if token not in stopwords]

    return " ".join(tokens_filtrados)

X_treino_limpo = [pré_processar(item[0]) for item in dados_treino]
y_treino = [item[1] for item in dados_treino]

# 2. VETORIZAÇÃO E TREINAMENTO
vectorizer = TfidfVectorizer()

# TODO 1.2: Aprenda o vocabulário e vetorize 'X_treino_limpo' em um único passo
X_vetorizado = vectorizer.fit_transform(X_treino_limpo)

modelo = LogisticRegression(C=10)
modelo.fit(X_vetorizado, y_treino)

# 3. EXTRAÇÃO DE ENTIDADE (REGEX)
def extrair_valor_reais(texto_original):
    match = re.search(r'(\d+)\s*reais', texto_original, re.IGNORECASE)
    # TODO 1.3: Se houver match, converta o grupo 1 para float. Caso contrário, retorne None.
    return float(match.group(1)) if match else None

# 4. PIPELINE NLU
def processar_nlu(mensagem_usuario, threshold=0.55):
    texto_p = pré_processar(mensagem_usuario)
    vetor_input = vectorizer.transform([texto_p])

    probas = modelo.predict_proba(vetor_input)[0]

    # TODO 1.4: Extraia a MAIOR probabilidade (max) e a intenção prevista (argmax em modelo.classes_)
    maior_confianca = max(probas)
    intencao_prevista = str(modelo.classes_[probas.argmax()])

    # TODO 1.5: Se maior_confianca < threshold ou intencao == "fora_escopo", retorne FALLBACK.
    # Caso contrário, retorne SUCESSO com a intenção, confiança e o valor extraído.
    if maior_confianca < threshold or intencao_prevista == "fora_escopo":
        return {"status": "FALLBACK", "confianca": round(float(maior_confianca), 3),
                "resposta": "Desculpe, nao entendi. Voce pode consultar saldo ou fazer um pix."}
    else:
        return {"status": "SUCESSO", "intencao": intencao_prevista,
                "confianca": round(float(maior_confianca), 3),
                "valor": extrair_valor_reais(mensagem_usuario)}

# --- TESTE 1 ---
if __name__ == "__main__":
    print(processar_nlu("???"))
    for frase in [
        "Quero fazer um pix de 250 reais",
        "Qual o meu saldo?",
        "Me conta uma piada",
        "xyz abc",
    ]:
        print(f"{frase!r} -> {processar_nlu(frase)}")
