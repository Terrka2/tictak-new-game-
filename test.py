import random
import turtle

# --- Настройка графики Turtle ---
screen = turtle.Screen()
screen.title("Крестики-нолики")
screen.setup(400, 400)

t_drawer = turtle.Turtle()
t_drawer.speed(0)
t_drawer.hideturtle()

def draw_grid():
    """Рисует игровое поле"""
    t_drawer.clear()
    t_drawer.pensize(3)
    t_drawer.pencolor("black")
    
    # Вертикальные линии
    for x in (-50, 50):
        t_drawer.penup()
        t_drawer.goto(x, -150)
        t_drawer.pendown()
        t_drawer.goto(x, 150)
        
    # Горизонтальные линии
    for y in (-50, 50):
        t_drawer.penup()
        t_drawer.goto(-150, y)
        t_drawer.pendown()
        t_drawer.goto(150, y)

def get_cell_center(index):
    """Превращает индекс от 0 до 8 в координаты на экране"""
    row = index // 3
    col = index % 3
    x = (col - 1) * 100
    y = (1 - row) * 100
    return x, y

def draw_symbol(index, symbol):
    """Рисует крестик или нолик в нужной клетке"""
    x, y = get_cell_center(index)
    t_drawer.penup()
    
    if symbol == "x":
        t_drawer.pencolor("blue")
        t_drawer.goto(x - 30, y - 30)
        t_drawer.pendown()
        t_drawer.goto(x + 30, y + 30)
        t_drawer.penup()
        t_drawer.goto(x - 30, y + 30)
        t_drawer.pendown()
        t_drawer.goto(x + 30, y - 30)
    elif symbol == "o":
        t_drawer.pencolor("red")
        t_drawer.goto(x, y - 30)
        t_drawer.pendown()
        t_drawer.circle(30)

def update_gui(table):
    """Обновляет графическое окно"""
    draw_grid()
    for i, val in enumerate(table):
        if val == "x" or val == "o":
            draw_symbol(i, val)

def bot(table: list):
    available = [i for i, val in enumerate(table) if isinstance(val, int)]
    if available:
        a = random.choice(available)
        table[a] = "o"
    return table

def result(table: list):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if table[a] == table[b] == table[c] and not isinstance(table[a], int):
            return table[a]
    if all(isinstance(x, str) for x in table):
        return "draw"
    return None

# Инициализация игры
table = [a for a in range(1, 10)]
draw_grid()  # Сразу рисуем сетку, никакого белого экрана!

while True:
    # Вызываем красивое графическое окошко для ввода номера клетки
    answer = turtle.numinput(
        "Крестики-нолики", 
        "Введите клетку (1-9) или 0 для выхода:", 
        minval=0, maxval=9
    )
    
    # Если закрыли окно или ввели 0
    if answer is None or answer == 0:
        print("Игра окончена!")
        break
        
    answer = int(answer)
    
    if 1 <= answer <= 9 and isinstance(table[answer - 1], int):
        table[answer - 1] = "x"
        update_gui(table)  # Отражаем крестик в окне
        
        # Проверка победы игрока
        winner = result(table)
        if winner == "x":
            turtle.textinput("Конец игры", "🎉 Вы победили! Нажмите Enter.")
            break
        elif winner == "draw":
            turtle.textinput("Конец игры", "🤝 Ничья! Нажмите Enter.")
            break

        # Ход бота
        bot(table)
        update_gui(table)  # Отражаем нолик бота в окне
        
        # Проверка победы бота
        winner = result(table)
        if winner == "o":
            turtle.textinput("Конец игры", "🤖 Вы проиграли боту! Нажмите Enter.")
            break
        elif winner == "draw":
            turtle.textinput("Конец игры", "🤝 Ничья! Нажмите Enter.")
            break
    else:
        print("Вы не можете так ходить!")

turtle.done()