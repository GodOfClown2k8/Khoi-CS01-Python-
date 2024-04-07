"""
#1. Đảo ngược chuỗi: Viết một chương trình Python nhận một chuỗi từ người dùng và in ra chuỗi đảo ngược của nó.
a = str(input(""))
print (a[::-1])
#2. Đếm số lần xuất hiện của một ký tự trong chuỗi: Sử dụng phương thức count() của chuỗi để đếm số lần xuất hiện của một ký tự.
b = str(input(""))
print(b.count(input("")))
#3. Chuẩn hóa chuỗi: Sử dụng các phương thức strip() và lower() để loại bỏ các khoảng trắng thừa và chuyển đổi chuỗi thành chữ thường.
c = str(input("           "))
x = c.strip("")
y = x.lower()
print(y)
"""
"""
import math 
a = input("")
b = input("")

print(int((a+b),(a/b),(a*b),(a-b)))
print(float((a+b),(a/b),(a*b),(a-b)))

c = float(input())
d = int(c)
print(d)
print(float(d))

#4. Tính diện tích và chu vi hình chữ nhật dựa trên chiều dài và chiều rộng nhập từ người dùng, in kết quả dưới dạng số nguyên và số thực
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is: ", int(area))
print("The perimeter of the rectangle is: ", int(perimeter))

print("The area of the rectangle is: ", float(area))
print("The perimeter of the rectangle is: ", float(perimeter))
"""
