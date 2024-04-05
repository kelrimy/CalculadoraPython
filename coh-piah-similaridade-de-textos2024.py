import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def soma_tamanho_palavras(palavras):
    '''Essa função recebe uma lista de palavras e devolve a soma do tamanho de todas as palavras'''
    return sum(len(palavra) for palavra in palavras)

def soma_tamanho_sentencas(sentencas):
    '''Essa função recebe uma lista de sentenças e devolve a soma do tamanho de todas as sentenças'''
    return sum(len(sentenca) for sentenca in sentencas)

def soma_tamanho_frases(frases):
    '''Essa função recebe uma lista de frases e devolve a soma do tamanho de todas as frases'''
    return sum(len(frase) for frase in frases)

def type_token_ratio(palavras):
    '''Essa função recebe uma lista de palavras e devolve a relação Type-Token'''
    return n_palavras_diferentes(palavras) / len(palavras)

def hapax_legomana_ratio(palavras):
    '''Essa função recebe uma lista de palavras e devolve a Razão Hapax Legomana'''
    return n_palavras_unicas(palavras) / len(palavras)

def complexidade_sentenca(sentencas, frases):
    '''Essa função recebe uma lista de sentenças e uma lista de frases e devolve a complexidade média da sentença'''
    return len(frases) / len(sentencas)

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    similaridade = 0
    for i in range(len(as_a)):
        similaridade += abs(as_a[i] - as_b[i])
    similaridade /= 6
    return similaridade

def calcula_assinatura(texto):
    '''Essa função recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    wal = soma_tamanho_palavras(palavras) / len(palavras)
    ttr = type_token_ratio(palavras)
    hlr = hapax_legomana_ratio(palavras)
    sal = soma_tamanho_sentencas(sentencas) / len(sentencas)
    sac = complexidade_sentenca(sentencas, frases)
    pal = soma_tamanho_frases(frases) / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)
        similaridades.append(similaridade)

    return similaridades.index(min(similaridades)) + 1

# Leitura da assinatura
assinatura = le_assinatura()

# Leitura dos textos
textos = le_textos()

# Avaliação dos textos
texto_plagio = avalia_textos(textos, assinatura)

print(f"O texto {texto_plagio} é o mais provável de ser um plágio.")
