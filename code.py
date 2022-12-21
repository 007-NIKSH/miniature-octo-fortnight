from tkinter import *
from tkinter import messagebox
import os
from time import *

os.system('clear')

class MAGIC_SQUARE:
    def __init__(self, root):
        self.root = root
        self.root.title("RAMANUJAN MAGIC SQUARE")
        self.root.geometry("1440x880")
        self.root.configure(bg = "black")

        numbers = []

        def Exit():
            self.root.destroy()

        def Empty_Check():
            a = Number_1.get()
            b = Number_2.get()
            c = Number_3.get()
            d = Number_4.get()

            if a == "" or b == "" or c == "" or d == "":
                messagebox.showinfo("ERROR", "INVALID INPUTS TO CREATE MAGIC SQUARE")
                return False
            
            elif int(a) > 9900 or int(b) > 9900 or int(c) > 9900 or int(d) > 9900:
                messagebox.showinfo("ERROR", "TOO BIG NUMBERS TO CREATE MAGIC SQUARE\n\nSELECT BETWEEN 0 - 9900")
                return False

            else:
                return True

        def Number_Creater():
            Numbers = [Number_1, Number_2, Number_3, Number_4]
            Check = Empty_Check()

            if Check == True:
                numbers.clear()

                for x in range(0, len(Numbers)):
                    num = Numbers[x].get()
                    numbers.append(num)
                    x += 1
                
                print(numbers)
                return True

        def Square_Creater():
            TF1 = Number_Creater()

            if TF1 == True:
                a = int(numbers[0])
                b = int(numbers[1])
                c = int(numbers[2])
                d = int(numbers[3])
                print(a)
                print(b)
                print(c)
                print(d)

                total.configure(text = a+b+c+d)

                Square_1.configure(text = a)
                Square_2.configure(text = b)
                Square_3.configure(text = c)
                Square_4.configure(text = d)

                Square_5.configure(text = d+1)
                Square_6.configure(text = c-1)
                Square_7.configure(text = b-3)
                Square_8.configure(text = a+3)

                Square_9.configure(text = b-2)
                Square_10.configure(text = a+2)
                Square_11.configure(text = d+2)
                Square_12.configure(text = c-2)

                Square_13.configure(text = c+1)
                Square_14.configure(text = d-1)
                Square_15.configure(text = a+1)
                Square_16.configure(text = b-1)

        title = Label(self.root, text = "RAMANUJAN MAGIC SQUARE", font = ("times new roman", 75, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        square_canvas = Canvas(self.root, width = 400, height = 300, bg = "gray")
        square_canvas.place(x = 800, y = 300)

        total_label = Label(self.root, text = " * NUMBERS * ", font = ("times new roman", 40, "bold"), bg = "gray", fg = "black", bd = 10, relief = GROOVE)
        total_label.place(x = 265, y = 150)

        Number_1 = Entry(self.root, font = ("times new roman", 20), bg = "gray", fg = "white")
        Number_1.place(x = 200, y = 250)

        Number_2 = Entry(self.root, font = ("times new roman", 20), bg = "gray", fg = "white")
        Number_2.place(x = 420, y = 250)

        Number_3 = Entry(self.root, font = ("times new roman", 20), bg = "gray", fg = "white")
        Number_3.place(x = 200, y = 350)

        Number_4 = Entry(self.root, font = ("times new roman", 20), bg = "gray", fg = "white")
        Number_4.place(x = 420, y = 350)

        total = Label(self.root, text = " * TOTAL * ", font = ("times new roman", 40, "bold"), bg = "gray", fg = "black", bd = 10, relief = GROOVE)
        total.place(x = 290, y = 450)

        total = Label(self.root, text = "    ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10, relief = GROOVE)
        total.place(x = 370, y = 550)

        Square_1 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_1.grid(row = 1, column = 1)

        Square_2 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_2.grid(row = 1, column = 2)

        Square_3 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_3.grid(row = 1, column = 3)

        Square_4 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_4.grid(row = 1, column = 4)


        Square_5 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_5.grid(row = 2, column = 1)

        Square_6 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_6.grid(row = 2, column = 2)

        Square_7 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_7.grid(row = 2, column = 3)

        Square_8 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_8.grid(row = 2, column = 4)


        Square_9 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_9.grid(row = 3, column = 1)

        Square_10 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_10.grid(row = 3, column = 2)

        Square_11 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_11.grid(row = 3, column = 3)

        Square_12 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_12.grid(row = 3, column = 4)


        Square_13 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_13.grid(row = 4, column = 1)

        Square_14 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_14.grid(row = 4, column = 2)

        Square_15 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_15.grid(row = 4, column = 3)

        Square_16 = Label(square_canvas, text = "     ", font = ("times new roman", 60, "bold"), bg = "gray", fg = "black", bd = 10)
        Square_16.grid(row = 4, column = 4)

        exit_button = Button(text = "    EXIT    ",  font = ("times new roman", 30, "bold"), command = lambda:Exit())
        exit_button.place(x = 100, y = 755)

        Create_button = Button(text = "  CREATE SQUARE  ",  font = ("times new roman", 30, "bold"), command = lambda:Square_Creater())
        Create_button.place(x = 350, y = 755)

        self.root.mainloop()

root = Tk()
MAGIC_SQUARE(root)
root.mainloop()
