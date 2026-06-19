# make code by using function to greet someone

def greet(name):
    print("Hello",name)


greet("Abdullah")  


#2nd also same 

def greet(name):
    print("Welcome",name)


greet("Ali")  


#3rd addition program by using function
def add(a,b):
    return a+b

print(add(2,6))


#4th square a number by functions
def square(a):
    return a*a

print(square(5))


#5th maximum value by functions
def find_highest(numbers):
 highest=numbers[0]
 for num in numbers:
    if num>highest:
       highest=num
 return highest       
numbers=[70, 80, 90, 60, 75]
print(find_highest(numbers))



