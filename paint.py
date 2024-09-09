from tkinter import *
from PIL import Image, ImageDraw
from random import randint
from tkinter import colorchooser, messagebox

def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=color)

def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    color_lab['bg'] = hx

def pour():
    canvas.delete('all')
    canvas['bg'] = color
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)

def clear_canvas():
    canvas.delete('all')
    canvas['bg'] = 'white'
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
    canvas.create_rectangle(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.rectangle((x, y, x + brush_size, y + brush_size), fill=color)

def circle():
    canvas.create_oval(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill=color)

def select(val):
    global brush_size
    brush_size = int(val)

x = 0
y = 0

root = Tk()
root.title("Paint")
root.geometry('1980x1080')
root.resizable(0, 0)

brush_size = 10
color = 'red'

root.columnconfigure(6, weight=1)
root.rowconfigure(2, weight=1)

canvas = Canvas(root, bg='white')
canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)

canvas.bind('<B1-Motion>', draw)
canvas.bind("<Button-3>", popup)

menu = Menu(root, tearoff=0)
menu.add_command(label="Квадрат", command=square)
menu.add_command(label="Круг", command=circle)

image1 = Image.new('RGB', (1280, 720), 'white')
draw_img = ImageDraw.Draw(image1)

Label(root, text='Параметры:').grid(row=0, column=0, padx=6)

Button(root, text='Выбрать цвет', width=11, command=chooseColor).grid(row=0, column=1, padx=6)

color_lab = Label(root, bg=color, width=10)
color_lab.grid(row=0, column=2, padx=6)

v = IntVar(value=10)
Scale(root, variable=v, from_=1, to=100, orient=HORIZONTAL, command=select).grid(row=0, column=3, padx=6)

Label(root, text="Действия:").grid(row=1, column=0, padx=6)

Button(root, text='Заливка', width=10, command=pour).grid(row=1, column=1)

Button(root, text='Очистить', width=10, command=clear_canvas).grid(row=1, column=2)

Button(root, text='Сохранить', width=10, command=save_img).grid(row=1, column=6)

root.mainloop()
