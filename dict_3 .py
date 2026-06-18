marks = {
    "Math": 90,
    "Physics": 85,
    "English": 80
}

for key,value in marks.items():
    print(key,value)
sum=0
for value in marks.values():
    sum+=value
    
print(sum)    
