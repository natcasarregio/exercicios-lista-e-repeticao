Letras = ['A','B','C','D','F','J','K','L','M','U']
Frutas = ['Amora','Banana',' Cereja','Damasco','Framboesa','Jabuticaba','Kiwi','Limão','Morango','Uva']
Listaintercalada = []

for itens in range(10):
    Listaintercalada.append(Letras[itens])
    Listaintercalada.append(Frutas[itens])

print('letras:',Letras)
print('frutas com eesas letras:', Frutas)
print('os dois juntos', Listaintercalada)