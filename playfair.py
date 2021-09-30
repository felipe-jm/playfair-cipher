# Matriz 5 x 5
# Y Q D L G M J X F U V W C P B O S K R E T H N A I --> Y	Q	D	L	G
#                                                       M	J	X	F	U
#                                                       V	W	C	P	B
#                                                       O	S	K	R	E
#                                                       T	H	N	A	I

# Frase a ser cifrada: E ESTA CIFRA E INQUEBRAVEL

# Codificação
# Cada par de caracteres é codificado utilizando a tabela de Playfair e aplicando as regras seguintes:

# 1. Se os dois caracteres estão na mesma linha na tabela, são substituídos pelos caracteres imediatamente à direita
# de cada um deles. Numa linha da tabela é considerado que à direita do último caracter está o primeiro.
# Exemplo: ES é codificado para OK.

# 2. Se ambos os caracteres estiverem na mesma coluna, são substituídos pelos caracteres imediatamente a baixo
# de cada um deles. Numa coluna da tabela é considerado que a baixo do último caracter está o primeiro.
# Exemplo: RA é codificado para AL

# 3. Se os dois caracteres estão em linhas e colunas diferentes na tabela, cada caracter é substituído pelo caracter
# na mesma linha e que está na mesma coluna em que está o outro caracter.
# Exemplo: CI é codificado por BN.

# Decifrar a Mensagem
# Para decifrar a mensagem usam-se as mesmas regras, mas se os dois caracteres estão na
# mesma linha devem ser substituídos pelos caracteres imediatamente à esquerda
# e, se estão na mesma coluna, pelos imediatamente a cima.

import numpy as np

escolha_disponiveis = [1, 2, 3, 4, 5, 6]

PRIMEIRA_COLUNA = 0
ULTIMA_COLUNA = 4

PRIMEIRA_LINHA = 0
ULTIMA_LINHA = 4


def preparar_mensagem(mensagem):
    mensagem = mensagem.lower()
    mensagem = mensagem.replace(" ", "")

    mensagem = list(mensagem)

    for i, caracter in enumerate(mensagem):
        proximo_caracter = i + 1
        if proximo_caracter < len(mensagem):
            if caracter == mensagem[proximo_caracter]:
                mensagem.insert(proximo_caracter, 'x')

    # Como a cifra é realizada de acordo com duas letras juntas, não
    # se pode ter um número ímpar de letras, por isso deve-se adicionar um
    # 'x' após última letra
    if len(mensagem) % 2 != 0:
        mensagem.append('x')

    return mensagem


def preparar_tabela_cifra(alfabeto):
    alfabeto = alfabeto.lower()
    tabela_cifra = alfabeto.split(' ')
    tabela_cifra = np.array_split(tabela_cifra, 5)
    return tabela_cifra


def achar_localizacao_caracter(caracter, tabela_cifra):
    for i in range(5):
        for j in range(5):
            if caracter == tabela_cifra[i][j]:
                return {"linha": i, "coluna": j}


def achar_proxima_letra_linha(linha, coluna, tabela_cifra, decifrar=False):
    operacao = -1 if decifrar else 1
    coluna_limite = PRIMEIRA_COLUNA if decifrar else ULTIMA_COLUNA
    proxima_coluna = ULTIMA_COLUNA if decifrar else PRIMEIRA_COLUNA

    if coluna != coluna_limite:
        # Letra no meio da matriz (andar uma coluna para a direita)
        proxima_letra = tabela_cifra[linha][coluna + operacao]
    else:
        # Letra na última coluna (ir para coluna inicial ou final)
        proxima_letra = tabela_cifra[linha][proxima_coluna]

    return proxima_letra


def achar_proxima_letra_coluna(linha, coluna, tabela_cifra, decifrar=False):
    operacao = -1 if decifrar else 1
    linha_limite = PRIMEIRA_LINHA if decifrar else ULTIMA_LINHA
    proxima_linha = ULTIMA_LINHA if decifrar else PRIMEIRA_LINHA

    if linha != linha_limite:
        # Letra no meio da matriz (andar uma coluna para a direita)
        proxima_letra = tabela_cifra[linha + operacao][coluna]
    else:
        # Letra na última linha (ir para linha inicial ou final)
        proxima_letra = tabela_cifra[proxima_linha][coluna]

    return proxima_letra


def formatar_mensagem_cifrada(mensagem):
    mensagem_final = ''
    counter = 0
    while counter < len(mensagem):
        letra1 = mensagem[counter]
        letra2 = mensagem[counter + 1]
        letra3 = mensagem[counter + 2]
        letra4 = mensagem[counter + 3]

        mensagem_final += f'{letra1}{letra2}{letra3}{letra4}'

        mensagem_final = mensagem_final.upper()

        mensagem_final += ' '

        counter += 4

    return mensagem_final


def formatar_mensagem_decifrada(mensagem):
    mensagem_final = ''
    counter = 0
    while counter < len(mensagem):
        letra1 = mensagem[counter]
        letra2 = mensagem[counter + 1]

        mensagem_final += f'{letra1}{letra2}'

        mensagem_final = mensagem_final.upper()

        mensagem_final += ' '

        counter += 2

    return mensagem_final


