# My first mini project
def find_lowest(numbers):
    lowest=numbers[0]
    for num in numbers:
        if num<lowest:
            lowest=num
    
    return lowest


def find_highest(numbers):
    highest=numbers[0]
    for num in numbers:
        if num>highest:
            highest=num
    return highest


def find_average(numbers):
    total=0
    for num in numbers:
        total+=num
    return total/len(numbers)


numbers= [70, 80, 90, 60, 75]

print("Highest Marks:", find_highest(numbers))
print("Lowest Marks:", find_lowest(numbers))
print("Average Marks:", find_average(numbers))