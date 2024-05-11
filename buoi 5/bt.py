###Phần 1: (Trả lời vào file python và comment lại)

##Câu 1. Liệt kê các đặc điểm giống nhau giữa list và tuple.
#+Cả List và Tuple đều được sắp xếp theo trình tự, có trình tự các items được quy định.  
#+Cả hai đều chứa được mọi kiểu dữ liệu và nhiều kiểu dữ liệu khác nhau cùng 1 list/tuple.
#+Cả hai đều có thể chứa các items lặp lại được. 

##Câu 2. Cho biến employee = ('Jane', 22, 'Engineer'). Làm thế nào để thay đổi giá trị của employee[1] thành 23?
# employee = ('Jane', 22, 'Engineer')
# l_e = list(employee)
# l_e[1] = 23
# print(l_e[1])

##Câu 3. Cho biến cars = ['Mercedes', 'Rolls Royce', 'Lamborghini', 'Range Rover']. Biểu thức nào sau đây trả về ['Lamborghini', 'Range Rover']?
# B. cars[2:]

##Câu 4. Câu lệnh nào sau đây khởi tạo list có giá trị [(1, 1), (2, 4), (3, 9), (4, 16)]?
# B. arr = [(x, x**2) for x in range(1, 5)]

##Câu 5. Cho đoạn code sau.
# arr = [1, 2, 3, 4]
# arr.append(5)
# arr_2 = arr.copy()
# arr = []
# Chọn giá trị đúng của arr_2 sau khi thực thi đoạn code trên:
# C. [1, 2, 3, 4, 5]

#Phần 2 
#Bài 1
# Original list
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Add 2
add_2 = [x + 2 for x in arr]

# Multiply by 2
multiply_2 = [x * 2 for x in arr]

# Shift 2
shift_2 = arr[2:] + arr[:2]

# Print the results
print("Original list :", arr)
print("Add 2         :", add_2)
print("Multiply by 2 :", multiply_2)
print("Shift 2       :", shift_2)

#Bài 2 
# Cho một mảng chứa thông tin của một chuỗi ký tự đã được mã hóa như sau:
arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l','o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']           
# Hãy tìm quy luật mã hóa và xây dựng lại chuỗi ký tự ban đầu. Kết quả mong đợi của chương trình là chuỗi ký tự trước khi được mã hóa.
arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l','o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
arr.reverse()
print(*arr)
#Bài 3 
# Lấy số Fibonacci cần in từ người dùng
n = int(input("Input a positive number: "))

# Khởi tạo hai số Fibonacci đầu tiên
a, b = 1, 1

# In số Fibonacci đầu tiên
print("First {} Fibonacci number(s): {}".format(n, a))

# In các số Fibonacci còn lại
for i in range(1, n):
    a, b = b, a + b
    print("{} ".format(a), end="")

print()
# Bài 4
'''
Mã này khởi tạo một danh sách trống để lưu trữ các mục menu. Sau đó nó sẽ nhắc người dùng nhập số lượng mục trong menu.
Sau đó, mã sẽ đi vào một vòng lặp nhắc người dùng nhập tên và giá của từng mặt hàng. Nó lưu trữ từng mục dưới dạng một bộ dữ liệu trong danh sách menu.
Sau khi lấy được tất cả các món trong menu, mã sẽ tính giá trung bình bằng cách cộng giá của tất cả các món rồi chia cho số món.
Sau đó, mã sẽ khởi tạo một danh sách trống để lưu trữ các mặt hàng có giá cao hơn mức trung bình. Sau đó, nó đi vào một vòng lặp lọc ra các mặt hàng có giá cao hơn mức trung bình và thêm chúng vào danh sách trên_trung bình.
Cuối cùng, mã in ra các mặt hàng có giá trên mức trung bình theo cách được định dạng.
'''
#Khởi tạo một danh sách trống để lưu trữ các mục menu
menu = []

#Lấy số lượng mục từ người dùng
num_items = int(input("Number of items: "))

#Lấy tên và giá của từng mặt hàng từ người dùng
for i in range(num_items):
    name = input("Item {} name: ".format(i+1))
    price = float(input("Price of item {}: ".format(i+1)))
    menu.append((name, price))

#Tính giá trung bình
average = sum(item[1] for item in menu) / num_items
print("Average price: {:.2f}".format(average))

#Khởi tạo một danh sách trống để lưu trữ các mặt hàng có giá cao hơn mức trung bình
above_average = []

#Lọc ra các mặt hàng có giá trên mức trung bình
for item in menu:
    if item[1] > average:
        above_average.append(item)

#In các mặt hàng có giá trên mức trung bình
print("Item(s) above average price:")
for item in above_average:
    print("  Item {}: {} (Price: {:.2f})".format(menu.index(item)+1, item[0], item[1]))

#bài 5
# Nhận câu từ người dùng
sentence = input("Write a sentence: ").lower()

# Chia câu thành một danh sách các từ
word_list = sentence.split(' ')

# Chuyển đổi danh sách các từ thành một bộ để loại bỏ trùng lặp
word_set = set(word_list)

# Chuyển đổi tập hợp trở lại danh sách để có được các từ duy nhất
unique_words = list(word_set)

# In số lượng từ duy nhất
print("Number of unique words: ", len(unique_words))