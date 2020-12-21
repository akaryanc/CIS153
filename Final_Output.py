import re
import math

from tkinter import *

root = Tk()


def game_submit():
    game=entry_1.get()
    gamemoney = open('gameincome.txt')
    money_totals = list()
    for line in gamemoney:
        line = line.rstrip()
        if re.search(game, line):
            lst = line.split()
            money_totals.append(float(lst[2]))
    Average_total = sum(money_totals)/len(money_totals)
    outputText = 'The daily average of ' + game + ' is $' + str(round(Average_total,2))
    label_1a = Label(root, text=outputText,font=("bold",10))
    label_1a.place(x=185,y=140)


def cat_submit():
    cat=entry_2.get()
    gamemoney = open('gameincome.txt')
    money_totals = list()
    for line in gamemoney:
        line = line.rstrip()
        if re.search(cat, line):
            lst = line.split()
            money_totals.append(float(lst[2]))
    Average_total = sum(money_totals)/len(money_totals)
    outputText = 'The daily average of ' + cat + ' Games is $' + str(round(Average_total,2))
    label_2a = Label(root, text=outputText,font=("bold",10))
    label_2a.place(x=185,y=240)


def most_submit():
    most=entry_3.get()
    gamemoney = open('gameincome.txt')
    money_totals = list()
    for line in gamemoney:
        line = line.rstrip()
        if re.search(most, line):
            lst = line.split()
            money_totals.append(float(lst[2]))
    sum_total = sum(money_totals)
    outputText = 'The total sales for ' + most + ' Games is $' + str(round(sum_total,2))
    label_3a = Label(root, text=outputText,font=("bold",10))
    label_3a.place(x=185,y=340)


def most_cat_submit():
    most_cat=entry_4.get()
    gamemoney = open('gameincome.txt')
    money_totals = list()
    for line in gamemoney:
        line = line.rstrip()
        if re.search(most_cat, line):
            lst = line.split()
            money_totals.append(float(lst[2]))
    sum_total = sum(money_totals)
    outputText = 'The total sales for ' + most_cat + ' Games is $' + str(round(sum_total,2))
    label_4a = Label(root, text=outputText,font=("bold",10))
    label_4a.place(x=185,y=440)


root.geometry('525x525')
root.title('Games Income Earned')

label_0 = Label(root,text="Game Income Results", width=20,font=("bold",20))
label_0.place(x=90,y=30)



label_1 = Label(root, text="See Average Daily Income For - ",font=("bold",10))
label_1.place(x=80,y=100)

list_of_games=[ 'Coin_Drop' , 'Balloon_Pop' , 'Pick_a_Duck' , 'Gone_Fishing' , 'Bean_Bag_Toss']

entry_1=StringVar()
droplist=OptionMenu(root, entry_1, *list_of_games)
droplist.config(width=15)
entry_1.set('Choose a Game')
droplist.place(x=275,y=95)

Button(root, text='Results', command = game_submit, width=20,bg="black",fg='white').place(x=25,y=135)



label_2 = Label(root, text="See Average Daily Income For - ",font=("bold",10))
label_2.place(x=80,y=200)

game_category_list=[ 'Skill' , 'Luck']

entry_2=StringVar()
droplist=OptionMenu(root,entry_2, *game_category_list)
droplist.config(width=15)
entry_2.set('Choose a Category')
droplist.place(x=275,y=195)

Button(root, text='Results', command=cat_submit, width=20,bg="black",fg='white').place(x=25,y=235)



label_3 = Label(root, text="Total for sales for -",font=("bold",10))
label_3.place(x=140,y=300)

entry_3=StringVar()
droplist=OptionMenu(root,entry_3, *list_of_games)
droplist.config(width=15)
entry_3.set('Choose a Game')
droplist.place(x=275,y=295)

Button(root, text='Results', command=most_submit, width=20,bg="black",fg='white').place(x=25,y=335)



label_4 = Label(root, text="Total for sales for -",font=("bold",10))
label_4.place(x=140,y=400)

game_category_list=[ 'Skill' , 'Luck']

entry_4=StringVar()
droplist=OptionMenu(root,entry_4, *game_category_list)
droplist.config(width=15)
entry_4.set('Choose a Category')
droplist.place(x=275,y=395)

Button(root, text='Results', command=most_cat_submit, width=20,bg="black",fg='white').place(x=25,y=435)



root.mainloop()
