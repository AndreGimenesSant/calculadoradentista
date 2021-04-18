# Meu código da calculadora de porcentagem:

import datetime
while True:
    print('Calculadora % da maquininha a repassar para Dentista')
    print()
    print('\033[4;30;45mATENÇÃO! NÃO UTILIZAR PONTOS NEM VÍRGULAS NOS VALORES, VALORES NÃO RECEBIDOS PREENCHER COM 0 ou dar Enter\033[m')
    print()
    x = datetime.date.today()
    print(x)
    
    Andre = str
    receita = float
    
    Dentista = str(input('Digite o nome do dentista:'))
    if Dentista == ('Andre') or ('André') or ('andre') or ('andré'):
        receita = 0.35
    else:
        receita = 0.50
    try:
        valor0 = float(input('Valor Total Recebido em Dinheiro:')) # valores recebidos e métodos de pagamentos
    except ValueError:
        valor0 = 0 
    try:
        valor = float(input('Valor Total recebido Debito:'))
    except ValueError:
        valor = 0 
    try:
        valor1 = float(input('Crédito a vista:'))
    except ValueError:
        valor1 = 0 
    try:
        valor2 = float(input('Crédito até 6x:'))
    except ValueError:
        valor2 = 0 
    try:
        valor3 = float(input('Crédito de 7x até 12x:'))
    except ValueError:
        valor3 = 0 
        print()
        print('\033[4;30;46mcalculadora % Cartão Elo\033[m')
    try:
        valor4 = float(input('Débito Elo:'))
    except ValueError:
        valor4 = 0 
    try:
        valor5 = float(input('Crédito a vista Elo:'))
    except ValueError:
        valor5 = 0 
    try:
        valor6 = float(input('Crédito Elo até 6x:'))
    except ValueError:
        valor6 = 0 
    try:
        valor7 = float(input('Crédito Elo de 7x até 12x:'))
    except ValueError:
        valor7 = 0 

    maq_debi = 0.0178  #Aqui são atribuídas as taxas da maquina de cartão para cada método de pagamento
    maq_cred = 0.0294
    maq_cred6 = 0.0350
    maq_cred12 = 0.0370
    maq_deb_elo = 0.0304
    maq_cred_elo = 0.0409
    maq_cred_elo6 = 0.0462
    maq_cred_elo12 = 0.0509
    # Aqui é feito o cálculo da porcentagem da maquininha a ser descontada do valor total
    porcent = valor * maq_debi
    porcent1 = valor1 * maq_cred
    porcent2 = valor2 * maq_cred6
    porcent3 = valor3 * maq_cred12
    porcent4 = valor4 * maq_deb_elo
    porcent5 = valor5 * maq_cred_elo
    porcent6 = valor6 * maq_cred_elo6
    porcent7 = valor7 * maq_cred_elo12

    # Aqui é feito o desconto da taxa da maquininha do valor total
    desco = valor - porcent
    desco1 = valor1 - porcent1
    desco2 = valor2 - porcent2
    desco3 = valor3 - porcent3
    desco4 = valor4 - porcent4
    desco5 = valor5 - porcent5
    desco6 = valor6 - porcent6
    desco7 = valor7 - porcent7

    # Aqui é feito os 35% a ser repassado para o dentista do valor com a taxa da maquininha descontada
    liq0 = valor0 * receita
    liq = desco * receita
    liq1 = desco1 * receita
    liq2 = desco2 * receita
    liq3 = desco3 * receita
    liq4 = desco4 * receita
    liq5 = desco5 * receita
    liq6 = desco6 * receita
    liq7 = desco7 * receita

    # Aqui imprimi na tela o valor total dos 35% a ser repassado ao dentista de todos os pagamentos
    print('\033[4;30;44mValor liquido a repassar para o dentista é\033[m', liq0 + liq + liq1 + liq2 + liq3 + liq4 + liq5 + liq6 + liq7)
    print()
    print()
    print()
    """ fim do programa """
