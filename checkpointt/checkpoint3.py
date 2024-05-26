#phần 1 
#bài 1
def is_even(num):
    if num % 2 == 0:
        return f"{num} is an even number."
    elif num % 2!= 0:
        return f"{num} is an odd number."
    else:
        return "Invalid Input"
num = int(input("Enter a number: "))
print(is_even(num))
#bài 2
def cal_area(radius): 
    return 3.14 * radius ** 2
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is {cal_area(radius)}")
#bài 3
def reverse_str(text):
    return text[::-1]
text = input("Enter a text: ")
print(reverse_str(text))
#bài 4
def is_palindrome(text) : 
    return text == reverse_str(text)
text = input("Enter a text: ")
print(is_palindrome(text))

#Phần 2.  
#bài 1
def tinhgiaithua(n):
   if n == 0:
        return 1
   else:
        return n * tinhgiaithua(n-1)
n = int(input("Enter a number: "))
print(f"The result is {tinhgiaithua(n)}")
#bài 2
original_list = [5, 1, 8, 92, -1, 30]

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def from_the_beginning(number, sorted_list):
    return sorted_list[:number]

sorted_list = bubble_sort(original_list)
print("Sorted list :", sorted_list)
#bài 3
def print_fibo(n):
    if n <= 0:
        return "Số n phải lớn hơn 0."
        
    elif n == 1:
        return "Phần tử đầu tiên của dãy Fibonacci: 1"
        
    else:
        fibo = [1, 1]
        for i in range(2, n):
            fibo.append(fibo[i-1] + fibo[i-2])
        print("Phần tử đầu tiên của dãy Fibonacci: ", *fibo[:n],end="")

print_fibo(5)
#phần 3
#bài 1
def tinh_hieu(n):
    hieu = n - 17
    if n > 17:
        hieu = hieu * 2
        if hieu < 0:
            hieu = -hieu
    return hieu

print(tinh_hieu(18))
#bài 2
from datetime import date

def tinh_ngay_giua_hai_ngay(date1, date2):
    if date2 > date1:
        return (date2 - date1).days
    else:
        return (date1 - date2).days
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(tinh_ngay_giua_hai_ngay(date1, date2), "ngày")
#bài 3
def dem_so_4(danh_sach):
    return danh_sach.count(4)

danh_sach = input("Nhập danh sách các số cách nhau bởi dấu phẩy: ")
danh_sach = [int(x) for x in danh_sach.split(",")]
so_4 = dem_so_4(danh_sach)
print(f"Trong danh sách có {so_4} số 4")
#bài 4
'''386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527'''
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
def print_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)
        elif i == 237 :
            break
print_even(numbers)
#bài 5
def ve_bieu_do_histogram(ky_tu, danh_sach):
    for so in danh_sach:
        print(ky_tu * so)
ky_tu = input("nhập kí tự :"" ")
danh_sach = []
danh_sach = input("Nhập danh sách các số cách nhau bởi dấu phẩy: ")
danh_sach = [int(x) for x in danh_sach.split(",")]
ve_bieu_do_histogram(ky_tu, danh_sach)

