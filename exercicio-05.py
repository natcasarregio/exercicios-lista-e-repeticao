todosnumeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,20)
numerospar = []
numeroimpar = []

print('lista de números',todosnumeros)

for numeros in todosnumeros:
    if numeros%2 == 0:
        numerospar.append(numeros)
    else:
        numeroimpar.append(numeros)

print('números par:', numerospar)
print('números impar:', numeroimpar)


