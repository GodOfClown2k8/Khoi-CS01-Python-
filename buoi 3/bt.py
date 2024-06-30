'''
# câu 1 
number = int(input("nhập số: "))
if number % 2 == 0:
    print(f"{number} là số chẵn")
else:
    print(f"{number} là số lẻ")
#câu 2 
number = float(input("nhập số: "))
if number == number // 1:
    print(f"{number} là số nguyên ")
else:
    print(f"{number} ko là số nguyên")
#câu 3
character = input("nhập số: ")
if character.isdigit():
    print(f"'{character}' là 1 chữ số")
else:
    print(f"'{character}' ko là 1 chữ số")
# câu 4
n = int(input("nhập số: "))

if n % 3 == 0 and n % 5 == 0:
    print(f"{n} chia hết cho 3 và 5")
elif n % 3 == 0:
    print(f"{n} chia hết cho 3")
elif n % 5 == 0:
    print(f"{n} chia hết cho 5")
else:
    print(f"{n} chia hết cho 3 hoặc 5")
# câu 5
admin_username = "admin"
admin_password = "12345"

username = input("Username: ")
password = input("Password: ")

if username == admin_username and password == admin_password:
    print(f"Bạn đã đăng nhập, {username}.")
else:
    print("Tên người dùng hoặc mật khẩu sai.")
#câu 6
line1 = float(input("nhập cạnh 1: "))
line2 = float(input("nhập cạnh 2: "))
line3 = float(input("nhập cạnh 3: "))

if line1 + line2 <= line3 or line1 + line3 <= line2 or line2 + line3 <= line1:
    print("3 đoạn thẳng không thể tạo thành hình tam giác.")
else:
    print("3 đoạn thẳng có thể tạo thành một hình tam giác.")

#câu 7 
from turtle import *

# Get user input
line1 = float(input("Input length 1: "))
line2 = float(input("Input length 2: "))
line3 = float(input("Input length 3: "))

# Check if the line segments can form a triangle
if line1 + line2 <= line3 or line1 + line3 <= line2 or line2 + line3 <= line1:
    print("The 3 line segments cannot form a triangle.")
else:
    # Calculate the lengths of the sides
    a = line1
    b = line2
    c = line3

    # Check if it is a right triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("The 3 line segments can form a right triangle.")

    # Check if it is an equilateral triangle
    elif a == b == c:
        print("The  3 line segments can form an equilateral triangle.")

#câu 8
for i in range(21):
    if i % 3 == 0:
        print(i)'''
#câu 9 
n = int(input("Nhập một số nguyên: "))
num_digits = len(str(n))
print(f"Số chữ số trong {n} là {num_digits}.")
