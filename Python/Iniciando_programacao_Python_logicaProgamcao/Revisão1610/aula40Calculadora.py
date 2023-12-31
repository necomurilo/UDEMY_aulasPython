""" Calculadora com while """

# while True:
#     sair = input('Quer sair? [s]im: ')
#     sair = sair.lower() # converte para minusculo
#     sair = sair.startswith('s')  # checa se começa com a letra s
#     # termina com uma letra .endswith
#     print(sair)

#RESUMO do código acima

while True:
    numero_1 = input('Digite um número: ')
    operador = input('digite o operador (+-/*) ')
    numero_2 = input('Digite um número: ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    #except Exception as error:
        #print(error)
    if numeros_validos is None:
        print('um ou ambos os números digitados são inválidos. ')
        continue
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador. ')
        continue

    print('Realizando sua conta, confira o resultado a baixo v ')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui.')




    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
