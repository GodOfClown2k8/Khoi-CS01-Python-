'''thisdict = {
    "class_name" : "CSB03",
    "year" : 2024,
    "student_count" : 10
}
#access item
print(thisdict["class_name"]) 
#change item 
thisdict["year"] = 2025
print(thisdict["year"])
#add item 
thisdict["new_student"] = "quynh anh "
print(thisdict)
#remove item 
#(theo key)
thisdict.pop("new_student")
del thisdict["new_student"]
#(remove phan tu cuoi)
thisdict.popitem()
#xoa toan bo
thisdict.clear()
del thisdict
#loop 
#duyet tat ca cac key
for y in thisdict : 
    print(y)
#duyet tat ca cac value
for x in thisdict:
    print(thisdict[x])
#duyet tat ca cac key va value
for x,y in thisdict.items():
    print(x,y)
#copy 
new_dict = thisdict.copy()
'''
'''
#nested(long vao nhau)

my_class = {
    "student 1":{
        "name" : "Tai",
        "age" : 20
        },
        "student 2":{
            "name" : "Lam",
            "age" : 21
            },
            "student 3":{
                "name" : "Huy",
                "age" : 22
                }
    }
for i in my_class:
    print(i["name"])
for x,y in my_class.items():
    print(y["name"])
    '''

#bai 1
laptop_dict = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
print(laptop_dict["MACBOOK"])
brand = input("nhap hang may tinh :")
if brand in laptop_dict:
    print(laptop_dict[brand])
else :
    print("khong co hang nao nhu vay ca")
#bai 2
character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}
#1
character["Gold"] += 50
#2
character["Backpack"].append("FlintStone")
#3
character["Pocket"] = ["MonsterDex", "Flashlight"]
print(character)
# bai 3
students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78}
}
if "David" in students_details:
    print(f"Thông tin của David: {students_details['David']}")
else:
    print("David không có trong danh sách")

def sort_students_by_score(students):
    return sorted(students.items(), key=get_score, reverse=True)

def get_score(student):
    return student[1]["score"]

sorted_students = sort_students_by_score(students_details)


for student, details in sorted_students:
    print(f"Học sinh: {student}, Tuổi: {details['age']}, Điểm số: {details['score']}")
