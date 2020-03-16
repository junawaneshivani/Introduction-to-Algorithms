

def towers(n, fr, to, spare):
    if n == 1:
        print("move from " + str(fr) + "to " + str(to))
    else:
        towers(n-1, fr, spare, to)
        towers(n, fr, to, spare)
        towers(n-1, spare, to, fr)


def fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-1, d)
        d[n] = ans
        return ans

