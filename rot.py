import random

def line():
    return print("","-"*13)

def show(table:list):
    line()
    for a in range(0, len(table)):
        if  (a+1) % 9 == 0:
            print(" |",table[a],"|")
            line()
        elif (a+1) % 3 == 0:
            print(" |", table[a] , "|")
            line()
        else:
            print(" |",table[a], end="")
    return table

def bot(table:list):
    available = [i for i, val in enumerate(table) if isinstance(val, int)]
    if available:
        a = random.choice(available)
        table[a] = "o"
    return table

def player(table:list, name1:str, name2:str):
    players = (name1,name2)
    show(table)
    global n
    answer = int (input("Ходит игрок "+ players[n]+ " : "))
    while True:
        if answer in table and isinstance(answer, int):
            if n == 0:
                n += 1
                table[answer - 1] = "x"
                return table
            elif n == 1:
                table[answer - 1] = "o"
                n = 0
                return table
        else: 
            print("Вы не можете так ходить! ") 
            break

def result(table:list):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if table[a] == table[b] == table[c] and not isinstance(table[a], int):
            return table[a]
    if all(isinstance(x,str) for x in table):
        return "draw"
    return None



table = [a for a in range(1,10)]


a = int(input("Хотите играть с другом или с ботом? \n1 - друг, 2 - бот\n"))
if a == 2:

    while True:
        answer = int(input("Выберите куда хотите пойти или 0 для завершения: "))
        if answer in table and isinstance(table[answer-1], int):
            table[answer-1] = "x"
            winner = result(table)

            if winner == "x":
                show(table)
                print("\n Вы победили!")
                break
            elif winner == "draw":
                show(table)
                print("ничья")
                break
            bot(table)
            show(table)
            winner = result(table)
            if winner == "o":
                print("\n Вы проебали боту!")
                break
            elif winner == "draw":
                print("ничья")
                break
            
        elif answer == 0:
            print("игра окончена!")
            break
        else:
            print ("Вы не можете так ходить!")
elif a == 1:
    name1 = input("Игрок 1 введи свое имя: ")
    name2 = input("Игрок 2 введи свое имя: ")
    if name1 == name2:
        print("Имена не могут быть похожими")
    else:
        n = 0
        while True:
            player(table, name1, name2)
            show(table)
            winner = result(table)
            if winner == "x":
                show(table)
                print("\n Поздравляю " , name1 ," победил!")
                break
            elif winner == "o":
                show(table)
                print("\n Поздравляю " , name2 ," победил!")
                break
            elif winner == "draw":
                show(table)
                print("ничья")
                break
            