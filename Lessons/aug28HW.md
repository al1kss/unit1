# Homework for ["if statements"](https://docs.google.com/presentation/d/1EWj1CgcyRq5s449eWLwJMolHJuGOiOXw8MY4Xg3Ul5A/edit#slide=id.gec4cfad2ea_0_40)

## 1st Exercise

```.py

a, b, c = map(int, input().split())

max_value = max(a, b, c)

if max_value == a:
    print(a, max(b, c), min(b, c))
elif max_value == b:
    print(b, max(a, c), min(a, c))
else:
    print(c, max(a, b), min(a, b))

```
<img width="116" alt="Screenshot 2024-08-29 at 14 53 36" src="https://github.com/user-attachments/assets/89b1967d-2c17-4bfc-bb48-6d987f3c8b72">


## 2nd Exercise

```.py
a = int(input())

if 0 < a <= 1000:
    print("Your tax is: ", a * 0.05)

elif 10001 <= a <= 50000:
    print("Your tax is: ", a * 0.1)

elif 50001 <= a <= 100000:
    print("Your tax is: ", a * 0.15)

elif 100001 <= a:
    print("Your tax is: ", a * 0.25)

else:
    print("Please enter a valid number")
```
<img width="189" alt="Screenshot 2024-08-29 at 14 54 49" src="https://github.com/user-attachments/assets/d5b08eda-db45-42f5-8388-ccf475048a73">

## 3rd Exercise

```.py
''' ----===Easy Version===----

bank = []

#if we can input one by one

for i in range(3):
    bank.append(input())

bank.sort()

#if we can print not in one line

for i in bank:
    print(i)

'''

bank = []

a, b, c = map(str, input().split())

bank.append(a)
bank.append(b)
bank.append(c)

bank.sort()

new_sorted = ""

for i in bank:
    new_sorted += i + " "

print("Sorted in alphabetical order:\n", new_sorted)
```
<img width="252" alt="Screenshot 2024-08-29 at 14 57 39" src="https://github.com/user-attachments/assets/80a508d1-08f0-4257-976f-95bc32570404">

## 4th Exercise

```.py
x = list(input())

while " " in x:
    x.remove(" ")

x.sort()

summa = 0

if len(x) == 4:
    print((int(x[1]) + int(x[2]))/2)
else:
    print(x[2])
```
<img width="96" alt="Screenshot 2024-08-29 at 14 58 47" src="https://github.com/user-attachments/assets/9e93aed7-8c6b-4368-a42d-b11c40415563">



### Information for me
This file is located in 
>Documents/Coding/CS Lessons/Homework/Homework 1
