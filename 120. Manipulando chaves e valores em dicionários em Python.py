#manipulação de chaves e valores em dicionario

pessoa = {}
# pessoa['nome'] = 'jonas'
# print(pessoa)
# print(pessoa['nome'])

chave = 'nome_completo'

pessoa [chave] = 'luiz otario'
pessoa ['sobrenome'] = 'miranda'

del pessoa ['sobrenome']

# try:
#     pessoa['sobrenome']
# except KeyError:
#     print('erro no sobrenome')

# print(pessoa.get('sobrenome'))

print(pessoa)

if pessoa.get('sobrenome') is None:
    print('Nao existe')
else:
    print(pessoa['sobrenome'])