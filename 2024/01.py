print(
    sum(
        abs(c0 - c1)
        for c0, c1 in zip(
            *(
                sorted(
                    b[i]
                    for b in [
                        list(map(int, a.split())) for a in open("01.txt").readlines()
                    ]
                )
                for i in range(2)
            )
        )
    )
)

print(
    (lambda c, d: sum(e * d.count(e) for e in c))(
        *(
            [
                b[i]
                for b in [
                    list(map(int, a.split())) for a in open("01.txt").readlines()
                ]
            ]
            for i in range(2)
        )
    )
)
