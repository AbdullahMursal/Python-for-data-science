def find_average(numbers):
    total=0
    for num in numbers:
        total+=num
    return total/len(numbers)
numbers=[70, 80, 90, 60, 75]

print(find_average(numbers))
