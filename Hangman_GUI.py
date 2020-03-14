from tkinter import *
import Word_Loader as word


def clicked_difficulty_btn(window, difficulty):
    return [window, difficulty]


def launch_main_window():
    main_window = Tk()
    main_window.title("3, 2, 1... Hangman!")
    main_window.geometry('500x500')
    main_window.resizable(0, 0)

    windowWidth2 = 500
    windowHeight2 = 500

    positionRight2 = int(main_window.winfo_screenwidth() / 2 - windowWidth2 / 2)          # Gets both half the screen width/height and window width/height
    positionDown2 = int(main_window.winfo_screenheight() / 2 - windowHeight2 / 2)

    main_window.geometry("+{}+{}".format(positionRight2, positionDown2))                  # Positions the window in the center of the page.

    main_window.mainloop()


def launch_welcome_window():
    difficulty_level = ""
    welcome_window = Tk()
    welcome_window.title("Hangman")
    welcome_window.geometry('300x200')

    windowWidth = welcome_window.winfo_reqwidth()                                           # Gets the requested values of the height and widht.
    windowHeight = welcome_window.winfo_reqheight()

    positionRight = int(welcome_window.winfo_screenwidth() / 2 - windowWidth / 2)           # Gets both half the screen width/height and window width/height
    positionDown = int(welcome_window.winfo_screenheight() / 2 - windowHeight / 2)

    welcome_window.geometry("+{}+{}".format(positionRight, positionDown))                   # Positions the window in the center of the page.

    welcome_window.resizable(0, 0)

    welcome_label = Label(welcome_window, text="Choose difficulty.\n", font=("Times new roman", 16))
    welcome_label.pack()
    welcome_label.place(relx=0.5, rely=0.15, anchor=CENTER)

    first_button = Button(welcome_window, text="   Easy  ", font=("Times new roman", 14), command=lambda: clicked_difficulty_btn(welcome_window, 0))
    first_button.pack()
    first_button.place(relx=0.5, rely=0.3, anchor=CENTER)

    second_button = Button(welcome_window, text="Medium", font=("Times new roman", 14), command=lambda: clicked_difficulty_btn(welcome_window, 1))
    second_button.pack()
    second_button.place(relx=0.5, rely=0.55, anchor=CENTER)

    third_button = Button(welcome_window, text="   Hard  ", font=("Times new roman", 14), command=lambda: clicked_difficulty_btn(welcome_window, 2))
    third_button.pack()
    third_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    welcome_window.mainloop()

