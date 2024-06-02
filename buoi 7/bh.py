import module 
module.summing(1,2)
#Bài 1
def solonhon(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("Số lớn hơn là :",solonhon(1,2))
#Bài 2

def check_int(a):
    if a % 2 == 0 :
        print("đây là số chẵn")
    elif a % 2 != 0:
        print("đây là số lẻ")
    else : 
        print("la so 0")
check_int(2)
#Bài 3
def la_nam_nhuan(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 == 0:
        print("là năm nhuận")
    else :
        print("ko là năm nhuận")
la_nam_nhuan(2016)
#Bài 4
def nhap_mang():
    n = int(input("Nhập số phần tử trong mảng: "))
    arr = []
    for i in range(n):
        x = input("Nhập phần tử thứ {}: ".format(i+1))
        
        try:
            arr.append(float(x))
        except str:
            print("Phần tử {} không phải là số, bỏ qua...".format(x))
    return arr

def tinh_tong(arr):
    if len(arr) == 0:
        return 0
    else:
        return sum(arr)

arr = nhap_mang()
tong = tinh_tong(arr)
print("Tổng các phần tử trong mảng là: ", tong)
#bài 5
def doi_chuoi(s):
    words = s.split(" , ")
    words.sort()
    return " , ".join(words)
s = input("Nhập chuỗi từ (các từ cách nhau bởi dấu phẩy): ")
print(doi_chuoi(s))
