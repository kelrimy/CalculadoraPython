import random

# Constante identificada com letras maiúsculas para destacar que não devem ser modificadas em outras partes do código
MAX_TENTATIVAS = 5

print(f"{'*' * 50}\n{'JOGO DA FORCA':^50}\n{'*' * 50}")

# Loop para repetir o jogo até o usuário querer parar
while True:
    # Opções de temas para o jogo
    tema = input("Escolha uma das temáticas: \n1- Animais.\n2- Frutas.\n3- Países.\n ").strip()

    # Controle de erro para digitação ou escolha fora das opções
    while tema not in "123":
        print("Escolha um dos temas sugeridos!")
        tema = input("Escolha uma das temáticas: \n1- Animais.\n2- Frutas.\n3- Países.\n ").strip()

    # Listas para cada tema
    if tema == "1":
        palavras = ["cachorro", "gato", "elefante", "cavalo", "formiga", "vaca", "macaco", "borboleta", "peixe", "lhama"]
    elif tema == "2":
        palavras = ["manga", "banana", "goiaba", "acerola", "laranja", "morango", "tangerina", "abacaxi", "framboesa", "uva"]
    elif tema == "3":
        palavras = ["Alemanha", "Brasil", "Uruguai", "Estados Unidos", "Espanha", "Irlanda", "Argentina", "Israel", "Reino Unido", "Holanda"]

    # Escolha aleatória de uma palavra
    palavra_secreta = random.choice(palavras)

    # Letras corretas que o jogador adivinhou
    letras_corretas = ['_'] * len(palavra_secreta)

    # Conjunto de letras erradas que o jogador já tentou
    letras_erradas = set()

    # Loop principal do jogo
    while MAX_TENTATIVAS > 0:
        # Mostrar o estado atual da palavra
        print('Palavra:', ' '.join(letras_corretas))

        # Solicitar uma letra ao jogador
        letra = input('Digite uma letra: ').lower()

        # Verificar se a letra já foi tentada
        if letra in letras_corretas or letra in letras_erradas:
            print('Você já tentou essa letra. Tente novamente.')
            continue

        # Verificar se a letra está na palavra secreta
        if letra in palavra_secreta:
            # Atualizar letras corretas com a nova letra
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_corretas[i] = letra
        else:
            # Decrementar o número de tentativas restantes e adicionar a letra errada ao conjunto
            MAX_TENTATIVAS -= 1
            letras_erradas.add(letra)
            print('Letra incorreta. Tentativas restantes:', MAX_TENTATIVAS)

        # Verificar se o jogador adivinhou a palavra
        if ''.join(letras_corretas) == palavra_secreta:
            print('Parabéns! Você ganhou! A palavra era:', palavra_secreta)
            break

    # Se o jogador esgotar todas as tentativas
    if MAX_TENTATIVAS == 0:
        print('Você perdeu! A palavra correta era:', palavra_secreta)

    print()

    continua = input("Deseja jogar novamente? [S/N] ").strip().lower()
    while continua not in "sn":
        print("Digite somente S ou N.")
        continua = input("Deseja jogar novamente? [S/N] ").strip().lower()

    if continua == "n":
        print("Obrigado e volte sempre!")
        break

