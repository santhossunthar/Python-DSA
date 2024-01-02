def quick(arr):
    if len(arr) <= 1: return arr

    pivot = arr[len(arr) // 2]
    lesser = [elem for elem in arr if elem < pivot]
    greater = [elem for elem in arr if elem > pivot]

    return quick(lesser) + [pivot] + quick(greater)

print(quick([5, 2, 8, 1]))