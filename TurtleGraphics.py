#TurtleGraphics.py
#Name:Jadon Wiebe
#Date:9/21/2025
#Assignment:Turtle Graphics

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    
tim = turtle.Turtle()
tim.up()
tim.goto(-150,175)
tim.down()
for i in range(5):
    tim.forward(50)
    tim.right(72)
tim.up()
tim.forward(125)
tim.down()
for i in range(8):
    tim.forward(35)
    tim.right(45)

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    
tim.up()
tim.forward(100)
tim.down()
for i in range(4):
    tim.forward(80)
    tim.right(90)
tim.up()
tim.forward(40)
tim.down()
tim.fillcolor("blue")
tim.begin_fill()
for i in range(4):
    tim.forward(40)
    tim.right(90)
tim.end_fill()

tim.up()
tim.goto(75,0)
tim.down()
tim.left(90)
for i in range(4):
    tim.forward(80)
    tim.right(90)
tim.fillcolor("red")
tim.up()

tim.down()
tim.begin_fill()
for i in range(4):
    tim.forward(40)
    tim.right(90)
tim.end_fill()

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    
tim.up()
tim.goto(-150,-40)
tim.down()
for i in range(4):
    tim.forward(100)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(70)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(40)
    tim.right(90)
    
tim.up()
tim.goto(0,-150)
tim.down()
for i in range(4):
    tim.forward(140)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(110)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(80)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(50)
    tim.right(90)
tim.up()
tim.right(45)
tim.forward(20)
tim.left(45)
tim.down()
for i in range(4):
    tim.forward(20)
    tim.right(90)

main()
