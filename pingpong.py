import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Pad A
pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("white")
pad_1.shapesize(stretch_wid=5, stretch_len=1)
pad_1.penup()
pad_1.goto(-350, 0)

# Paddle B
pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.color("white")
pad_2.shapesize(stretch_wid=5, stretch_len=1)
pad_2.penup()
pad_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball Speed
ball.dx = 3
ball.dy = 3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions for movement of pads
def pad_1_up():
    y = pad_1.ycor()
    y += 20
    pad_1.sety(y)


def pad_1_down():
    y = pad_1.ycor()
    y -= 20
    pad_1.sety(y)


def pad_2_up():
    y = pad_2.ycor()
    y += 20
    pad_2.sety(y)


def pad_2_down():
    y = pad_2.ycor()
    y -= 20
    pad_2.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(pad_1_up, "w")
wn.onkeypress(pad_1_down, "s")
wn.onkeypress(pad_2_up, "Up")
wn.onkeypress(pad_2_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Checking game window

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < pad_1.ycor() + 50 and ball.ycor() > pad_1.ycor() - 50:
        ball.dx *= -1


    elif ball.xcor() > 340 and ball.ycor() < pad_2.ycor() + 50 and ball.ycor() > pad_2.ycor() - 50:
        ball.dx *= -1


