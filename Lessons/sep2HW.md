# Mystery Boxes

## Codes

### Mystery Box 1
```.py
bank = {
    "A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h",
    "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p",
    "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x",
    "Y": "y", "Z": "z"
}

def mystery_box1(a:str, b:str) -> str:
    output = ""
    if b == "True":
        for i in range(len(a)):
            if i != len(a) - 1:
                output += a[len(a) - i - 1]
            if i == len(a) - 1:
                output += bank.get(a[0])
    else:
        for i in range(len(a)):
            output += a[len(a) - i - 1]
    return output

put = input()
state = input()
print(mystery_box1(put, state))
```

### Mystery Box 2
```.py
bank = {
    "a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", "g": "G", "h": "H",
    "i": "I", "j": "J", "k": "K", "l": "L", "m": "M", "n": "N", "o": "O", "p": "P",
    "q": "Q", "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", "x": "X",
    "y": "Y", "z": "Z"
}

def mystery_box2(a:str) -> str:
    output = ""
    output += bank.get(a[0])

    for i in range(1, len(a)):
        output += a[i]
    return output

gmail = input()
full_name, mail = gmail.split("@")

name, surname = full_name.split(".")

x = mystery_box2(name)
y = mystery_box2(surname)

print(x, y)
print(mail)
```
