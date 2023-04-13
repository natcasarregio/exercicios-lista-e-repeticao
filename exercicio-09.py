numerosinteiros = [2,3,4,5,6,7,8,9,10,11]
listaVazia = []
soma = 0

for numeros in numerosinteiros:
    quadrados = int(numeros) ** 2
    listaVazia.append(quadrados)

for valores in listaVazia:
    soma = soma + valores

print('números inteiros:',numerosinteiros)
print ('números inteiros ao quadrado',listaVazia)
print('soma dos números ao quadrado:', soma)