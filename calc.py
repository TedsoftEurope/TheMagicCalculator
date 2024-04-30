# Based on a tutorial I found, this uses tkinter but it seems to be easy enough to edit
# Yes, I had to test this on my own pc
# Added FOUR NEW COMMENTS in total (including this one)

# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

from tkinter import *

expression = "" 
 # THIS HAS TO BE BLANK
 
def press(num): 
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 
# setting the equation. Pretty much says so
def equalpress(): 
    try: 
        global expression 
        total = str(eval(expression)) 
 
        equation.set(total) 
 # Convert numbers into strings
 
        expression = "" 
         # LEAVE THIS EMPTY, ALWAYS ALWAYS ALWAYS
         
            # divide by zero or some other funny error
    except: 
        equation.set(" OH NO!!!! ") 
        expression = "" 
 #then clear
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

#the GUI
import os
if __name__ == "__main__": 
    gui = Tk() 
 # I have no clue what this does apart from importing something and setting the GUI to tkinter. I’m not touching this.
# If you see stuff like #AABBCC, that’s hex colour code. Nothing to be scared of, seeing as you can read this code.
    gui.configure(background="#FFD9C6") 
    gui.title("The Magic Calculator") 
    gui.geometry("330x330") 
    #a cool variable
    equation = StringVar() 
 
    # I don't know what else to do with this
    # I could probably convert this to regular text
    expression_field = Entry(gui, textvariable=equation)
 
    # the grid, i'd rather not mess this up
    expression_field.grid(columnspan=3, ipadx=3)
    #   THE NUMBERS (and clear and equals)
    button1 = Button(gui, text=' 1 ', fg='black', bg='#fafa6e', 
                    command=lambda: press(1), height=4, width=8) 
    button1.grid(row=2, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='#ddfa70', 
                    command=lambda: press(2), height=4, width=8) 
    button2.grid(row=2, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='#bef977', 
                    command=lambda: press(3), height=4, width=8)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='#9ff881', 
                    command=lambda: press(4), height=4, width=8) 
    button4.grid(row=3, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='#7ef58e', 
                    command=lambda: press(5), height=4, width=8) 
    button5.grid(row=3, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='#57f19d', 
                    command=lambda: press(6), height=4, width=8) 
    button6.grid(row=3, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='#16edac', 
                    command=lambda: press(7), height=4, width=8) 
    button7.grid(row=4, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='#00e7bc', 
                    command=lambda: press(8), height=4, width=8) 
    button8.grid(row=4, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='#00dfcb', 
                    command=lambda: press(9), height=4, width=8) 
    button9.grid(row=4, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='#00d7d6', 
                    command=lambda: press(0), height=4, width=8) 
    button0.grid(row=5, column=0)
    
    clear = Button(gui, text='Clear', fg='white', bg='red', 
                command=clear, height=4, width=8) 
    clear.grid(row=5, column=1)
    
    equal = Button(gui, text=' = ', fg='white', bg='green', 
                command=equalpress, height=4, width=8) 
    equal.grid(row=5, column=2)
    
                    # BUTTONS NEXT TO THE NUMBERS
    plus = Button(gui, text=' + ', fg='black', bg='#ffc862', 
                command=lambda: press("+"), height=4, width=8 ) 
    plus.grid(row=2, column=3) 
 
    minus = Button(gui, text=' - ', fg='black', bg='#ddec48', 
                command=lambda: press("-"), height=4, width=8) 
    minus.grid(row=3, column=3) 
 
    multiply = Button(gui, text=' * ', fg='black', bg='#7dd92f', 
                    command=lambda: press("*"), height=4, width=8) 
    multiply.grid(row=4, column=3) 
 
    divide = Button(gui, text=' / ', fg='black', bg='#33C479', 
                    command=lambda: press("/"), height=4, width=8) 
    divide.grid(row=5, column=3) 
  
    Decimal= Button(gui, text='.', fg='black', bg='#FF7070', 
                    command=lambda: press('.'), height=4, width=8) 
    Decimal.grid(row=5, column=4)
    
    # start the GUI, a bit anticlimactic
    gui.mainloop()