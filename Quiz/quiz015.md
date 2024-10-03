# Quiz 015

## Paper Solution
![WhatsApp Image 2024-10-03 at 20 03 14](https://github.com/user-attachments/assets/ba0d6f35-61a2-47e4-ab94-428cda3129a1)


## Code
```.py
# SL
def averageLength(words):
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

out = averageLength(words = ["Computer Science", "Art"])
print(out)


#HL
def averageLengthNoSpace(words):
    total = 0
    for word in words:
        total += len(word.replace(" ", ""))
    return total / len(words)

out = averageLengthNoSpace(words = ["Computer Science", "Art"])
print(out)
```

## Proof of work
<img width="1470" alt="Screenshot 2024-10-03 at 20 07 31" src="https://github.com/user-attachments/assets/881573e0-be82-4f04-b992-ce620f950f3b">

## Flow Diagram
![CompScience FlowDiagrams - Page 1 (6)](https://github.com/user-attachments/assets/841a750a-3b11-4a39-8f96-5eee8e77cd6e)

### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz015
