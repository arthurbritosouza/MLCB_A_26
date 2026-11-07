# Modelo híbrido: K-Means + Random Forest
# pip install scikit-learn
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

# Dados: [idade, renda em milhares]
X = [
    [20, 2], [22, 2.5], [25, 3],
    [45, 8], [48, 9], [50, 10]
]

# 1. K-Means descobre 2 grupos automaticamente
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
grupos = kmeans.fit_predict(X)
print("Grupos descobertos:", grupos)

# 2. Random Forest aprende a reproduzir esses grupos
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X, grupos)

# 3. Classifica um novo cliente: 30 anos, renda de R$ 4 mil
novo_cliente = [[30, 4]]
grupo_previsto = modelo.predict(novo_cliente)
print("Grupo previsto:", grupo_previsto[0])
