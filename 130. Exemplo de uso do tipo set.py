
'''###########exemplo de uso##########
import os
letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('parabens')
        break
    
    os.system('cls')
    print(letras)
'''

#####################################
s1 = {1, 2, 3 }
s2 = {2, 3, 4}
s3 = s1 | s2

print(s3)
