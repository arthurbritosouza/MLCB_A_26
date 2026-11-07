--- PARTE 1: K-MEANS + RANDOM FOREST (MODELO HÍBRIDO) ---

Código: `kmeans_random_forest.py`

Output:

```
Grupos descobertos: [0 0 0 1 1 1]
Grupo previsto: 0
```

1 - O K-Means achou 2 grupos sem rótulo: os 3 primeiros clientes (jovens, renda baixa) no grupo 0 e os 3 últimos (mais velhos, renda alta) no grupo 1.
2 - O Random Forest foi treinado usando esses grupos como rótulo e classificou o novo cliente (30 anos, R$ 4 mil) no grupo 0, o dos mais novos e de renda menor.
3 - É um exemplo só demonstrativo: com 6 dados o modelo não é confiável, ele só reproduz os grupos que o K-Means encontrou.

--- FASE 1 / ETAPA 1: BANCO DE DADOS (`src/database.py`) ---

Output da primeira execução (dentro de `src/`):

```
 Dados iniciais de teste (seeds) inseridos com sucesso!
 Banco 'mesafartai.db' criado e atualizado!
```

Output da segunda execução (as seeds não são inseridas de novo):

```
 Banco 'mesafartai.db' criado e atualizado!
```

O arquivo `src/mesafartai.db` foi gerado.

--- FASE 1 / ETAPA 2: MOTOR NLU (`src/nlu.py`) ---

Comando: `python src/nlu.py`

Output:

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

A trava de threshold (< 0.60) funcionou nas 3 frases incertas ou fora de escopo. O relatório com as 5 respostas está em `docs/relatório_fase1_etapa2.md` e as regras em `docs/regras.txt`.

--- OBSERVAÇÃO ---

Ficaram fora desta pasta os itens do guia que não são código: criar o repositório PROJETO-MESAFARTAI no GitHub, README com RA, logotipo por IA e o e-mail ao professor.
