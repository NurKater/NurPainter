import turtle

# Настройка екрану Turtle
screen = turtle.Screen()
screen.title("Paint")

# Настройка пера
turtle.pensize(10)
turtle.pencolor("red")

# Функція для очистки екрану
def clear_screen():
    turtle.clear()

# Функція для зміни кольору
def change_color():
    color = screen.textinput("Колір", "Введіть новий колір:")
    if color:
        turtle.pencolor(color)

# Функція для зміни розміру пензля
def change_size():
    size = screen.numinput("Розмір пензля", "Введіть новий розмір пензля:", minval=1, maxval=50)
    if size is not None:
        turtle.pensize(size)

# Функції для управління фоном
def change_background():
    color = screen.textinput("Фон", "Введіть новий колір фону:")
    if color:
        screen.bgcolor(color)

def load_background_image():
    filename = screen.textinput("Фон", "Введіть шлях до зображення:")
    if filename:
        try:
            screen.clear()  # Очистить старый фон
            screen.bgpic(filename)
        except turtle.TurtleGraphicsError:
            print("Не вдалося завантажити зображення. Перевірте шлях до файлу.")


# Функції для управління черепашкою
def move_right():
    turtle.setheading(0)  # Установлюємо напрямок вправо
    turtle.forward(10)    # Рухаємось вперед

def move_left():
    turtle.setheading(180)  # Установлюємо напрямок вліво
    turtle.forward(10)     # Рухаємось вперед

def move_forward():
    turtle.setheading(90)  # Установлюємо напрямок вверх
    turtle.forward(10)    # Рухаємось вперед

def move_backward():
    turtle.setheading(270)  # Установлюємо напрямок вниз
    turtle.forward(10)     # Рухаємось вперед

def change_shape():
    shape = screen.textinput("Форма", "Введіть форму черепашки (наприклад, 'turtle', 'circle', 'square'):")
    if shape:
        turtle.shape(shape)

def undo_last():
    turtle.undo()

# Інструкції
def display_instructions():
    print("Використовуйте 'W' щоб рухатись вперед, 'S' для руху назад, 'A' щоб повернути вліво, 'D' щоб повернути вправо")
    print("Натисніть 'C' щоб стерти все, 'R' щоб вибрати колір, 'O' щоб змінити розмір пензля.")
    print("Натисніть 'B' щоб змінити колір фону, 'L' щоб завантажити зображення фону.")
    print("Натисніть 'M' щоб змінити форму черепашки.")
    print("Натисніть 'U' щоб скасувати останню дію.")

# Відображення інструкцій
display_instructions()

# Налаштування управління

turtle.onkeypress(clear_screen, 'c')
turtle.onkeypress(change_color, 'r')
turtle.onkeypress(change_size, 'o')
turtle.onkeypress(change_background, 'b')
turtle.onkeypress(load_background_image, 'l')
turtle.onkeypress(change_shape, 'm')
turtle.onkeypress(undo_last, 'u')
turtle.onkeypress(move_right, 'd')
turtle.onkeypress(move_left, 'a')
turtle.onkeypress(move_forward, 'w')
turtle.onkeypress(move_backward, 's')
turtle.listen()
# Очікування закриття вікна по кліку
screen.mainloop()
