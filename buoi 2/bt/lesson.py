'''
import math
bk = float(input("Enter the radius of the circle: "))
cv = 2 * math.pi * bk
dt = math.pi * bk ** 2
print("Chu vi của vòng tròn là:", cv)
print("Diện tích của vòng tròn là:", dt)
'''
'''
import math
canh = float(input("cạnh của hình vuông là: "))
dgcheo = math.sqrt(2) * canh
print("Đường chéo của hình vuông là:", dgcheo)
'''

'''
account_name = input("Enter the account name: ")
domain = input("Enter the domain: ")
email = account_name + "@" + domain
print("The email address is:", email)
'''

'''
date_input = input("Enter a date (MM/DD/YYYY): ")
date_obj = datetime.datetime.strptime(date_input, "%m/%d/%Y")
print("Date in DD/MM/YYYY format:", date_obj.strftime("%d/%m/%Y"))
'''
'''
initial_deposit = float(input("Nhập số tiền gửi ban đầu là: "))
balance_1_year = initial_deposit * 1.05
balance_2_year = initial_deposit * 1.05 ** 2
balance_10_year = initial_deposit * 1.05 ** 10
print("Tài khoản sau 1 năm:", round(balance_1_year, 2))
print("Tài khoản sau 2 năm:", round(balance_2_year, 2))
print("Tài khoản sau 10 năm:", round(balance_10_year, 2))
'''
'''
from turtle import *
bgcolor("white")
speed(10)
pencolor('#de5246')
fillcolor('#de5246')
begin_fill()
forward(150)
right(90)
forward(100)
right(90)
forward(150)
right(90)
forward(100)
end_fill()
penup()
goto(-25, 50)
pendown()
pencolor('#fff')
fillcolor('#fff')
begin_fill()
right(180)
forward(50)
right(135)
forward(70.71)
right(135)
forward(70.71)
right(180)
mainloop()
'''
'''
from turtle import *
Screen()
bgcolor("white")
Turtle()
speed(10)
pencolor('#cf8f03')
fillcolor('#cf8f03')
begin_fill()
right(70)
forward(150)
right(140)
forward(150)
right(180)
forward(150)
right(140)
forward(150)
end_fill()
penup()
goto(-50, -50)
pendown()
pencolor('#0b2c3c')
fillcolor('#0b2c3c')
begin_fill()
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(150)
right(120)
end_fill()
hideturtle()
mainloop()
'''
