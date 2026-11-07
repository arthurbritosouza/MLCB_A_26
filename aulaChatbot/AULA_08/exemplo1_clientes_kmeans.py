# Exemplo 1: Agrupando clientes (K-Means)
# pip install scikit-learn matplotlib pandas

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Dados: [idade, renda em milhares R$]
dados = [
    [20, 2],
    [22, 2.5],
    [25, 3],
    [45, 8],
    [48, 9],
    [50, 10]
]


# Cria o algoritmo pedindo 2 grupos
modelo = KMeans(n_clusters=2, random_state=42, n_init=10)

# O algoritmo procura os grupos automaticamente
grupos = modelo.fit_predict(dados)


# Mostra o resultado
for i, grupo in enumerate(grupos):
    print("Cliente", i + 1, "→ Grupo", grupo)


# Visualização dos grupos
plt.scatter(
    [x[0] for x in dados],
    [x[1] for x in dados],
    c=grupos
)

plt.xlabel("Idade")
plt.ylabel("Renda (milhares)")
plt.title("Agrupamento de Clientes com K-Means")

plt.savefig("grupos_clientes.png")  # salva o gráfico (o plt.show() abaixo abre a janela)
plt.show()
