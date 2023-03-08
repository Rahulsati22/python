# importing three libraries
import time
import turtle
import random

# creating variables
delay = 0.1
score = 0
highScore = 0
segments = []

# creating window screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray')
screen.title('Snake Game By Rahul Sati')
screen.tracer(0)


# creating head of snake
headSnake = turtle.Turtle()
headSnake.shape('square')
headSnake.fillcolor('white')
headSnake.speed(0)
headSnake.penup()
headSnake.goto(0, 0)
headSnake.direction = "stop"

# creating snakeFood
food = turtle.Turtle()
food.shape('circle')
food.speed(0)
food.fillcolor('blue')
food.penup()
food.goto(210, 200)

# creating scoreBoard
scoreBoard = turtle.Turtle()
scoreBoard.shape('square')
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write(f'Score : 0 | HighScore : 250')
scoreBoard.speed(0)

# creating functions to go up down left and right
def moveUp():
    if headSnake.direction != 'down':
        headSnake.direction = 'up'


def moveDown():
    if headSnake.direction != 'up':
        headSnake.direction = 'down'


def moveLeft():
    if headSnake.direction != 'right':
        headSnake.direction = 'left'


def moveRight():
    if headSnake.direction != 'left':
        headSnake.direction = 'right'


# creating function to move
def move():
    if (headSnake.direction == 'up'):
        y = headSnake.ycor()
        headSnake.sety(y + 20)

    if (headSnake.direction == 'down'):
        y = headSnake.ycor()
        headSnake.sety(y - 20)

    if (headSnake.direction == 'left'):
        x = headSnake.xcor()
        headSnake.setx(x - 20)

    if (headSnake.direction == 'right'):
        x = headSnake.xcor()
        headSnake.setx(x + 20)


# writing code for event listening
screen.listen()
screen.onkeypress(moveUp, 'Up')
screen.onkeypress(moveDown, 'Down')
screen.onkeypress(moveLeft, 'Left')
screen.onkeypress(moveRight, 'Right')


# writing main Logic of the game
while True:
    screen.update()

    # when the snake is at the end of the screen
    if headSnake.xcor() > 290:
        headSnake.setx(-290)

    if headSnake.xcor() < -290:
        headSnake.setx(290)

    if headSnake.ycor() > 290:
        headSnake.sety(-290)

    if headSnake.ycor() < -290:
        headSnake.sety(290)

    # when snake eats food
    if headSnake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape('square')
        # newSegment.fillcolor('blue')
        newSegment.penup()
        newSegment.fillcolor('blue')
        segments.append(newSegment)
        delay -= 0.001
        score += 10
        if score > highScore:
            highScore = score
        scoreBoard.clear()
        scoreBoard.write(f"Score : {score} | HighScore : {highScore}")

    for indx in range(len(segments)-1, 0, -1):
        x = segments[indx-1].xcor()
        y = segments[indx-1].ycor()
        segments[indx].goto(x, y)

    if len(segments) > 0:
        x = headSnake.xcor()
        y = headSnake.ycor()
        segments[0].goto(x, y)

    move()
    for segment in segments:
        if (headSnake.distance(segment) < 20):
            time.sleep(1)
            headSnake.goto(0, 0)
            headSnake.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1
            scoreBoard.clear()
            scoreBoard.write("Score : {} High Score : {} ".format(
                score, highScore), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
wn.mainloop()
