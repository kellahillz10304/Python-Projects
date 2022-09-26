print("Welcome to the Golf Club Helper!")
hitBall = input("Did you hit the ball on the green y/n? ")
ballDistance = int(input("How far is the ball from the the hole in feet? "))

if hitBall is "y":
    print("Use a putter")

if hitBall != "y":
    if ballDistance >= 200:
        print("Use a driver")
    elif ballDistance >=140 <200:
        print("Use a 5-iron")
    elif ballDistance >= 100 < 140:
        print("Use a 9-iron")
    elif ballDistance < 100:
        print("Use a pitching wedge")