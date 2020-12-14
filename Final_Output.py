from tkinter import *

root = Tk()


def submit_game():
    print('Hi')


root.geometry('500x500')
root.title('Games Income Earned')


label_0 = Label(root,text="Game Income Results", width=20,font=("bold",20))
label_0.place(x=90,y=30)


#Most popular game per period of time.
label_1 = Label(root, text="See How Much Earned By",font=("bold",10))
label_1.place(x=80,y=100)
label_1a = Label(root, text="From (mm/dd/yyyy)", font=("bold",10))
label_1a.place(x=50,y=135)
label_1a = Label(root, text="To (mm/dd/yyyy)", font=("bold",10))
label_1a.place(x=260,y=135)


list_of_games=[ 'Pick a Duck' , 'Coin Drop' , 'Ballon Pop' , 'Gone Fishing' , 'Bean Bag Toss']

entry_1=StringVar()
droplist=OptionMenu(root,entry_1, *list_of_games)
droplist.config(width=15)
entry_1.set('Choose a Game')
droplist.place(x=250,y=95)

entry_1a = Entry(root, width=12, justify=RIGHT)
entry_1a.place(x=170,y=135)
entry_1b = Entry(root, width=12, justify=RIGHT)
entry_1b.place(x=370,y=135)

Button(root, text='Submit', command=submit_game, width=20,bg="black",fg='white').place(x=180,y=165)

root.mainloop()
