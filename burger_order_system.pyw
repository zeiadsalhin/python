import os
from tkinter import *
from PIL import *
import webbrowser
import random

window = Tk()
window.state('zoomed')


def open():
    webbrowser.open_new("https://github.com/zeiadsalhin")


def sandwich():
    texts = Label(window, font=("Arial", 25), text="Select sandwich")
    texts.pack()

    bbeef = Button(window, font=("Arial", 40), text="Beef")
    bbeef.pack()

    bch = Button(window, font=("Arial", 40), text="Chicken")
    bch.pack()


# def cart():
#     cart = [5]
#     cartitems = (cart.__len__(), "total:", str(sum(cart)), "EGP")
#     entry.insert(0, cartitems)
#     return cart
#
#
# def total():
#     price = 0.14 * sum(cart()) + sum(cart())
#     pd = ("Your order total is: " + str(price) + " EGP")
#     entry.insert(0, pd)


def new():
    os.startfile("burger_order_system.pyw")


def restart():
    window.destroy()
    os.startfile("burger_order_system.exe")


def exit():
    window.destroy()


def openNewWindow():
    newWindow = Toplevel(window)


frame1 = LabelFrame(window, bg="gray", borderwidth=0)
frame1.pack()

menubar = Menu(window)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="restart", command=restart)
file_menu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file_menu)
window.config(menu=menubar)

window.title("Burger Order")
window.geometry("500x500")
window.minsize(500, 500)
window.iconbitmap("logo.ico")
window.config(bg="gray")
# frame = Frame(window, bd=1, relief=SOLID)
# frame.pack()

width = 80
height = 80
image = PhotoImage(file="bk.gif").zoom(15).subsample(30)
canvas = Canvas(frame1, width=width, height=height, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack(side=TOP)


def main():
    text1 = Label(frame1, font=("Arial", 25), text="Welcome to Burger King")
    text1.pack()

    text2 = Label(frame1, font=("Arial", 15), text="Order System")
    text2.pack()

    def next():
        canvas.destroy()
        text1.destroy()
        text2.destroy()
        button1.destroy()
        button2.destroy()
        entry.destroy()

        def meals():
            global cart

            def beef():
                def others():
                    def total():
                        cart = Label(window, font=("Bold", 40), text="Cart")
                        cart.pack(fill=X, pady=5)

                        items = Label(window, font=("Arial", 30), text="Items no")
                        items.pack(padx=20)
                        totali = Entry(window, font=("Roboto", 20))
                        totali.pack()
                        totalfinal = Entry(window, font=("Roboto", 20))
                        totalfinal.pack(fill=X)

                        def cart():
                            cart = []

                            cartitems = (cart.__len__())
                            totali.insert(0, cartitems)
                            return cart

                        def total():
                            price = 0.14 * sum(cart()) + sum(cart())
                            pd = ("Your order total is: " + str(price) + " EGP")
                            totalfinal.insert(0, pd)

                        total()


                        def conf():
                            text3 = Label(window, font=("Arial", 40), text="Your order no is")
                            text3.pack(pady=20, side=LEFT)

                            orn = Entry(window, font=("Arial", 61))
                            orn.pack(side=LEFT)

                            pr = (random.randint(1, 99))
                            orn.insert(0, pr)



                        conf()

                        salad.destroy()
                        fries.destroy()

                    salad = Button(frame1, text="Salad", font=("Arial", 40), command=total)
                    salad.pack(side=LEFT)
                    fries = Button(frame1, text="Fries", font=("Arial", 40), command=total)
                    fries.pack(padx=10)

                    chkn.destroy()
                    beefm.destroy()
                    single.destroy()
                    double.destroy()
                    large.destroy()
                    medium.destroy()
                    regular.destroy()

                single = Button(frame1, text="Single", font=("Arial", 40), command=others)
                single.pack(pady=20)
                double = Button(frame1, text="double", font=("Arial", 40), command=others)
                double.pack(pady=20)
                large = Button(frame1, text="large", font=("Arial", 40), command=others)
                large.pack(pady=20)
                medium = Button(frame1, text="medium", font=("Arial", 40), command=others)
                medium.pack(pady=20)
                regular = Button(frame1, text="regular", font=("Arial", 40), command=others)
                regular.pack(pady=20)

                chkn.destroy()
                beefm.destroy()

            def chicken():
                def others():
                    def total():
                        cart = Label(window, font=("Bold", 40), text="Cart")
                        cart.pack(fill=X, pady=5)

                        items = Label(window, font=("Arial", 30), text="Items no")
                        items.pack(padx=20)
                        totali = Entry(window, font=("Roboto", 20))
                        totali.pack()
                        totalfinal = Entry(window, font=("Roboto", 20))
                        totalfinal.pack(fill=X)

                        def cart():
                            cart = []

                            cartitems = (cart.__len__())
                            totali.insert(0, cartitems)
                            return cart

                        def total():
                            price = 0.14 * sum(cart()) + sum(cart())
                            pd = ("Your order total is: " + str(price) + " EGP")
                            totalfinal.insert(0, pd)

                        total()

                        def conf():
                            text3 = Label(window, font=("Arial", 40), text="Your order no is")
                            text3.pack(pady=20, side=LEFT)

                            orn = Entry(window, font=("Arial", 61))
                            orn.pack(side=LEFT)

                            pr = (random.randint(1, 99))
                            orn.insert(0, pr)

                        conf()

                        salad.destroy()
                        fries.destroy()

                    salad = Button(frame1, text="Salad", font=("Arial", 40), command=total)
                    salad.pack(side=LEFT)
                    fries = Button(frame1, text="Fries", font=("Arial", 40), command=total)
                    fries.pack(padx=10)

                    chkn.destroy()
                    beefm.destroy()
                    single.destroy()
                    double.destroy()
                    large.destroy()
                    medium.destroy()
                    regular.destroy()

                single = Button(frame1, text="Single", font=("Arial", 40), command=others)
                single.pack(pady=20)
                double = Button(frame1, text="double", font=("Arial", 40), command=others)
                double.pack(pady=20)
                large = Button(frame1, text="large", font=("Arial", 40), command=others)
                large.pack(pady=20)
                medium = Button(frame1, text="medium", font=("Arial", 40), command=others)
                medium.pack(pady=20)
                regular = Button(frame1, text="regular", font=("Arial", 40), command=others)
                regular.pack(pady=20)

                chkn.destroy()
                beefm.destroy()

            beefm = Button(frame1, text="Beef", font=("Arial", 40), command=beef)
            beefm.pack(side=TOP, padx=20, pady=20)

            chkn = Button(frame1, text="Chicken", font=("Arial", 40), command=chicken)
            chkn.pack(side=TOP, padx=20, pady=20)

        meals()

    button1 = Button(frame1, font=("Arial", 20), command=next, text="Order")
    button1.pack(side=TOP, pady=20)

    def contact():
        con = ("call: 144 6228 723")
        entry.insert(0, con)

    startb.destroy()

    button2 = Button(frame1, font=("Arial", 20), command=contact, text="Contact")
    button2.pack(side=TOP, pady=20)

    entry = Entry(frame1, font=("Roboto", 15))
    entry.pack()


button3 = Button(window, font=("Arial", 10), command=open, text="my github")
button3.pack(side=BOTTOM)

startb = Button(window, text="Start", font=("Italic", 20), command=main)
startb.pack(fill=X)

mainmenu = Button(frame1, text="Home", font=("Arial", 20), command=restart)
mainmenu.pack(pady=20)

window.mainloop()
