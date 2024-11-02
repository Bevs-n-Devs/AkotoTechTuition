import random, turtle

# Set up the game screen
myscreen = turtle.Screen()
myscreen.bgcolor('light blue')  # Background color of the screen
myscreen.setup(1.0, 1.0)  # Full-screen setup
myscreen.title('Turtle Race Game')  # Title of the game window

# Initialize the pen to draw the race track
pen = turtle.Turtle()
pen.speed(0)  # Set pen speed to the fastest
pen.penup()  # Lift the pen up to avoid drawing while moving
pen.goto(-200, 200)  # Position the pen at the starting point for the track
pen.pendown()  # Lower the pen to start drawing

# Draw race track lines and labels
for i in range(1, 11):  # Loop to create 10 lines
    pen.write(i, font=('Arial', 10))  # Label each line with a number
    pen.setheading(-90)  # Point the pen downwards
    pen.forward(250)  # Draw the line downwards for 250 pixels
    if i == 10:  # If it's the last line
        pen.write(" FINISH", font=('Arial', 14))  # Write "FINISH" at the end
    pen.back(250)  # Move the pen back to starting point of line
    pen.penup()  # Lift the pen to avoid drawing while repositioning
    pen.setheading(0)  # Point the pen to the right
    pen.forward(50)  # Move the pen to the right for the next line
    pen.down()  # Lower the pen to start drawing again

# Define the finish line position on the x-axis
finishLineX = 250

# Function to create a turtle player with given color and position
def createTurtlePlayer(color, startx, starty):
    player = turtle.Turtle()
    player.color(color)  # Set turtle color
    player.shape("turtle")  # Set turtle shape
    player.penup()  # Lift pen to avoid drawing while moving to starting position
    player.goto(startx, starty)  # Place turtle at the specified starting position
    player.pendown()  # Lower pen in case we want to draw its movement path
    return player  # Return the player object for later use

# Create four turtle players with different colors and starting positions
p1 = createTurtlePlayer('red', -210, 150)  # Red turtle, positioned at line 1
p2 = createTurtlePlayer('blue', -210, 100)  # Blue turtle, positioned at line 2
p3 = createTurtlePlayer('orange', -210, 50)  # Orange turtle, positioned at line 3
p4 = createTurtlePlayer('green', -210, 0)  # Green turtle, positioned at line 4

# Main loop to move turtles randomly until one reaches the finish line
while True:
    # Move red turtle by a random amount and check if it has reached the finish line
    p1.forward(random.randint(5, 10))
    if p1.pos()[0] >= finishLineX:  # Check if red turtle reached or crossed finish line
        p1.write(' I won the race!!', font=('Arial', 30))  # Announce winner
        break  # Exit the loop if red turtle wins

    # Move blue turtle by a random amount and check if it has reached the finish line
    p2.forward(random.randint(5, 10))
    if p2.pos()[0] >= finishLineX:  # Check if blue turtle reached or crossed finish line
        p2.write(' I won the race!!', font=('Arial', 30))  # Announce winner
        break  # Exit the loop if blue turtle wins

    # Move orange turtle by a random amount and check if it has reached the finish line
    p3.forward(random.randint(5, 10))
    if p3.pos()[0] >= finishLineX:  # Check if orange turtle reached or crossed finish line
        p3.write(' I won the race!!', font=('Arial', 30))  # Announce winner
        break  # Exit the loop if orange turtle wins

    # Move green turtle by a random amount and check if it has reached the finish line
    p4.forward(random.randint(5, 10))
    if p4.pos()[0] >= finishLineX:  # Check if green turtle reached or crossed finish line
        p4.write(' I won the race!!', font=('Arial', 30))  # Announce winner
        break  # Exit the loop if green turtle wins

# End the turtle graphics session
turtle.done()
