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


def add_remove_coins(): #Tells user how many coins to add/ remove if weight is mismatched
    if weight < coins[coin_type][2]:
        bag_weight = coins[coin_type][2]
        difference = bag_weight - weight

        coins_add = difference / coins[coin_type][3]
        print(f"add {coins_add} coins")
    else:
        bag_weight = coins[coin_type][2]
        difference = weight - bag_weight

        coins_remove = difference / coins[coin_type][3]
        print(f"remove {coins_remove} coins")

#reading text file, storing in dict
try:
    f = open("CoinCount.txt", "r")
    lines = f.readlines()
    f.close()
    print(lines)
    names = {
        #name: [bags checked, value, accuracy]
        }

    for line in lines:
        parts = line.strip("\n").split(",")   
        names[parts[0]] = [parts[1].strip(), parts[2].strip(), parts[3].strip()]


    print(names)
except:
    f = open("CoinCount.txt", "w")
    f.close()
    names = {
        #name: [bags checked, value, accuracy]
        }


choice = input("do you want to input coins [1] or view list [2]: ")    

while choice == "1": #input coins and weight 
    bags_checked = 0

    print(f"Valid coins: {valid_coins}")

    volunteer = input("Enter name: ").title()
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

    bags_checked += 1

    if volunteer in names: 
        names[volunteer][0] = int(names[volunteer][0]) + bags_checked

        f = open("CoinCoint.txt", "w")
        for name in names:
            f.write(f"{name}, {names[name][0]}, {names[name][1]}, {names[name][2]}\n")

        f.close()

    choice = input("do you want to input coins [1] or view list [2]: ") 



    
    
    #Store txt data in list of dictionary, edit it during program, use "w" at end of program to overwrite txt file woth new data (doesn't work yet)
  