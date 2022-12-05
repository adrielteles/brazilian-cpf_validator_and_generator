import cpfLib as cpfLib

while True:

    try:
        print('-'*25)
        print('Brazilian CPF tool')
        print('-'*25)
        print('options:')
        print('1. Validate')
        print('2. Generate')
        print('3. Exit')
        option = int(input('Option: '))
        if option == 1:
            print('-'*25)
            print('CPF Validator')
            print('-'*25)
            cpf = input('Enter the CPF: ')
            if cpfLib.cpfValidator(cpf):
                print('valid CPF')
            else:
                print('invalid CPF')
        elif option == 2:
            print('-'*25)
            print('CPF Generator')
            print('-'*25)
            num_cpf = input('How many CPF: ')
            cpfLib.cpfGenerator(num_cpf)
        elif option == 3:
            break
        else:
            print('Invalid Option')
    except ValueError:
        print('Invalid Option')
    except EOFError:
        break