# Função para calcular a operação matemática
def calculate():
    operation = input('''
Por favor, digite a operação matemática que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '*':
        result = number_1 * number_2
    elif operation == '/':
        if number_2 !=  0:
            result = number_1 / number_2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return
    else:
        print('Operador inválido, por favor, tente novamente.')
        return

    print('{} {} {} = {}'.format(number_1, operation, number_2, result))

# Função para perguntar ao usuário se deseja calcular novamente
def again():
    calc_again = input('Deseja calcular novamente? Digite Y para SIM ou N para NÃO.\n')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

# Chama a função principal
calculate()
again()
