# My first mini project
def find_lowest_student(students):
    lowest=100
   
    for num in students.values():
        if num<lowest:
            lowest=num
    
    return lowest


def find_top_highest(students):
    highest=0
    for num in students.values():
        if num>highest:
            highest=num
    return highest


def find_average(students):
    total=0
    for num in students.values():
        total+=num
    return total/len(students)

def passed_students(students):
    count=0
    for marks in students.values():
        if marks>=50:
            count+=1
    return(count)        

def failed_students(students):
    count=0
    for marks in students.values():
        if marks < 50:
            count+=1
    return(count)        

students = {
    "Ali": 80,
    "Ahmed": 95,
    "Sara": 88,
    "Fatima": 92,
    "Zain": 45
}

print("Highest Marks:", find_top_highest(students))
print("Lowest Marks:", find_lowest_student(students))
print("Average Marks:", find_average(students))
print("passed students:", passed_students(students))
print("Failed students:", failed_students(students))
