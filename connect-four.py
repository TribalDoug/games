import turtle
import time     # Imports required items for project
import random

# Collects the name of the person playing

global playername
playername=input('Who will be playing today? ')

# Sets up the screen for the game

screen = turtle.Screen()
screen.setup(800,700)       # Resizes the screen
draw = turtle.Turtle()
draw.hideturtle()           # Defines turtles to use in the project
stamp = turtle.Turtle()
stamp.hideturtle()

# Defines different colours for the project

outline = 'gray25'
red = 'salmon'
yellow = '#F4F186'
fill = 'gray50'
border = 'gray25'

# Runs a short intro scene

intro1 = turtle.Turtle()        # Creates turtles to use in the intro
intro1.hideturtle()
intro2 = turtle.Turtle()
intro2.hideturtle()

def intro():
    stamp.speed(0)
    stamp.up()
    stamp.shape('circle')           # Creates a red-token-like turtle
    stamp.shapesize(2.5,2.5,2)
    stamp.color('#CC252C',red)
    stamp.setpos(-150,-150)
    stamp.stamp()                   # This stamps tokens around the board
    stamp.setpos(-90,-210)
    stamp.stamp()
    stamp.setpos(200,175)
    stamp.stamp()
    stamp.color('#EFCC90', '#F4F186')   # And now it will stamp yellow tokens
    stamp.setpos(-200,175)
    stamp.stamp()
    stamp.setpos(100,-150)
    stamp.stamp()
    stamp.setpos(260,115)
    stamp.stamp()    
    
    draw.speed(0)
    draw.up()
    draw.color(border)          # This then writes Connect Four on the screen
    draw.fillcolor(fill)
    draw.setpos(-225,0)
    draw.write('C  nnect',font=('Berlin Sans FB Demi',90,'bold'))
    draw.setpos(-115,-100)
    draw.write('F  ur',font=('Berlin Sans FB Demi',90,'bold'))
    intro1.up()
    intro1.shape('circle')
    intro1.shapesize(2.75,2.75,2)
    intro1.color('#CC252C','salmon')
    intro2.up()
    intro2.shape('circle')
    intro2.shapesize(2.75,2.75,2)
    intro2.color('#EFCC90', '#F4F186')

    intro1.speed(0)
    intro1.setpos(-120,400) 
    intro1.showturtle()
    intro1.speed(4)
    
    intro1.setpos(-120,55)      # These create the bounce like animations
    intro1.speed(2)
    intro1.setpos(-120,150)
    intro1.speed(1)
    intro1.setpos(-120,200)     # It slows at the peak of the bounce
    intro1.setpos(-120,150)
    intro1.speed(2)
    intro1.setpos(-120,55)      # And then drops down quickly again
                                # This is the same for each little bounce section
    intro1.setpos(-120,100)
    intro1.speed(1)
    intro1.setpos(-120,150)
    intro1.setpos(-120,100)
    intro1.speed(2)
    intro1.setpos(-120,55)

    intro1.setpos(-120,60)
    intro1.speed(1)
    intro1.setpos(-120,100)
    intro1.setpos(-120,60)
    intro1.speed(2)
    intro1.setpos(-120,55)

    intro2.speed(0)             # An then this brings in the second token
    intro2.setpos(-19,400)  
    intro2.showturtle()
    intro2.speed(4)

    intro2.setpos(-19,-45)      # The bounce is the same as annotated above
    intro2.speed(2)
    intro2.setpos(-19,150)
    intro2.speed(1)
    intro2.setpos(-19,200)
    intro2.setpos(-19,150)
    intro2.speed(2)
    intro2.setpos(-19,-45)

    intro2.setpos(-19,100)
    intro2.speed(1)
    intro2.setpos(-19,150)
    intro2.setpos(-19,100)
    intro2.speed(2)
    intro2.setpos(-19,-45)

    intro2.setpos(-19,25)
    intro2.speed(1)
    intro2.setpos(-19,75)
    intro2.setpos(-19,25)
    intro2.speed(2)
    intro2.setpos(-19,-45)

    intro2.setpos(-19,-25)
    intro2.speed(1)
    intro2.setpos(-19,25)
    intro2.setpos(-19,-25)
    intro2.speed(2)
    intro2.setpos(-19,-45)
    
    time.sleep(3)
    
    draw.clear()            # This clears out all the intro parts
    intro1.hideturtle()
    intro2.hideturtle()
    stamp.clear()

