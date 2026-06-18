sentence=input("Enter any sentence:")
sentence=sentence.lower()
vowels="aeiou"
count=0

for character in sentence:
    if character in vowels:
        count += 1
print(count )