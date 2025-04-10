'''
def saudacao(msg):#paranmetro
    return msg

def executa(funcao, texto):
    return funcao(texto)

#argumento igual a valor
v = executa(saudacao, 'bom dia')
print(v)
'''
###################################################
"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)