# Draws an outline of the board

def drawboard():
    draw.up()
    draw.setpos(0,0)
    draw.forward(225)
    draw.left(90)
    draw.down()
    draw.color('#2E5984')
    draw.fillcolor('#528AAE')
    draw.pensize(3)
    draw.begin_fill()
    draw.forward(162.5)
    draw.circle(25,90)
    draw.forward(390)
    draw.circle(25,90)
    draw.forward(325)
    draw.circle(25,90)
    draw.forward(390)
    draw.circle(25,90)
    draw.forward(162.5)
    draw.end_fill()
    draw.up()
    draw.hideturtle()
    draw.setpos(0,0)
    draw.setheading(0)

# Draw a border around the screen

borders = turtle.Turtle()
borders.hideturtle()
borders.speed(0)

def addborder():
    borders.seth(0)
    borders.up()
    borders.pensize(3)
    borders.shape('circle')
    borders.color('#7EB786','white')
    borders.shapesize(1.5,1.5,3)
    borders.setpos(365,320)
    borders.stamp()
    borders.setpos(365,-320)
    borders.stamp()
    borders.setpos(-365,-320)
    borders.stamp()
    borders.setpos(-365,320)
    borders.stamp()
    borders.shapesize(0.5,0.5)
    borders.setpos(335,320)
    borders.stamp()
    borders.back(15)
    borders.down()
    borders.back(640)
    borders.up()
    borders.back(15)
    borders.stamp()
    borders.right(90)
    borders.setpos(-365,290)
    borders.stamp()
    borders.forward(15)
    borders.down()
    borders.forward(550)
    borders.up()
    borders.forward(15)
    borders.stamp()
    borders.left(90)
    borders.setpos(-335,-320)
    borders.stamp()
    borders.forward(15)
    borders.down()
    borders.forward(640)
    borders.up()
    borders.forward(15)
    borders.stamp()
    borders.left(90)
    borders.setpos(365,-290)
    borders.stamp()
    borders.forward(15)
    borders.down()
    borders.forward(550)
    borders.up()
    borders.forward(15)
    borders.stamp()

# Draw the profile pictures

def drawprofiles():
    global playername
    global redwins
    global yellowwins
        # Adds Computers Name and Picture
    draw.hideturtle()
    draw.up()
    draw.setpos(-140,235)
    draw.color(outline)
    draw.write('Computer',font=('Comfortaa',12,'bold'))
    draw.left(90)
    draw.back(1)
    draw.pensize(2)
    draw.setpos(-155,217)
    draw.down()
    draw.color('#CC252C')
    draw.fillcolor(red)
    draw.begin_fill()
    draw.circle(12.5,180)
    draw.up()
    draw.right(90)
    draw.back(25)
    draw.right(90)
    draw.circle(12.5,90)
    draw.down()
    draw.right(180)
    draw.circle(7.5,360)
    draw.end_fill()
    draw.up()
    draw.setpos(-150,217)
    draw.left(180)
    draw.down()
    draw.color(outline)
    for counter in range(4):
        draw.forward(35)
        draw.right(90)
    draw.hideturtle()
    stamp.shape('circle')
    stamp.shapesize(0.75,0.75)
    stamp.color('#CC252C',red)
    stamp.setpos(-130,224)
    stamp.seth(0)
    for i in range(int(redwins)):
        stamp.stamp()
        stamp.forward(20)   
    
        # Adds Players Name and Profile Picture
    draw.up()
    draw.setheading(0)
    draw.setpos(-140,-235)
    draw.color(outline)
    draw.write(playername,font=('Comfortaa',12,'bold'))
    draw.left(90)
    draw.pensize(2)
    draw.setpos(-155,-253)
    draw.down()
    draw.color('#EFCC90')
    draw.fillcolor(yellow)
    draw.begin_fill()
    draw.circle(12.5,180)
    draw.up()
    draw.right(90)
    draw.back(25)
    draw.right(90)
    draw.circle(12.5,90)
    draw.down()
    draw.right(180)
    draw.circle(7.5,360)
    draw.end_fill()
    draw.up()
    draw.setpos(-150,-253)
    draw.left(180)
    draw.down()
    draw.color(outline)
    draw.fillcolor('#9ADDFB')
    draw.begin_fill()
    for counter in range(4):
        draw.forward(35)
        draw.right(90)
        draw.end_fill()
    stamp.color('#EFCC90', yellow)
    stamp.setpos(-130,-246)
    stamp.seth(0)
    for i in range(int(yellowwins)):
        stamp.stamp()
        stamp.forward(20)

