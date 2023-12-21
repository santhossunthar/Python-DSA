def bs(input):
    for i in range(len(input)):
        for j in range(len(input) - i - 1):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bs(my_list)

print("Sorted array:", my_list)
