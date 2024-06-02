#bài 1
num = input("nhập num :")
def is_int(num):
    if type(num) is float:
        return num.is_integer()
    elif type(num) is int:
        return True
    else:
        return False
print(num,"is an integer")
#bài 2
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
#bài 3
num = input("nhập num :")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

n = int(input("Nhập số nguyên dương n: "))
print("N " + str(n) + " số nguyên tố đầu tiên: " + str(first_n_primes(n)))
#bài 4
def tichphactorial(n):
    if n == 0:
        return 1
    else:
        return n * tichphactorial(n-1)

def tongtichphactorial(n):
    total = 0
    for i in range(1, n+1):
        total += tichphactorial(i)
    return total

n = int(input("Nhập vào số nguyên dương n: "))
print("Tổng các giá trị sau: 1! + 2! + ... +", n, "!", "là:", tongtichphactorial(n))
#bài 5
from datetime import datetime

now = datetime.now()

print("Today is", now.strftime('%d/%m/%Y'))
print("Time right now:", now.strftime('%H:%M:%S'))