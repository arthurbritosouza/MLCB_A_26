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
