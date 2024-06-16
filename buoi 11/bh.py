'''# 'w' viet 1 file moi 
# 'a' viet them vao 1 file co san 
# 'r' mo 1 file de doc 
# 'x' tao 1 file moi 
# read file 
f = open('csb03.txt','a')
print(f.read())
print(f.readline()) #read first line 
print(f.readline()) 
print(f.readline()) #read 2 first line 
print(f.readlines()) #print a list line of all file 
#write file 
f.write("hello world") 
#close file 
f.close()
#delete file 
# import os 
# os.remove("names.txt")
#Kiểm Tra Xem File Còn Ở Trong Máy Hay Ko
# import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# mở file mà có thể tự động đóng
 with open('csb03.txt','r') as f :
 print(f.read())
'''
#Bai 1
f = open('names.txt','r')
print("List of names :")
for x in f :
    print(x)
#Bai 3
filename = "vo_nguyen_minh_khoi.txt"
f = open(filename,'w')
f.write("Ho ten hoc sinh : Vo Nguyen Minh Khoi.\n")
f.write("Lop dang hoc : CSB03\n")
f.write("Truong : MINDX\n")
f.close()

f = open(filename, 'r')
print(f.read())
f.close()
#Bai 2
import os
filename = input("Enter a filename: ")

if os.path.exists(filename):
    with open(filename, 'r') as f:
        print(f.read())
else:
    print("File not found.")
