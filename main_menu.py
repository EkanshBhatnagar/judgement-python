from main import *
from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter.font import BOLD,Font


def get_input():
    no_of_players = int(entrybox1.get())
    max_cards = int(entrybox2.get())
    main_menu.quit()
    Game(no_of_players,max_cards)
    

main_menu = Tk()

canvas = Canvas(main_menu,width=1280, height=720)
canvas.pack()
img = Image.open("JPEG/honor_clubs.jpg")
img = img.resize((480,280), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

canvas.create_image(640,300,image = img)

entrybox1 = Entry(main_menu)
canvas.create_window(700,500,window=entrybox1)
entrybox2 = Entry(main_menu)
canvas.create_window(700,550, window=entrybox2)
heading_font = Font(main_menu, size = 25, weight = BOLD)
l_heading = Label(main_menu, text="Judgement!", font=heading_font)
canvas.create_window(640,100, window=l_heading)
l1 = Label(main_menu,text = "Enter Player No.")
canvas.create_window(550,500, window=l1)
l2 = Label(main_menu,text = "Enter Maximum Card Round")
canvas.create_window(550,550, window=l2)
btn = Button(main_menu, text="Start Game!", command=get_input)
canvas.create_window(600, 600, window=btn)
main_menu.resizable(False,True)
main_menu.mainloop()


