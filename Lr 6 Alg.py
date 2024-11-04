def heapify(arr, n, i): #индекс
    smallest = i  #  элемент как корень , предположение что корень = маленький эл
    left = 2 * i + 1   #потомок
    right = 2 * i + 2


    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i: # не явл корнем,то
        arr[i], arr[smallest] = arr[smallest], arr[i]

        heapify(arr, n, smallest) #для поддерева = мин-куча

def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): #с конца до -1 с шагом 1
        heapify(arr, n, i)

def print_heap(arr):
    print("Мин-куча:", arr)

# Пример использования
if __name__ == "__main__":
    n = int(input("Введите количество элементов массива: "))  # Ввод количества элементов
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))  # Ввод элементов массива

    if len(A) != n:
        print("Количество введенных элементов не соответствует указанному.")
    else:
        build_min_heap(A)
        print_heap(A)