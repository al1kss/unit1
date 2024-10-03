# Quiz 011

## Paper Solution
![WhatsApp Image 2024-10-03 at 19 33 19](https://github.com/user-attachments/assets/71122f09-20a5-4027-8f74-91309ce53cab)

## Code
```.py
type = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
name = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
start = {1:1, 2:4, 3:5, 4:1, 5:3, 6:6, 7:1, 8:4, 9:7, 10:2, 11:5, 12:3}

def bestMonth(month:int):
    count = start[month]-1
    output = ""
    output += f"     {name[month]} 2024\n"
    output += "Mo Tu We Th Fr Sa Su\n"
    output += "   " * (start[month] - 1)
    for i in range(1, type[month]+1):
        output += f"{i:2d} " # :2d means 2 digits always. i.e. 1 -> ( 1); 12 -> (12)
        count += 1
        if count == 7:
            output += "\n"
            count = 0
    return output

x = int(input())
print(bestMonth(x))
```

## Proof of work
<img width="181" alt="Screenshot 2024-10-03 at 19 39 21" src="https://github.com/user-attachments/assets/5b8ddad9-9049-4317-948e-efab62f7f1d0">
<img width="186" alt="Screenshot 2024-10-03 at 19 39 32" src="https://github.com/user-attachments/assets/d524722f-9a96-40b4-b2bf-d27bab716c7f">
<img width="181" alt="Screenshot 2024-10-03 at 19 39 50" src="https://github.com/user-attachments/assets/d12a891a-9e3e-4991-96f8-ba5d54ac9534">

## Flow Diagram
![CompScience FlowDiagrams - Page 1 (2)](https://github.com/user-attachments/assets/f6c41d9d-987d-4255-a6eb-20a086763058)

### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz011
