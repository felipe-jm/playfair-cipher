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


def cifrar(mensagem, tabela_cifra):
    print(mensagem)
    print(tabela_cifra)

    counter = 0

    while counter < len(mensagem):
        caracter_atual = mensagem[counter]
        proximo_caracter = mensagem[counter + 1]

        print('caracter_atual', caracter_atual)
        print('proximo_caracter', proximo_caracter)

        localizacao_caracter_atual = achar_localizacao_caracter(
            caracter_atual, tabela_cifra
        )

        localizacao_proximo_caracter = achar_localizacao_caracter(
            proximo_caracter, tabela_cifra
        )

        print('localizacao_caracter_atual', localizacao_caracter_atual)
        print('localizacao_proximo_caracter', localizacao_proximo_caracter)

        # Execução das regras da cifra de Playfair
        if localizacao_caracter_atual['linha'] == localizacao_proximo_caracter['linha']:
            print('Executa primeira regra')
        elif localizacao_caracter_atual['coluna'] == localizacao_proximo_caracter['coluna']:
            print('Executa segunda regra')
        else:
            print('Executa terceira regra')

        counter += 2


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

    tabela_cifra = preparar_tabela_cifra(alfabeto)

    mensagem_a_cifrar = 'E ESTA CIFRA E INQUEBRAVEL'

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

        if escolha == 5:
            print(alfabeto)

            escolha = requisitar_escolha()


main()
