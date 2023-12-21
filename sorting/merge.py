def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def ms(input):
    if len(input) <= 1: return input

    mid = int(len(input)/2)
    left = ms(input[:mid])
    right = ms(input[mid:])

    return merge(left, right)

lis = [3, 4, 1, -1, 100, 23, 55]
print(ms(lis))