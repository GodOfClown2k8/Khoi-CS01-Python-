'''
a = int(input("nhập số :"))
if a > 0 : 
    print("a là số dương")
elif a < 0 : 
    print("a là số âm")
else : 
    print("a bằng 0")


a = int(input("nhập số : "))
if a % 2 != 0 : 
    print("a là số lẻ")
else:
    print("a là số chẵn")
   

i = 1
while i < 6: 
    i+=1
    print(i)

import math 
i = 1
sum = 0 
while i <= 100: 
    sum = math.s
    i+= 1
    print(i)
print(sum) 

my_list = [1,2,3,4,5]
for i in my_list:
    print(my_list[1])
    break

for i in range(1,21,1):
    print(i)

#1.Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng
a = int(input("nhập số 1:"))
b = int(input("nhập số 2:"))
c = int(input("nhập số 3:"))
if a > b  and a > c:
    print ("số lớn nhất là a")
elif b > a and  b > c:
    print ("số lớn nhất là b")
else:
    print ("số lớn nhất là c")
#cách 2 
max_number = a 
numbers = [a,b,c]
for i in numbers : 
    if i > max _number:
        max_number = i
print(max_number)


#2. Viết chương trình xác định một năm có phải năm nhuận không (Năm nhuận là năm chia hết cho 4. Trong trường hợp năm chia hết cho 100 thì phải chia hết cho 400).
a = int(input("nhập năm : "))
if a % 4 == 0 :
    print(a,"là năm nhuận")
elif a % 100 == 0 and a % 400 == 0:
    print(a, " là năm nhuận")
else : 
    print(a,"không phải là năm nhuận")

#3. Dùng vòng lặp in ra các dãy số sau (mỗi dãy số là 1 vòng lặp):
     #- 0 1 2 3 4 5 6
     #- 100 101 102 103 104 105
     #- 9 8 7 6 5 4 3 2
for i in range(7):
    print(i, end=" ")
print("\n")

for i in range(100, 106):
    print(i, end=" ")
print("\n")

for i in range(9, 1, -1):
    print(i, end=" ")
print("\n")

#4. In ra các  số chia hết cho 3 từ 0 đến 20, mỗi số một dòng
for i in range(1,21):
    if i%3==0:
        print(i)

#5. Tính số chữ số của một số nguyên do người dùng nhập vào
a = int(input(" nhập số: "))
digit = len(str(abs(a)))
print("Số chữ số của số là",digit)

'''

