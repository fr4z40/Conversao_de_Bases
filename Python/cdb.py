#!/usr/bin/env python3
# Author: Eduardo Frazão ( http://github.com/fr4z40 )
# Created in: 19 Sep 2015

from subprocess import call
from time import sleep

def main_msg():
    print("\n\n\t\t\t\tEntrada\n\n")
    print("\t1 - Binario\t\t2 - Hexadecimal")
    print("\t3 - Decimal\t\t4 - Octal")

def msg():
    print("\n\tTrabalho de Avaliação")
    print("\tDiciplina: Organização de Computadores.")
    print("\n\tConversão de Bases Numericas.")
    sleep(5)


###########################################################################
################################  Decimal  ################################

def dec_to_bin(dec):
    #
    # Método alternativo.
    #
    # função nativa "bin".
    # bin(Numero_Decimal) => Retorna Binario
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # numero_decimal / 2 ---> resultado...
    #     se maior ou igual a 2:
    #         mantem a divisão, e o resto "0" ou "1" é acrescido
    #         ao array "rst",
    #     senao:
    #         encerra com o resto da divisão sendo acrescido
    #         ao array.
    # Ao final, o array deve ser retorna de modo reverso.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    while 1:
        if (dec > 1):
            rst.append(str(dec % 2))
            dec = (dec // 2)
        else:
            rst.append(str(dec % 2))
            break
    return(str(int((''.join(rst))[::-1])))



def dec_to_hex(dec):
    #
    # Método alternativo.
    #
    # função nativa "hex".
    # hex(Numero_Decimal) => Retorna Hexadecimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # idêntica à conversão de decimal para binário,
    # sendo que a divisão deve ser realizada por 16, e a "tolerancia"
    # "maior ou igual", passa a ser 9 e 16,
    # valores de resultado, de 10 à 15 tem representação em letras,
    # de "A" à "F", sendo A=10 e F=15.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    hx = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    rst = []
    while 1:
        if (dec >= 16):
            vlr = (dec % 16)
            if vlr >= 10:
                rst.append(hx[vlr])
            else:
                rst.append(str(vlr))
            dec = (dec // 16)
        else:
            vlr = (dec % 16)
            if vlr >= 10:
                rst.append(hx[vlr])
            else:
                rst.append(str(vlr))
            break
    return((''.join(rst))[::-1])



def dec_to_oct(dec):
    #
    # Método alternativo.
    #
    # Função nativa "oct".
    # oct('Valor Decimal') => Retorna Octal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # numero_decimal / 8 ---> resultado...
    #     se maior ou igual a 8:
    #         mantem a divisão, e o resto é acrescido ao array "rst".
    #     senao:
    #         encerra com o resto da divisão sendo acrescido ao array.
    # Ao final, o array deve ser retorna de modo reverso.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    while 1:
        if (dec >= 1):
            rst.append(str(dec % 8))
            dec = (dec // 8)
        else:
            rst.append(str(0))
            break
    return(str(int((''.join(rst))[::-1])))



###########################################################################
##############################  Hexadecimal  ##############################

def hex_to_bin(hex_in):
    #
    # Método alternativo.
    #
    # função nativa "bin".
    # bin(int("Valor em Hexa", 16))[2:] => Retorna binario
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Primeiro entende-se a string de entrada Hex_In como um array,
    # cada item deste array deve ser "entendido" como Decimal, e
    # em seguida, convertido para binario.
    #
    #   Exemplo: C1F ==> C=12, 1=1, F=15 ==> 12,1,15
    #            --------------------
    #               12 = 1100
    #                1 = 1
    #               15 = 1111
    #            --------------------
    #                12 - 1  -  5
    #               1100-***1-1111
    #               1100-0001-1111
    #
    # Se no resultado final houverem "0" a esquerda,
    # os mesmos podem ser removidos
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    hx = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    for h in hex_in:
        if (str.isnumeric(h) == True):
            vlr = dec_to_bin(int(h))
            rst.append('%s%s' % (('0' * (4 - len(vlr))), vlr))
        else:
            h = h.upper()
            vlr = dec_to_bin(hx[h])
            rst.append('%s%s' % (('0' * (4 - len(vlr))), vlr))
    return(str(int(''.join(rst))))



def hex_to_dex(hex_in):
    #
    # Método alternativo.
    #
    # função nativa "int".
    # int("Valor em Hexa", 16) => Retorna Decimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # A conversão de números hexadecimais em decimais é
    # realizada através da soma dos dígitos hexadecimais
    # multiplicados pela base 16 elevada à posição colunar(inversa)
    #
    #   Exemplo: 23F  ==>  2,3,15  =====>  15  3  2
    #   * ----->  posição colunar  ----->   0  1  2
    #            --------------------
    #          ( 2 * (16 ** 2)) ==> 512
    #          ( 3 * (16 ** 1)) ==> 48
    #          (15 * (16 ** 0)) ==> 15
    #            --------------------
    #          ( 512 + 48 + 15 ) ==> 575
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    hx = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    rng = (len(hex_in) - 1)
    for h in hex_in:
        if str.isnumeric(h):
            rst.append(str(int(h) * (16 ** rng)))
            rng = (rng - 1)
        else:
            h = h.upper()
            rst.append(str(hx[h] * (16 ** rng)))
            rng = (rng - 1)
    return(eval('+'.join(rst)))



def hex_to_oct(hex_in):
    #
    # Método alternativo.
    #
    # funções nativas "int" e "oct".
    # oct(int('Valor Hexadecimal',16))[2:] => Retorna Octal.
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # O Método mais Prático de conversão
    # de Hexa para Octa, é converte-lo para decimal
    # e de decimal para Octal.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    hex_in = str(hex_in)
    return(dec_to_oct(hex_to_dex(hex_in)))



###########################################################################
################################  Binario  ################################

def bin_to_hex(bin_in):
    #
    # Método alternativo.
    #
    # funções nativas "int" e "hex".
    # hex(int('Valor Binario', 2)) => Retorna Hexadecimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Para converter um número binário em hexadecimal, separa-se
    # o número binário em grupos de 4 bits, da direita para a
    # esquerda.
    # Se o número nao tiver um "tamanho"(length) multiplo de 4, é
    # preciso acrescer com "0" até que o mesmo seja multiplo de 4,
    # é possível resolver isto com um laço "while" e com constante
    # checagem do resto da operação de divisão por 4, ou seja,
    # acrescer "0" até que (("length" de "bin_in") % 4) seja igual a
    # 0, "%4" significa resto divisão por 4.
    #
    # Em seguida, transforma-se cada grupo de 4 bits em hexadecimal.
    # cada dígito binario deve ser multiplicado pelo resultado de
    # 2 elevado à "posição colunar reversa", ao final,
    # simplesmente une-se os resultados em um só.
    #
    #   Exemplo: 11010  ==>  ***1 1010  ==> 0 0 0 1 - 1 0 1 0
    #   * ----->  posição colunar  -------> 3 2 1 0 - 3 2 1 0
    #           Total de 8 dígitos, logo, 2 "grupos"
    #      --------------------------------------------------------
    #           (0*(2**3)) ==> 0    |    (1*(2**3)) ==> 8
    #           (0*(2**2)) ==> 0    |    (0*(2**2)) ==> 0
    #           (0*(2**1)) ==> 0    |    (1*(2**1)) ==> 2
    #           (1*(2**0)) ==> 1    |    (0*(2**0)) ==> 0
    #      --------------------------------------------------------
    #             0+0+0+1 = 1       |   8+0+2+0 = 10 => 10 => A
    #      --------------------------------------------------------
    #                      11010   ==>  1A
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    bin_in = str(int(bin_in))
    hx = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    lng = len(bin_in)
    if (len(bin_in) % 4 != 0):
        lng = len(bin_in)
        while 1:
            if (lng % 4 != 0):
                lng = (lng + 1)
            else:
                break
        bin_in = ('%s%s' % (('0' * (lng - len(bin_in))), bin_in))
    for r in range(lng // 4):
        blk = bin_in[:4]
        vlr = int((int(blk[0]) * (2 ** 3)) + (int(blk[1]) * (2 ** 2)))
        vlr = (vlr + ((int(blk[2]) * (2 ** 1)) + (int(blk[3]) * (2 ** 0))))
        if vlr < 10:
            rst.append(str(vlr))
        else:
            rst.append(hx[vlr])
        bin_in = bin_in[4:]
    return(''.join(rst))



def bin_to_dex(bin_in):
    #
    # Método alternativo.
    #
    # função nativa "int".
    # int('Valor Binario', 2) => Retorna Decimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # A soma de cada um dos dígitos do número binário multiplicado
    # pelo resultado de 2 elevado à posição colunar(reversa)
    #
    #   Exemplo: 11011  ==>  1 1 0 1 1
    #   * posição colunar >  4 3 2 1 0
    #      --------------------------
    #           (1*(2**4)) => 16
    #           (1*(2**3)) => 8
    #           (0*(2**2)) => 0
    #           (1*(2**1)) => 2
    #           (1*(2**0)) => 1
    #      --------------------------
    #           16+8+0+2+1 = 27
    #      --------------------------
    #            11011 ==> 27
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    bin_in = str(bin_in)
    col = (len(bin_in) - 1)
    for b in bin_in:
        rst.append(str(int(b) * (2 ** col)))
        col = (col - 1)
    return(eval('+'.join(rst)))



def bin_to_oct(bin_in):
    #
    # Método alternativo.
    #
    # funções nativas "int" e "oct".
    # oct(int('Valor Binario', 2))[2:] => Retorna Octal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # Assim como na conversão de Binario para Hexa, divide-se o
    # numero em grupos de "N" dígitos, sendo que neste caso, grupos
    # de 3 dígitos.
    # Deve-se acrescer com "0" ao "Binario de entrada" caso o
    # tamanho(length) do mesmo, nao seja um valor multiplo de 3,
    # usando o mesmo método, usado na conversão para Hexa, sendo que
    # neste caso focando um Multiplo de 3.
    # Em seguida, transforma-se cada grupo de 3 bits em Octal.
    # cada dígito binario deve ser multiplicado pelo resultado de
    # 2 elevado à "posição colunar reversa", somados e ao final,
    # simplesmente une-se os resultados em um só.
    #
    #   Exemplo: 11011  ==>  *11 - 011  ==> 0 1 1 - 0 1 1
    #   * ----->  posição colunar  -------> 2 1 0 - 2 1 0
    #           Total de 6 dígitos, logo, 2 "grupos"
    #    --------------------------------------------------
    #        (0*(2**2)) ==> 0    |    (0*(2**2)) ==> 0
    #        (1*(2**1)) ==> 2    |    (1*(2**1)) ==> 2
    #        (1*(2**0)) ==> 1    |    (1*(2**0)) ==> 1
    #    --------------------------------------------------
    #          0+2+1 = 3         |      0+2+1 = 3
    #    --------------------------------------------------
    #                     11011  ==>  33
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    bin_in = str(int(bin_in))
    lng = len(bin_in)
    if (len(bin_in) % 3 != 0):
        lng = len(bin_in)
        while 1:
            if (lng % 3 != 0):
                lng = (lng + 1)
            else:
                break
        bin_in = ('%s%s' % (('0' * (lng - len(bin_in))), bin_in))
    for r in range(lng // 3):
        blk = bin_in[:3]
        vlr = int((int(blk[0]) * (2 ** 2)) + (int(blk[1]) * (2 ** 1)))
        vlr = (vlr + (int(blk[2]) * (2 ** 0)))
        rst.append(str(vlr))
        bin_in = bin_in[3:]
    return(''.join(rst))



###########################################################################
#################################  Octal  #################################

def oct_to_dex(oct_in):
    #
    # Método alternativo.
    #
    # função nativa "int".
    # int('Valor Octal', 8) => Retorna Decimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # A conversão de números octais em decimais é obtida através da
    # soma dos dígitos do número octal multiplicados pela resultado de
    # 8(base) elevada à posição colunar(reversa) do dígito
    #
    #   Exemplo:   935      ==>     5 3 9
    #   * posição colunar   -->     0 1 2
    #     ------------------------------
    #         (5 * (8 ** 0)) => 5
    #         (3 * (8 ** 1)) => 24
    #         (9 * (8 ** 2)) => 576
    #     ------------------------------
    #            576+24+5 = 605
    #     ------------------------------
    #             935 ==> 605
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    rst = []
    oct_in = str(oct_in)
    rng = (len(oct_in) - 1)
    for o in oct_in:
        rst.append(str(int(o) * (8 ** rng)))
        rng = (rng - 1)
    return(eval('+'.join(rst)))



def oct_to_bin(oct_in):
    #
    # Método alternativo.
    #
    # funções nativas "int" e "bin".
    # bin(int('Valor Octal', 8))[2:] => Retorna Binario
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # O Método mais Prático de conversão
    # de Octal para Binario, é converte-lo para decimal
    # e de decimal para Binario.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    return(dec_to_bin(oct_to_dex(oct_in)))



def oct_to_hex(bin_in):
    #
    # Método alternativo.
    #
    # funções nativas "int" e "hex".
    # hex(int('Valor Octal', 8))[2:] => Retorna Hexadecimal
    #
    #
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    # O Método mais Prático de conversão
    # de Octal para Hexadecimal, é converte-lo para decimal
    # e de decimal para Hexadecimal.
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    return(dec_to_hex(oct_to_dex(bin_in)))

###########################################################################
###########################################################################


def oct_f():
    nn = str(input('Número >> '))
    try:
        print('Octal para Binario:\t%s' % str(oct_to_bin(nn)))
        print('Octal para Decimal:\t%s' % str(oct_to_dex(nn)))
        print('Octal para Hexa:\t%s' % str(oct_to_hex(nn)))
        input()
    except Exception as err:
        print(err)


def bin_f():
    nn = str(input('Número >> '))
    try:
        print('Binario para Decimal:\t%s' % str(bin_to_dex(nn)))
        print('Binario para Hexa:\t%s' % str(bin_to_hex(nn)))
        print('Binario para Octal:\t%s' % str(bin_to_oct(nn)))
        input()
    except Exception as err:
        print(err)


def hex_f():
    nn = str(input('Número >> '))
    try:
        print('Hexadecimal para Binario:\t%s' % str(hex_to_bin(nn)))
        print('Hexadecimal para Decimal:\t%s' % str(hex_to_dex(nn)))
        print('Hexadecimal para Octal:\t\t%s' % str(hex_to_oct(nn)))
        input()
    except Exception as err:
        print(err)


def dec_f():
    nn = int(input('Número >> '))
    try:
        print('Decimal para Binario:\t\t%s' % str(dec_to_bin(nn)))
        print('Decimal para Hexadecimal:\t%s' % str(dec_to_hex(nn)))
        print('Decimal para Octal:\t\t%s' % str(dec_to_oct(nn)))
        input()
    except Exception as err:
        print(err)



if __name__ == '__main__':
    try:
        msg();
        call('title Conversor de Bases Numericas', shell=True) #=> Windows
        while 1:
            options = {4:oct_f, 3:dec_f, 2:hex_f, 1:bin_f}
            call('cls', shell=True) #=> windows
            #call('reset', shell=True) #=> Linux
            main_msg()
            opt = str(input('\n\n>> '))
            if (str.isnumeric(opt.strip()) == True):
                try:
                    ((options[int(opt.strip())])())
                except:
                    pass
            elif (((opt.strip()).lower()) == 'sair'): # comando "Sair".
                quit()
            else:
                pass
    except:
        pass