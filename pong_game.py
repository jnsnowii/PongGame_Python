import turtle
import os

wn = turtle.Screen()                # call screen window
wn.title("Pong by @JnSnowii")       # title name
wn.bgcolor("black")                 # bg color
wn.setup(width=800, height=600)     # size of win
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)                   # speed for animation
paddle_a.shape("square")            # shape of paddle
paddle_a.color("white")             # color of paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    # size shape pix
paddle_a.penup()                    # turtle draw a line and we don't want to have line
paddle_a.goto(-350, 0)              # paddle start position (x corner)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2                     # d:delta/change, x speed
ball.dy = -2                     # d:delta/change, y speed 

# Pen / Turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0    |    Player B : 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()         # ycor = turtle module return y coordinate
    y += 20                     # y = y + 20
    paddle_a.sety(y)            # set y to new y (update pos)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")     # press 'w' go up
wn.onkeypress(paddle_a_down, "s")   # press 's' go down
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()                 # Always update on the screen

    # Exit game
    

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:       # screen 800x600, centerToTop(y): 0 - 300
        ball.sety(290)
        ball.dy *= -1           # bounce ball
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:      # screen 800x600, centerToDown(-y): 0 - -300
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)         # set new pos of ball to center 
        ball.dx *= -1
        score_a += 1
        pen.clear()             # clear old text
        pen.write("Player A : {}    |    Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}    |    Player B : {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
