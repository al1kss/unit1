# Quiz 014

## Paper Solution
![WhatsApp Image 2024-10-03 at 20 00 51](https://github.com/user-attachments/assets/c4af4c63-63f7-4a4e-90dc-7a716a6ad712)

## Code
```.py
def open_doors(num_students):
    output = 0
    for i in range(1, num_students + 1):
        count = 0
        for k in range(1, num_students + 1):
            if i % k == 0:
                count += 1 # count how many times the door was flipped
        if count % 2 == 1: # if the door was flipped odd number of times, it will be open
            output +=1
    return output

print(open_doors(10))
print(open_doors(100))
print(open_doors(200))
print(open_doors(5678))
```

## Proof of work
<img width="65" alt="Screenshot 2024-10-03 at 20 00 12" src="https://github.com/user-attachments/assets/319bbf57-05a9-4666-9152-17d72b82650d">

## Flow Diagram
![CompScience FlowDiagrams - Page 1 (5)](https://github.com/user-attachments/assets/d0bc8f59-3146-4b64-90e5-6d681083ed28)


### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz014
