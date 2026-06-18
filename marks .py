numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
print(len(numbers))

fruits = ["apple", "banana", "mango"]
print(fruits[-1])

marks = [70, 80, 90]
marks.append(30)
print(marks)


marks_1 = [70, 80, 90, 60, 75]
print(max(marks_1))
print(min(marks_1))

print(sum(marks_1)/len(marks_1))
total=0
for mark in marks_1:
    total += mark
print(total)

highest=marks_1[0]
for mark in marks_1:
    if mark > highest:
     highest=mark
print(highest)    