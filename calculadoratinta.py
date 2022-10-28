from math import ceil
print('\033[1;34;7m=-=-\033[m'*9)
print('{:*^40}'.format('\033[1;35mCALCULADORA DE TINTA\033[m'))
print('\033[1;34;7m=-=-\033[m'*9)
print('''\033[1;34;mEscolha o tipo de lata
[1]Balde 20L
[2]Lata 18L
[3]Galão 3,6L\033[m''')
opção = int(input('Escolha uma opção: '))
rendimento = int(input('Rendimento(M²) acabado : '))
demãos = int(input('Quantidade demãos: '))
rend2 = rendimento / demãos
área_total = float(input('Área total (M²): '))
qtd = área_total / rend2
if opção == 1:
    print('\033[1;35;7mTotal: {} lata(s) de 20L\033[m'.format(ceil(qtd)))
elif opção == 2:
    print('\033[1;35;7mTotal: {} lata(s) de 18L\033[m'.format(ceil(qtd)))
else:
    print('\033[1;32;7mTotal: {} galão(ões) de 3,6L\033[m'.format(ceil(qtd)))
print('\033[1;40;7mATENÇÃO: As condições da superfície influenciam diretamente no rendimento do produto.\033[m')
print('\033[1;40;7mPara um bom rendimento é necessário que as paredes não tenham irregularidades.\033[m')
