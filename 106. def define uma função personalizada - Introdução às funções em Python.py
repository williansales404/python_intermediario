
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')

#######################################################
# def Print():
#     print('varias')
#     print('varias')
#     print('varias')
#     print('varias')
# Print()

#######################################################
# def imprimir (a, b, c): #parametro e a variavel
#     print(a, b, c)
# imprimir(1, 2, 3) #valor igual argumento
#######################################################

# def saudacao(nome = 'sem nome'):
#     print(f'ola {nome}')

# saudacao('luiz otavio')
# saudacao('douglas')
# saudacao()
#######################################################


