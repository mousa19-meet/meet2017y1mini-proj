import turtle
import random
import time

turtle.tracer(1,0)
score = 0
size_x = 800
size_y = 500
turtle.setup(size_x,size_y)

turtle.penup()

square_size = 20
start_len = 10

pos_list =[]
stamp_list = []
food_pos = []
food_stamp = []
score_list = []

snake = turtle.clone()
snake.shape('square')

turtle.hideturtle()

for s in range(start_len):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos+= square_size

    my_pos = (x_pos , y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)

    stamp_me = snake.stamp()
    stamp_list.append(stamp_me)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW ="Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR ="space"
UP = 0
LEFT = 2
DOWN = 1
RIGHT = 3
direction = UP
up_edge = 250
down_edge = -250
right_edge = 400
left_edge = -400

def up_1():
    global direction
    direction = UP
    print('up key')
def down_1():
    global direction
    direction = DOWN
    print('down key')
def left_1():
    global direction
    direction = LEFT
    print('left key')
def right_1():
    global direction
    direction = RIGHT
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
        print('move right')
    elif direction ==LEFT:
        snake.goto(x_pos - square_size,y_pos)
        print('move left')
    elif direction == UP:
        snake.goto(x_pos,y_pos + square_size)
        print('move up')
    elif direction == DOWN:
        snake.goto(x_pos, y_pos - square_size)
        print('move down')
        
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
        print('you hit the right edge , GAME OVER!')
        quit()
    elif new_xpos <= left_edge:
        print('you hit the left edge , GAME OVER!')
        quit()
    elif new_ypos >= up_edge:
        print('you hit the up edge, GAME OVER!')
        quit()
    elif new_ypos <= down_edge:
        print('you hit the down edge , GAME OVER!')
        quit()

    if pos_list[-1] in pos_list[0:-1]:
        print("You ate yourself")
        quit()
        
    global food_stamps,fod_pos,score, score_list
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you ate food')
        make_food()
        stamp_list.append(stamp_me)
        
        
        score = score + 1
        score_list.append(score)
        turtle.write("score : "+ str(score))
        #turtle.clear()

    
        
     
    turtle.ontimer(move_snake,TIME_STEP)
    
    
    
food = turtle.clone()
food.shape('turtle')

food_pos = []
food_stamps = []


def make_food():
    
    min_x =-int(size_x/2/square_size)+1
    max_x =int(size_x/2/square_size)-1
    min_y=-int(size_y/2/square_size)-1
    max_y=int(size_y/2/square_size)+1

    food_x = random.randint(min_x,max_x)*square_size
    food_y = random.randint(min_y,max_y)*square_size
    food_tup=(food_x, food_y)
    food_pos.append(food_tup)
    food.goto(food_x,food_y)

    food_stamp1 = food.stamp()
    food_stamps.append(food_stamp1)
     
make_food()
move_snake()
