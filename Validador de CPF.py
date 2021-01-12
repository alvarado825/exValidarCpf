'''Validador de CPF'''

while(1):

    cpf = input("Digite um CPF: ")
    cpfFiltrado = ''
    for i in cpf:
        if i == '.' or i == '-':
            continue
        else:
            cpfFiltrado +=  i

    cpfFiltrado = cpfFiltrado[:-2]
    print(cpfFiltrado)

    contador = 10
    total = 0
    for index in cpfFiltrado:

        total = total + (int(index) * (contador))
        print(f'{int(index)} * {contador} = {int(index)*(contador)}')
        contador -= 1

    print(f'Resultado: {total}')
    resultado = 11 - (total % 11)
    digito1 = 0 if (resultado > 9) else resultado

    print(f'O digito 1 é: {digito1}')
    print(f'\n{10*"#"}Verificando o Segundo Digito',end= 10* '#')
    print('\n')

    cpfFiltrado += str(digito1)
    contador = 11
    total = 0
    for index in cpfFiltrado:
        total = total +(int(index) * contador)
        print(f'{index} * {contador} = {int(index) * contador}')
        contador -= 1

    print(f'Resultado: {total}')
    digito2 = 11-(total % 11)
    print(f'O digito 2 é: {digito2}')

    cpfResultante = cpfFiltrado + str(digito2)

    retorno = "Cpf Válido" if(cpfResultante == (cpf.replace('.','')).replace('-', '')) else 'Cpf Inválido'
    print('\n',retorno)


