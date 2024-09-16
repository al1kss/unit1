# Quiz 006

## Paper Solution
![WhatsApp Image 2024-09-16 at 12 43 54](https://github.com/user-attachments/assets/64323f6c-a712-4aba-b9a4-b8334164929b)


## Code
```.py
from random import randint

wordBank = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>?/"

a = input()
b = ""
if len(a) > 0:
    a, b = a.split(", ")

for i in range(int(a) if len(a) > 0 else 20):
    if len(b)>0 and b == "True":
        rand = randint(0, len(wordBank) - 1)
        print(wordBank[rand], end="")
    else:
        rand = randint(0, len(wordBank)-29)
        print(wordBank[rand], end="")
```


## Proof of work

<img width="183" alt="Screenshot 2024-09-11 at 23 43 57" src="https://github.com/user-attachments/assets/a7e923a2-1a21-4ba5-a4a9-e84214db2590">
<img width="332" alt="Screenshot 2024-09-11 at 23 44 19" src="https://github.com/user-attachments/assets/c3b8b504-cfdd-464f-a4f3-233d6bc1215a">

### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz006
