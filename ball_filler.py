# V = 4/3(pi)r ** 3
# V = ((4/3 * 3.14 * 4.25(cubed)) - 124(cubed)) * 100

import math
ballEnter = int( input("Enter the number of balls to manufacture: "))
diameter = float( input("Enter the diameter for each ball: "))
volCor = float( input("Enter the core volume: "))
y = math.pow( (diameter/2), 3 )
z = math.pi
V = (((4/3) * (z * y)) - volCor) * ballEnter
print( V )