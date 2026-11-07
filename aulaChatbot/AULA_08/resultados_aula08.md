--- RESULTADOS DO EXEMPLO 1 (K-Means - Agrupando clientes) ---

Código: `exemplo1_clientes_kmeans.py`

Output:

```
Cliente 1 → Grupo 0
Cliente 2 → Grupo 0
Cliente 3 → Grupo 0
Cliente 4 → Grupo 1
Cliente 5 → Grupo 1
Cliente 6 → Grupo 1
```

1 - O K-Means separou os 6 clientes em 2 grupos sem nenhum rótulo: os 3 mais novos e com renda menor ficaram juntos e os 3 mais velhos e com renda maior ficaram no outro grupo.
2 - O gráfico foi salvo em grupos_clientes.png.
3 - O número do grupo (0 ou 1) é só um nome, o algoritmo não diz o que cada grupo significa.


--- RESULTADOS DO EXEMPLO 2 (K-Means - Perfis de alunos) ---

Código: `exemplo2_alunos_kmeans.py`

Output:

```
Aluno 1: [2, 5.0] → Grupo 0
Aluno 2: [3, 5.5] → Grupo 0
Aluno 3: [4, 6.0] → Grupo 0
Aluno 4: [8, 8.0] → Grupo 1
Aluno 5: [9, 8.5] → Grupo 1
Aluno 6: [10, 9.0] → Grupo 1

Centros dos grupos:
[[3.  5.5]
 [9.  8.5]]
```

1 - Grupo com poucas horas de estudo e notas menores: alunos 1, 2 e 3. Grupo com muitas horas e notas maiores: alunos 4, 5 e 6.
2 - cluster_centers_ são os centróides: a média de horas de estudo e de nota de cada grupo (cerca de 3 h / 5,5 e 9 h / 8,5).


--- OBSERVAÇÃO ---

O Bloco 3 da Aula 08 (kickoff do projeto MESAFARTAI, guia_projeto_mesafartai_aula06102026) só vale se for feito em sala de aula, em grupo.
Por isso ele não está neste arquivo.
