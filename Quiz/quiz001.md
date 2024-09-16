# Quiz 001

## Paper Solution

![0D100E62-6617-4A03-AC56-BAC7DD380A70_1_201_a](https://github.com/user-attachments/assets/b2332979-3616-4680-b224-9071400debd4)


## Code
```.py
def counter():
    for i in range(len(words)):
        word = words[i]
        length = len(word)
        if length > 2:
            print(word[0] + str(length - 2) + word[-1], end = ' ')
        else:
            print(word, end=' ')

a = input("Input: ")

words = a.split( )
counter()
```

## Proof of Work

<img width="245" alt="Screenshot 2024-08-21 at 20 40 15" src="https://github.com/user-attachments/assets/33e83c93-8c7b-4bfb-b8c8-0d555eeeacb7">
<img width="168" alt="Screenshot 2024-08-21 at 20 52 50" src="https://github.com/user-attachments/assets/0f872593-03ee-490f-aa73-419ff2db17b2">
<img width="180" alt="Screenshot 2024-08-21 at 20 41 12" src="https://github.com/user-attachments/assets/c3667c3c-ea0d-4536-9e54-bd4a9c126b8b">
<img width="210" alt="Screenshot 2024-08-21 at 20 45 08" src="https://github.com/user-attachments/assets/ee3b4e89-5caf-44ad-a1b1-8f2f5bbbbc6d">
<img width="299" alt="Screenshot 2024-08-21 at 20 46 04" src="https://github.com/user-attachments/assets/888e8888-1be1-40cd-a9df-56fc4c78973c">

## Flow Diagram
![CompScience FlowDiagrams (1)](https://github.com/user-attachments/assets/557a1d99-627e-4db4-a6c8-6cffa8e43dc4)
