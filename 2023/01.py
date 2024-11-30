print(
    sum(
        int((lambda b: b[0] + b[-1])(list(filter(str.isdigit, a))))
        for a in open("01.txt").readlines()
    )
)


import re

z = "one two three four five six seven eight nine".split()
print(
    sum(
        (lambda c: c[0] * 10 + c[-1])(
            [
                int(b) if b.isdigit() else z.index(b) + 1
                for b in re.findall(rf"(?=(\d|{'|'.join(z)}))", a)
            ]
        )
        for a in open("01.txt").readlines()
    )
)
