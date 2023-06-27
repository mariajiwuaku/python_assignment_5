# Task_3
str = "The quick brown fox jumps over the lazy dog"
print(str)
print(len(str))
print(str.upper())
print(str.lower())
print(str.title())
print(str[::-1])
print(str[::-1].title())
print(str.count("a"))
print(str.count("the"))
print(str.replace('the', 'a'))

#Task_4


frequency = {}

for items in str:
    if items in frequency:
        frequency[items] += 1
    else:
        frequency [items] = 1
print(frequency)





#Task_5
people = ['Jane', 'John','Jack','Janet']
sex = ["Female", "Male", "Male", "Female"]
age = [23, 34, 16, 28]

for i in range(len(people)):
    print("{} the {} is {} years old." .format(people[i], sex[i], age[i]))
