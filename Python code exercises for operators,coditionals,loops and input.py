# Exercise 1 ASKING USER NAME AND PRINTING THEIR  IDENTITY BASED ON THEIR AGE
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Exercise 2 PRINTING ALL EVEN NUMBERS FROM 1 TO 20 USING  LOOP
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercise 3 A LOOP THAT PRINTS NUMBER 1 TO 50 BUT STOPS WHEN HITS MULTIPLE OF 7
for i in range(1, 50):
    if i % 7 == 0:
        break
        print(i)

# Exercise 4 ASK A USER TO ENTER A NUMBER & PRINTS IT MULTIPLICATION TABLE(1*n UP TO 10*n)
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{i}*{n} = {i*n}")
