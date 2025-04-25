#emcapsulamento e desencapsulamento

def executa(funcao, *args):
    return funcao(*args)

#função soma
def soma(x, y):
    return x + y

#########função a ser transformada em lambda##############
def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
######################################
# x = criar_multiplicador(2)
# print(x(2))
################## lambda ###################################

'''# exemplo 1
print(
     executa(lambda x, y: x + y, 2, 2),

     executa(soma, 2 ,3 ),

     soma(2, 4)
)
'''

'''# exemplo 2 para enetender função executa com *args
# Aqui:
# A função soma é passada como argumento para executa.
# Os valores 10 e 5 são passados como argumentos (*args).
# A função executa invoca soma(10, 5) e retorna o resultado.

def soma(a, b):
    return a + b

resultado = executa(soma, 10, 5)
print(resultado)  # Saída: 15

'''

