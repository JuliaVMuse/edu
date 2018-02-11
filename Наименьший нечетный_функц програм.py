print(
    min(
        filter(
            lambda x: x % 2 > 0,
            map(
                int,
                list(
                    map(
                        int,
                        input().split())))
        )
    )
)
