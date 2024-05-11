hs = ["huy", "hong"]
student = list(("huy","ngoc"))# tao list
print(hs[1])
hs[1]= "hieu" #change the value of second element in the list to  "hieu"
print(hs[1])
student.append("hieu")# them vao cuoi danh sach 
student.insert(1,"mmb") # them vao vi tri chi dinh
student.extend(hs)# Để nối các phần tử từ danh sách khác vào danh sách hiện tại(hoặc nối các loại phần tử khác nhau)
student.pop(1)#xoa phan tu theo vi tri 
student.remove("ngoc")#xoa phan tu theo giá trị
del  student[0] # xóa phần tử theo vi tri
student.clear() # xóa toàn bộ danh sách
# vong lap for trong danh sach 
for i in student :
    print(i)

# vong lap while 
x = 0 
while x < len(student):
    print(student[x])
    x += 1
# cong danh sach
newList = student + hs 
TheTuple = ("stun","mmb","clm","tục") #tuple
theList = tuple((1,4,5,6,7,8))
MyList = list(TheTuple)
#câu 1
#Ý số 1
food_list = []
while True:
    food = input("Chọn món ăn yêu thích (hoặc chọn 'quit' để dừng): ")
    if food.lower() == 'quit':
        break
    food_list.append(food)
print("Món ăn yêu thích:")
for food in food_list:
    print(food)

#Ý số 2
while True:
    remove_food = input("Chọn món ăn để loại bỏ (hoặc chọn 'quit' để dừng): ")
    if remove_food.lower() == 'quit':
        break
    if remove_food in food_list:
        print(f"Loại bỏ {remove_food} khỏi danh sách...")
        food_list.remove(remove_food)
    else:
        print(f"{remove_food} không ở trong danh sách.")
print("Danh sách món ăn yêu thích sau khi cập nhật:")
for food in food_list:
    print(food)

#câu 2 
num_list = []
user_input = input("Nhập các số cách nhau bằng dấu cách: ")
num_list = [int(x) for x in user_input.split()] # Chia chuỗi đầu vào thành danh sách các số

sum_of_numbers = sum(num_list)
print("Tổng của các số là:", sum_of_numbers)
#câu 3
max_of_numbers = max(num_list)
print("số lớn nhất là :", max_of_numbers)

#câu 4
n = len(num_list)
for i in range(n):
    for j in range(0, n-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
for num in num_list :
    print(num)
