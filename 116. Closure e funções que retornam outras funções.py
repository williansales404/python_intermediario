"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('bom dia')

print(falar_bom_dia('maria'))
print(falar_boa_noite('junior'))

# for nome in ['Maria', 'Joana', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))



'''##################segundo exemplo#######################################
###########'https://www.youtube.com/watch?v=HGZgv1VDCYE'################
#closure
def func():
    y = 0
    def func2():
        nonlocal y
        y += 1
        return y
    return func2

#### cada variavel e uma função nova criada então recomeça a contagem###
x = func()
print(x())
print(x())

h = func()
print(h())
print(h())
'''
