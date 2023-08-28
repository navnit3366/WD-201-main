list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0:2])  # prints [1, 2]
print(
    list_with_numbers[:2]
)  # prints [1, 2] not specifying a start index will start from the beginning
print(
    list_with_numbers[2:]
)  # prints [3, 4, 5] not specifying an end index will end at the end
print(list_with_numbers[-1])  # prints 5
print(
    list_with_numbers[-3:-1]
)  # prints [3, 4, 5] ( the last three items with the start included)
print(list_with_numbers[2:4])
