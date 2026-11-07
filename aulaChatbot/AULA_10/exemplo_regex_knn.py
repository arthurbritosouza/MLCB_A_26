import re
import numpy as np
from sklearn.neighbors import NearestNeighbors

# =====================================================================
# 1. ETAPA REGEX: Transformar texto livre em Dados Estruturados
# =====================================================================
mensagem_chat = "Olá! Tenho 25 kg de tomate para doar hoje perto do centro."

# Padrão Regex para capturar números seguidos de 'kg' ou 'quilos'
padrao_massa = r'(\d+(?:[\.,]\d+)?)\s*(?:kg|quilos)'
# padrão r'(\d+(?:[\.,]\d+)?)\s*(?:kg|quilos)' busca por números inteiros ou decimais (aceitando tanto ponto quanto vírgula, ex: 2,5 ou 2.5) seguidos opcionalmente por espaços e pelas palavras kg ou quilos.

match = re.search(padrao_massa, mensagem_chat, re.IGNORECASE)
quantidade_extraida = float(match.group(1)) if match else 1.0

print(f"Texto bruto do chat: '{mensagem_chat}'")
print(f"-> [Regex] Quantidade limpa extraída para o SQLite: {quantidade_extraida} kg\n")

# =====================================================================
# 2. ETAPA KNN: Encontrar a ONG mais próxima para receber os 25 kg
# =====================================================================
# Localização do Doador (Latitude, Longitude)
coordenada_doador = [[-23.615, -46.785]]

# ONGs cadastradas no Banco de Dados: [ID, Nome, Lat, Long]
ongs_banco = [
    [1, "ONG Prato Quente", -23.612, -46.781], # ~0.5 km
    [2, "Abrigo Esperança", -23.630, -46.800]  # ~2.2 km
]

# Matriz apenas com as coordenadas (Lat, Long) para o algoritmo
coords_ongs = np.array([[ong[2], ong[3]] for ong in ongs_banco])

# Treinamento do KNN para encontrar o 1º vizinho mais próximo
knn = NearestNeighbors(n_neighbors=1, metric='euclidean')
knn.fit(coords_ongs)

# Cálculo da menor distância
distancias, indices = knn.kneighbors(coordenada_doador)

idx_ong = indices[0][0]
ong_recomendada = ongs_banco[idx_ong]
distancia_km = distancias[0][0] * 111  # Conversão aproximada para KM

print(f"-> Match Logístico Realizado!")
print(f"   ONG Recomendada: {ong_recomendada[1]} (ID: {ong_recomendada[0]})")
print(f"   Distância Calculada: {distancia_km:.2f} km do doador.")
