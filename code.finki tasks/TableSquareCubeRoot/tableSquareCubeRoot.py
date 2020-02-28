import math

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())

    tablica = {}
    bool = True
    if m > n:
        print("nema podatoci")
        bool = False

    else:
        for m in range(m,n+1):
            tablica[m] = (m*m, m*m*m, round(math.sqrt(m), 5))

    if x > n and bool:
        print("nema podatoci")

    if x <= n: print(tablica[x])
    print(sorted(tablica.items()))