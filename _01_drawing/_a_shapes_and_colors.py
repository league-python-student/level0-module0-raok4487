import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('red')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    myTurtle = turtle.Turtle()
    
    # Make your turtle's shape 'turtle', .shape('turtle')
    myTurtle.shape('turtle')
    # Set your turtle's speed using .speed(2)
    myTurtle.speed(10)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    myTurtle.color('green')
    # Move your turtle forward using .forward(100)
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(90)
    myTurtle.left(90)
    myTurtle.forward(100)
    myTurtle.left(90)
    myTurtle.forward(100)
    # TEST    Did your turtle move forward?
    myTurtle.pencolor('blue')
    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.

    # TEST    Did your turtle draw a square?
    myTurtle.width(width=10)
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
