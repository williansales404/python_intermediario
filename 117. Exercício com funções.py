'''
def duplica(x):
    return x * 2

def triplica(x):
    return x*3

def quatruplica(x):
    return x*4

print(duplica(2))
print(triplica(2))
print(quatruplica(2))
'''
#########solução professor######################
def criar_multiplicador(multiplica):
    def numero_mult(numero):
        return multiplica * numero
    
    return numero_mult

x = criar_multiplicador(2)
print(x(4))