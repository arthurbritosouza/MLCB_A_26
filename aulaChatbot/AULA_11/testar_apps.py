# Teste automático dos dois apps da Aula 11 (sem abrir navegador), com o AppTest do Streamlit.
# Rodar dentro da pasta AULA_11:  python testar_apps.py
import os
import sys
from streamlit.testing.v1 import AppTest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))  # app.py importa nlu, entities...

print("=== TAREFA 1: app_streamlit.py (meta 200 kg, máximo 25 kg por doação) ===")
at = AppTest.from_file("app_streamlit.py", default_timeout=30).run()
campo = at.number_input[0]
print("Limite da quantidade por doação:", campo.max)

for i in range(1, 9):
    at.text_input[0].set_value(f"Doador {i}")
    at.number_input[0].set_value(25)
    registrar = [b for b in at.button if b.label == "Registrar doação"][0]  # há outro botão: "Zerar painel" (sidebar)
    registrar.click().run()
    print(f"Doação {i}: total = {at.metric[0].value} | faltam = {at.metric[2].value}")

print("Barra de progresso final:", at.progress[0].value, "(100 = meta atingida)")
assert not at.exception, at.exception

print("\n=== PARTE 2: src/app.py (chat + dashboard) ===")
app = AppTest.from_file("src/app.py", default_timeout=60).run()
assert not app.exception, app.exception
print("Mensagem inicial:", app.chat_message[0].markdown[0].value[:60], "...")

for frase in [
    "Tenho 20 kg de arroz para doar hoje no centro",
    "Nossa ONG precisa de doações de alimentos",
    "Qual é a receita de bolo de cenoura?",
]:
    app.chat_input[0].set_value(frase).run()
    assert not app.exception, app.exception
    print(f"\nUsuário: {frase}")
    print("Assistente:", app.chat_message[-1].markdown[0].value)

print("\nDashboard:", [(m.label, m.value) for m in app.metric])
