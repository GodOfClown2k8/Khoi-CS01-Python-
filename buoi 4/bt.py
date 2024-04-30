#bài 1 
n = int(input("Input number: "))
for i in range(1, n+1):
    print("#" * i)
#bài 2 
while True:
    num = float(input("Input a positive number: "))
    if num > 0:
        print("Thank you.")
        break
    else:
        print("Input a positive number: ")
#bài 3 
n = int(input("Input number: "))
if n < 0:
    print("Invalid")
elif n == 0:
    print("0! = 1")
else:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(f"{n}! = {fact}")
#bài 4 
n = int(input("Input number: "))
if n < 1:
    print("Invalid input")
else:
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    print(f"Sum of digits of {n} = {sum_digits}")
#bài 5 
count = 0
num = 1000
while count < 10:
    if sum(int(digit) for digit in str(num)) == 9:
        print(num)
        count += 1
    num += 1
