def quick_sort(arr: list[int]) -> list[int]:
    """ Быстрая сортировка """
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    even_numbers = [i for i in numbers if i%2 ==0]
    print(f'Чётные числа: {even_numbers}')
    print(f'Максимальное значение: {max(numbers)}')
    print(f'Минимальное значение: {min(numbers)}')
    print(f'Отсортированный массив: {quick_sort(numbers)}')