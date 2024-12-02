print(
    sum(
        (
            lambda d: len(set(e < f for e, f in d)) == 1
            and all(1 <= abs(e - f) <= 3 for e, f in d)
        )(list(__import__("itertools").pairwise(map(int, b.split()))))
        for b in open("02.txt").readlines()
    )
)


print(
    sum(
        (
            lambda d=list(map(int, b.split())): any(
                (
                    lambda j=d[:], f=__import__("itertools").pairwise: (j.pop(i) and 0)
                    or len(set(e < f for e, f in f(j))) == 1
                    and all(1 <= abs(e - f) <= 3 for e, f in f(j))
                )()
                for i in range(len(d))
            )
        )()
        for b in open("02.txt").readlines()
    )
)
