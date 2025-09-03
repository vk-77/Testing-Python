ItemsInCart = 0
#Now 2 items will be added to cart.

if ItemsInCart != 2:
    #raise Exception("Product count is not matching.") #Raise is used to create exception.from
    pass

assert(ItemsInCart == 0) # Another way to inform user regarding the error or execption.

#Try and Catch to raise and handle the exception.
try:
    with open('textfile1.txt','r') as reader:
        reader.read()

except:
    print("Somehow I reached this blcok coz there is a failure in try block")


finally:
    print("Cleaning up Resources")