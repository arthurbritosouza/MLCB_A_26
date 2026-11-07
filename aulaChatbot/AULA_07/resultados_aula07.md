--- RESULTADOS DO LAB 01 (Regressão Logística - Chatbot Bancário) ---

Código: `lab01_aula07_MLCB.py`

Output:

```
{'status': 'FALLBACK', 'confianca': 0.474, 'resposta': 'Desculpe, nao entendi. Voce pode consultar saldo ou fazer um pix.'}
'Quero fazer um pix de 250 reais' -> {'status': 'SUCESSO', 'intencao': 'fazer_pix', 'confianca': 0.897, 'valor': 250.0}
'Qual o meu saldo?' -> {'status': 'SUCESSO', 'intencao': 'consultar_saldo', 'confianca': 0.844, 'valor': None}
'Me conta uma piada' -> {'status': 'FALLBACK', 'confianca': 0.685, 'resposta': 'Desculpe, nao entendi. Voce pode consultar saldo ou fazer um pix.'}
'xyz abc' -> {'status': 'FALLBACK', 'confianca': 0.474, 'resposta': 'Desculpe, nao entendi. Voce pode consultar saldo ou fazer um pix.'}
```

1 - A mensagem '???' caiu em FALLBACK (47,4%), abaixo do threshold de 55%.
2 - 'Quero fazer um pix de 250 reais' foi para fazer_pix com 89,7% e o Regex extraiu o valor 250.0.
3 - 'Me conta uma piada' foi classificada como fora_escopo (68,5%), por isso também deu FALLBACK mesmo com confiança acima do threshold.


--- RESULTADOS DO LAB 02 (Naive Bayes - Triagem de Chamados) ---

Código: `lab02_aula07_MLCB.py`

Output:

```
{'status': 'FALLBACK', 'confianca': 0.546, 'resposta': 'Nao consegui classificar o chamado. Descreva o problema com mais detalhes.'}
'Erro grave no sistema, protocolo inc1234' -> {'status': 'FALLBACK', 'confianca': 0.538, 'resposta': 'Nao consegui classificar o chamado. Descreva o problema com mais detalhes.'}
'Como faco para solicitar novo mouse' -> {'status': 'FALLBACK', 'confianca': 0.586, 'resposta': 'Nao consegui classificar o chamado. Descreva o problema com mais detalhes.'}
'Qual o horario de funcionamento' -> {'status': 'FALLBACK', 'confianca': 0.394, 'resposta': 'Nao consegui classificar o chamado. Descreva o problema com mais detalhes.'}
'banana azul' -> {'status': 'FALLBACK', 'confianca': 0.4, 'resposta': 'Nao consegui classificar o chamado. Descreva o problema com mais detalhes.'}
--- threshold 0.50 ---
{'status': 'SUCESSO', 'intencao': 'incidente_critico', 'confianca': 0.546, 'protocolo': 'INC-9982'}
{'status': 'SUCESSO', 'intencao': 'incidente_critico', 'confianca': 0.538, 'protocolo': 'INC1234'}
```

1 - Com o threshold de 0.60 todos os testes deram FALLBACK: o Naive Bayes treinado com só 5 frases fica em torno de 54% de confiança. O protocolo INC-9982 só aparece no SUCESSO.
2 - Baixando o threshold para 0.50 o chamado foi classificado como incidente_critico e o protocolo foi extraído em maiúsculas (INC-9982 e INC1234).
3 - Conclusão: o problema é o tamanho do dataset, o modelo não tem exemplos suficientes para ter confiança alta.


--- RESULTADOS DO LAB 03 (Árvore de Decisão - Chatbot de E-Commerce) ---

Código: `lab03_aula07_MLCB.py`

Output:

```
{'status': 'SUCESSO', 'intencao': 'rastrear_pedido', 'confianca': 1.0, 'rastreio': 'BR987654321'}
'Onde esta a minha encomenda br123456789' -> {'status': 'SUCESSO', 'intencao': 'rastrear_pedido', 'confianca': 1.0, 'rastreio': 'BR123456789'}
'Quero cancelar o pedido e pedir reembolso' -> {'status': 'SUCESSO', 'intencao': 'cancelar_compra', 'confianca': 1.0, 'rastreio': None}
'Qual o horario de atendimento' -> {'status': 'FALLBACK', 'confianca': 1.0, 'resposta': 'Nao entendi. Voce quer rastrear um pedido ou cancelar uma compra?'}
'banana azul' -> {'status': 'SUCESSO', 'intencao': 'rastrear_pedido', 'confianca': 1.0, 'rastreio': None}
```

1 - A Árvore devolveu 100% de confiança em todas as respostas, porque as folhas são puras com poucos dados.
2 - O código de rastreio BR987654321 foi extraído corretamente (e BR123456789 em minúsculas também, por causa do re.IGNORECASE + .upper()).
3 - 'banana azul' foi classificada como rastrear_pedido com 100%: a Árvore fica confiante demais e o threshold não protege. Só o fora_escopo caiu em FALLBACK pela regra da intenção.

