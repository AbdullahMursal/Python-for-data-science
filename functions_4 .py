def find_even(numbers):
    count=0
    for num in numbers:
        if num%2 == 0:
         count += 1
    return count

def find_odd(numbers):
    count=0
    for num in numbers:
        if num%2 != 0:
         count += 1
    return count


numbers = [10, 15, 20, 25, 30]
print("Total even numbers are" ,find_even(numbers))  
print("Total odd numbers are" ,find_odd(numbers))  



