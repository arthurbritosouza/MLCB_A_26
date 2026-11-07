--- EXEMPLO DA AULA: REGEX + KNN ---

Código: `exemplo_regex_knn.py`

Output:

```
Texto bruto do chat: 'Olá! Tenho 25 kg de tomate para doar hoje perto do centro.'
-> [Regex] Quantidade limpa extraída para o SQLite: 25.0 kg

-> Match Logístico Realizado!
   ONG Recomendada: ONG Prato Quente (ID: 1)
   Distância Calculada: 0.55 km do doador.
```

1 - O Regex pegou o número que vem antes de kg/quilos e transformou em float (25.0), pronto para virar coluna `quantidade_kg` no SQLite.
2 - O KNN calculou a distância euclidiana entre o doador e cada ONG e escolheu a mais perto: ONG Prato Quente, a ~0,55 km.

--- DESAFIO "O FILTRO ANTI-DESPERDÍCIO" (Regex) ---

Código: `desafio_regex.py`

Padrões usados:

```
padrao_qtd  = r'(\d+(?:[\.,]\d+)?)\s*(lt|litros?|kg|quilos?)\b'    # captura 35 lt
padrao_dias = r'(\d+)\s*dias?\b'                                    # captura 2 dias
padrao_alimento = r'\d+(?:[\.,]\d+)?\s*(?:lt|litros?|kg|quilos?)\s+de\s+(\w+)'   # captura leite
```

Output:

```
Alimento: Leite | Quantidade: 35.0 lt | Urgência: ALTA (Vence em 2 dias)
'oi!! tenho 2,5 kg de arroz pra doar, vence em 10 dias' -> Alimento: Arroz | Quantidade: 2.5 kg | Urgência: NORMAL (Vence em 10 dias)
'DOANDO 12 litros de suco de uva, vence em 1 dias' -> Alimento: Suco | Quantidade: 12.0 litros | Urgência: ALTA (Vence em 1 dias)
'tenho comida sobrando' -> Alimento: Não identificado | Quantidade: Não identificada | Urgência: BAIXA (sem validade informada)
```

1 - A saída da primeira linha é igual à saída esperada no enunciado.
2 - Regra de urgência que eu defini: ALTA quando vence em até 3 dias, NORMAL acima disso e BAIXA quando não há validade.
3 - O padrão aceita vírgula ou ponto nos decimais (2,5) e ignora maiúsculas/minúsculas (re.IGNORECASE).
4 - Limite: no "suco de uva" o alimento sai só "Suco", porque o padrão pega uma palavra depois do "de".

--- ETAPA 3 DA AC-3: ENTIDADES E MATCHMAKING (`src/entities.py` e `src/matchmaking.py`) ---

O enunciado da etapa 3 não está no repositório do professor (ele envia depois do desafio). Montei os dois módulos com a teoria da aula e com a assinatura que o `app.py` da Aula 11 usa (`ExtratorEntidades.processar_texto` e `MotorMatchmaking.encontrar_ong_mais_proxima`).

Comando: `python src/entities.py` (as datas dependem do dia da execução, 03/11/2026)

```
'Olá! Tenho 25 kg de tomate para doar hoje perto do centro.'
   -> {'alimento': 'Tomate', 'quantidade_kg': 25.0, 'data_validade': '2026-11-03'}
'Quero doar 15 kg de arroz que vencem amanhã'
   -> {'alimento': 'Arroz', 'quantidade_kg': 15.0, 'data_validade': '2026-11-04'}
'Posso entregar 2,5 quilos de feijão, vence em 3 dias'
   -> {'alimento': 'Feijão', 'quantidade_kg': 2.5, 'data_validade': '2026-11-06'}
'Tenho comida sobrando'
   -> {'alimento': 'Alimento não identificado', 'quantidade_kg': 1.0, 'data_validade': 'Não informada'}
```

Comando: `python src/matchmaking.py` (cadastra a 2ª ONG do exemplo da aula, Abrigo Esperança, no `mesafartai.db`)

```
ONGs carregadas do SQLite: ['ONG Prato Quente', 'Abrigo Esperança']
Doador no centro (-23.615, -46.785): {'ong_id': 1, 'ong_nome': 'ONG Prato Quente', 'distancia_estimada': 0.55}
Doador perto do abrigo (-23.629, -46.799): {'ong_id': 3, 'ong_nome': 'Abrigo Esperança', 'distancia_estimada': 0.16}
```

1 - O KNN lê as ONGs direto do SQLite e escolhe a de menor distância; quando o doador muda de lugar, a ONG escolhida muda.
2 - Sem ONG cadastrada ou sem banco, `encontrar_ong_mais_proxima` devolve `None` e o app não quebra.
