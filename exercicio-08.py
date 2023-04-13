listaDeIdades = []
listaDeAlturas = []
listaVazia = []
listaVazia2 = []

for idades in range (0, 5):
    print('insira idade:')
    idade = (input())
    listaDeIdades.append(idade)

for i in range (0, 5):
    listaVazia.append(listaDeIdades.pop())

for altura in range (0, 5):
    print('insira altura:')
    altura = (input())
    listaDeAlturas.append(altura)

for i in range (0, 5):
    listaVazia2.append(listaDeAlturas.pop())

print(listaVazia)
print(listaVazia2)
