#print numbers from 10 to 1
for i in range(10, 0, 2):
    print(i)

#print even numbers from 2 to 50    
for i in range(2, 51, 2):
    print(i)

#print odd numbers from 1 to 50 
for i in range(1, 51, 2):
    print(i)

#Multiplication table 
number = int(input("Enter number:"))

for i in range(1, 11):
    print(number, "X", i, "=", number * i)

#summ of numbers from 1 to n
n = int(input("Enter a number:"))    
total = 0
for i in range(1, n + 1):
    total =total + i
print("Sum:",total)

#factorial of a number
n = int(input("Enter a number:"))
factorial = 1 
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial:",factorial)    

# count of multiples of 3
n = int(input("enter n:"))

count = 0 

for i in range(1, n + 1):
    if i % 3 == 0:
        count = count + 1

print("count:", count)     


# sum of multiples of 5
n = int(input("enter n:"))

total = 0 

for i in range(1, n + 1):
    if i % 5 == 0:
        total = total + i

print("Sum:", total)     

# print all even numbers from 2 to 50
i = 2
while i <= 50:
    print(i)
    i = i + 2   
#print total of numbers entered by user until 0 is entered 
total = 0 
number = int(input("Enter number:"))
while number !=0:
    total = total + number 
    number = int(input("Enter number:"))
print("Total:", total)         

# password check
password = ""
while password != "python143":
    password = input("Enter password:")
print("login successful")

#count the number of digits in a number 
number = int(input("Enter number:"))
count = 0
while number > 0:
    number = number //10
    count = count + 1
    print("Number of digits:", count)

#count the number of digits in a number 
number = int(input("Enter number:"))
total = 0
while number > 0:
    digit = number % 10
    total = total + digit
    number = number //10
    print("Sum of digits:", total)

#reverse a number 
number = int(input("Enter number:"))
reverse = 0
while number > 0:
    digit = number % 10 
    number = number // 10 
    reverse = reverse * 10 + digit 
    print("Reverse:", reverse)

#check if a number is a palindrone
number = int(input("Enter number:"))
original = number 
reverse = 0
while number > 0:
    digit = number % 10 
    number = number // 10 
    reverse = reverse * 10 + digit 
if original == reverse:
    print("palindrone")
else:    
    print("Not palindrone")

#check if a number is prime 
number = int(input("Enter number:"))
count = 0 
for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")          

for i in range(1, 11):
    if i == 5:
        break #exit the loop
    print(i)
for i in range(1, 11):
    if i == 5:
        continue #exit the loop
    print(i)    

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

age = 20 
if age >= 18:
    pass # eligible
else:
    print("Not eligible")

for i in range(1, 11):
    if i ==7:
        print("Number found")
        break
    print(i)

#print odd numbers from 1 to 10 
for i in range(1, 11):
    if i % 2 == 0:
       continue
print(i)

# print numbers until user enters 0
while True:
    number = int(input("Enter number:"))
    if number == 0:
        break 
    print("You entered:",number)

# print numbers from 1 to 100, but skip multiples of 3 and stop at 50
for i in range(1, 101):
    if i == 50:
        break 
    if i % 3 == 0:
        continue
    print(i)

# calculate the sum of positive numbers entered by the user
total = 0
while True:
    number = int(input("Enter number:"))
    if number <0:
        continue 
    if number == 0:
        break
    total = total + number 
    print("Total:", total)

























































