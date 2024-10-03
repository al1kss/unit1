# Quiz 010

## Paper Solution
![WhatsApp Image 2024-09-16 at 15 09 57](https://github.com/user-attachments/assets/011a0598-5689-47ea-b190-42aa29a43c19)

## Code
```.py
def powersTen(number, type):
    data = {12: "Tera", 9: "Giga", 6: "Mega", 3: "Kilo", 0: "Unit", -3: "Mili", -6: "Micro", -9: "Nano", -12: "Pico"}
    output = ""

    for i in range(12, -13, -3):
        if i >= 0:
            value = f"{number * (10 ** i):,}".replace(",", " ")
            # found it online how to use {:,} ; link: https://www.peterbe.com/plog/format-thousands-in-python
        else:
            value = f"{number * (10 ** i):.12f}".rstrip('0')
            parts = value.split(".")
            spacing = parts[1]
            value = ""
            for c in range(len(spacing)):
                if c % 3 ==0 and c != 0:
                    value += " "
                value += spacing[c]
            value = parts[0] + "." + value

        output += f"{value:<21} {data[i]} {type}\n"
        # Formatting for width; I used it on my Project so I already know how it works, link was in project 1 repositorie

    return output


x = input()
l = x.split()
print(powersTen(int(l[0]), l[1] if len(l)>1 else ""))
```

## Proof of work
<img width="244" alt="Screenshot 2024-10-03 at 19 36 04" src="https://github.com/user-attachments/assets/d1f57214-2ab6-4314-99e9-36ddc12f169b">
<img width="260" alt="Screenshot 2024-10-03 at 19 36 30" src="https://github.com/user-attachments/assets/f6d17bc3-bcd2-4b92-b160-430f6750c374">

## Flow Diagram
![CompScience FlowDiagrams - Page 1 (1)](https://github.com/user-attachments/assets/9db82587-0a4f-4539-9ad4-56579436edf3)

### For my info
Where is it on PC
>Documents/Coding/CS Lessons/Quizzes/Unit 1/quiz010
