import turtle
import random

def stamp_walls_and_make_lists(n, m, num_walls, square_size):
    """
    Constructs the lists all_squares, free_squares,
    and wall_squares based on turtle (x,y) coordinates
    """
    global all_squares, free_squares, wall_squares, start_x, start_y
    # wall turtle stamper setup
    wall_stamper = turtle.clone()
    wall_stamper.shape("square")
    wall_stamper.color("gray")
    wall_stamper.hideturtle()
    wall_stamper.penup()
    # make the random wall coordinates
    start_x =  - (m * square_size) // 2
    start_y =  - (n * square_size) // 2
    # wall_coords = [(random.randint(0,n-1), random.randint(0,m-1)) for c in range(num_walls)]
    wall_coords = set() # to eliminate repeats
    while len(wall_coords) < num_walls: # to get exact number of walls
        random_pos = (random.randint(0,n-1), random.randint(0,m-1))
        wall_coords.add(random_pos)
    wall_coords = list(wall_coords) # easier way to deal with the coords
    # loop over all coordinates and construct the lists
    for r in range(n):
        for c in range(m):
            this_square = (start_x + (c * square_size), start_y + (r * square_size))
            if (r,c) in wall_coords: # if it's a wall
                wall_squares.append(this_square)
                wall_stamper.goto(this_square)
                wall_stamper.stamp()
            else: # it's a free square
                free_squares.append(this_square)
            all_squares.append(this_square)

def make_maze(n, m, num_walls, square_size, num_food):
    """
    Consists of two parts:
    1. Stamping the walls and making
        corresponding lists
    2. Drawing the grid
    """
    global x_list, y_list
    # stamp walls and make lists
    stamp_walls_and_make_lists(n, m, num_walls, square_size)
    # add food
    # make_food(num_food)
    # draw grid
    # make grid drawing turtle object
    grider = turtle.clone()
    grider.color("gray")
    grider.pensize(9)
    grider.hideturtle()
    grider.penup()
    # make the lists of x and y positions where the grid will be
    x_list = [x - (square_size // 2) for x in range(start_x, ((m)*square_size + start_x) + 1, square_size)]
    y_list = [y - (square_size // 2) for y in range(start_y, ((n)*square_size + start_y) + 1, square_size)]
    # draw the vertical grid lines
    for x in x_list:
        grider.goto(x,start_y - (square_size // 2))
        grider.pendown()
        grider.goto(x,y_list[-1])
        grider.penup()
    # draw the vertical grid lines
    for y in y_list:
        grider.goto(start_x - (square_size // 2), y)
        grider.pendown()
        grider.goto(x_list[-1],y)
        grider.penup()

def up():
    global direction
    direction = "up"
    move_player()

def down():
    global direction
    direction = "down"
    move_player()

def right():
    global direction
    direction = "right"
    move_player()

def left():
    global direction
    direction = "left"
    move_player()

def move_player():
    global all_squares, free_squares, wall_squares, x_list, y_list, direction, player, square_size, food_squares, food_stamps
    # check intended direction and maze boundaries
    new_pos = None
    if direction == "right" and player.pos()[0] <= x_list[-2]:
        new_pos = (player.pos()[0] + square_size, player.pos()[1])
    elif direction == "left" and player.pos()[0] >= x_list[1]:
        new_pos = (player.pos()[0] - square_size, player.pos()[1])
    elif direction == "up" and player.pos()[1] <= y_list[-2]:
        new_pos = (player.pos()[0], player.pos()[1] + square_size)
    elif direction == "down" and player.pos()[1] >= y_list[1]:
        new_pos = (player.pos()[0], player.pos()[1] - square_size)
    # make sure to move only onto free square
    if new_pos not in wall_squares:
        player.goto(new_pos)
        # if player eats food
        if new_pos in food_squares:
            food_index = food_squares.index(new_pos)
            food_squares.pop(food_index)
            food.clearstamp(food_stamps[food_index])
            food_stamps.pop(food_index)
            free_squares.append(new_pos)

def make_food(num_food):
    global all_squares, free_squares, wall_squares, food_squares, food_stamps, food, player
    food_squares = []
    food_stamps = []
    while len(food_squares) != num_food:
        # choose random free square position
        random_index = random.randint(0, len(free_squares) - 1)
        food_pos = free_squares[random_index]
        while food_pos == player.pos():
            random_index = random.randint(0, len(free_squares) - 1)
            food_pos = free_squares[random_index]
        # add to the food square position to food_squares
        food_squares.append(food_pos)
        # use the food object to stamp itself at the random position
        food.goto(food_pos)
        food_stamps.append(food.stamp())
        # remove food square position from free_squares
        free_squares.remove(food_pos)


# ---------------------------------------------------------------------------------

# welcome message
# print("Welcome! We'll be playing a maze game")
turtle.hideturtle()
turtle.tracer(1,0)

# init variables
# n = int(input("Enter maze height: "))
# m = int(input("Enter maze width: "))
# num_walls = int(input("Enter the number of walls: "))
square_size = 30
n = 5
m = 10
num_walls = (n*m) // 4
num_food = int(num_walls)
direction = None

# draw the maze
all_squares = []
free_squares = []
wall_squares = []
make_maze(n, m, num_walls, square_size, num_food)

# player turtle initialization
player = turtle.clone()
player.hideturtle()
player.penup()
player.shape("circle")
player.color("blue")

# food turtle initizalization
food = turtle.clone()
food.hideturtle()
food.penup()
food.shape("circle")
n = 0.7
food.turtlesize(n,n,n)
food.color("green")

# find first empty spot to put the player
player.goto(min(free_squares))
player.showturtle()

# onkeypress and listening
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.listen()
 
make_food(10)

turtle.mainloop()



