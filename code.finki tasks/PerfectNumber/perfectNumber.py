import math

def sovrshen_broj(n):
    sum = 0

    for i in range(1, n):
        if n%i == 0:
            sum += i

    if sum == n: return True
    else: return False

if __name__ == "__main__":
    n = eval(input())
    if sovrshen_broj(n) is True:
        print(f"Brojot {n} e sovrshen")
    else: print(f"Brojot {n} ne e sovrshen")
