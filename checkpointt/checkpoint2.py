#Phần 1 
#Bài 1
colors = ["blue", "red", "teal", "green"]
'''
print(colors)
#bài 2 
print("Colors list :",*colors)
#bài 3 
while True :
    color = input("Input a new color(or 'quit' to stop): ")
    if color.lower() != 'quit':
        colors.append(color)
    else :
        break

print("New colors list :",*colors)

#Phần 2 
#Bài 1 
position = int(input("Input position: "))

if 1 <= position <= len(colors):
    print(f"Color at position {position}: {colors[position - 1]}")
else:
    print("Invalid position")    
'''
'''
#Bài 2
position = int(input("Input position: "))
item_to_delete = input("Item to delete: ")

if item_to_delete.isdigit():
    position = int(item_to_delete)
    if 1 <= position <= len(colors):
        del colors[position - 1]
    else:
        print("Invalid position")
else:
    if item_to_delete in colors:
        colors.remove(item_to_delete)

print("New color list:", *colors)
'''
#Phần 3
'''
#Bài 1
numbers = [5, 1, 8, 92, -1, 30]

number_to_find = int(input("Input a number: "))

if number_to_find in numbers:
    position = numbers.index(number_to_find) + 1
    print(f"Number found at position {position}")
else:
    print("Number not found")
#Bài 2 
tong = sum(numbers)
print("Sum of all numbers:",tong)

#Bài 3
numbers = []

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)

sum_of_numbers = sum(numbers)

print(f"Sum of numbers in list: {sum_of_numbers}")

#Phần 4 
#bài 1
numbers = [5, 1, 8, 92, 7, 30]
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers: ",*even_numbers)

#bài 2
numbers = []
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)
even_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print("Even numbers: ",*even_numbers)
'''
#Phần 5
#bài 1
districts = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]

print(f"Districts: {districts}")
print(f"Populations: {populations}")
#bài 2
districts = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
populations = [247100, 333300, 266800, 420900, 318000]

dong_nhat = populations.index(max(populations))
vang_nhat = populations.index(min(populations))

print(f"Indices of:")
print(f"- Most populated dist.: {dong_nhat}")
print(f"- Least populated dist.: {vang_nhat}")
#bài 3
quan_dong_nhat = districts[dong_nhat]
quan_vang_nhat = districts[vang_nhat]
print("Names of:")
print(f"- Most populated dist.: {quan_dong_nhat}")
print(f"- Least populated dist.: {quan_vang_nhat}")
#PHần 6
#bài 1
areas = [9.224,43.35,12.04,9.96,10.49]
population_densities = [population / area for population, area in zip(populations, areas)]
print("\nPopulation densities of districts :")
for i in range(len(population_densities)):
    print(f"- {districts[i]}: {population_densities[i]:.2f}")
#bài 2
population_densities_average = sum(population_densities) / len(districts)
print("average population densities :",population_densities_average)
#Phần 7 
#bài 1 
high_scores = [78, 56, 67]
#bài 2 
print("High scores:")
for i in range(len(high_scores)):
   print(f"{i+1}. {high_scores[i]}")
#bài 3
new_score = int(input("Input new high score :"))
high_scores.append(new_score)
#high_scores = sorted(high_scores, reverse=True)
print("High scores:")
for i in range(len(high_scores)):
   print(f"{i+1}. {high_scores[i]}")
#Phần 8
#Bài 1
new_score = int(input("Input new high score :"))
high_scores.append(new_score)
high_scores = sorted(high_scores, reverse=True)
print("High scores:")
for i in range(len(high_scores)):
   print(f"{i+1}. {high_scores[i]}")
#Bài 2
high_scores = [78, 56, 67, 45, 70]
new_score = int(input("Input new high score :"))
high_scores.append(new_score)
high_scores = sorted(high_scores, reverse=True)
print("High scores:")
for i in range(5):
    print(f"{i+1}. {high_scores[i]}")