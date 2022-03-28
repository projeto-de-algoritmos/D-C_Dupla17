# https://codeforces.com/problemset/problem/873/D

n, k = map(int,input().split())

a = []


def merge(start, end, call):
    if call < 2:
        a.extend(range(start, end))
        return call
    if end - start == 1:
        a.append(start)
        return call

    call -= 2
    mid = (start + end + 1) // 2
    call = merge(mid, end, call)
    call = merge(start, mid, call)
    return call


call = merge(1, n + 1, k - 1)

if call == 0:
    print(' '.join(map(str, a)))
else:
    print(-1)
