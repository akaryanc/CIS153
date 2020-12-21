from tkinter import * #Import the tkinter library

root = Tk() #creates the root tk window


def submit(): #defines the submit command for the submit button
    game=entry_1.get() #turns the entry into recallable text.
    money=entry_2.get() #turns the entry into recallable text.
    category=entry_3.get() #turns the entry into recallable text.
    date=entry_4.get() #turns the entry into recallable text.
    enter_data = open('gameincome.txt', 'a') #open the database file and make it appendable.
    enter_data.write(str(game)) #enter the first entry box as a string
    enter_data.write(' :: ') #spaceing for the database line to make it more human readable.
    enter_data.write(str(money)) #enter the second entry box as a string
    enter_data.write(' :: ') #spaceing for the database line to make it more human readable.
    enter_data.write(str(category)) #enter the third entry box as a string
    enter_data.write(' :: ') #spaceing for the database line to make it more human readable.
    enter_data.write(str(date)) #enter the forth entry box as a string
    enter_data.write('\n') #start a new line for the nest entry


try:
    gameincome = open('gameincome.txt') #check to see if file exists and open it
except:
    gameincome = open('gameincome.txt', 'w') #if file doesn't exist create it.


root.geometry('500x600') # make tk window 500 by 600 pixels
root.title('Games Income Entry') #the title of the tk window


label_0 = Label(root,text="Game Income Reporting", width=20,font=("bold",20)) #first text box and it's format
label_0.place(x=90,y=60) #The label's location


label_1 = Label(root,text="Which Game?", width=20,font=("bold",10)) #text box and it's format
label_1.place(x=60,y=130) #The label's location

list_of_games=[ 'Pick_a_Duck' , 'Coin_Drop' , 'Balloon_Pop' , 'Gone_Fishing' , 'Bean_Bag_Toss'] #list for dropdown menu

entry_1=StringVar() #make the user entry a string
droplist=OptionMenu(root, entry_1, *list_of_games) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_1.set('Choose a Game') #text for button
droplist.place(x=240,y=125) #The label's location


label_2 = Label(root,text="How Much Money Earned?", width=20,font=("bold",10))  #text box and it's format
label_2.place(x=60,y=180) #The label's location

entry_2 = Entry(root, justify=RIGHT) #blank entry box with text at the right
entry_2.place(x=240,y=180) #The label's location


label_3 = Label(root,text="Choose game type -", width=20,font=("bold",10)) #text box and it's format
label_3.place(x=60,y=230) #The label's location

game_category_list=[ 'Skill' , 'Luck'] #list for dropdown menu

entry_3=StringVar() #make the user entry a string
droplist=OptionMenu(root,entry_3, *game_category_list) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_3.set('Choose a Type') #text for button
droplist.place(x=240,y=225) #The label's location


label_4=Label(root,text="Date (MM/DD/YYYY)",width=20,font=("bold",10)) #text box and it's format
label_4.place(x=70,y=280) #The label's location

entry_4 = Entry(root, justify=RIGHT) #blank entry box with text at the right
entry_4.place(x=240,y=280) #The label's location


Button(root, text='Submit', command = submit, width=20,bg="black",fg='white').place(x=180,y=380) #text box and it's format


root.mainloop() #keeps the root tk window running and open

input('Press ENTER to exit') #end program
