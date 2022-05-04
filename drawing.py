from turtle import *
from random import *
import time
import json

players = input("Введите длину трассы(от 1 до 10): ")

turtle_1 = Turtle()
turtle_1.color("yellow")
turtle_1.shape("turtle")
turtle_1.penup()
turtle_1.goto(-100, 70)
turtle_1.pendown()

turtle_2 = Turtle()
turtle_2.color("red")
turtle_2.shape("turtle")
turtle_2.penup()
turtle_2.goto(-100, 10)
turtle_2.pendown()

def race():
    speed(-2)
    for race in range(100):
        turtle_1.forward(randint(1, 10))
        turtle_2.forward(randint(1, 10))

def lines(player):
    if player == "clear":
        clear_score()

    players = int(player)
    penup()
    speed(7)
    left(90)
    forward(100)
    left(90)
    forward(70)
    right(180)

    for _ in range(players):
        write(_ + 1, align="center")
        right(90)
        penup()
        forward(10)
        pendown()
        forward(200)
        penup()
        backward(210)
        left(90)
        forward(50)

def race_result():
    speed(1)
    win = 0
    if turtle_2.xcor() > turtle_1.xcor():
        penup()
        left(90)
        forward(150)
        left(90)
        forward(500)
        write("Жёлтая черепашка победила!")
        time.sleep(1)
        penup()
        right(90)
        forward(7)
        pendown()
        right(90)
        forward(160)
        penup()
        forward(10)
        right(90)
        forward(10)
        write("Красная черепашка победила")
        win = 1

    elif turtle_2.xcor() < turtle_1.xcor():
        penup()
        left(90)
        forward(150)
        left(90)
        forward(500)
        write("Красная черепашка победила!")
        time.sleep(1)
        penup()
        right(90)
        forward(7)
        pendown()
        right(90)
        forward(160)
        penup()
        forward(10)
        right(90)
        forward(10)
        write("Жёлтая черепашка победила")
        win = 0

def untouch():
    results = {"red": 0, "yellow": 0}
    return results

def main():
    lines(players)
    race()
    race_result()

if __name__ == '__main__':
    main()
    done()