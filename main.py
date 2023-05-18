
import turtle
import time
import random

pencere = turtle.Screen()
pencere.title("Yılan Oyunu")
pencere.bgcolor("black")
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("white")
kafa.penup()
kafa.goto(0, 100)
kafa.direction = "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()
yemek.goto(0, 0)

kuyruklar = []

skor = 0
skorTurtle = turtle.Turtle()
skorTurtle.speed(0)
skorTurtle.color("white")
skorTurtle.penup()
skorTurtle.hideturtle()
skorTurtle.goto(0, 260)
skorTurtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

hiz = 0.15

restartButton = turtle.Turtle()
restartButton.speed(0)
restartButton.color("white")
restartButton.penup()
restartButton.hideturtle()
restartButton.goto(200, 250)
restartButton.write("Restart (r)", align="center", font=("Courier", 16, "normal"))

quitButton = turtle.Turtle()
quitButton.speed(0)
quitButton.color("white")
quitButton.penup()
quitButton.hideturtle()
quitButton.goto(-200, 250)
quitButton.write("Quit (q)", align="center", font=("Courier", 16, "normal"))

buttons = [restartButton, quitButton]

def move():
    if kafa.direction == "up":
        y = kafa.ycor()
        kafa.sety(y + 20)

    if kafa.direction == "down":
        y = kafa.ycor()
        kafa.sety(y - 20)

    if kafa.direction == "right":
        x = kafa.xcor()
        kafa.setx(x + 20)

    if kafa.direction == "left":
        x = kafa.xcor()
        kafa.setx(x - 20)

def goUp():
    if kafa.direction != "down":
        kafa.direction = "up"

def goDown():
    if kafa.direction != "up":
        kafa.direction = "down"

def goRight():
    if kafa.direction != "left":
        kafa.direction = "right"

def goLeft():
    if kafa.direction != "right":
        kafa.direction = "left"

def clearKuyruklar():
    for kuyruk in kuyruklar:
        kuyruk.goto(1000, 1000)
    kuyruklar.clear()

def gameOver():
    kafa.direction = "stop"
    time.sleep(1)
    kafa.clear()
    yemek.clear()
    clearKuyruklar()
    skorTurtle.clear()
    skorTurtle.goto(0, 0)
    skorTurtle.write("Game Over", align="center", font=("Courier", 24, "normal"))
    time.sleep(2)
    skorTurtle.clear()
    skorTurtle.goto(0, 260)
    skorTurtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))
    kafa.goto(0, 100)
    yemek.goto(0, 0)
    kafa.direction = "stop"

def restartGame():
    for button in buttons:
        button.hideturtle()
    pencere.update()
    time.sleep(1)
    kafa.goto(0,100)
    kafa.direction = 'stop'
    yemek.goto(0,0)
    clearKuyruklar()
    kuyruklar.clear()
    kafa.clear()
    skorTurtle.clear()
    global skor
    skor = 0
    skorTurtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))
    hiz = 0.15

    restartButton.goto(200, 250)
    restartButton.write("Restart (r)", align="center", font=("Courier", 16, "normal"))
    quitButton.goto(-200, 250)
    quitButton.write("Quit (q)", align="center", font=("Courier", 16, "normal"))

def quitGame():
    pencere.bye()

restartButton.goto(200, 250)
restartButton.clear()
quitButton.goto(-200, 250)
quitButton.clear()

pencere.listen()
pencere.onkeypress(goUp, "Up")
pencere.onkeypress(goDown, "Down")
pencere.onkeypress(goRight, "Right")
pencere.onkeypress(goLeft, "Left")
pencere.onkeypress(restartGame, "r")
pencere.onkeypress(quitGame, "q")

while True:
    pencere.update()

    if kafa.xcor()>290 or kafa.xcor()<-290 or kafa.ycor()>290 or kafa.ycor()<-290:
        gameOver()

    if kafa.distance(yemek) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yemek.goto(x, y)

        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("square")
        yeniKuyruk.color("grey")
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

        skor += 10
        if skor > 50:
            hiz = 0.1
        if skor > 100:
            hiz = 0.05
        skorTurtle.clear()
        skorTurtle.write("Skor: {}".format(skor), align="center", font=("Courier", 24, "normal"))

    for index in range(len(kuyruklar)-1, 0, -1):
        x = kuyruklar[index-1].xcor()
        y = kuyruklar[index-1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()

    for segment in kuyruklar:
        if segment.distance(kafa) < 20:
            gameOver()

    time.sleep(hiz)
