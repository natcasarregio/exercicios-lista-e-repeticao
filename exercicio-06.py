notasAlunos = [['Farias',[8, 7, 9, 8]],['Leticia',[10, 9, 9, 8]],['Lorena',[7, 9, 6, 6]],['Mayara',[7, 5, 8, 7]],['Laura',[8, 9, 6, 5]],['Ribeiro',[10, 7, 7, 8]],['Cintia',[3, 8, 7, 7]],['João',[3, 9, 4.5, 9]],['Maykon',[6, 9, 9, 7]], ['Henrique',[6, 5, 9, 7]]]

for aluno in notasAlunos:
    notas = aluno[1]
    media = sum(notas)/len(notas)
    print (f"A média das notas de {aluno[0]} é {media:.2f}")
