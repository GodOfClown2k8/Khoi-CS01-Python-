#Câu 1 
print("Input first number: ", end="")
num1 = int(input())
print("Input second number: ", end="")
num2 = int(input())
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")
#Câu 2
a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("The equation has no real solutions.")
elif delta == 0:
    x = -b / (2*a)
    print(f"The equation has 1 solution: x = {x:.1f}")
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print(f"The equation has 2 solutions: x = {x1:.1f} or x = {x2:.1f}")
#câu 3 
def reverse_str(text) : 
    return text[::-1]
def is_palindrome(text) : 
    return text == reverse_str(text)
text = input("Enter a text: ")
print(is_palindrome(text))
#câu 4
ordered_dishes = []

print("== Welcome to MindX Restaurant ==")

while True:
    dish = input("Please choose a dish: ")
    if dish in ordered_dishes:
        print("You chose this already.")
    else:
        ordered_dishes.append(dish)
        print("Great choice!")
    response = input("Anything else? (y/n): ")
    if response.lower() == 'n':
        break

print("Well done! Your order:")
for dish in ordered_dishes:
    print(f"- {dish}")
#câu 5
print("Chương trình 1: ")
phone = { 
    "Iphone12" : 28000000,
    "Samsung N10" : 16000000,
    "Oppo 93" : 7500000,
    "Vsmart" : 7400000,
    "Vivo" : 4200000
}
phone_name = input("Nhập tên điện thoại :")
if phone_name in phone:
    print(f"Giá của {phone_name} là {phone[phone_name]}")
else : 
    print("Không có sản phẩm này")
print("Chương Trình 2 : ")
budget = input("Nhập số tiền bạn có :")
print("Phones that fit your budget:")
for phone_name, price in phone.items():
    if price <= int(budget):
        print(f"- {phone_name} : {price}")
    else : 
        print("Không có sản phẩm nào phù hợp với budget của bạn ")
#câu 6
num = int(input("Input a number : "))
if num > 0 : 
    num_digits = len(str(num))
print(f"Số chữ số trong {num} là {num_digits}.")
#câu 7 
print("Original list:")
arr = [5, 1, 8, 92, -1, 30]
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
sorted_list = bubble_sort(arr)
print("Sorted list :", sorted_list)
#câu 8
def print_fibo(n):
    if n <= 0:
        return "Số n phải lớn hơn 0."
        
    elif n == 1:
        return "Phần tử đầu tiên của dãy Fibonacci: 1"
        
    else:
        fibo = [1, 1]
        for i in range(2, n):
            fibo.append(fibo[i-1] + fibo[i-2])
        print(f"{n} phần tử đầu tiên của dãy Fibonacci: ", *fibo[:n],end="")

print_fibo(8)





