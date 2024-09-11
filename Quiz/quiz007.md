# Quiz 007

## Paper Solution
![WhatsApp Image 2024-09-12 at 01 04 55](https://github.com/user-attachments/assets/2982fffd-3335-4e5b-9ac7-970311488fc5)


## Code
```.py
'''
    BUBBLE SORTING QUIZ
'''
x = [5, -3, 10, 2, 11]
f = True
while f:
    f = False
    for j in range(len(x)-1):
        if x[j] > x[j+1]:
            T = x[j]
            x[j] = x[j+1]
            x[j+1] = T
            f = True
print(x)
```

## Proof of work
<img width="157" alt="Screenshot 2024-09-12 at 1 07 34" src="https://github.com/user-attachments/assets/c5adb850-5a67-4aad-9a06-f1427ca2b40e">


### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz007
