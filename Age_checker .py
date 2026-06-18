age=int(input("Enter your age:"))
if age<0:
    print("Enter correct age")

elif age>=60:
    print("Senior Citizen") 

elif age>=18:
    print("Adult")

elif age<18:
    print("Minor")