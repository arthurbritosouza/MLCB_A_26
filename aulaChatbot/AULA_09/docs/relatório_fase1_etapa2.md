# Relatório de execução - Fase 1 / Etapa 2 (AC-3)

**Motor NLU do MESAFARTAI: TF-IDF + Random Forest + trava de threshold**

## 1. Quantas árvores foram utilizadas no motor NLU?

80 árvores (`RandomForestClassifier(n_estimators=80, random_state=42)`).

## 2. Qual o valor de threshold utilizado no limiar de confiança?

0.60 (60%). Se a maior probabilidade ficar abaixo disso, ou se a intenção prevista for `fora_de_escopo`, o motor devolve `fallback`.

## 3. Resultado da primeira execução (`python src/nlu.py`)

```
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!

--- BATERIA DE TESTES DE ESTRESSE NLU ---

Entrada: 'Tenho 30 kg de banana para doar'
Intenção: cadastrar_doacao | Confiança: 0.93
Retorno: Intenção 'cadastrar_doacao' identificada com 92.5% de confiança.

Entrada: 'Nossa instituição precisa de mantimentos'
Intenção: fallback | Confiança: 0.41
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?

Entrada: 'Qual é a receita de bolo de cenoura?'
Intenção: fallback | Confiança: 0.49
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?

Entrada: 'coisa comida doar la'
Intenção: fallback | Confiança: 0.42
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?
```

Leitura do resultado: só a frase de doação ficou acima do threshold (92,5%). A frase fora de escopo e a frase confusa caíram corretamente no fallback. Já "Nossa instituição precisa de mantimentos" era um pedido válido de ONG (solicitar_alimentos), mas ficou com 41% e também caiu no fallback, porque nenhuma palavra dela aparece no treino.

## 4. Como melhorar os resultados e aumentar a confiança?

- Aumentar o dataset: hoje são só 21 frases (4 a 8 por intenção). Com 50 a 100 frases por intenção o modelo vê mais variações.
- Incluir sinônimos e jeitos diferentes de falar o mesmo pedido (instituição, mantimentos, cesta, entidade, abrigo, ONG).
- Balancear as classes: `cadastrar_doacao` tem 8 frases e `consultar_status` tem 4.
- Pré-processar o texto (minúsculas, tirar acentos e stopwords, lematizar) antes do TF-IDF.
- Ajustar os hiperparâmetros do Random Forest (número de árvores, profundidade) com validação cruzada e escolher o threshold olhando erros reais.
- Mais frases de `fora_de_escopo`, para o modelo aprender o que é ruído.

## 5. Por que o Random Forest foi o melhor método para essa fase?

- Combina várias árvores que votam, então erra menos e tem menos overfitting do que uma Árvore de Decisão sozinha (que costuma dar 100% de confiança em tudo, como visto na Aula 7).
- `predict_proba` devolve a proporção de votos de cada classe, o que serve direto para a trava de threshold/fallback.
- Funciona bem com TF-IDF e poucos dados, sem precisar de GPU, e treina em milissegundos.
- É rápido para responder, bom para um chatbot, e fácil de explicar (votação das árvores).
