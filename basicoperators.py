a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

numbers = [20, 20 ,30, 20]
numbers.remove(20)
print(numbers)

numbers = [20, 20 ,30]
numbers.clear()
print(numbers)

numbers = [10, 20, 30, 40]
print(numbers.index(30))

numbers = [10, 20, 20, 30, 20]
print(numbers.count(20))

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

a = [1, 2, 3,]
b = a.copy()
print(b)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])
print(numbers[::-5])
print(numbers[-1::])
print(numbers[-4::])
print(numbers[::-4])
print(numbers[-2:1:-3])

#tuples in python
#Tuple is a collection of multiple values that is ordered and cannot be changed after creation 
student = ("bharath",98,"python")
print(student[0])

#tupies are immutable, meaning they cannot be changed after creation 
numbers = (10, 20, 20, 30, 20)
print(numbers.count(20))

numbers = (10, 20, 30, 40)
print(numbers.index(30))

numbers = (10, 20, 30, 40,)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python 
#set is a collection of unique values that is unordered and 
numbers = {10, 20, 30, 20, 10}
print(numbers)

#why use set?

#add values to a set 
subjects = {"python", "SQL"}
subjects.add("Java")
print(subjects)
subjects.remove("SQL")
print(subjects)

#sets do not allow duplicate values
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)

#dictionaries in python
#dictionary is a collection of key-value pairs enclosed in curly braces. Each key is unique,
student = {"name": "Bhargavi", "age": 25, "course": "python"}
print(student["name"])
print(student["age"])
print(student["course"])

#access elements in dictionary
student = {"name": "Bhargavi", "age": 25, "course": "python"}
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))