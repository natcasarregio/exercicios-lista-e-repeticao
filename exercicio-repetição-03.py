sexos = ['M', "F"]
Estados = ["C","S","D","V"]
validadeNome = False
while validadeNome == False:
    nome = (input('Digite seu nome:'))
    if len(nome) > 3:
        validadeNome = True
    else:
        print('tente de novo com mais de 3 letras no nome')

validadeidade = False
while validadeidade == False:
    idade = float(input('Digite sua idade:'))
    if idade>0 and idade <150 :
        validadeidade = True
    else:
        print('tente de novo')

validadeSalario = False
while validadeSalario == False:
    Salario = float(input('Digite seu salario sem ponto e virgula:'))
    if Salario >0:
        validadeSalario = True
    else:
        print('tente de novo')

validadeSexo = False
while validadeSexo == False:
    Sexo = (input('Digite seu sexo "F" para feminino e "M" para masculino:'))
    if Sexo in sexos:
        validadeSexo = True
    else:
        print('tente novamente')

validadeEstadoCivil = False
while validadeEstadoCivil == False:
    EstadoCivil = (input('Digite seu Estato civil "S" solteiro, "C" casado, "V" viuvo, "D" divorciado :'))
    if EstadoCivil in Estados:
        validadeEstadoCivil = True
    else:
        print('tente novamente')
print('Nome:',nome)
print('Idade:',idade)
print('Salario:',Salario)
print('Sexo:',Sexo)
print('Esatado Civil:',EstadoCivil)