def cifrar(mensagem, tabela_cifra, decifrar=False):
    counter = 0

    mensagem_cifrada = mensagem

    while counter < len(mensagem):
        primeiro_caracter = mensagem[counter]
        segundo_caracter = mensagem[counter + 1]

        localizacao_primeiro_caracter = achar_localizacao_caracter(
            primeiro_caracter, tabela_cifra
        )

        localizacao_segundo_caracter = achar_localizacao_caracter(
            segundo_caracter, tabela_cifra
        )

        linha_primeiro_caracter = localizacao_primeiro_caracter['linha']
        coluna_primeiro_caracter = localizacao_primeiro_caracter['coluna']

        linha_segundo_caracter = localizacao_segundo_caracter['linha']
        coluna_segundo_caracter = localizacao_segundo_caracter['coluna']

        # Execução das regras da cifra de Playfair
        if linha_primeiro_caracter == linha_segundo_caracter:
            # Primeira regra
            proxima_letra_primeiro_caracter = achar_proxima_letra_linha(
                linha_primeiro_caracter,
                coluna_primeiro_caracter,
                tabela_cifra,
                decifrar=decifrar
            )

            mensagem_cifrada[counter] = proxima_letra_primeiro_caracter

            proxima_letra_segundo_caracter = achar_proxima_letra_linha(
                linha_segundo_caracter,
                coluna_segundo_caracter,
                tabela_cifra,
                decifrar=decifrar
            )

            mensagem_cifrada[counter + 1] = proxima_letra_segundo_caracter

        elif coluna_primeiro_caracter == coluna_segundo_caracter:
            # Segunda regra
            proxima_letra_primeiro_caracter = achar_proxima_letra_coluna(
                linha_primeiro_caracter,
                coluna_primeiro_caracter,
                tabela_cifra,
                decifrar=decifrar
            )

            mensagem_cifrada[counter] = proxima_letra_primeiro_caracter

            proxima_letra_segundo_caracter = achar_proxima_letra_coluna(
                linha_segundo_caracter,
                coluna_segundo_caracter,
                tabela_cifra,
                decifrar=decifrar
            )

            mensagem_cifrada[counter + 1] = proxima_letra_segundo_caracter

        else:
            # Terceira regra
            proxima_letra_primeiro_caracter = tabela_cifra[linha_primeiro_caracter][coluna_segundo_caracter]

            proxima_letra_segundo_caracter = tabela_cifra[linha_segundo_caracter][coluna_primeiro_caracter]

            mensagem_cifrada[counter] = proxima_letra_primeiro_caracter

            mensagem_cifrada[counter + 1] = proxima_letra_segundo_caracter

        counter += 2

    if decifrar:
        print('Mensagem decifrada: ',
              formatar_mensagem_decifrada(mensagem_cifrada))
    else:
        print('Mensagem cifrada: ', formatar_mensagem_cifrada(mensagem_cifrada))

    return mensagem_cifrada


def requisitar_escolha():
    print(
        '''
-------------------------------------------
| 1. Escolher uma tabela de cifra nova    |
| 2. Introduzir uma mensagem para cifrar  |
| 3. Ver a mensagem cifrada               |
| 4. Decifrar mensagem                    |
| 5. Ver o alfabeto                       |
| 6. Terminar                             |
-------------------------------------------
        '''
    )

    escolha = int(input())
    return escolha


def main():
    alfabeto = 'Y Q D L G M J X F U V W C P B O S K R E T H N A I'

    print('Alfabeto inicial: ', alfabeto)

    tabela_cifra = preparar_tabela_cifra(alfabeto)

    mensagem_a_cifrar = 'E ESTA CIFRA E INQUEBRAVEL'

    print('Mensagem inicial: ', mensagem_a_cifrar)

    mensagem_a_cifrar = preparar_mensagem(mensagem_a_cifrar)

    escolha = requisitar_escolha()

    while escolha != 6:
        if escolha not in escolha_disponiveis:
            print('Faça uma escolha válida')

            escolha = requisitar_escolha()
            continue

        if escolha == 1:
            print('Insira a nova tabela de cifra')

            alfabeto = input()
            tabela_cifra = preparar_tabela_cifra(tabela_cifra)

            cifrar(mensagem_a_cifrar, tabela_cifra)

            escolha = requisitar_escolha()
            continue

        if escolha == 2:
            print('Insira a nova mensagem que será cifrada')

            mensagem = input()
            mensagem_a_cifrar = preparar_mensagem(mensagem)

            cifrar(mensagem_a_cifrar, tabela_cifra)

            escolha = requisitar_escolha()
            continue

        if escolha == 3:
            cifrar(mensagem_a_cifrar, tabela_cifra)

            escolha = requisitar_escolha()

        if escolha == 4:
            mensagem_cifrada = cifrar(mensagem_a_cifrar, tabela_cifra)

            cifrar(mensagem_cifrada, tabela_cifra, decifrar=True)

            escolha = requisitar_escolha()

        if escolha == 5:
            print(alfabeto)

            escolha = requisitar_escolha()


main()
