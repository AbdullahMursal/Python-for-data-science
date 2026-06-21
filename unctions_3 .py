def find_lowest(numbers):
    lowest=numbers[0]
    for num in numbers:
        if num<lowest:
            lowest=num
    
    return lowest
numbers = [70, 80, 90, 60, 75]

print(find_lowest(numbers))            