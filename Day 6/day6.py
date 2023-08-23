import tkinter as tk
from tkinter import ttk
import turtle as t

def execute_task_1():
    selected_color = color_var.get()
    t.reset()  # Очистка рисунка
    t.color(selected_color)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)


def draw_rectangle():
    width = float(width_entry.get())
    height = float(height_entry.get())

    t.clear()

    t.penup()
    t.goto(-width / 2, -height / 2)
    t.pendown()
    t.width(2)
    t.bgcolor("green")
    t.begin_fill()
    t.color("orange")

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.penup()
    t.end_fill()

    t.color("yellow")
    t.pendown()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
# Создание главного окна
root = tk.Tk()
root.title("Задания для выполнения")

# Создание вкладок
notebook = ttk.Notebook(root)

# Создание вкладки "Задача 1"
task1_tab = ttk.Frame(notebook)
notebook.add(task1_tab, text="Задача 1")

# Создание вкладки "Задача 2"
task2_tab = ttk.Frame(notebook)
notebook.add(task2_tab, text="Задача 2")

# Добавление выпадающего списка для выбора цвета
color_label = tk.Label(task1_tab, text="Выберите цвет линии:")
color_label.pack()

color_choices = ["black", "red", "green", "blue"]
color_var = tk.StringVar()
color_var.set(color_choices[0])
color_menu = tk.OptionMenu(task1_tab, color_var, *color_choices)
color_menu.pack()

# Добавление кнопки "Выполнить задание 1"
execute_button = tk.Button(task1_tab, text="Выполнить задание 1", command=execute_task_1)
execute_button.pack()
# Добавление на 2 вкладку
width_label = tk.Label(task2_tab, text="Ширина:")
width_label.pack()

width_entry = tk.Entry(task2_tab)
width_entry.pack()

height_label = tk.Label(task2_tab, text="Высота:")
height_label.pack()

height_entry = tk.Entry(task2_tab)
height_entry.pack()

draw_button = tk.Button(task2_tab, text="Выполнить задание", command=draw_rectangle)
draw_button.pack()

# Добавление вкладок на главное окно
notebook.pack()

# Инициализация черепашки
t_screen = t.Screen()
t_screen.setworldcoordinates(-200, -200, 200, 200)
t_screen.update()

# Запуск основного цикла обработки событий
root.mainloop()