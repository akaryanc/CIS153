import re #import the regular expression library
import math #import math library

from tkinter import * #Import the tkinter library

root = Tk() #creates the root tk window


def game_submit(): #defines the game submit command for the submit button
    game=entry_1.get() #turns the entry into recallable text.
    gamemoney = open('gameincome.txt') #open the database file
    money_totals = list() #make a list of the individual totals
    for line in gamemoney: #check individual lines in database
        line = line.rstrip() #break the line into individual parts
        if re.search(game, line): #search each line for the entry
            lst = line.split() #splits the line
            money_totals.append(float(lst[2])) #adds the money totals to the list
    Average_total = sum(money_totals)/len(money_totals) #finds the average
    outputText = 'The daily average of ' + game + ' is $' + str(round(Average_total,2))
    label_1a = Label(root, text=outputText,font=("bold",10)) #first text box and it's format
    label_1a.place(x=185,y=140) #The label's location


def cat_submit(): #defines the cat submit command for the submit button
    cat=entry_2.get() #turns the entry into recallable text.
    gamemoney = open('gameincome.txt') #open the database file
    money_totals = list() #make a list of the individual totals
    for line in gamemoney: #check individual lines in database
        line = line.rstrip() #break the line into individual parts
        if re.search(cat, line): #search each line for the entry
            lst = line.split() #splits the line
            money_totals.append(float(lst[2])) #adds the money totals to the list
    Average_total = sum(money_totals)/len(money_totals) #finds the average
    outputText = 'The daily average of ' + cat + ' Games is $' + str(round(Average_total,2))
    label_2a = Label(root, text=outputText,font=("bold",10))  #first text box and it's format
    label_2a.place(x=185,y=240) #The label's location


def most_submit(): #defines the most submit command for the submit button
    most=entry_3.get() #turns the entry into recallable text.
    gamemoney = open('gameincome.txt') #open the database file
    money_totals = list() #make a list of the individual totals
    for line in gamemoney: #check individual lines in database
        line = line.rstrip() #break the line into individual parts
        if re.search(most, line): #search each line for the entry
            lst = line.split() #splits the line
            money_totals.append(float(lst[2])) #adds the money totals to the list
    sum_total = sum(money_totals) #finds the total
    outputText = 'The total sales for ' + most + ' Games is $' + str(round(sum_total,2))
    label_3a = Label(root, text=outputText,font=("bold",10)) #first text box and it's format
    label_3a.place(x=185,y=340) #The label's location


def most_cat_submit(): #defines the most cat submit command for the submit button
    most_cat=entry_4.get() #turns the entry into recallable text.
    gamemoney = open('gameincome.txt') #open the database file
    money_totals = list() #make a list of the individual totals
    for line in gamemoney: #check individual lines in database
        line = line.rstrip() #break the line into individual parts
        if re.search(most_cat, line): #search each line for the entry
            lst = line.split() #splits the line
            money_totals.append(float(lst[2])) #adds the money totals to the list
    sum_total = sum(money_totals) #finds the total
    outputText = 'The total sales for ' + most_cat + ' Games is $' + str(round(sum_total,2))
    label_4a = Label(root, text=outputText,font=("bold",10)) #first text box and it's format
    label_4a.place(x=185,y=440) #The label's location


root.geometry('525x525')  # make tk window 525 by 525 pixels
root.title('Games Income Earned') #the title of the tk window

label_0 = Label(root,text="Game Income Results", width=20,font=("bold",20)) #first text box and it's format
label_0.place(x=90,y=30) #The label's location



label_1 = Label(root, text="See Average Daily Income For - ",font=("bold",10)) #first text box and it's format
label_1.place(x=80,y=100) #The label's location

list_of_games=[ 'Coin_Drop' , 'Balloon_Pop' , 'Pick_a_Duck' , 'Gone_Fishing' , 'Bean_Bag_Toss'] #where to pull dropdown menu info from

entry_1=StringVar() #make the user entry a string
droplist=OptionMenu(root, entry_1, *list_of_games) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_1.set('Choose a Game') #text for button
droplist.place(x=275,y=95) #The label's location

Button(root, text='Results', command = game_submit, width=20,bg="black",fg='white').place(x=25,y=135) #first text box and it's format



label_2 = Label(root, text="See Average Daily Income For - ",font=("bold",10)) #first text box and it's format
label_2.place(x=80,y=200) #The label's location

game_category_list=[ 'Skill' , 'Luck'] #where to pull dropdown menu info from

entry_2=StringVar() #make the user entry a string
droplist=OptionMenu(root,entry_2, *game_category_list) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_2.set('Choose a Category') #text for button
droplist.place(x=275,y=195) #The label's location

Button(root, text='Results', command=cat_submit, width=20,bg="black",fg='white').place(x=25,y=235) #first text box and it's format



label_3 = Label(root, text="Total for sales for -",font=("bold",10)) #first text box and it's format
label_3.place(x=140,y=300) #The label's location

entry_3=StringVar() #make the user entry a string
droplist=OptionMenu(root,entry_3, *list_of_games) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_3.set('Choose a Game') #text for button
droplist.place(x=275,y=295) #The label's location

Button(root, text='Results', command=most_submit, width=20,bg="black",fg='white').place(x=25,y=335) #first text box and it's format



label_4 = Label(root, text="Total for sales for -",font=("bold",10)) #first text box and it's format
label_4.place(x=140,y=400) #The label's location

game_category_list=[ 'Skill' , 'Luck'] #list for dropdown menu

entry_4=StringVar() #make the user entry a string
droplist=OptionMenu(root,entry_4, *game_category_list) #where to pull dropdown menu info from
droplist.config(width=15) #set width of button
entry_4.set('Choose a Category') #text for button
droplist.place(x=275,y=395) #The label's location

Button(root, text='Results', command=most_cat_submit, width=20,bg="black",fg='white').place(x=25,y=435) #first text box and it's format



root.mainloop() #keeps the root tk window running and open

input('Press ENTER to exit') #end program
