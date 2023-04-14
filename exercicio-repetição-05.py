validadePopA = False
while validadePopA == False:
    população_A = float(input('Digite o número de habitantes da população 1:'))
    if população_A>0:
        validadePopA = True
    else:
        print('tente novamente com um número maior')
        validadePopA= False

validadecrescimentoA = False
while validadecrescimentoA == False:
    crescimento_A = float(input('digite a taxa de crescimento da população um(não pode estar em porcentagem):'))
    if crescimento_A>0:
        validadecrescimentoA = True
    else:
        print('tente novamente com um número maior')
        validadecrescimentoA= False
crescimento_A = float(input('digite a taxa de crescimento da população um(não pode estar em porcentagem):'))

validadePopB = False
while validadePopB == False:
    população_B = float(input('Digite o número de habitantes da população 2:'))
    if população_B >0:
        validadePopB = True
    else:
        print('tente novamente com um número maior')
        validadePopB= False

validadecrescimentoB = False
while validadecrescimentoB == False:
    crescimento_B = float(input('digite a taxa de crescimento da população um(não pode estar em porcentagem):'))
    if crescimento_B>0:
        validadecrescimentoB = True
    else:
        print('tente novamente com um número maior')
        validadecrescimentoB= False

anos = 0

while população_A < população_B:
    anos = anos +1
    população_A = população_A * (crescimento_A +1)
    população_B = população_B * (crescimento_B +1)

print(f"Sera preciso {anos} anos para a o número de habitantes da população A ultrapassar a população B")