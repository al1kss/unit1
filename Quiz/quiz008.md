# Quiz 008

## Paper Solution
<sub> _soon..._ </sub>

## Code
```.py
a = input()

room = 1
floor = 1
if len(str(a)) == 0:
    for i in range(1, 101):
        print(f"{i}-Room {floor}F{room:02}")
        room += 1

        if room > 10:
            floor +=1
            room = 1

else:
    for i in range(1, int(a)+1):
        if i == int(a):
            print(f"{a}-Room {floor}F{room:02}")
        room += 1

        if room > 10:
            floor +=1
            room = 1

```

## Proof of work
<img width="155" alt="Screenshot 2024-09-12 at 0 08 32" src="https://github.com/user-attachments/assets/75da368d-8b8b-4ce0-a3da-c204506ef0c8">
<img width="127" alt="Screenshot 2024-09-12 at 0 08 46" src="https://github.com/user-attachments/assets/65e1bb18-0eb1-4c11-a5ef-ececd39997f6">
<img width="132" alt="Screenshot 2024-09-12 at 0 09 04" src="https://github.com/user-attachments/assets/3c3152d3-0de2-4928-82b3-7fe15d20f55c">
<img width="146" alt="Screenshot 2024-09-12 at 0 09 18" src="https://github.com/user-attachments/assets/1ca521b4-184e-4c14-83bf-673e11a6c687">


### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz008
