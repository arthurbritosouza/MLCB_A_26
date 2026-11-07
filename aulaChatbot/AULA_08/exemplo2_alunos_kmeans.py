# Exemplo 2: Descobrindo perfis de alunos (K-Means)
# pip install scikit-learn

from sklearn.cluster import KMeans


# [horas de estudo, nota média]
alunos = [
    [2, 5.0],
    [3, 5.5],
    [4, 6.0],
    [8, 8.0],
    [9, 8.5],
    [10, 9.0]
]


# Queremos descobrir 2 grupos
modelo = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)


# O algoritmo encontra os grupos
grupos = modelo.fit_predict(alunos)


# Mostra o resultado
for i, grupo in enumerate(grupos):

    print(
        f"Aluno {i + 1}: "
        f"{alunos[i]} → Grupo {grupo}"
    )


# Mostra os centros encontrados pelo algoritmo
print("\nCentros dos grupos:")

print(modelo.cluster_centers_)
