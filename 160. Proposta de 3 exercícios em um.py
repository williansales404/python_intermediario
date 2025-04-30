'''
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
'''
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
'''
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
'''

'''#minha solução
indice = 0
for i in produtos:
    produtos[indice]['preco'] = produtos[indice]['preco']*1.10
    indice += 1

novos_produtos = copy.deepcopy(produtos)
lista_decrecente = sorted(novos_produtos, key=lambda x: x['nome'], reverse=True)

lista_cresente = sorted(novos_produtos, key=lambda x: x['preco'])

for i in lista_decrecente:
    print(i)

print()
print()

for i in lista_cresente:
    print(i)
'''
import copy



'''#solução professor
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [{**p, 'preco': round(p['preco'] * 1.1, 2)}for p in copy.deepcopy(produtos)]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos),key=lambda p: p['nome'],reverse=True)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos),key=lambda p: p['preco'])

# FINAL
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
'''