# Function that will draw a trophy when somebody wins the game

global linestart    # A variable which will drawn the winning line
global redwins
global yellowwins
redwins = 0
yellowwins = 0
linestart = 0
def winner(colour,outer,win):
    global linestart
    global redwins
    global yellowwins
    draw.up()
    col = int(linestart[1])-1
    row = int(linestart[0])-1
    y = -150+row*60             # Finds coordinates of the winning piece
    x = -175+col*60 
    draw.setpos(x,y)
    if linestart[2] == '1':     # Decides which direction to draw the line
        draw.seth(0)
        draw.back(5)
        length = 190
    elif linestart[2] == '2':
        draw.seth(90)
        draw.back(5)
        length = 190
    elif linestart[2] == '3':
        draw.seth(45)
        draw.back(5)
        length = 265
    elif linestart[2] == '4':
        draw.seth(315)
        draw.back(5)
        length = 265
    draw.down()
    draw.color('palegreen')
    draw.speed(2)
    draw.pensize(7.5)           # Draws the winning line
    draw.forward(length)
    time.sleep(3)
    draw.undo()
    for key in board.keys():
        board[key].hideturtle()     # Clears all the pieces when theres a win
    draw.clear()
    stamp.clear()
    borders.clear()
  # Sets up the turtle to begin drawing the tropy
    draw.speed(0)
    draw.up()
    draw.setpos(0,-150)
    draw.pensize(5)
    draw.color(outer)
    draw.fillcolor(colour)
    draw.seth(0)
    draw.down()
    draw.begin_fill()
  # Draws the first layer of the base
    draw.forward(75)
    draw.circle(10,90)
    draw.forward(10)
    draw.circle(10,90)
    draw.forward(150)
    draw.circle(10,90)
    draw.forward(10)
    draw.circle(10,90)
    draw.forward(75)
  # Moves the turtle to draw the next section
    draw.up()
    draw.end_fill()
    draw.forward(65)
    draw.left(90)
    draw.forward(30)
    draw.begin_fill()
    draw.down()
  # Draws the second layer of the base
    draw.left(15)
    draw.forward(45.13)
    draw.circle(10,75)
    draw.forward(87.32)
    draw.circle(10,75)
    draw.forward(45.13)
    draw.left(105)
    draw.forward(130)
  # Moves the turtle to draw the next section  
    draw.end_fill()
    draw.up()
    draw.back(65)
    draw.left(90)
    draw.forward(51)
    draw.left(90)
    draw.down()
    draw.begin_fill()
  # Moves the turtle to draw the first handle   
    draw.end_fill()
    draw.up()
    draw.right(90)
    draw.forward(285)
    draw.right(90)
    draw.forward(96.26)
    draw.right(180)
    draw.down()
    draw.begin_fill()
  # Draws the first handle
    draw.circle(65)
    draw.end_fill()
    draw.up()
    draw.fillcolor('white')
    draw.left(90)
    draw.forward(25)
    draw.right(90)
    draw.down()
    draw.begin_fill()
    draw.circle(40)
  # Moves to draw the second handle
    draw.end_fill()
    draw.up()
    draw.right(90)
    draw.forward(25)
    draw.left(90)
    draw.forward(192.52)
    draw.fillcolor(colour)
    draw.down()
    draw.begin_fill()
  # Draws the second handle
    draw.circle(65)
    draw.end_fill()
    draw.up()
    draw.fillcolor('white')
    draw.left(90)
    draw.forward(25)
    draw.right(90)
    draw.down()
    draw.begin_fill()
    draw.circle(40)
  # Moves to draw the next section
    draw.end_fill()
    draw.up()
    draw.seth(0)
    draw.forward(96.26)
    draw.right(90)
    draw.forward(260)
    draw.right(90)
    draw.down()
    draw.fillcolor(colour)
    draw.begin_fill()
  # Draws the stem and cup of the trophy  
    draw.forward(30)
    draw.right(90)
    draw.forward(75)
    draw.circle(40,45)
    draw.forward(15)
    draw.right(180)
    draw.circle(150,-45)
    draw.right(180)
    draw.forward(75)
    draw.circle(5,90)
    draw.right(180)
    draw.circle(5,-180)
    draw.right(180)
    draw.forward(202.52)
    draw.right(180)
    draw.circle(5,-180)
    draw.right(180)
    draw.circle(5,90)
    draw.forward(75)
    draw.right(180)
    draw.circle(150,-45)
    draw.right(180)
    draw.forward(15)
    draw.circle(40,45)
    draw.forward(75)
    draw.right(90)
    draw.forward(30)
    draw.end_fill()
    draw.up()
    draw.seth(0)
    draw.color('gray25')
    if win == 'r':              # Writes the winning (or losing) message
        draw.setpos(-175,25)
        draw.write('Oh No!',font=('Berlin Sans FB Demi',90,'bold'))
        draw.setpos(-175,-10)
        draw.write('Better luck next time',font=('Berlin Sans FB Demi',30,'bold'))
        redwins += 1
    else:
        draw.setpos(-225,25)
        draw.write('You Win!',font=('Berlin Sans FB Demi',90,'bold'))
        yellowwins += 1
    for key in board.keys():
        board[key] = 'blank'
    time.sleep(5)
    draw.clear()
    setup()

