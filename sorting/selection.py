def selection(arr):
    for i in range(len(arr)):
        minIndex = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    return arr

print(selection([4, 1, 8, 5]))
