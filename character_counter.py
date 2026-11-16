
s = "raju123#@!$%"

digits = 0
specialcharacters = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        digits += 1

    elif not (ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z'):
        specialcharacters += 1

print("Digits:", digits)
print("Special Characters:", specialcharacters)
