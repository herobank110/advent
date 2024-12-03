print(
    sum(
        int(a) * int(b)
        for a, b in __import__("re").findall(
            r"mul\((\d{1,3}),(\d{1,3})\)", open("033.txt").read()
        )
    )
)


import re

s = 0
p = r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)"
d = True
for m in re.finditer(p, open("03.txt").read()):
    if m.group() == "don't()":
        d = False
    elif m.group() == "do()":
        d = True
    elif d:
        s += int(m.group(1)) * int(m.group(2))
print(s)
