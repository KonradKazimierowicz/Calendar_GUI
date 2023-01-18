from tkinter import *
import calendar


def Cal():
    gui = Tk()
    gui.config(background='light grey')
    gui.title("Calender of year")
    gui.geometry("775x900")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Helvetica 10 bold").pack()
    calYear.grid(row=5, column=1,padx=50)
    gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")
    cal = Label(new, text="Calendar",bg='grey',font=("arial", 28, "bold"))
    year = Label(new, text="Enter year", bg='green')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',fg='Black',bg='Green',command=Cal)

    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()
