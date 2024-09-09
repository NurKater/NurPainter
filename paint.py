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
    print("Натисни 'C' щоб стерти все, 'R' щоб вибрати колір, 'O' щоб змінити розмір пензля.")


def load_background_image():
    filename = simpledialog.askstring("Input", "Введіть шлях до зображення:")
    if filename:
        screen.bgpic(filename)


def change_shape():
    shape = simpledialog.askstring("Input", "Введіть форму черепашки (например, 'turtle', 'circle', 'square'):")
    if shape:
        turtle.shape(shape)


def fill_shape():
    turtle.begin_fill()

    turtle.end_fill()


def change_speed():
    speed = simpledialog.askinteger("Input", "Введіть нову швидкість (від 1 до 10):", minvalue=1, maxvalue=10)
    if speed is not None:
        turtle.speed(speed)


def undo_last():
    turtle.undo()


def change_background():
    color = simpledialog.askstring("Input", "Новий колір фону?")
    if color:
        screen.bgcolor(color)


display_instructions()
turtle.onkeypress(change_background, 'b')
turtle.onkeypress(undo_last, 'u')
turtle.onkeypress(change_speed, 'v')
turtle.onkeypress(fill_shape, 'f')
turtle.onkeypress(change_shape, 'm')
turtle.onkeypress(load_background_image, 'l')
turtle.onkeypress(clear_screen, 'c')
turtle.onkeypress(change_color, 'r')
turtle.onkeypress(change_size, 'o')
turtle.onkeypress(move_right, 'd')
turtle.onkeypress(move_left, 'a')
turtle.onkeypress(move_forward, 'w')
turtle.onkeypress(move_backward, 's')
turtle.listen()


turtle.exitonclick()
