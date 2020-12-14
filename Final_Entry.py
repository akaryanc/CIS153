from tkinter import *

root = Tk()


def submit():
    game=entry_1.get()
    money=entry_2.get()
    type=entry_3.get()
    date=entry_4.get()
    enter_data = open('gameincome.txt', 'a')
    enter_data.write(str(game))
    enter_data.write(' :: ')
    enter_data.write(str(money))
    enter_data.write(' :: ')
    enter_data.write(str(type))
    enter_data.write(' :: ')
    enter_data.write(str(date))
    enter_data.write('\n')


try:
    gameincome = open('gameincome.txt')
except:
    gameincome = open('gameincome.txt', 'w')


root.geometry('500x500')
root.title('Games Income')


label_0 = Label(root,text="Game Income Reporting", width=20,font=("bold",20))
label_0.place(x=90,y=60)


label_1 = Label(root,text="Which Game?", width=20,font=("bold",10))
label_1.place(x=60,y=130)

list_of_games=[ 'Pick a Duck' , 'Coin Drop' , 'Ballon Pop' ,'Gone Fishing' , 'Bean Bag Toss']

entry_1=StringVar()
droplist=OptionMenu(root,entry_1, *list_of_games)
droplist.config(width=15)
entry_1.set('Choose a Game')
droplist.place(x=240,y=125)


label_2 = Label(root,text="How Much Money Earned?", width=20,font=("bold",10))
label_2.place(x=60,y=180)

entry_2 = Entry(root, justify=RIGHT)
entry_2.place(x=240,y=180)


label_3 = Label(root,text="Choose game type -", width=20,font=("bold",10))
label_3.place(x=60,y=230)

game_category_list=[ 'Skill' , 'Luck']

entry_3=StringVar()
droplist=OptionMenu(root,entry_3, *game_category_list)
droplist.config(width=15)
entry_3.set('Choose a Type')
droplist.place(x=240,y=225)


label_4=Label(root,text="Date (MM/DD/YYYY)",width=20,font=("bold",10))
label_4.place(x=70,y=280)

entry_4 = Entry(root, justify=RIGHT)
entry_4.place(x=240,y=280)


Button(root, text='Submit', command = submit, width=20,bg="black",fg='white').place(x=180,y=380)


root.mainloop()
