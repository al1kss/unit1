# Quiz 004

## Paper Solution

![WhatsApp Image 2024-09-16 at 12 43 55 (1)](https://github.com/user-attachments/assets/e54ccef6-45d9-4c7a-b24a-66ee805477f8)

## Code
```.py
number = int(input())

perf_number = 0
for i in range(1, 10000000):
    if number % i == 0 and number != i:
        perf_number += i
        print(i, end=" ")
        if perf_number == number:
            print(True)
```

## Proof of work
<img width="238" alt="Screenshot 2024-09-11 at 23 22 13" src="https://github.com/user-attachments/assets/9e497984-5a05-43d3-9607-1678ba912a80">
<img width="91" alt="Screenshot 2024-09-11 at 23 22 32" src="https://github.com/user-attachments/assets/bf0d55d5-0e5d-49ae-855f-e00ecd8a6ff0">


### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/quiz004
