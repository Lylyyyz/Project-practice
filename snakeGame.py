# This program implements the classic Snake Game using Python's turtle module.
# It draws the game board, the snake, and the artifacts that allow the snake to grow.
#
#                   === Rules ===
#
# 1. If the snake eats an artifact, it grows by one unit.
# 2. If the snake hits the edge of the game board, it dies.
# 3. If the snake's head collides with its own body, it dies.


import turtle as t 
import time
import random


# ================= Global variables ===================

delay = 0.1             # Delay between each move of the head

window = t.Screen()

game_running = True     #  variable is true until head meets snake's body => game stop running

score = 0


# ====================== Functions ======================

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def generateRandomFood():
    x = random.randint(-230, 230)
    y = random.randint(-230, 230)
    food.goto(x, y)

def hide_food_temporarily():
    food.goto(1000, 1000)                       # Hide food
    window.ontimer(generateRandomFood, 1500)    # Generate new food + makes it apear after 2 seconds


# Makes Sake grow by adding a new segment 
def growingSnake():
    new_segment = t.Turtle()
    new_segment.color("gold")      
    new_segment.shape("square")
    new_segment.speed(0)           
    new_segment.up()
    segments.append(new_segment)


def game_Over():
    time.sleep(0.3)
    message = t.Turtle()
    message.hideturtle()
    message.fillcolor("white")
    message.speed(0)
    message.up()
    message.back(125)
    message.down()

    message.begin_fill()
    
    # Upper-left border
    for i in range(3):
        message.left(90)
        message.fd(15)
        message.right(90)
        message.fd(15)
    
    # Top side
    message.fd(160)
    
    # Upper-right border
    for i in range(3):
        message.fd(15)
        message.right(90)
        message.fd(15)
        message.left(90)
    message.right(90)
    
    # Lower-right border
    for i in range(3):
        message.fd(15)
        message.right(90)
        message.fd(15)
        message.left(90)
    message.right(90)
    
    # Bottom side
    message.fd(160)

    # Lower-left border
    for i in range(3):
        message.fd(15)
        message.right(90)
        message.fd(15)
        message.left(90)
    
    message.end_fill()
    
    # Positionning turtle to write "Game Over"
    message.right(180)
    message.up()
    message.fd(125)
    message.right(90)
    message.fd(15)
    message.down()
    message.write("Game Over", align="center", font=("Arial", 20, "bold"))


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 15)


def writeScore():
    pen.clear()  # clear previous score
    pen.write(f"Score : {score}", align="center", font=("Arial", 15, "normal"))


# ====================== Set screen ======================

window.title("Snake Game par Lyna following a tutorial so meme pas par elle quand meme") # mon ego a mal mais that's true so je laisse
                                                                                         # ça comme ça
window.bgcolor("gray10")
window.setup(500, 500)
window.tracer(0)        # Run off animation (draw in hidden mode) to fasten drawings 
                        # wait for window.update to show drawing


# ====================== Create head ======================

head = t.Turtle()
head.color("goldenrod")      # link for turtle colors: https://cs111.wellesley.edu/labs/lab02/colors
head.shape("square")
head.speed(0)           # define head speed (0 = speedest / 10 = slowest)
head.up()
head.goto(0,0)          # head starts in the middle of screen anyway but it is good practice to add this line
head.direction = "stop"


# ====================== Initiate body ======================

segments = []      

# ====================== Snake food ======================

food = t.Turtle()
food.color("firebrick1")      
food.shape("circle")
food.speed(0)           
food.up()
generateRandomFood()


# ====================== Write score ======================

pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.ht()
pen.up()
pen.goto(0, 220)
writeScore()


# ====================== Keyword bindings ======================

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")


# ====================== Main game loop ======================

while game_running:
    window.update()

    move()

    # Check for a collision with the border
    if abs(head.xcor()) > 240 or abs(head.ycor()) > 240:
        game_Over()
        break                       # Sortie de la boucle principale

    for segment in segments:
        if segment.distance(head) < 20:
            game_Over()
            game_running = False
            break                   # Sortie de la boucle principale

    # Check for a collision between snake and food
    if head.distance(food) < 20:    # The radius of a basic shape in turtle is 10, so when the head meets the food,
                                    # there's a gap of 20 between them
        score += 1
        writeScore()
        delay -= 0.002              # Decreasing the delay as the score increases to add some challenge to the game
        growingSnake()
        hide_food_temporarily()     # If snake eat food, food disapear 2 sec then reappear in a new random place

    # Position of each segment of the snake body at every loop
    if len(segments) > 0:
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)
        x = head.xcor()
        y = head.ycor()
        if head.direction == "up":
            segments[0].goto(x , y - 15)
        if head.direction == "down":
            segments[0].goto(x, y + 15)
        if head.direction == "right":
            segments[0].goto(x - 15, y)
        if head.direction == "left":
            segments[0].goto(x + 15, y)
        
    time.sleep(delay)               # Head waits for time set in delay variable

t.done()