# Exercício - sistema de perguntas e respostas

'''###########solução professor######################
# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
'''

################## minha solução ##########################
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

import os

cont = 0
acerto = 0
while cont < len(perguntas):

    pergunta = perguntas[cont]['Pergunta']
    print(f'Pergunta: {pergunta}')
###################################################################
    chaves = perguntas[cont]['Opções']
    for index, i in enumerate(chaves):
        print(f'{index}) {i}')
####################################################################
    try:
        entrada_perg = input('Escolha uma opção: ')
        entrada_perg_int = int(entrada_perg)
    except ValueError:
        print('digite somente um valor inteiro ')
        continue
####################################################################

    if len(entrada_perg) > 1:
        print('digite somente um caracter interiro')
        continue
    if pergunta == 'Quanto é 2+2?':
       
        if entrada_perg == '2':
            acerto += 1
            print('acerto')
        else:
            print('erro')
    
    if pergunta == 'Quanto é 5*5?':
       
        if entrada_perg == '0':
            acerto += 1
            print('acerto')
        else:
            print('erro')
    
    if pergunta == 'Quanto é 10/2?':
       
        if entrada_perg == '1':
            acerto += 1
            print('acerto')
        else:
            print('erro')



    cont += 1

print(f'voce acerto {acerto} de 3 perguntas')