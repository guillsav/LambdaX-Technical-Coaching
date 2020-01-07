def zeros_to_right(arr: list) -> int:
    left, right, count = 0, len(arr) - 1, 0

    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            swap(arr, left, right)
            left += 1
            count += 1
        else:
            if arr[left] != 0:
                left += 1
                count += 1
            if arr[right] == 0:
                right -= 1
    return count


def swap(arr: list, zero: int, num: int) -> None:
    arr[zero], arr[num] = arr[num], arr[zero]


print(zeros_to_right([0, 3, 1, 0, -2]))
print(zeros_to_right([4, 2, 1, 5]))
print(zeros_to_right([0, 0, 0, 0, 0]))
print(zeros_to_right([1, 2, 3, 0, 4, 0, 0]))
print(zeros_to_right([0, 0, 0, 0, 3, 2, 1]))
