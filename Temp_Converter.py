for tempCoversions in range(3):
    inputFarString = input("Enter the temperature in F: ")
    tempInF = float(inputFarString)
    tempInC = (tempInF - 32) * .55
    print( "The temperature in C is", tempInC )
