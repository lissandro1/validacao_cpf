txt = ' verificação de cpf '
print(f'{txt.upper():#^32}')

while True:
    cpf_str = input('Digite seu CPF\n(ex: XXX.XXX.XXX-XX): ').split('-')
    if len(cpf_str[0]) == 11 and '.' in cpf_str[0]:
        next
    else:
        print('Digite um valor válido (Ex: XXX.XXX.XXX-XX)')
        continue

    cpf_numb = cpf_str[0].split('.')
    cpf_ok = []
    for i in cpf_numb:
        cpf_ok += i

    # validação do primeiro digito
    d = 10
    sum_1 = 0
    for digit in cpf_ok:
        sum_1 += int(digit) * d
        d -= 1

    resul_1 = (sum_1 * 10) % 11
    if resul_1 > 9:
        digit_ver_1 = 0
    else:
        digit_ver_1 = resul_1

    # validação do segundo dígito
    cpf_ok.append(digit_ver_1)
    sum_2 = 0
    for digit2 in cpf_ok:
        sum_2 += int(digit2)
        
    
    resul_2 = (sum_2 * 10) % 11
    if resul_2 > 9:
        digit_ver_2 = 0
    else:
        digit_ver_2 = resul_2

    valid_1 = cpf_str[1][0]
    valid_2 = cpf_str[1][1]
    if digit_ver_1 == int(valid_1) and digit_ver_2 == int(valid_2):
        print(f'CPF verificado. Está OK!')
        break
    else:
        print('CPF verificado e o número não confere!')
