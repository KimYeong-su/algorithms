cases = int(input())

for case in range(cases):
    n = int(input())
    base = list(map(int, input().split()))
    r_base = []

    for j in range(len(base) - 1, 0, -1):
        for i in range(j):
            if base[i] > base[i + 1]:
                base[i], base[i + 1] = base[i + 1], base[i]
    for i in range(-1, -len(base) - 1, -1):
        r_base.append(base[i])

    result = []
    for i in range(len(base)):
        if i % 2 == 0:
            result.append(r_base[0])
            base.remove(r_base[0])
            del r_base[0]
        else:
            result.append(base[0])
            r_base.remove(base[0])
            del base[0]

    result = ' '.join(list(map(str, result))[:10])
    print('#{} {}'.format(case + 1, result))
