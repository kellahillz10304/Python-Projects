import graphics as g 

win = g.GraphWin( "House", 500, 500 )

win.setBackground( 'blue' )

horizon = g.Line( g.Point( 0, 450 ), g.Point( 500, 450 ) )
horizon.draw( win )
horizon.setFill( 'green' )
horizon.setWidth( 10 )

house = g.Rectangle( g.Point( 150, 250 ), g.Point( 350, 450 ) )
house.draw( win )
house.setFill( 'red' )

door = g.Rectangle( g.Point( 225, 375 ), g.Point( 275, 450 ) )
door.draw( win )
door.setFill( 'orange' )

doorknob = g.Circle( g.Point( 265, 415 ),  3 )
doorknob.draw( win )
doorknob.setFill( 'black' )

roof1 = g.Line( g.Point( 150, 250 ), g.Point( 250, 175 ) )
roof1.draw( win )
roof1.setFill( 'gray' )
roof1.setWidth( 6 )

roof2 = g.Line( g.Point( 250, 175 ), g.Point( 350, 250 ) )
roof2.draw( win )
roof2.setFill( 'gray' )
roof2.setWidth( 6 )

window1 = g.Rectangle( g.Point( 175, 300), g.Point( 215, 350 ) )
window1.draw( win )

window2 = g.Rectangle( g.Point( 285, 300 ), g.Point( 325, 350  ) )
window2.draw( win )

window1.setFill( 'blue' )
window2.setFill( 'blue' )

treeTrunk = g.Line( g.Point( 425, 350 ), g.Point( 425, 450) )
treeTrunk.draw( win )
treeTrunk.setWidth( 9 )
treeTrunk.setFill( 'brown' )

tree = g.Circle( g.Point( 425, 350 ),  25  )
tree.setFill( 'green' )
tree.draw( win )

sun = g.Circle( g.Point( 75, 75 ), 45 )
sun.draw( win )
sun.setFill( 'yellow' )

houseMessage = g.Text( g.Point( 250, 475 ), "Welcome home!" )
houseMessage.draw( win )
houseMessage.setFill( 'white' )

clickPoint = win.getMouse()
win.setBackground( 'black' )
sun.setFill( 'white' ) 









