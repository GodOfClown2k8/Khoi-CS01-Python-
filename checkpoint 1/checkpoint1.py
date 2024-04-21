'''
#Phần 1 
#bài 1 
first_name =  input("Enter your first name: ")
last_name = input ("Enter your last name :")
print("Your full name is",first_name," ",last_name)
#bài 2
input = input("Enter something :")
print(input.upper())

#bài 3
Square= int(input("Enter number:"))
print(float(Square**2))

#bài 4
from turtle import * 
radius = int(input("Enter the radius of the circle: "))
circle(radius)
mainloop()

#Phần 2
#Bài 1
for i in range(2,12): 
    i+=1
    print(i)

#Bài 2
n = int(input("Enter a number :"))
for i in range(0,n+1):
    print(i)

#Bài 3
n = int(input("Enter a number :"))
for i in range(1,n,2):
    if i % 2 == 1:
        print(i)

#Bài 4
edge =  int(input("edge :"))
angle = 360/edge
from turtle import *
for i in range(edge):
  left(angle)
  forward(100)
mainloop()

#Phần 3
#Bài 1
n =  int(input("Nhập số n:"))
if n > 13 :
    print("This number is larger than 13")
elif n < 13 : 
    print("This number is not larger than 13")
#bài 2 
n =  int(input("Nhập số n:"))
if n % 2 == 0 :
    print("This number is even")
else : 
    print("This number is not even")
#bài 3 
month = int(input("Nhập tháng:"))
if month in [1,3,5,7,8,10,12]:
    print("This month has 31 days.")
elif month in [4,6,9,11]:
    print("This month has 30 days.")
else :
    print("This month has 28  or 29 days.")
#Phần 4 
#bài 1
username = input("Username: ")
password = int(input("Password : "))
email = input("Email : ")
print("Username : ", username , "\n Password : ", password,"\n Email :", email)
print("Registered successfully")
#bài 2
username = input("Username: ")
password = int(input("Password : "))
repeat_password = int(input("Repeat password : "))
while password!= repeat_password:
    print("Passwords not match. Please input again.")
    password = int(input("Password : "))
    repeat_password = int(input("Repeat password : "))
email = input("Email(example@gmail.com): ")
print("Username : ", username, "\n Password : ", password,"\n Email :", email)
print("Registered successfully")

#bài 3 

def is_valid_password (password):
   if len(password)<8:
      return False
   else:
      return True

username = input("Username: ")
password = input("Password: ")

while not is_valid_password(password):
  print("Invalid password. Please input again.")

password = input("Password: ")
repeat_password = input("Repeat password: ")

while password != repeat_password:
   print("Passwords do not match. Please input again.")

repeat_password = input("Repeat password: ")
email = input("Email: ")
def is_valid_email(email):
   if "@" in email and "." in email:
      return True
   else:
      return False

while not is_valid_email(email):
   print("Invalid email. Please input again.")

email = input("Email: ")
print("Registered successfully.")
'''