validade = False
while validade == False:
    print('Digite seu nome de usuario')
    nome = (input())
    print('Digite uma senha:')
    senha = (input())
    if senha != nome:
        print('Esse é seu nome de ususario:', nome)
        print('Essa é sua senha:', senha)
        validade = True
    else:
        print('A senha não pode ser igual o nome, porfavor digite tudo novamente:')
