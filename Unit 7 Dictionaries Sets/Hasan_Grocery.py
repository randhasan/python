'''
Rand Hasan
Grocery Application
This program is used to simulate check out at a grocery store.
'''

'''
The loadData function opens the file with the description and prices of most of the 
items in the store.
'''


def loadData(filename):
    inFile = open(filename,"r")
    products = {}
    for line in inFile:
        wordList = line.strip().split(", ")
        products[wordList[0].strip()]= wordList[1:]
    inFile.close()
    return products

'''
The checkUPC function processes the UPC code entered by the user to determine whether or not
the code is valid.
'''
    
def checkUPC(code):
    for pos in range(len(code)): #checks to see if their are any non-numberical digits in the UPC code
        try:
            pos = int(code[pos])
        except ValueError:
            print("UPC may only contain numerical digits.")
            return False                
            
    if len(code)!=12: #valid UPC code must contain 12 numbers
        print("Invalid UPC.")
        return False
    else:
        sum = 0
        for pos in range(len(code)):
            if pos%2 == 0: # it's in an even position
                sum += int(code[pos])*3 # multiply number in the even positions by three
            else:
                sum += int(code[pos])
        if sum%10 == 0: #valid UPC
            return True
        else: #invalid UPC
            print("Invalid UPC.")
            return False
  

'''
The checkOut function is similiar to the checkUPC function as it determines whether or not the
user's credit card number is valid.

'''
def checkOut(cardNum):
    notNum = False
    for pos in range(len(cardNum)): #checks to see if their are any non-numberical digits in the credit card number
        try:
            pos = int(cardNum[pos])
        except ValueError:
            print("Credit card number may only contain numerical digits. \n")
            return False          
        
    if len(cardNum)!= 16: #valid credit card number must contain 16 numbers
        print("Invalid credit card number.")
        print()        
        return False
    else:
        evens = 0
        odds = 0
        misOdds = 0 #numbers in odd positions that are greater than 4
        sum1 = 0
        lastDigit = 0
        list1 = []
        for pos in range(0,(len(cardNum))-1): #first 15 numbers
            if pos%2 != 0:
                evens += int(cardNum[pos])
            else:
                odds += int(cardNum[pos])
                if pos>4: # if a number in an odd position is greater than 4, it is added to the "misOdds" variable
                    misOdds += 1
        for pos in range(len(cardNum)): #includes all 16 numbers
            list1.append(cardNum[pos]) #puts every number in the credit card number into a list
        lastDigit = list1[-1] #last number in list
        odds *= 2 #sum of odds is multiplied by 2
        sum1 = evens+odds+misOdds
        sum1 = 10 - (sum1%10) #what you would add to make the total sum a multiple of 10
        if int(sum1)==int(lastDigit): #valid credit card number
            print()
            print("Payment Accepted! \n")
            print("Thank you for shopping with us!")              
            return True
        else: #invalid credit card number
            print("Invalid credit card number.")
            print()            
            return False

'''
The addProductToDatabase allows the cashier to add products to the dictionary "products" if the
user wishes to purchase an item that is in the store but not in the dictionary.

'''            
def addProductToDatabase(code,products,filename):
    format1 = "{:.2f}"
    name = input("Enter product description for UPC "+str(code)+": ").title()
    price = input("Enter the price of "+name+": ")
    price = format1.format(float(price))
    products[code] = [name,price] #adds product description and price to "products" dictionary
    outFile = open(filename,"a") #opens the file to append the new product
    outFile.write(code+", "+name+", "+price+"\n")
    outFile.close()
    print("Item "+str(code)+" has been added to the database.")
    print() #formatting
               
'''
The outputCart function prints out all of the items in the cart after each time an item gets scanned
'''
def outputCart(cart,products):
    subtotal = 0
    strFormat = "{0:40}${1:4.2f}"
    print("Currently Scanned Items:")
    print("-------------------------")
    for code in cart:
        info = products.get(code)
        description = info[0]
        price = info[1]
        print(strFormat.format(description,float(price)))
        subtotal+=float(price)
    print("-------------------------")
    print(strFormat.format("Total Due:",float(subtotal)))
    
def main():
    cart = []
    filename = "UPC.txt"
    products = loadData(filename)
    code = ""
    while code.lower()!="x":
        code = input("Enter UPC (or x to check out): ")
        if code.lower()!="x":
            check = checkUPC(code)
            if check == True:
                print()
                if code in products:
                    cart.append(code) #add products to card
                    scannedItems = outputCart(cart,products) #print every item in the cart
                else:
                    print("UPC "+ str(code)+" is not currently a product in our product database.")
                    addProduct = input("Would you like to add it? (y/n): ")
                    if addProduct[0].lower() == "y":
                        print()
                        add = addProductToDatabase(code,products,filename)   
                        cart.append(code)
                        scannedItems = outputCart(cart,products)
            print()
    if code.lower()=="x": #user wants to pay
        purchase = False #user has not paid yet
        print()
        if len(cart)==0: #if user hasn't put anything in their cart a message is display
            print("Thank you for shopping with us!")
        else:
            print("-------------------------")
            print()
            while purchase!=True:
                cardNum = input("Enter credit card number: ")
                purchase = checkOut(cardNum)
                
 
main()
