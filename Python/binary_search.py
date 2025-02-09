lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_busca(list, value):
    init = 0 #começo do vetor / position
    end = len(list) #fim do vetor / position

    while(init <= end):
        middle = (init + end)//2 #meio do vetor / position
        print(middle)

        if(list[middle] == value):
            return print(f"Valor {value} encontrado na posição {middle+1}º")
        
        if(list[middle] < value):
            init = middle + 1

        if(list[middle] > value):
            end = middle - 1

    print("Elemento não encontrado")

binary_busca(lista, 7)

vetor = [10, 7, 1, 12, 4, 9, 6, 5]

def busca_binaria_em_vetor_nao_ordenado(vetor, valor):
    # Ordena o vetor antes de aplicar a busca binária
    vetor_ordenado = sorted(vetor)
    print(f"Vetor ordenado: {vetor_ordenado}")

    # Aplicação da busca binária
    esquerda = 0
    direita = len(vetor_ordenado) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        print(f"Verificando posição {meio} (valor: {vetor_ordenado[meio]})")

        if vetor_ordenado[meio] == valor:
            return print(f"Valor {valor} encontrado na posição {meio}º no vetor ordenado.")
        elif vetor_ordenado[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    print("Elemento não encontrado no vetor.")

# Exemplo de uso com vetor não ordenado
vetor_nao_ordenado = [10, 3, 6, 2, 8, 1, 7, 9, 4, 5]
busca_binaria_em_vetor_nao_ordenado(vetor_nao_ordenado, 8)
