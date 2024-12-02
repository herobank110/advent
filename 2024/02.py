print(
    sum(
        (
            lambda d: len(set(e < f for e, f in d)) == 1
            and all(1 <= abs(e - f) <= 3 for e, f in d)
        )(list(__import__("itertools").pairwise(map(int, b.split()))))
        for b in open("02.txt").readlines()
    )
)
