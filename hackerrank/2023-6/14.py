# Is Fibo

def main():
    t = int(input())

    global set_fibos
    set_fibos = set()

    a, b = 0, 1
    while a < 10**10:
        set_fibos.add(a)
        a, b = b, a + b

    for _ in range(t):
        n = int(input())
        print('IsFibo' if is_fibo(n) else 'IsNotFibo')


def is_fibo(n):
    return n in set_fibos


if __name__ == '__main__': main()
