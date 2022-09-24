def getIntBetween( message,low, high):
    num=low-1
    while num>high or num<low:
        try:
            num = int(input(message + " between "+str(low) + " and " + str(high) + ": "))
            if num>high or num<low:
                print("error- invalid number entered")
        
        
        except ValueError:
            print("Error- numeric value expected- try again\n")
        
    
    return num

def getFloatBetween( message,low, high):
    num=low-1
    while num>high or num<low:
        try:
            num = float(input(message + " between "+str(low) + " and " + str(high) + ": "))
            if num>high or num<low:
                print("error- invalid number entered")
        
        
        except ValueError:
            print("Error- numeric value expected- try again\n")
        
    
    return num