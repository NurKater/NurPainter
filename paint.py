import customtkinter
from customtkinter import *
from PIL import Image, ImageDraw
from random import randint
from tkinter import colorchooser, messagebox, Menu

# История для undo/redo
history = []
redo_stack = []

def save_state():
    global history
    history.append(image1.copy())

def undo():
    global history, redo_stack
    if history:
        redo_stack.append(image1.copy())
        last_state = history.pop()
        canvas.delete('all')
        img = last_state
        draw_img = ImageDraw.Draw(img)
        canvas_image.paste(img)

def redo():
    global redo_stack
    if redo_stack:
        save_state()
        next_state = redo_stack.pop()
        canvas.delete('all')
        img = next_state
        draw_img = ImageDraw.Draw(img)
        canvas_image.paste(img)

# Режимы рисования
drawing_mode = 'brush'

def change_mode(mode):
    global drawing_mode
    drawing_mode = mode

def draw(event):
    global drawing_mode
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    if drawing_mode == 'brush':
        canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
        draw_img.ellipse((x1, y1, x2, y2), fill=color)
    elif drawing_mode == 'line':
        canvas.create_line(x1, y1, x2, y2, fill=color, width=brush_size)
        draw_img.line((x1, y1, x2, y2), fill=color, width=brush_size)

def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    if hx:
        color = hx
        color_lab.configure(fg_color=color)

def pour():
    save_state()
    canvas.delete('all')
    canvas.configure(bg=color)
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)

def clear_canvas():
    save_state()
    canvas.delete('all')
    canvas.configure(bg='white')
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill='white')

def save_img():
    filename = f'image_{randint(0, 10000)}.png'
    image1.save(filename)
    messagebox.showinfo('Сохранение', f'Сохранено под названием {filename}')

def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)

def square():
    save_state()
    canvas.create_rectangle(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.rectangle((x, y, x + brush_size, y + brush_size), fill=color)

def circle():
    save_state()
    canvas.create_oval(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill=color)

def select(val):
    global brush_size
    brush_size = int(val)

x = 0
y = 0

root = CTk()
root.title("Paint")
root.geometry('1280x720')

brush_size = 10
color = 'red'

root.columnconfigure(6, weight=1)
root.rowconfigure(2, weight=1)

canvas = customtkinter.CTkCanvas(root, bg='white', width=1280, height=720)
canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

# Загрузка изображения для рисования
image1 = Image.new('RGB', (1280, 720), 'white')
draw_img = ImageDraw.Draw(image1)
canvas_image = Image.new("RGB", (1280, 720), "white")

# Контекстное меню для выбора фигуры
menu = Menu(root, tearoff=0)
menu.add_command(label="Квадрат", command=square)
menu.add_command(label="Круг", command=circle)

canvas.bind('<B1-Motion>', draw)
canvas.bind("<Button-3>", popup)

# Панель инструментов
tool_bar = customtkinter.CTkFrame(root)
tool_bar.grid(row=0, column=0, columnspan=7, sticky="nsew")

# Кнопка для выбора цвета
customtkinter.CTkButton(tool_bar, text='Выбрать цвет', command=chooseColor).grid(row=0, column=0, padx=6)

color_lab = customtkinter.CTkLabel(tool_bar, text='', width=10, fg_color=color)
color_lab.grid(row=0, column=1, padx=6)

# Слайдер для выбора размера кисти
brush_slider = customtkinter.CTkSlider(tool_bar, from_=1, to=100, command=select)
brush_slider.set(brush_size)
brush_slider.grid(row=0, column=2, padx=6)

# Кнопка для выбора заливки
customtkinter.CTkButton(tool_bar, text='Заливка', command=pour).grid(row=0, column=3, padx=6)

# Кнопка очистки
customtkinter.CTkButton(tool_bar, text='Очистить', command=clear_canvas).grid(row=0, column=4, padx=6)

# Кнопка для сохранения
customtkinter.CTkButton(tool_bar, text='Сохранить', command=save_img).grid(row=0, column=5, padx=6)

# Кнопка для undo
customtkinter.CTkButton(tool_bar, text='Undo', command=undo).grid(row=0, column=6, padx=6)

# Кнопка для redo
customtkinter.CTkButton(tool_bar, text='Redo', command=redo).grid(row=0, column=7, padx=6)

# Выбор режима рисования
customtkinter.CTkButton(tool_bar, text='Линия', command=lambda: change_mode('line')).grid(row=1, column=0, padx=6)
customtkinter.CTkButton(tool_bar, text='Кисть', command=lambda: change_mode('brush')).grid(row=1, column=1, padx=6)

root.mainloop()
