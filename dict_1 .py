student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

print(student["name"])
print(student["age"])

student["cgpa"]=3.5

student["age"]=21

for key,value in student.items():
    print(key,value)


