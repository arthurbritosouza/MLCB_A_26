### Resumo Simples do Relatório

**O Melhor Modelo: KNN (K=3)**

Ambos os modelos (KNN e Árvore de Decisão) tiveram resultados perfeitos nos testes padrões. No entanto, quando testamos com frases novas (interativamente):

*   **KNN:** Acertou mais, foi mais flexível e soube pedir ajuda (fallback) quando não entendia a frase. Isso o torna mais confiável na prática.
*   **Árvore de Decisão:** Errou em algumas frases simples (como "ajuda") e não pedia ajuda (fallback) mesmo quando estava errado, mostrando excesso de confiança. Isso o torna menos prático para situações reais.

Por isso, o **KNN** é a melhor escolha, pois ele se adapta melhor e é mais seguro para o uso diário.
