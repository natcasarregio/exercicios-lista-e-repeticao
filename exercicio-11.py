Letras = ['A','B','C','D','F','J','K','L','M','U']
Frutas = ['Amora','Banana',' Cereja','Damasco','Framboesa','Jabuticaba','Kiwi','Limão','Morango','Uva']
Notas = ['9','10','3','2','4','11','8','10','8','8']
Listaintercalada = []

for itens in range(10):
    Listaintercalada.append(Letras[itens])
    Listaintercalada.append(Frutas[itens])
    Listaintercalada.append(Notas[itens])

print('letras legais:',Letras)
print('frutas legais e gostosas:', Frutas)
print('Notas da frutas:', Notas)
print('os tres juntos perfeitos', Listaintercalada)