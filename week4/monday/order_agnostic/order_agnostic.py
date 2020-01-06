def order_agnostic(arr: list, target: int) -> int:
    start, end = 0, len(arr) - 1

    if arr[start] == arr[end]:
        if target == arr[start]:
            return start
        return -1

    is_ascending = arr[start] < arr[end]
    
    if is_ascending:
        return ascending_binary_search(arr, target, start, end)     
    else:
        return descending_binary_search(arr, target, start, end)


def ascending_binary_search(arr: list, target: int, start: int, end: int) -> int:
    while start <= end:
        middle = start + (end - start) // 2
        if arr[middle] > target:
            end = middle - 1
        elif arr[middle] < target:
            start = middle + 1
        else:
            return middle
    return -1


def descending_binary_search(arr: list, target: int, start: int, end: int) -> int:
    while start <= end:
        middle = start + (end - start) // 2
        if arr[middle] > target:
            start = middle + 1
        elif arr[middle] < target:
            end = middle - 1
        else:
            return middle
    return -1


arr1 = [4, 6, 10]
arr2 = [1, 2, 3, 4, 5, 6, 7]
print(order_agnostic(arr1, 10))
print(order_agnostic(arr2, 5))

