
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random 

turtle.tracer(1,0) 
turtle.pu()
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 

SQUARE_SIZE = 20
START_LENGTH = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()


for i in range (START_LENGTH) :
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    

    x_pos+= SQUARE_SIZE

    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos) 
   

    pos_list.append(my_pos) 

    
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")
turtle.onkeypress(up, UP_ARROW)

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the left key!")
turtle.onkeypress(left, LEFT_ARROW)

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the down key!")
turtle.onkeypress(down, DOWN_ARROW)

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the right key!")
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    def move_snake():
        new_pos = snake.pos()
        new_x_pos = new_pos[0]
        new_y_pos = new_pos[1]
        if new_x_pos >= RIGHT_EDGE:
            print("You hit the right edge! Game over!")
            quit()

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP :
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print ("you moved up")
    elif direction==DOWN :
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print ("you moved down")

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
for this_food_pos in food_pos :
   
    
    ####WRITE YOUR CODE HERE!!



