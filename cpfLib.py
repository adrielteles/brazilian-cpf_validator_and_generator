import random

def cpfValidator(cpf:str):
    cpf_refactory = cpf.replace('.','').replace('-','').replace(' ','')
    invalid_cpf = cpf_refactory[0]*len(cpf_refactory)

    if invalid_cpf == cpf_refactory:
        return False
    
    nove_digitos = cpf_refactory[:9]
    contador_regressivo = 10
    resultado = 0
    for digito in nove_digitos:
        resultado += int(digito)*contador_regressivo
        contador_regressivo -=1

    primeiro_digito = (resultado*10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <=9 else 0
    

    dez_digitos = nove_digitos + str(primeiro_digito)
    contador_regressivo_2 = 11
    resultado2 = 0

    for digito in dez_digitos:
        resultado2 += int(digito)*contador_regressivo_2
        contador_regressivo_2 -=1

    segundo_digito = (resultado2*10) % 11
    segundo_digito = segundo_digito if segundo_digito <=9 else 0

    result_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

    return True if result_cpf == cpf_refactory else False


def cpfGenerator(quantity:int):

    if int(quantity) > 0:

        for _ in range(int(quantity)):
            nove_digitos = ''
            for _ in range(9):
                nove_digitos += str(random.randint(0,9))

            contador_regressivo = 10
            resultado = 0
            for digito in nove_digitos:
                resultado += int(digito)*contador_regressivo
                contador_regressivo -=1

            primeiro_digito = (resultado*10) % 11
            primeiro_digito = primeiro_digito if primeiro_digito <=9 else 0
            

            dez_digitos = nove_digitos + str(primeiro_digito)
            contador_regressivo_2 = 11
            resultado2 = 0

            for digito in dez_digitos:
                resultado2 += int(digito)*contador_regressivo_2
                contador_regressivo_2 -=1

            segundo_digito = (resultado2*10) % 11
            segundo_digito = segundo_digito if segundo_digito <=9 else 0

            result_cpf = f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:]}-{primeiro_digito}{segundo_digito}'
            print(result_cpf)
    else:
        print('Invalid Quantity.')