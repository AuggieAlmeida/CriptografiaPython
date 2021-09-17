alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def criptografar(code, roll):
    cryptcode = ''
    for i in code:
        if i in alfabeto:
            letra_pos = alfabeto.index(i)
            cryptcode += alfabeto[(letra_pos + roll) % len(alfabeto)]
        else:
            cryptcode += i

    return cryptcode

def descriptografar(code, roll):
    decryptcode = ''
    for i in code:
        if i in alfabeto:
            letra_pos = alfabeto.index(i)
            decryptcode += alfabeto[(letra_pos - roll) % len(alfabeto)]
        else:
            decryptcode += i

    return decryptcode

code = str(input('Digite a mensagem: '))
roll = int(input('Digite a variação de letras: '))
print('Deseja criptografar ou descriptografar sua mensagem?')
resp = input('[1] Criptografar\t[2] Descriptografar')
if resp == '1':
    print(criptografar(code, roll))

elif resp == '2':
    print(descriptografar(code, roll))
else:
    print('Valor inválido!')