import graphics as g

win = g.GraphWin( "Gradient", 400, 400 )

color1 = g.Rectangle( g.Point( 0, 0 ), g.Point( 66.6, 400 ) )
color1.setFill( g.color_rgb( 0, 77, 0 ))
color1.draw( win )
color1.setWidth(0)


color2 = color1.clone()
color2.move( 66.6, 0 )
color2.draw( win )
color2.setFill( g.color_rgb( 0, 102, 0) )

color3 = color2.clone()
color3.move( 66.6, 0 )
color3.draw( win )
color3.setFill( g.color_rgb( 0, 128, 0 ) )

color4 = color3.clone()
color4.move( 66.6, 0 )
color4.draw( win )
color4.setFill( g.color_rgb( 0, 153, 0 ) )

color5 = color4.clone()
color5.move( 66.6, 0 )
color5.draw( win )
color5.setFill( g.color_rgb( 0, 204, 0 ) )


color6 = color5.clone()
color5.move(  66.6, 0 )
color6.draw( win )
color6.setFill( g.color_rgb( 0, 179, 0 ) )

# I had to change the color numbers for the last two
# colors, because they did not look right when placed
#in the sequential, numerical order.


