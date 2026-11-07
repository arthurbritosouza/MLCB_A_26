--- PARTE 1: CONHECENDO O STREAMLIT (TAREFA 1) ---

Código: `app_streamlit.py` (rodar com `streamlit run app_streamlit.py`)

Regra da tarefa: chegar a 200 kg (meta do slider) com no máximo 25 kg por doação. Por isso troquei o `max_value` do `st.number_input` de 100 para 25.

Teste automático (`testar_apps.py`, usa o AppTest do Streamlit para preencher o formulário e clicar em "Registrar doação"):

```
=== TAREFA 1: app_streamlit.py (meta 200 kg, máximo 25 kg por doação) ===
Limite da quantidade por doação: 25.0
Doação 1: total = 25 kg | faltam = 175 kg
Doação 2: total = 50 kg | faltam = 150 kg
Doação 3: total = 75 kg | faltam = 125 kg
Doação 4: total = 100 kg | faltam = 100 kg
Doação 5: total = 125 kg | faltam = 75 kg
Doação 6: total = 150 kg | faltam = 50 kg
Doação 7: total = 175 kg | faltam = 25 kg
Doação 8: total = 200 kg | faltam = 0 kg
Barra de progresso final: 100 (100 = meta atingida)
```

1 - Foram necessárias 8 doações de 25 kg para chegar aos 200 kg. Na 8ª doação o total chegou na meta, "Faltam para a meta" foi para 0 kg e a barra de progresso foi a 100% (é nesse momento que o `st.balloons()` dispara).
2 - O campo de quantidade não deixa passar de 25 kg.
3 - O app também foi iniciado de verdade com `streamlit run` e respondeu em http://localhost:8501 (health ok, página 200).
4 - O print `docs/teste_streamlit.png` precisa ser tirado a mão com o app aberto (não consigo tirar print da tela do navegador por aqui).

--- PARTE 2: AC-4 PARTE 1 (`src/app.py`) ---

Código: `src/app.py` (rodar com `streamlit run src/app.py`), usando os módulos `nlu.py`, `entities.py`, `matchmaking.py` e o banco `mesafartai.db`.

TODOs que preenchi: ícone (🍲), título (MESAFARTAI), subtítulo (Logística e Inteligência Assistiva no Combate à Fome (ODS 2)) e a mensagem inicial do chat.

Ajustes pequenos que fiz no código do enunciado:
- O `nlu.py` da Aula 9 só tinha `processar_mensagem`; o `app.py` chama `nlu.predizer_intencao(prompt)`, então acrescentei esse método (devolve intenção e confiança, sem o fallback). O método antigo continua lá.
- O caminho do banco é montado a partir da pasta do arquivo, para o app funcionar de qualquer pasta.
- `use_container_width=True` virou `width="stretch"` (o Streamlit novo avisa que o primeiro está em desuso).

Teste automático do chat e do dashboard:

```
=== PARTE 2: src/app.py (chat + dashboard) ===
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!
Mensagem inicial: Olá! Eu sou o assistente do MESAFARTAI. Quer doar alimentos  ...
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!

Usuário: Tenho 20 kg de arroz para doar hoje no centro
Assistente: **Doação Registrada com Sucesso!**

• **Item:** Arroz
• **Quantidade:** 20.0 kg
• **Validade Estimada:** 2026-11-03

**Match Logístico (KNN):** Encaminhado para **ONG Prato Quente** (~0.55 km).
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!

Usuário: Nossa ONG precisa de doações de alimentos
Assistente: Entendemos seu pedido. Estamos buscando doações disponíveis próximas a você no banco de dados.
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!

Usuário: Qual é a receita de bolo de cenoura?
Assistente: Desculpe, não entendi perfeitamente sua mensagem. Poderia informar o alimento e a quantidade em kg?

Dashboard: [('Total de ONGs Ativas', '2'), ('Alimentos Arrecadados (kg)', '1,250 kg'), ('Refeições Estimadas Proporcionadas', '~2,500 refeições')]
```

1 - A frase de doação foi reconhecida (cadastrar_doacao com confiança acima de 60%), o Regex extraiu arroz, 20 kg e a validade, e o KNN encaminhou para a ONG Prato Quente (~0.55 km).
2 - O pedido da ONG caiu em solicitar_alimentos e a frase fora de escopo caiu na resposta de fallback.
3 - O Dashboard mostra 2 ONGs ativas (Prato Quente e Abrigo Esperança, as do banco da Aula 10); os outros dois indicadores (1,250 kg e ~2,500 refeições) são valores fixos da versão 1 do professor.
4 - O app foi iniciado de verdade com `streamlit run src/app.py` e respondeu (health ok, página 200).
5 - O print `docs/etapa_ac4_parte1.png` também precisa ser tirado a mão com o app aberto.
