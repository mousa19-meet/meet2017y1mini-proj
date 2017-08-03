import turtle
import random
import time

#variables
turtle.tracer(1,0)
score = 0
size_x = 800
size_y = 500
turtle.setup(size_x,size_y)
turtle.penup()
square_size = 20
start_len = 11
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW ="Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR ="space"
time_o= 5000
UP = 0
LEFT = 2
DOWN = 1
RIGHT = 3
direction = UP
up_edge = 250
down_edge = -250
right_edge = 400
left_edge = -400

#lists
food_score_list = []
pos_list =[]
stamp_list = []
food_pos = []
food_stamp = []
score_list = []
high_score = []

#make the box
"""
box = turtle.clone()
box.color('blue')
box.hideturtle()
box.penup()
box.goto(left_edge,up_edge)
box.pendown()
box.goto(right_edge,up_edge)
box.goto(right_edge,down_edge)
box.goto(left_edge,down_edge)
box.goto(left_edge,up_edge)
box.penup()
"""
#'snake' options
snake = turtle.clone()
snake.shape('turtle')
snake.color('green')

turtle.hideturtle()

#stamping the snake so it can be visable
for s in range(start_len):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]
    x_pos+= square_size
    my_pos = (x_pos , y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_me = snake.stamp()
    stamp_list.append(stamp_me)

#direction functions
def up_1():
    global direction
    if direction != DOWN: #this doesnt let the user click down
        direction = UP     #if going up
    print('up key')
def down_1():
    global direction
    if direction != UP:  #this doesnt let the user click up
        direction = DOWN  #if going down
    print('down key')
def left_1():
    global direction
    if direction != RIGHT: #this doesnt let the user click right    
        direction = LEFT    #if going left
    print('left key')
def right_1():
    global direction
    if direction != LEFT:   #this doesnt let the user click left
        direction = RIGHT    #if going right
    print('right key')

turtle.onkeypress(up_1,UP_ARROW)
turtle.onkeypress(down_1,DOWN_ARROW)
turtle.onkeypress(right_1,RIGHT_ARROW) 
turtle.onkeypress(left_1,LEFT_ARROW)
turtle.listen()
    

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + square_size, y_pos)
    elif direction ==LEFT:
        snake.goto(x_pos - square_size,y_pos)
    elif direction == UP:
        snake.goto(x_pos,y_pos + square_size)
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - square_size)
        
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_xpos = new_pos[0]
    new_ypos = new_pos[1]

    if new_xpos >= right_edge:
        turtle.write('You hit the right edge , GAME OVER!',align="center", font=("Arial", 30, "normal"))
        time.sleep(1.5)
        quit()
    elif new_xpos <= left_edge:
        turtle.write('You hit the left edge , GAME OVER!',align="center", font=("Arial", 30, "normal"))
        time.sleep(1.5)
        quit()
    elif new_ypos >= up_edge:
        turtle.write('You hit the up edge, GAME OVER!',align="center", font=("Arial", 30, "normal"))
        time.sleep(1.5)
        quit()
    elif new_ypos <= down_edge:
        turtle.write('You hit the down edge , GAME OVER!',align="center", font=("Arial", 30, "normal"))
        time.sleep(1.5)
        quit()

    if pos_list[-1] in pos_list[0:-1]:
        turtle.write('YOU ATE YOURSELF! WAIT !!',align="center", font=("Arial", 30, "normal"))
        time.sleep(2.5)
        
    global food_stamps,fod_pos,score, score_list,food_score,food_score_list
    if snake.pos() in food_pos:
        
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you ate food')
        make_food()
        stamp_list.append(stamp_me)

        #the score display
        score = score + 1
        score_list.append(score)
        turtle.clear()
        turtle.write("SCORE : "+ str(score),align="center",font=("Arial", 15, "normal"))
          
    turtle.ontimer(move_snake,TIME_STEP)
    
#get the shape of the skull as food
turtle.register_shape('skull.gif')
food = turtle.clone()
food.shape('skull.gif')


food_pos = []
food_stamps = []


def make_food():
    global food_pos,pos_list
    min_x =-int(size_x/2.5/square_size)+1
    max_x =int(size_x/2.5/square_size)-1
    min_y=-int(size_y/2.5/square_size)-1
    max_y=int(size_y/2.5/square_size)+1

    food_x = random.randint(min_x,max_x)*square_size 
    food_y = random.randint(min_y,max_y)*square_size
    
    food_tup=(food_x, food_y)
    food_pos.append(food_tup)
    food.goto(food_x,food_y)

    food_stamp1 = food.stamp()
    food_stamps.append(food_stamp1)
make_food()
move_snake()
