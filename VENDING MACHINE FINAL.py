# function to ask the user if they want to start the vending machine or not
def startVendingMachine():
    while True:
        startChoice = input("Do you want to start the vending machine? (y/n): ").strip().lower()
        # function to continue to the vending machine
        if startChoice == 'y':
            return True
        # functiom to end the program
        elif startChoice == 'n':
            print("Have a great day!")
            print(r"""

   _____                 _ _                _ 
  / ____|               | | |              | |
 | |  __  ___   ___   __| | |__  _   _  ___| |
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ | |
 | |__| | (_) | (_) | (_| | |_) | |_| |  __|_|
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___(_)
                                  __/ |       
                                 |___/        
         
""")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# function to compute the user's change
def computeChange(insertedMoney, productPrice):
    # calculates and returns the change if the inserted money exceeds the product price.
    return insertedMoney - productPrice

# welcome message/introduction to ma vending machine
print("\nWelcome gang to my..")
print(r""" 
      
 __      __            _ _               __  __            _     _            
 \ \    / /           | (_)             |  \/  |          | |   (_)           
  \ \  / /__ _ __   __| |_ _ __   __ _  | \  / | __ _  ___| |__  _ _ __   ___ 
   \ \/ / _ \ '_ \ / _` | | '_ \ / _` | | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
    \  /  __/ | | | (_| | | | | | (_| | | |  | | (_| | (__| | | | | | | |  __/
     \/ \___|_| |_|\__,_|_|_| |_|\__, | |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                  __/ |                                       
                                 |___/                                        
""")

# displaying the vending machine menu
def vendingMachineMenu():
    print("Product          Price       Code")
    print("resees           $2          1")
    print("lays             $5          2")
    print("chuckie          $9          3")
    print("biscuit          $4          4")
    print("peanuts          $8          5")
    print("doritos          $6          6")
    print("cheetos          $7          7")
    print("oreo             $3          8")
    print("pringles         $10         9")
    print("snickers         $2          10")
    print("milkyway         $4          11")
    print("twix             $3          12")
    print("skittles         $5          13")
    print("m&ms             $4          14")
    print("kitkat           $3          15")

# product prices of the vending machine
productPrices = {
    1: 2,    # resees
    2: 5,    # lays
    3: 9,    # chuckie
    4: 4,    # biscuit
    5: 8,    # penuts
    6: 6,    # doritos
    7: 7,    # cheetos
    8: 3,    # oreo
    9: 10,   # pringles
    10: 2,   # snickers
    11: 4,   # milkyway
    12: 3,   # twix
    13: 5,   # skittles
    14: 4,   # m&ms
    15: 3    # kitkat
}

# matches the usercode the user entered from the vending machine's list.
def processPurchase():
    try:
        userCode = int(input("Enter the product code to continue: "))
        if userCode in productPrices:
            price = productPrices[userCode]
            # product list using list indexing 
            productName = [
                "resees", "lays", "chuckie", "biscuit", "peanuts",
                "doritos", "cheetos", "oreo", "pringles", "snickers",
                "milkyway", "twix", "skittles", "m&ms", "kitkat"
            ][userCode - 1]
            
            print(f"You have selected {productName}, pay ${price}")
            insertedMoney = float(input("Insert money: "))
            
            # a loop for insufficient funds
            while insertedMoney < price:
                print(f"Insufficient funds. You need to insert ${price - insertedMoney:.2f} more.")
                # where it asks the user to  add/insert more money
                insertedMoney += float(input("Insert more money: "))
            
            if insertedMoney == price:
                print(f"You have inserted ${price}. {productName} is dispensing, please wait...")
                print("Product Dispensed! Enjoy!")
            elif insertedMoney > price:
                change = computeChange(insertedMoney, price)
                print(f"You have inserted more than ${price}. {productName} is dispensing...")
                print(f"Here is your change: ${change:.2f}")
        else:
            print("Invalid product code. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# main loop for the vending machine
if startVendingMachine():
    while True:
        # Calling the vending machine and Displays the menu
        vendingMachineMenu()
        
        # where it processes the user's purchase
        processPurchase()
        
        # asks the user if they want to purchase more items
        while True:
            userChoice = input("\nWould you like to purchase more items? (y/n): ").strip().lower()
            # if the user presses 'n' the machine ends along with the thank you message
            if userChoice == 'n':
                print("Thank you for using the vending machine!")
                print(r"""
                      
       _____                                           _       _ 
      / ____|                         /\              (_)     | |
     | |     ___  _ __ ___   ___     /  \   __ _  __ _ _ _ __ | |
     | |    / _ \| '_ ` _ \ / _ \   / /\ \ / _` |/ _` | | '_ \| |
     | |___| (_) | | | | | |  __/  / ____ \ (_| | (_| | | | | |_|
      \_____\___/|_| |_| |_|\___| /_/    \_\__, |\__,_|_|_| |_(_)
                                            __/ |                
                                           |___/                 
    """)
    
                exit() # funtion where the program ends
            elif userChoice == 'y':
                # restarts the loop for the user to make another purchase
                break
            else:
                print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