# Create turtles to act as the board circles

board={}    # Opens dictionary to store piece data

def addturtles():
    for row in range(6):
        for col in range(7):
            x = -175 + col * 60     # Finds turtles column
            y = -150 + row * 60     # Finds turtles row
            name=str(row+1)+str(col+1)      # Sets turtle names to position
            board[name]=turtle.Turtle()     # Add the turtle to the dictionary
            board[name].hideturtle()
            board[name].penup()
            board[name].speed(0)
            board[name].shape('circle')
            board[name].shapesize(2.5,2.5,2)    # Turns turtle into piece
            board[name].color('#2E5984','white')
            board[name].goto(x, y)
            board[name].showturtle()

# Find lowest free space in a column

def checklegalmove(column):
    global lowest, current
    lowest='99' 
    for key in board.keys():    # Checks through dictionary to find lowest ↧
        if int(key[1]) == int(column) and board[key].color()[1]=='white':
             current=key
             if int(current[0]) < int(lowest[0]):
                 lowest = current
    return lowest   # Returns lowest available column spot

# Check for a win condition

def checkwin():
    global linestart
    # Check horizontal
    for row in range(6):
        for col in range(4):
            position1 = str(row+1)+str(col+1)   # Gathers all column names
            position2 = str(row+1)+str(col+2)
            position3 = str(row+1)+str(col+3)
            position4 = str(row+1)+str(col+4)   # Compares to check for win ↧
            if (board[position1].color()[1] == board[position2].color()[1] == board[position3].color()[1] == board[position4].color()[1]) and (board[position1].color()[1] != 'white'):
                linestart = str(position1)+'1'
                return True
    # Check vertical
    for col in range(7):
        for row in range(3):
            position1 = str(row+1)+str(col+1)   # Gathers all column names
            position2 = str(row+2)+str(col+1)
            position3 = str(row+3)+str(col+1)
            position4 = str(row+4)+str(col+1)   # Compares to check for win ↧
            if (board[position1].color()[1] == board[position2].color()[1] == board[position3].color()[1] == board[position4].color()[1]) and (board[position1].color()[1] != 'white'):
                linestart = str(position1)+'2'
                return True
           
    # Check diagonal (down-right)
    for row in range(3):
        for col in range(4):
            position1 = str(row+1)+str(col+1)   # Gathers all column names
            position2 = str(row+2)+str(col+2)
            position3 = str(row+3)+str(col+3)
            position4 = str(row+4)+str(col+4)   # Compares to check for win ↧
            if (board[position1].color()[1] == board[position2].color()[1] == board[position3].color()[1] == board[position4].color()[1]) and (board[position1].color()[1] != 'white'):
                linestart = str(position1)+'3'
                return True
            
    # Check diagonal (up-right)
    for row in range(3,6):
        for col in range(4):
            position1 = str(row+1)+str(col+1)   # Gathers all column names
            position2 = str(row)+str(col+2)
            position3 = str(row-1)+str(col+3)
            position4 = str(row-2)+str(col+4)   # Compares to check for win ↧
            if (board[position1].color()[1] == board[position2].color()[1] == board[position3].color()[1] == board[position4].color()[1]) and (board[position1].color()[1] != 'white'):
                linestart = str(position1)+'4'
                return True

