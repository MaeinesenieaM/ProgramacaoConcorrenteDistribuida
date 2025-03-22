import random
import threading

# Função principal do QuickSort

threads = []

def sort_lesser(arr, target, pivot):
    buffer = [x for x in arr[:-1] if x <= pivot]
    target.extend(buffer)

def sort_bigger(arr, target, pivot):
    buffer = [x for x in arr[:-1] if x > pivot]
    target.extend(buffer)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1] #Usando um número negativo em uma array, ele conta de do fim ao início, aki ele sempre pega o último.

    left = []
    right = []
    left_thread = threading.Thread(target = sort_lesser, args = (arr, left, pivot))
    right_thread = threading.Thread(target = sort_bigger, args = (arr, right, pivot))

    left_thread.start()
    right_thread.start()
    left_thread.join()
    right_thread.join()

    return quicksort(left) + [pivot] + quicksort(right)

# Função para gerar números aleatórios

def gerar_numeros_aleatorios(n=10, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função principal para testar o QuickSort

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios()
    
    print("Primeiros 10 números antes da ordenação:", numeros)
    numeros_ordenados = quicksort(numeros)    
    print("Primeiros 10 números após a ordenação:", numeros_ordenados)