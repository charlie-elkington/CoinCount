valid_coins = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
coins = {
        #type: [coin value(...p), bag value(...p), bag weight(...g) coin weight(...g)]
        "1p": [1, 100, 356, 3.65], 
        "2p": [2, 100, 356,7.12], 
        "5p": [5, 500, 325, 3.25] , 
        "10p": [10, 500, 325, 6.50], 
        "20p": [20, 1000, 250, 5.00], 
        "50p": [50, 1000, 160, 8.00], 
        "£1": [100, 2000, 175, 8.75], 
        "£2": [200, 2000, 120, 12.00]
}


def add_remove_coins():
    if weight < coins[coin_type][2]:
        bag_weight = coins[coin_type][2]
        difference = bag_weight - weight

        coins_add = difference // coins[coin_type][3]
        print(f"add {coins_add} coins")
    else:
        bag_weight = coins[coin_type][2]
        difference = weight - bag_weight

        coins_remove = difference / coins[coin_type][3]
        print(f"remove {coins_remove} coins")



print(f"Valid coins: {valid_coins}")

name = input("Enter name: ").title()
coin_type = input("Enter type of coin: ")

while coin_type not in valid_coins:
    coin_type = input("Enter type of coin: ")

while True: #weight validation
    try:
        weight = float(input("Enter weight of bag in grams: "))
        break
    except:
        print("Not a valid float")


if weight == coins[coin_type][2]:
    print("Correct number of coins")
else:
    add_remove_coins()
