# This GUI uses Tkinter to "DRAW" (MANUALLY PROGRAMMED) roman numerals that the user inputs -- acceptable inputs: MDCLXVI
# the user can also customize the style of the roman numeral drawing

from tkinter import *
import random

class Application(Frame):
    """ GUI Application for Roman Numerals GUI. """
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets for Roman Numerals GUI. """

        # create TOP label
        Label(self,
              text = "Roman Numeral Canvas"
              ).grid(row = 0, column = 0, columnspan = 5)

        # create Number label
        Label(self,
              text = "Number:"
              ).grid(row = 1, column = 1)

        #create Entry box for the Number
        self.ent1 = Entry(self, width=30)
        self.ent1.grid(row = 1, column = 2)

        self.numbers = BooleanVar() #special boolean var setup for the checkbutton

        #create "acceptable inputs" label
        Label(self, text = "Acceptable inputs: MDCLXVI",
                    ).grid(row = 1, column = 3, columnspan = 2)

        # create line width label
        Label(self,
              text = "Line Width:"
              ).grid(row = 2, column = 1)

        # create variable for line width
        self.width = StringVar() #StringVar() is for radiobuttons
        self.width.set(1) #setting the default to 1

        # create 1 radio button
        Radiobutton(self,
                    text = "1",
                    variable = self.width,
                    value = 1,
                    #command = self.update_text
                    ).grid(row = 2, column = 2)

        # create 3 radio button
        Radiobutton(self,
                    text = "3",
                    variable = self.width,
                    value = 3,
                    #command = self.update_text
                    ).grid(row = 2, column = 3)

        # create 5 radio button
        Radiobutton(self,
                    text = "5",
                    variable = self.width,
                    value = 5,
                    #command = self.update_text
                    ).grid(row = 2, column = 4)

        # create line color label
        Label(self,
              text = "Line Color:"
              ).grid(row = 3, column = 1)

        # create variable for line color
        self.color = StringVar()
        self.color.set("black") #setting the default to black

        # create black radio button
        Radiobutton(self,
                    text = "Black",
                    variable = self.color,
                    value = "black",
                    #command = self.update_text
                    ).grid(row = 3, column = 2)

        # create red radio button
        Radiobutton(self,
                    text = "Red",
                    variable = self.color,
                    value = "red",
                    #command = self.update_text
                    ).grid(row = 3, column = 3)

        # create blue radio button
        Radiobutton(self,
                    text = "Blue",
                    variable = self.color,
                    value = "blue",
                    #command = self.update_text
                    ).grid(row = 3, column = 4)

        #make sure roman.gif is in same directory of this file
        self.roman = PhotoImage(file="roman.gif")

        #create button for roman
        self.bttn1 = Button(self, image=self.roman, command = self.draw_roman)
        self.bttn1.grid(row = 4, column = 1, rowspan = 2, columnspan = 2)

        #make sure random.gif is in same directory of this file
        self.random = PhotoImage(file="random.gif")

        #create button for random
        self.bttn2 = Button(self, image=self.random, command = self.draw_random)
        self.bttn2.grid(row = 4, column = 3, rowspan = 2, columnspan = 2)

        # create canvas to draw results
        self.canvas = Canvas(self, height=310, width = 500)
        self.canvas.grid(row = 1, column = 0, rowspan = 5)

        #starting the pen here
        self.x, self.y = 20, 20

        #sets random class variable to off
        self.random_on = False


    def draw_roman(self):
        """This function calls the other functions to draw roman numerals"""
        my_roman = str(self.ent1.get())

        #this checks to see if you hit the random button
        #if you did not, then it will choose line width and color depending on what you chose
        if not self.random_on:
            self.my_width = self.width.get()
            self.my_fill = self.color.get()

        for roman in my_roman:
            if roman.upper() == "M":
                self.draw_m()
            elif roman.upper() == "D":
                self.draw_d()
            elif roman.upper() == "C":
                self.draw_c()
            elif roman.upper() == "L":
                self.draw_l()
            elif roman.upper() == "X":
                self.draw_x()
            elif roman.upper() == "V":
                self.draw_v()
            elif roman.upper() == "I":
                self.draw_i()

        self.random_on = False #resetting the random module to off


    def draw_random(self):
        """This function chooses a random line width and color"""
        self.random_on = True #setting random module to be on

        self.my_width = random.randrange(1,6) #chooses a random width

        color_list = ["black", "red", "blue", "green"] #chooses a random color
        self.my_fill = random.choice(color_list)

        self.draw_roman() #then runs the roman drawing method


    def draw_m(self):
        """This function draws an M"""

        #first two lines are upper vertical dashes
        self.canvas.create_line(self.x, self.y,
                                self.x+5, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+15, self.y,
                                self.x+20, self.y,
                                width = self.my_width, fill = self.my_fill)

        #next two lines are long horizontal strokes
        self.canvas.create_line(self.x+2, self.y,
                                self.x+2, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+17, self.y,
                                self.x+17, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #next two lines are lower vertical dashes
        self.canvas.create_line(self.x, self.y+40,
                                self.x+5, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+15, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #final two lines are the meetings of the M
        self.canvas.create_line(self.x+3, self.y,
                                self.x+10, self.y+10,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+18, self.y,
                                self.x+10, self.y+10,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_d(self):
        """This function draws a D"""

        #first line is the vertical left side of D
        self.canvas.create_line(self.x, self.y,
                                self.x, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #next two lines are the top and bottom vertical strokes of D
        self.canvas.create_line(self.x, self.y,
                                self.x+10, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+40,
                                self.x+10, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #next line is the vertical dash on the right side of D
        self.canvas.create_line(self.x+20, self.y+10,
                                self.x+20, self.y+30,
                                width = self.my_width, fill = self.my_fill)

        #final two lines are the angular lines
        self.canvas.create_line(self.x+10, self.y,
                                self.x+20, self.y+10,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+10, self.y+40,
                                self.x+20, self.y+30,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_c(self):
        """This function draws a C"""

        #first 2 lines are the horizontal top and bottom of C
        self.canvas.create_line(self.x+10, self.y,
                                self.x+20, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+10, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)


        #next line is the vertical dash on the left side of C
        self.canvas.create_line(self.x, self.y+10,
                                self.x, self.y+30,
                                width = self.my_width, fill = self.my_fill)

        #final two lines are the angular lines
        self.canvas.create_line(self.x, self.y+10,
                                self.x+10, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+30,
                                self.x+10, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_l(self):
        """This function draws an L"""

        #first 2 lines are the horizontal top and bottom of L
        self.canvas.create_line(self.x, self.y,
                                self.x+10, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)


        #next line is the vertical dash of L
        self.canvas.create_line(self.x+5, self.y,
                                self.x+5, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_x(self):
        """This function draws an X"""

        #first 2 lines are the horizontal top and bottom of X
        self.canvas.create_line(self.x, self.y,
                                self.x+20, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #final two lines are the angular lines
        self.canvas.create_line(self.x+5, self.y,
                                self.x+15, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+15, self.y,
                                self.x+5, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_v(self):
        """This function draws a V"""

        #first 2 lines are the horizontal top and bottom of V
        self.canvas.create_line(self.x, self.y,
                                self.x+20, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #final two lines are the angular lines
        self.canvas.create_line(self.x+5, self.y,
                                self.x+10, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x+15, self.y,
                                self.x+10, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50

    def draw_i(self):
        """This function draws a I"""

        #first 2 lines are the horizontal top and bottom of I
        self.canvas.create_line(self.x, self.y,
                                self.x+20, self.y,
                                width = self.my_width, fill = self.my_fill)

        self.canvas.create_line(self.x, self.y+40,
                                self.x+20, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #final line is the vertical line of the I
        self.canvas.create_line(self.x+10, self.y,
                                self.x+10, self.y+40,
                                width = self.my_width, fill = self.my_fill)

        #once done drawing, move the X coordinate along to draw the next
        self.x += 30

        #if the x coordinate is about to reach the edge of the screen, reset X coordinate and move Y coordinate down to start a new line
        if self.x > 480:
            self.x = 20
            self.y += 50


# main
root = Tk()
root.title("Roman Numerals")
root.geometry("950x350")
app = Application(root)
root.mainloop()
