def contar_trocas_minimas(permutacao):
# Calcula o número mínimo de trocas para transformar uma permutação em ordem crescente.
    n = len(permutacao)
    visitado = [False] * n
    ciclos = 0

# Percorre cada elemento da permutação
    for i in range(n):
        if not visitado[i]:
            ciclos += 1
            j = i
            # Marca todos os elementos do ciclo como visitados
            while not visitado[j]:
                visitado[j] = True
                j = permutacao[j] - 1

# O número mínimo de trocas é igual ao tamanho da permutação menos o número de ciclos
    return n - ciclos

def resolver_linhas_contenedores(): # função principal
     # Lê o número de linhas (L) e colunas (C)
    L, C = map(int, input().split())

    
    matriz_atual = []
# Lê a matriz atual de contêineres
    
    for _ in range(L):
        linha = list(map(int, input().split()))
        matriz_atual.append(linha)

     # Lista que mapeia cada linha atual para sua linha original
    P_linhas_atual_para_original = [0] * L
    # Conjunto para garantir que não haja duplicidade de linhas originais
    linhas_originais_encontradas = set()


     # Verifica se cada linha contém contêineres da mesma linha original
    for l in range(L):
        X_l_1 = matriz_atual[l][0]
        # Calcula a linha original com base no primeiro número da linha
        linha_original = (X_l_1 + C - 1) // C


         # Se essa linha original ainda não foi usada
        if linha_original not in linhas_originais_encontradas:
            for c in range(C):
                cont_num = matriz_atual[l][c]
                # Verifica se todos os contêineres da linha pertencem à mesma linha original
                if (cont_num + C - 1) // C != linha_original:
                    return '*' # Impossível reorganizar
            linhas_originais_encontradas.add(linha_original)
            P_linhas_atual_para_original[l] = linha_original
        else:
            return '*' # Linha original duplicada

    # Verifica se todas as linhas originais estão presentes
    if len(linhas_originais_encontradas) != L:
        return '*'

    # Cria a permutação das linhas
    P_linhas_alvo = [0] * L
    for pos_atual, linha_original in enumerate(P_linhas_atual_para_original):
       
        P_linhas_alvo[linha_original - 1] = pos_atual + 1
        
        # Calcula o número mínimo de trocas de linhas
    trocas_linhas = contar_trocas_minimas(P_linhas_alvo)

   # Seleciona a linha que deveria ser a linha 1 original
    pos_linha_1_original = P_linhas_alvo[0] - 1
    linha_para_analisar = matriz_atual[pos_linha_1_original]

# Cria a permutação das colunas
    P_colunas_alvo = [0] * C
    for col_atual in range(C):
        cont_num = linha_para_analisar[col_atual]
         # Verifica se os contêineres estão dentro do intervalo esperado
        if not (1 <= cont_num <= C):
            return '*' # Contêiner fora da faixa esperada
        coluna_original = cont_num
        P_colunas_alvo[coluna_original - 1] = col_atual + 1


    # Calcula o número mínimo de trocas de colunas
    trocas_colunas = contar_trocas_minimas(P_colunas_alvo)

     # Retorna o total mínimo de trocas necessárias
    return trocas_linhas + trocas_colunas

# Executa a função principal e imprime o resultado
print(resolver_linhas_contenedores())
