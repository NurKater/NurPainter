import turtle
from turtle import *
from tkinter import simpledialog, Tk


root = Tk()
root.withdraw()


for ko in ("NurKater"):
    print(ko * 226)


pensize(10)
pencolor("red")


screen = turtle.Screen()
screen.title("Paint")


def clear_screen():
    turtle.clear()


def change_color():
    color = simpledialog.askstring("Input", "Новий колір?:")
    if color:
        turtle.pencolor(color)


def change_size():
    size = simpledialog.askinteger("Input", "Enter new pen size:", minvalue=1, maxvalue=50)
    if size is not None:
        turtle.pensize(size)


def move_right():
    turtle.right(1)


def move_left():
    turtle.left(1)


def move_forward():
    turtle.forward(1)


def move_backward():
    turtle.backward(1)


def display_instructions():
    print("Використай 'W' щоб рухатись вперед, 'S' для руху назад, 'A' щоб повернути вліво, 'D' щоб повернути вправо")
    print(
        "Натисни 'C' щоб стерти все, 'R' щоб вибрати колір, 'O' щоб змінити розмір пензля.")


display_instructions()
turtle.onkeypress(clear_screen, 'c')
turtle.onkeypress(change_color, 'r')
turtle.onkeypress(change_size, 'o')
turtle.onkeypress(move_right, 'd')
turtle.onkeypress(move_left, 'a')
turtle.onkeypress(move_forward, 'w')
turtle.onkeypress(move_backward, 's')
turtle.listen()


turtle.exitonclick()
