import time
import random

def contar_trocas_minimas(permutacao):
    n = len(permutacao)
    visitado = [False] * n
    ciclos = 0
    for i in range(n):
        if not visitado[i]:
            ciclos += 1
            j = i
            while not visitado[j]:
                visitado[j] = True
                j = permutacao[j] - 1
    return n - ciclos

def resolver_linhas_contenedores(L, C, matriz_atual):
    P_linhas_atual_para_original = [0] * L
    linhas_originais_encontradas = set()

    for l in range(L):
        X_l_1 = matriz_atual[l][0]
        linha_original = (X_l_1 + C - 1) // C
        if linha_original not in linhas_originais_encontradas:
            for c in range(C):
                cont_num = matriz_atual[l][c]
                if (cont_num + C - 1) // C != linha_original:
                    return '*'
            linhas_originais_encontradas.add(linha_original)
            P_linhas_atual_para_original[l] = linha_original
        else:
            return '*'

    if len(linhas_originais_encontradas) != L:
        return '*'

    P_linhas_alvo = [0] * L
    for pos_atual, linha_original in enumerate(P_linhas_atual_para_original):
        P_linhas_alvo[linha_original - 1] = pos_atual + 1

    trocas_linhas = contar_trocas_minimas(P_linhas_alvo)

    pos_linha_1_original = P_linhas_alvo[0] - 1
    linha_para_analisar = matriz_atual[pos_linha_1_original]

    P_colunas_alvo = [0] * C
    for col_atual in range(C):
        cont_num = linha_para_analisar[col_atual]
        if not (1 <= cont_num <= C):
            return '*'
        coluna_original = cont_num
        P_colunas_alvo[coluna_original - 1] = col_atual + 1

    trocas_colunas = contar_trocas_minimas(P_colunas_alvo)

    return trocas_linhas + trocas_colunas

def ler_entradas_arquivo(nome_arquivo):
    """
    Lê entradas de um arquivo TXT separadas por '@'
    Retorna uma lista de tuplas (L, C, matriz)
    """
    entradas = []
    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().strip()
        
        # Divide as entradas pelo caractere '@'
        blocos_entrada = conteudo.split('@')
        
        for bloco in blocos_entrada:
            if not bloco.strip():
                continue
                
            linhas = bloco.strip().split('\n')
            
            # Primeira linha contém L e C
            dimensoes = linhas[0].split()
            L = int(dimensoes[0])
            C = int(dimensoes[1])
            
            # Linhas seguintes formam a matriz
            matriz = []
            for i in range(1, 1 + L):
                if i < len(linhas):
                    linha_numeros = list(map(int, linhas[i].split()))
                    matriz.append(linha_numeros)
            
            if len(matriz) == L:
                entradas.append((L, C, matriz))
    
    return entradas

def processar_entradas_arquivo(nome_arquivo_entrada, nome_arquivo_saida):
    """
    Processa todas as entradas do arquivo e salva resultados em arquivo de saída
    """
    print(f"Processando entradas do arquivo: {nome_arquivo_entrada}")
    print(f"Salvando resultados em: {nome_arquivo_saida}")
    print("=" * 60)
    
    # Ler entradas do arquivo
    entradas = ler_entradas_arquivo(nome_arquivo_entrada)
    
    resultados = []
    tempo_total = 0
    
    # Processar cada entrada
    for i, (L, C, matriz) in enumerate(entradas, 1):
        print(f"Entrada {i}: {L}×{C} = {L*C} elementos")
        
        inicio = time.time()
        resultado = resolver_linhas_contenedores(L, C, matriz)
        fim = time.time()
        
        tempo_execucao = fim - inicio
        tempo_total += tempo_execucao
        
        resultados.append(resultado)
        
        print(f"  Resultado: {resultado}")
        print(f"  Tempo: {tempo_execucao:.3f} segundos")
        print(f"  {'-' * 40}")
    
    # Salvar resultados no arquivo de saída
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        for resultado in resultados:
            arquivo_saida.write(f"{resultado}\n")
    
    # Relatório final
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL:")
    print("=" * 60)
    
    print(f"Total de entradas processadas: {len(entradas)}")
    print(f"Tempo total de execução: {tempo_total:.3f} segundos")
    print(f"Tempo médio por entrada: {tempo_total/len(entradas):.3f} segundos")
    print(f"Resultados salvos em: {nome_arquivo_saida}")
    
    # Mostrar preview dos resultados
    print(f"\nNúmero de trocas:")
    for i, resultado in enumerate(resultados, 1):
        print(f"Entrada {i}: {resultado}")



# Fluxo principal
if __name__ == "__main__":
    nome_arquivo_entrada = "entradas_teste.txt"
    nome_arquivo_saida = "saidas_teste.txt"
    
    # Opção 1: Gerar arquivo de exemplo (descomente a linha abaixo)
    # gerar_arquivo_exemplo(nome_arquivo_entrada, 100)
    
    # Opção 2: Processar arquivo existente
    try:
        processar_entradas_arquivo(nome_arquivo_entrada, nome_arquivo_saida)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo_entrada}' não encontrado!")
        print("Gerando arquivo de exemplo...")
        gerar_arquivo_exemplo(nome_arquivo_entrada, 10)  # Gera 10 entradas para teste
        print("\nExecute novamente para processar as entradas.")