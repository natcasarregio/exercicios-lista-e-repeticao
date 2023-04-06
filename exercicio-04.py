palavra = ['h','i','p','o','c','r','i','s','i','a']
vogal = ['a', 'e', 'i', 'o', 'u']
numerodeconsoantes = 0
print('palavra =',palavra)

for letras in palavra:
    if letras not in vogal:
        numerodeconsoantes = numerodeconsoantes + 1
        print('consoante:',letras)
print('número de consoantes =', numerodeconsoantes)



