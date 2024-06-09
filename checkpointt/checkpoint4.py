#PHan 1
#bai 1
laptop_dict = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
#bai 2
print("Available MACBOOKs:",laptop_dict["MACBOOK"])
#bai 3
brand = input("nhap hang may tinh :")
if brand in laptop_dict:
    print(f"\nAvailable",brand,":",laptop_dict[brand])
else :
    print("khong co hang nao nhu vay ca")
#PHan 2
#bai 1
laptop_dict2 = {
    "TOSHIBA": 10
}
laptop_dict.update(laptop_dict2)
print(laptop_dict)
#bai 2
brand = input("nhap hang may tinh :")
amount = input("nhap so luong may tinh :")
laptop_dict[brand] = amount
print("Available products:")
for brand,amount in laptop_dict.items():
    print(f"-{brand}: {amount}")
#bai 3
laptop_dict["DELL"]+= 10
laptop_dict["MACBOOK"]+= -10
print("Available products:")
print(f"-{brand}: {amount}")
#bai 4
total = sum(laptop_dict.values())
print("total products :",total)

#Phan 3 
#bai 1 
computer_price = {
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 1200,
    "ASUS": 400
}
#bai 2
print("Price of ASUS :",computer_price["ASUS"])
#bai 3
brand = input("nhap hang may tinh :")
if brand in computer_price:
    print(f"\nPrice of {brand}:",computer_price[brand])
else :
    print("khong co hang nao nhu vay ca")
#phan 4 
#bai 1
so_asus = int(input("Nhap so luong may ASUS: "))
asus_price = computer_price["ASUS"]
total_price = asus_price * so_asus
print("Total price:", total_price)
#bai 2
br_and = input("nhap hang may tinh :")
amo_unt = int(input("Nhap so luong may : "))
if br_and in computer_price:
    total_price =computer_price[br_and]*amo_unt
    print("Total price :",total_price)
else : 
     print(" no way brand")
#bai 3
computer_prices = {
    "DELL": 650,
    "MACBOOK": 1200,
    "HP": 20,
    "ASUS": 400
}

computer_stock = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}

brand = input("Input a brand: ").upper()
amount_to_buy = int(input("Input amount to buy: "))

if brand in computer_prices and brand in computer_stock:
    if computer_stock[brand] >= amount_to_buy:
        total_price = computer_prices[brand] * amount_to_buy
        print(f"Total price: ${total_price:.2f}")
        computer_stock[brand] -= amount_to_buy
        print("Available products:")
        for brand, stock in computer_stock.items():
            print(f"- {brand}: {stock}")
    else:
        print("Not enough stock for this brand.")
else:
    print("No such brand exists.")
# Phan 5
# bai 1
computer_prices = {
    "DELL": 650,
    "MACBOOK": 1200,
    "HP": 600,
    "ASUS": 400
}
computer_stock = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30
}
total_value = {}
print("Total value of available brands:")
for brand, stock in computer_stock.items():
    total_price = computer_prices[brand] * stock
    total_value[brand] = total_price
    print(f"- {brand}: {total_price}")
#bai 2
total_value_all_items = sum(total_value.values())
print("Total value of available items:", total_value_all_items)
#PHan 6
#bai 1
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
#bai 2
character["Gold"] += 50
#bai 3
character["Backpack"].append("FlintStone")
#PHan 7
#bai 1 
skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]

# bai 2
for i in range(len(skills)):
    print(f"Skill {i+1}: {skills[i]['Name']}")
#PHan 8
#bai 1
skills = [
    {"Name": "Tackle", "Minimum level": 1, "Damage": 5, "Hit rate": 0.3},
    {"Name": "Quick Attack", "Minimum level": 2, "Damage": 3, "Hit rate": 0.5},
    {"Name": "Strong Kick", "Minimum level": 4, "Damage": 9, "Hit rate": 0.2}
]

level = 2

print("Cho phép:")
for i in range(len(skills)):
    print(f"Skill {i+1}: {skills[i]['Name']}")

while True:
    choice = int(input("Choose skill by number: "))
    if 1 <= choice <= len(skills):
        skill = skills[choice - 1]
        if skill["Minimum level"] <= level:
            print(f"You chose {skill['Name']}.")
            print(f"Damage: {skill['Damage']}")
            break
        else:
            print(f"Cannot deploy. Required level {skill['Minimum level']}.")
            break
    else:
        print("Invalid choice. Please choose again.")
#bai 2
import random

skills = [
    {"Name": "Tackle", "Minimum level": 1, "Hit rate": 0.8, "Damage": 10},
    {"Name": "Quick Attack", "Minimum level": 1, "Hit rate": 0.9, "Damage": 15},
    {"Name": "Strong Kick", "Minimum level": 2, "Hit rate": 0.7, "Damage": 20}
]

level = 2

print("Choose a skill:")
i = 1
for skill in skills:
    print(f"{i}. {skill['Name']}")
    i += 1

while True:
    choice = int(input("Enter the number of your chosen skill: "))
    if 1 <= choice <= len(skills):
        chosen_skill = skills[choice - 1]
        if chosen_skill["Minimum level"] <= level:
            if random.random() < chosen_skill["Hit rate"]:
                print(f"You chose {chosen_skill['Name']}.")
                print(f"Damage: {chosen_skill['Damage']}")
            else:
                print(f"You chose {chosen_skill['Name']}.")
                print("Missed.")
            
        else:
            print(f"Cannot deploy. Required level {chosen_skill['Minimum level']}.")
    else:
        print("Invalid choice. Please choose again.")