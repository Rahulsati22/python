import turtle


# creating score variables
scoreA = 0
scoreB = 0


# creating screen for game
wn = turtle.Screen()
wn.title("Game by rahul sati")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# creating paddleA
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)


# creating paddleB
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)


# creating ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.fillcolor("green")
ball.penup()
ball.goto(0, 0)
x = 0.5
y = 0.5
# creating function when user will key up for paddle1


# creating score board
scoreBoard = turtle.Turtle()
scoreBoard.write("Player1 : 0  |  Player2 : 0", font=8)
scoreBoard.color('white')
scoreBoard.penup()
scoreBoard.goto(-80, 260)


def keyUp():
    if paddle1.ycor() <= 235:
        y = paddle1.ycor()
        paddle1.sety(y + 40)

# creating function when user will key down for paddle1


def keyDown():
    if paddle1.ycor() > -230:
        y = paddle1.ycor()
        paddle1.sety(y - 40)

# creating function when user will key up for paddle2


def keyUp2():
    if paddle2.ycor() <= 235:
        y = paddle2.ycor()
        paddle2.sety(y + 40)

# creating function when user will key down for paddle2


def keyDown2():
    if paddle2.ycor() > -230:
        y = paddle2.ycor()
        paddle2.sety(y - 40)


# listening the keyboard events
wn.listen()
wn.onkeypress(keyUp, "w")
wn.onkeypress(keyDown, "s")
wn.onkeypress(keyUp2, "Up")
wn.onkeypress(keyDown2, "Down")

# ball.goto(330,0)
# main game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + x)
    ball.sety(ball.ycor() + y)

    # checking the distance
    if ball.ycor() > 290:
        ball.sety(290)
        y *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        y *= -1

    if ball.xcor() > 390:
        scoreA += 1
        scoreBoard.clear()
        scoreBoard.write(f"PlayerA : {scoreA} | PlayerB : {scoreB}", font=8)
        scoreBoard.goto(-80, 260)
        ball.goto(0, 0)
        x *= -1

    if ball.xcor() < -390:
        scoreB += 1
        scoreBoard.clear()
        scoreBoard.write(f"PlayerA : {scoreA} | PlayerB : {scoreB}", font=(8))
        scoreBoard.goto(-80, 260)
        ball.goto(0, 0)
        x *= -1

    # paddle2 and ball collision
    if (ball.xcor() >= 325 and ball.xcor() <= 335) and (ball.ycor() <= paddle2.ycor() + 50 and ball.ycor() >= paddle2.ycor() - 50):
        x *= -1

    # paddle1 and ball collision
    if (ball.xcor() <= -325 and ball.xcor() >= -335) and (ball.ycor() <= paddle1.ycor() + 50 and ball.ycor() >= paddle1.ycor() - 50):
        x *= -1
