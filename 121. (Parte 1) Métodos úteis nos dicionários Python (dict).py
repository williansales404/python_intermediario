'''# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
'''

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}

pessoa.setdefault('idade')
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)


'''#################Shallow Copy vs Deep Copy#################
import copy
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}
#d2 = d1.copy()

#copy.deepcopy() representa uma copia real
d2 = copy.deepcopy(d1)

d2 ['c1'] = 1000
d2['l1'][1] = 9999

print(d1)
print(d2)
'''


'''############### get, pop, popitem, update #################
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)
'''