valid_coins = ["1p", "2p", "5p", "10p", "20p", "50p", "£1", "£2"]
coins = {
        #type: [coin value(...p), bag value(...p), bag weight(...g) coin weight(...g)]
        "1p": [1, 1.00, 356, 3.65], 
        "2p": [2, 1.00, 356,7.12], 
        "5p": [5, 5.00, 325, 3.25] , 
        "10p": [10, 5.00, 325, 6.50], 
        "20p": [20, 10.00, 250, 5.00], 
        "50p": [50, 10.00, 160, 8.00], 
        "£1": [100, 20.00, 175, 8.75], 
        "£2": [200, 20.00, 120, 12.00]
}


def add_remove_coins(): #Tells user how many coins to add/ remove if weight is mismatched
    if weight < coins[coin_type][2]:
        bag_weight = coins[coin_type][2]
        difference = bag_weight - weight

        coins_add = difference // coins[coin_type][3]
        print(f"add {coins_add} coins")
    else:
        bag_weight = coins[coin_type][2]
        difference = weight - bag_weight

        coins_remove = difference // coins[coin_type][3]
        print(f"remove {coins_remove} coins")

#reading text file, storing in dict
try:
    f = open("CoinCount.txt", "r")
    lines = f.readlines()
    f.close()
    print(lines)
    names = {
        #name: [bags checked, incorrect bags, value, accuracy]
        }

    for line in lines:
        parts = line.strip("\n").split(",")   
        names[parts[0]] = [parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip()]


    

except:
    f = open("CoinCount.txt", "w")
    f.close()
    names = {
        #name: [bags checked, incorrect bags, value, accuracy]
        }


choice = input("do you want to input coins [1] or view list [2]: ")    

if choice == "1": #input coins and weight 
    bags_checked = 0
    incorrect_bags = 0

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
        incorrect_bags = 1
        add_remove_coins()

    bags_checked += 1

    if volunteer in names: 
        names[volunteer][0] = int(names[volunteer][0]) + bags_checked
        names[volunteer][1] = int(names[volunteer][1]) + incorrect_bags
        names[volunteer][2] = float((names[volunteer][2])) + coins[coin_type][1]
        print(incorrect_bags + int(names[volunteer][1]))
        print(names[volunteer][0] + bags_checked)
        names[volunteer][3] = ((names[volunteer][0] - names[volunteer][1]) / names[volunteer][0]) * 100
        

        print(names)

        f = open("CoinCount.txt", "w")
        for name in names:
            f.write(f"{name}, {names[name][0]}, {names[name][1]}, {names[name][2]}, {names[name][3]}\n")

        f.close()

    choice = input("do you want to input coins [1] or view list [2]: ") 


elif choice == "2":
    print(f"\n{"-" * 10}\nVolunteers\n{"-" * 10}\n")
    print("Name, Bags checked, Incorrect bags, Total bag value, Accuracy")
    for name in names:
        print(f"{name}, {names[name][0]}, {names[name][1]}, £{names[name][2]}, {names[name][3]}%")

    
    
    #Store txt data in list of dictionary, edit it during program, use "w" at end of program to overwrite txt file woth new data (doesn't work yet)
  