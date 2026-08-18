--- RESULTADOS DO LAB 01 ---
Mensagem: 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Pode me ajudar a fazer um pix?' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Gostaria de cancelar meu cartão de crédito' ==> Intenção Predita: [cancelar_conta]
1 - a mensagem Quero consultar quanto dinheiro tenho veio com o resultado errado
2 - Colocar mais frases de consulta para o modelo entender que quando tiver consultar, dinheiro sempre tem que ser consultar_saldo
3 - Treina o modelo com os dados vetorizados e os dados normais

--- RESULTADOS DO LAB 02 ---
Mensagem de Teste: 'Gostaria de devolver o produto que comprei'
Intenção Predita: troca_devolucao

--- Distribuição de Probabilidades por Classe ---
Classe [duvida_frete]: 27.99%
Classe [rastrear_pedido]: 24.54%
Classe [troca_devolucao]: 47.46%
1 - Resultado correto troca_devolucao
2 - O modelo está correto, retornou corretamente
3 - Ele pega a vetorização que foi feita com os dados de treinamento e colocar também o o resultado correto de cada vetor

--- RESULTADOS DO LAB 03 ---
Acurácia do Modelo: 33.33%

Detalhes:
Tamanho treino: 6 | Tamanho teste: 3
Exemplos de teste:
  'Nao consigo imprimir documentos' -> real: suporte_impressora | previsto: problema_conexao
  'Não consigo entrar no sistema' -> real: reset_senha | previsto: problema_conexao
  'Minha conexao caindo toda hora' -> real: problema_conexao | previsto: problema_conexao

1 - foi 33.33, foi correto por conta dos dados pequenos
2 - ele utiliza a vetorização para verificar se aquela frase com os outros vetores, e faz a prediçao
3 - limita o quanto de dado que ele pode verificar
