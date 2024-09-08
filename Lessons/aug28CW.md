# Classwork

## KidsMath

```.py
'''


1. Show a mupltiplication table -> ask after for input (validate)

2. Show the factors (DONE)

3. Count to a number by steps
    - Ask for number + steps


4. Find the iterations to reducea number
    - input(513) -> 5*1*3 -> 15 -> 1*5 -> 5
    - repeat until 1 digit (no need to chekc for zero because it is 1 digit)



    WhAT NUMBER WILL TAKE 7 ITERATIONS
        -- count backwards

'''
def table(x):
    for i in range(1, 10):
        print(f"{x} * {i} = {x * i}")

def validate(num):
    for i in num:
        if i not in '0123456789':
            print("Number not valid, try again!")
            return None
    return int(num)

def iterations(x):
    k=1
    while len(str(x)) > 1:

        multiplication = 1
        for i in str(x):
            multiplication *= int(i)
        x = multiplication
        print(f"Iteration {k}: {x}")
        k += 1
    return x





print("    Welcome to the Kids Math")

x = input("1. Show a mupltiplication table \n"
          "2. Show the factors \n"
          "3. Count to a number by steps\n"
          "4. Find the iterations to reduce number\n"
          "0. To exit\n")

while x != "0":
    if x == "1":
        num = input("Enter a number: ")
        num = validate(num)
        if num is not None:
            table(num)
    elif x == "2":
        num = input("Enter a number: ")
        num = validate(num)
        if num is not None:
            for i in range(2, num - 1):
                if num % i == 0:
                    print(f"{i} is a factor of {num}")
    elif x == "3":
        num = input("Enter a number: ")
        x = input("Enter steps: ")
        num = validate(num)
        x = validate(x)
        if num is not None and x is not None:
            for i in range(0, num + 1, x):
                print(i)
    elif x == "4":
        num = input("Enter a number: ")
        num = validate(num)
        if num is not None:
            num = iterations(num)
            print(num)
    x = input("\n1. Show a mupltiplication table \n"
                      "2. Show the factors \n"
                      "3. Count to a number by steps\n"
                      "4. Find the iterations to reduce number\n"
                      "0. To exit\n")


```


## Find as many iterations as you want

```.py
def iterations(x):
    initial_value = x
    k = 0

    while len(str(x)) > 1:

        multiplication = 1
        for i in str(x):
            multiplication *= int(i)
        x = multiplication
        k += 1
        if k == 8: #change this value to how many iterations you wanna find
            print("GOT IT!")
            print(f"Iteration {k}: {initial_value}")
            exit()
    return x

for t in range(1,11111111111111):
    iterations(t)
```

### Information for me
This file is located in 
>Documents/Coding/CS Lessons/Classwork/Unit 1/Classwork
