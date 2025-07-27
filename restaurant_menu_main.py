# Menu of the Restaurant 

menu = {"Pizza": 240,
        "Burger": 180,
        "Pasta" : 200,
        "Cold Coffee" : 90,
        "Chowmein" : 120,
        "Stew" : 90,
        "Salad" :185,
        "French Fries" : 80,
        "Choco lawa cake" : 155,
        "Cold Drink " : 40,
        "water" : 20
        }

#Greet
print("Welcome to the Python Restaurant :)")
print("Pizza: Rs 240 \nBurger: Rs 180 \nPasta: Rs 200 \nCold Coffee: Rs 80 \nChowmein: Rs 120 \nStew: Rs 90 \nSalad: Rs 185 \nFrench Fries: Rs 80 \nChoco lawa cake: Rs 155 \nCold Drink: Rs 40 \nwater: Rs 20")

order_total = 0  

item_1 = input("Enter your order: ")

if (item_1 in menu):
    order_total += (menu[item_1] + (menu[item_1] * 0.18))
    print(f"Your item {item_1} have been added to your order")

else:
    print(f"The current item {item_1} is not available yet!")

another_order =  input("Do you want to add another item? (Yes/No) ")

if (another_order == "Yes"):
    item_2 = input("Enter your order: ")
    if (item_2 in menu):
        order_total += (menu[item_2] + (menu[item_2] * 0.18))
        print(f"Your item {item_2} have been added to your order")
    
    else:
        print(f"The current item {item_2} is not available yet!")    

print(f"Thanks for ordering \nYour total order is of Rs {order_total}")        