# Adds piece to the column which is clicked

def getcolumn(x, y):
    global iswinner
    global placement
    global previouscol
    global previouscombo
    if iswinner == False:
        col = int((x + 200) // 60) + 1  # Rounds to find nearest column
        if col > 0 and col < 8:         # Checks if it's in the boundary
            if y > -200 and y < 200:
                if col == previouscol:
                    setmove = True      # Check if opponent block needed
                    placement = previouscol
                    previouscombo = 0
                    previouscol = col
                elif col == previouscol + 1:
                    placement = previouscol + 2
                    setmove = True      # Check if opponent block needed
                    previouscombo = '2R'  # Registers to prevent loopholes
                    previouscol = col
                elif col == previouscol - 1:
                    placement = previouscol - 2
                    setmove = True      # Check if opponent block needed
                    previouscombo = '2L'  # Registers to prevent loopholes
                    previouscol = col
                elif col == previouscol - 2 and previouscombo == '2R':
                    placement = previouscol - 3
                    setmove = True      # Check if opponent block needed
                    previouscombo = 0  # Registers to prevent loopholes
                    previouscol = col
                elif col == previouscol + 2 and previouscombo == '2L':
                    placement = previouscol + 3
                    setmove = True      # Check if opponent block needed
                    previouscombo = 0  # Registers to prevent loopholes
                    previouscol = col
                else:
                    previouscol = col
                    setmove = 0
                    previouscombo = 0
                position = checklegalmove(col)  # Checks where to place the piece
                if position != '99':
                    board[position].color('#EFCC90','#F4F186')  # Places piece
                    if checkwin() == True:      # Checks for a winner
                        iswinner = True
                        winner('#F4F186','#EFCC90','y')
                    time.sleep(0.5)
                    if iswinner != True:    # Stops a glitch of drawing two trophies
                        computer(setmove, placement)   # The computer moves
    else:
        return
                
def computer(indicator, move):
    global placement
    global iswinner
    if indicator == True:    # Checks whether a block is needed
        column = move
    else:
        column = random.randint(1, 7)   # Picks a new column to place in
    position = checklegalmove(column)   # Checks if computer move is legal
    while position == '99':
        column = random.randint(1, 7)
        position = checklegalmove(column)
    board[position].color('#CC252C',red)  # places the piece
    if checkwin() == True:      # Checks for a win
        iswinner = True
        winner(red,'#CC252C','r')

# A function which sets up the board

global placement
global previouscol
global previouscombo
global iswinner
global setmove
def setup():
    global placement
    global previouscol
    global previouscombo
    global iswinner
    global setmove
    previouscol = 0
    placement = 0
    previouscombo = 0
    setmove = 0
    drawboard()     # Draws the board outline
    addborder()     # Draws the screen border
    drawprofiles()  # Draws the profile pictures
    addturtles()    # Add the game pieces
    iswinner = False        # Resets and reenables piece placement

# Begins and the runs the game

intro()
setup()
screen.onclick(getcolumn)   # Enables piece placement and starts game
turtle.done()
