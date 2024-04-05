# Função para que o computador escolha quantas peças tirar
def computador_escolhe_jogada(n, m):
    jogcomp = 0
    # Lógica para determinar quantas peças o computador irá tirar
    if n > m and n % (m + 1) != 0:
        jogcomp = n % (m + 1)
    elif n > m and n % (m + 1) == 0:
        jogcomp = m
    elif n <= m:
        jogcomp = n

    # Exibição das mensagens conforme as regras do jogo
    if jogcomp > 1 and (n - jogcomp) > 1:
        print(f'O computadpr tirou {jogcomp} peças.\nAgora restam {n - jogcomp} peças no tabuleiro.')
    elif jogcomp == 1 and (n - jogcomp) > 1:
        print(f'O computadpr tirou uma peça.\nAgora restam {n - jogcomp} peças no tabuleiro.')
    elif jogcomp == 1 and (n - jogcomp) == 1:
        print(f'O computadpr tirou uma peça.\nAgora resta apenas uma peça no tabuleiro.')
    elif jogcomp > 1 and (n - jogcomp) == 1:
        print(f'O computadpr tirou {jogcomp} peças.\nAgora resta apenas uma peça no tabuleiro.')

    return jogcomp


# Função para que o usuário escolha quantas peças tirar
def usuario_escolhe_jogada(n, m):
    jogusu = int(input('Quantas peças você vai tirar? '))
    if jogusu > m or jogusu <= 0 or jogusu > n:
        print('Oops! Jogada inválida! Tente de novo.')
        jogusu = usuario_escolhe_jogada(n, m)
    elif jogusu <= m and jogusu > 1 and (n - jogusu) > 1:
        print(f'Você tirou {jogusu} peças.\nAgora restam {n - jogusu} peças no tabuleiro.')
    elif jogusu <= m and jogusu > 1 and (n - jogusu) == 1:
        print(f'Você tirou {jogusu} peças.\nAgora resta apenas uma peça no tabuleiro.')
    elif jogusu == 1 and (n - jogusu) > 1:
        print(f'Você tirou uma peça.\nAgora restam {n - jogusu} peças no tabuleiro.')
    elif jogusu == 1 and (n - jogusu) == 1:
        print(f'Você tirou uma peça.\nAgora resta apenas uma peça no tabuleiro.')
    elif (n - jogusu) == 0 and jogusu > 1:
        print(f'Você tirou {jogusu} peças.\n Fim de jogo! Você ganhou!')
    elif (n - jogusu) == 0 and jogusu == 1:
        print(f'Você tirou uma peça.\n Fim de jogo! Você ganhou!')

    return jogusu


# Função para executar uma partida do jogo NIMz
def partida():
    while True:
        # Solicita a quantidade de peças
        n = int(input('Quantas peças? '))

        # Validação da entrada de n
        if n <= 0:
            print('Valor inválido para o número de peças. Por favor, insira um valor inteiro maior que zero.')
        else:
            break

    # Solicita o limite de peças por jogada
    while True:
        m = int(input('Limite de peças por jogada? '))

        # Validação da entrada de m
        if m <= 0 and m > n:
            print('Valor inválido para o limite de peças por jogada. Por favor, insira um valor positivo menor que o número de peças.')
        else:
            break

    # Lista para armazenar o número de peças retiradas de cada jogada
    pecas_retiradas = []

    # Verifica quem começa a partida
    if n % (m + 1) == 0:
        print('Você começa!')
        vencedor = 1
    else:
        print('Computador começa!')
        vencedor = 2

    # Executa os turnos até o fim do jogo
    while n > 0:
        if vencedor == 1:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            pecas_retiradas.append(jogada_usuario)
            if n == 0:
                print(f'Você tirou {jogada_usuario} peças.')
                print('Fim do jogo! Você ganhou!')
                return 1
            vencedor = 2
        else:
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            pecas_retiradas.append(jogada_computador)
            if n == 0:
                print(f'O computador tirou {jogada_computador} peças.')
                print('Fim do jogo! O computador ganhou.')
                return 2
            vencedor = 1


# Outra opção de jogo e chamada de funções
placar_usuario = 0
placar_computador = 0

tipodepartida = input(
    "Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n\n :   ")
while tipodepartida not in ['1', '2']:
    print('INVÁLIDO! Digite somente 1 ou 2')
    tipodepartida = input(
        "Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato \n\n:   ")

if tipodepartida == '1':
    print('Você escolheu jogada única!')
    partida()
else:
    print('Você escolheu campeonato!')
    for p in range(1, 4):
        print(f'**** Rodada {p} ****')
        vencedor = partida()
        if vencedor == 1:
            placar_usuario += 1
        else:
            placar_computador += 1

    print('\n**** Final do campeonato! ****\n')
    print(f'Placar: Você {placar_usuario} x {placar_computador} Computador')



