"""
MESAFARTAI - Matchmaking logístico com KNN
Arquivo: src/matchmaking.py
Descrição: encontra a ONG mais próxima do doador usando as coordenadas das ONGs cadastradas no SQLite.
"""

import os
import sqlite3
import numpy as np
from sklearn.neighbors import NearestNeighbors

CAMINHO_BANCO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mesafartai.db")


class MotorMatchmaking:
    def __init__(self, caminho_banco=CAMINHO_BANCO):
        self.caminho_banco = caminho_banco
        self.ongs = []  # [id, nome, latitude, longitude]
        self.knn = None
        self.recarregar_ongs()

    def recarregar_ongs(self):
        """Lê as ONGs ativas do SQLite e treina o KNN com as coordenadas (lat, long)."""
        self.ongs, self.knn = [], None
        if not os.path.exists(self.caminho_banco):
            return
        conn = sqlite3.connect(self.caminho_banco)
        linhas = conn.execute(
            "SELECT id, nome, latitude, longitude FROM usuarios "
            "WHERE tipo = 'ONG' AND latitude IS NOT NULL AND longitude IS NOT NULL"
        ).fetchall()
        conn.close()
        if linhas:
            self.ongs = [list(linha) for linha in linhas]
            self.knn = NearestNeighbors(n_neighbors=1, metric='euclidean')
            self.knn.fit(np.array([[ong[2], ong[3]] for ong in self.ongs]))

    def encontrar_ong_mais_proxima(self, latitude, longitude):
        """Devolve {'ong_id', 'ong_nome', 'distancia_estimada'} (km) ou None se não houver ONG cadastrada."""
        if self.knn is None:
            return None
        distancias, indices = self.knn.kneighbors([[latitude, longitude]])
        ong = self.ongs[indices[0][0]]
        return {
            "ong_id": ong[0],
            "ong_nome": ong[1],
            "distancia_estimada": round(float(distancias[0][0]) * 111, 2),  # graus -> km (aproximado)
        }


# --- TESTE DO MÓDULO EM TEMPO DE EXECUÇÃO ---
if __name__ == "__main__":
    # Para mostrar o KNN escolhendo entre duas ONGs, cadastra a 2ª ONG do exemplo da aula (se ainda não existir)
    conn = sqlite3.connect(CAMINHO_BANCO)
    if not conn.execute("SELECT 1 FROM usuarios WHERE nome = 'Abrigo Esperança'").fetchone():
        conn.execute("INSERT INTO usuarios (nome, tipo, cep, latitude, longitude, telefone) "
                     "VALUES ('Abrigo Esperança', 'ONG', '06710-000', -23.630, -46.800, '11999990002')")
        conn.commit()
    conn.close()

    motor = MotorMatchmaking()
    print("ONGs carregadas do SQLite:", [ong[1] for ong in motor.ongs])
    print("Doador no centro (-23.615, -46.785):", motor.encontrar_ong_mais_proxima(-23.615, -46.785))
    print("Doador perto do abrigo (-23.629, -46.799):", motor.encontrar_ong_mais_proxima(-23.629, -46.799))
