from tkinter import *


def clicked_button(window):
    window.destroy()
    main_window = Tk()
    main_window.title("3, 2, 1... Hangman!")
    main_window.geometry('500x500')

    main_window.mainloop()


def launch_game():

    welcome_window = Tk()
    welcome_window.title("Hangman")
    welcome_window.geometry('200x200')

    welcome_label = Label(welcome_window, text="     Choose difficulty.\n", font=("Times new roman", 16))
    welcome_label.grid(column=0, row=0)

    first_button = Button(welcome_window, text="   Easy  ", font=("Times new roman", 14), command= lambda: clicked_button(welcome_window))
    first_button.grid(column=0, row=3)

    second_button = Button(welcome_window, text="Medium", font=("Times new roman", 14), command= lambda: clicked_button(welcome_window))
    second_button.grid(column=0, row=5)

    third_button = Button(welcome_window, text="   Hard  ", font=("Times new roman", 14), command= lambda: clicked_button(welcome_window))
    third_button.grid(column=0, row=7)

    welcome_window.mainloop()

launch_game()
