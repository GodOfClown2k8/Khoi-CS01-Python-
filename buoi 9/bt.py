#bai 1
numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
           'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}

roman_number = input("Nhập số La Mã: ")

if roman_number in numbers:
    print(f"Số Ả Rập tương ứng: {numbers[roman_number]}")
else:
    print("Not found")
#bai 2
numbers_2 = {'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15,
                   'XVI': 16, 'XVII': 17, 'XVIII': 18, 'XIX': 19, 'XX': 20}
numbers.update(numbers_2)
print(numbers)
roman_number = input("Nhập số La Mã: ")

if roman_number in numbers:
    print(f"Số Ả Rập tương ứng: {numbers[roman_number]}")
else:
    print("Not found")
#bai 3
number_list = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
               'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']

numbers = {}
i = 1
for roman in number_list:
    numbers[roman] = i
    i += 1

roman_number = input("Nhập số La Mã: ")

if roman_number in numbers:
    print(f"Số Ả Rập tương ứng: {numbers[roman_number]}")
else:
    print("Not found")
#bai 4
students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
            {'firstName': 'Mervin', 'lastName': 'Friedland'},
            {'firstName': 'Aron', 'lastName': 'Wilkins'}]

print("Danh sách học sinh:")
for student in students:
    print(f"- {student['firstName']} {student['lastName']}")
#bai 5
names = {
  'students': [
    {'firstName': 'Nikki', 'lastName': 'Roysden'},
    {'firstName': 'Mervin', 'lastName': 'Friedland'},
    {'firstName': 'Aron', 'lastName': 'Wilkins'}
  ],
  'teachers': [
    {'firstName': 'Amberly', 'lastName': 'Calico'},
    {'firstName': 'Regine', 'lastName': 'Agtarap'}
  ]
}

print("Danh sách học sinh:")
for student in names['students']:
    print(f"- {student['firstName']} {student['lastName']}")

print("\nDanh sách giáo viên:")
for teacher in names['teachers']:
    print(f"- {teacher['firstName']} {teacher['lastName']}")
#bai 6
def count_characters():
    sequence = input("Nhập vào một chuỗi ký tự: ")
    char_frequency = {}

    for char in sequence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    print("Tần suất xuất hiện của từng ký tự:")
    print(char_frequency)

count_characters()