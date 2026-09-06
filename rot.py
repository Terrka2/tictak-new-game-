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

show(table)
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
    