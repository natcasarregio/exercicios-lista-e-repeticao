notas = [70, 80, 90, 100]
print('notas do aluno:' , notas)

quantidade = len(notas)
soma = 0

for valores in notas:
    soma = soma + valores

print('media total do aluno:', soma/quantidade)

