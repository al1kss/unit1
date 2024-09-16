# Quiz 002

## Paper Solution
![WhatsApp Image 2024-09-16 at 12 54 07](https://github.com/user-attachments/assets/5c7b0c32-e908-441c-9ae1-ef56d2a72f09)


## Code

```.py
def check_twenty(a, b):
    if a == 20 or b == 20 or (a + b) == 20:
        print(True)
        quit()

k = input()

k = k.replace("[", "").replace("]", "").replace(",", "").strip()

a = k.split()

length = len(a)

for i in range(int(length/2)):
    first = int(a[i])
    second = int(a[i + int(length/2)])
    check_twenty(first, second)

print(False)
```

## Proof of Work
<img width="76" alt="Screenshot 2024-08-29 at 15 37 49" src="https://github.com/user-attachments/assets/3b808ac1-8909-4cd7-80bf-8b4f85584a5b">
<img width="79" alt="Screenshot 2024-08-29 at 15 38 25" src="https://github.com/user-attachments/assets/db850fde-fc84-4bff-9023-1abbff1cf6cc">
<img width="89" alt="Screenshot 2024-08-29 at 15 38 47" src="https://github.com/user-attachments/assets/c4b20d9f-4546-4406-8a7e-1ac912f56979">
<img width="109" alt="Screenshot 2024-08-29 at 15 39 15" src="https://github.com/user-attachments/assets/b8afa62d-918b-4808-ae8c-6d4ee56dfeca">
<img width="269" alt="Screenshot 2024-08-29 at 15 39 47" src="https://github.com/user-attachments/assets/512074ee-38a5-4194-9fd5-7ea17bd53875">


### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/quiz002
