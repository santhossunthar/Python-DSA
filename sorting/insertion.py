def insertion(input):
    for i in range(1, len(input)):
        data = input[i]
        j = i - 1

        while j>=0 and input[j] > data:
            input[j + 1] = input[j]
            j -= 1

        input[j + 1] = data

li = [3, 5, 10, 1, 7, 40, 22]
insertion(li)
print(li)