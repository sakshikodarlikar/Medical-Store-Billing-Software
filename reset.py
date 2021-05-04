import csv
from tkinter import *
from tkinter import messagebox

with open('medical.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    data.pop(0)
d=[]
for l in range(len(data)):
    d.append(str(data[l][0]))


root = Tk()
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
#root.attributes('-fullscreen', False)
root.state('zoomed')

item = []
quantity = []
op = []
price = []


def refresh(self):
    self.destroy()
    self.__init__()

def Search():
    listbox.delete(0, 'end')
    x1 = medEntry.get()
    op.clear()
    for i in range(len(data)):
        if (str(x1) in data[i][0]):
            op.append(data[i][0])
    for j in range(len(op)):
        listbox.insert(j+1,op[j])


def Add():
    global l4,l5,l6
    try:
        l4.destroy()
        l5.destroy()
        l6.destroy()
    except:
        pass
    if (str(op[listbox.curselection()[0]]) in item):
        quantity[item.index(op[listbox.curselection()[0]])] = quantity[item.index(op[listbox.curselection()[0]])] + 1

    else:
        item.append(op[listbox.curselection()[0]])
        quantity.append(1)
        price.append(data[d.index(op[listbox.curselection()[0]])][1])
    print(item,quantity)
    view()

def Subtract():
    global l4,l5,l6
    try:
        l4.destroy()
        l5.destroy()
        l6.destroy()
    except:
        pass
    try:
        if (str(op[listbox.curselection()[0]]) in item):
            quantity[item.index(op[listbox.curselection()[0]])] = quantity[item.index(op[listbox.curselection()[0]])] - 1
    except:
        messagebox.showerror("Error", "No Such Item Present")
    if (0 in quantity):
        item.pop(quantity.index(0))
        price.pop(quantity.index(0))
        quantity.pop(quantity.index(0))
        try:
            l4.destroy()
            l5.destroy()
            l6.destroy()
        except:
            pass
    print(item,quantity)
    view()

def reset ():
    global l4,l5,l6
    item.clear()
    price.clear()
    quantity.clear()
    refresh(root)
    main()

def view():
    global l4,l5,l6
    l1 = Label(root,text = "Item",font=("bold", 20))
    l1.place(x=800, y=270)
    l2 = Label(root,text = "Quantity",font=("bold", 20))
    l2.place(x=1200, y=270)
    l3 = Label(root,text = "Price",font=("bold", 20))
    l3.place(x=1400, y=270)

    try:
        l4.destroy()
        l5.destroy()
        l6.destroy()
    except:
        pass
    k = 0
    p = 0
    if item:
        for k in range(len(item)):
            l4 = Label(root,text = item[k],font=("bold", 20))
            l4.place(x=800, y=(320+40*k))
            l5 = Label(root,text = quantity[k],font=("bold", 20))
            l5.place(x=1200, y=(320+40*k))
            p = int(price[k])*int(quantity[k])
            l6 = Label(root,text = p ,font=("bold", 20))
            l6.place(x=1400, y=(320+40*k))
    if not item:
        try:
            l4.destroy()
            l5.destroy()
            l6.destroy()
        except:
            pass
        print("LOL")
        main()

def main ():
    root.geometry("%dx%d" % (width, height))
    #root.attributes('-fullscreen', False)
    root.state('zoomed')
    root.title("Billing Software")
    Head = Label(text = "SHREE PHARMACY",font=('Times New Roman', 35,'bold')).place(x=530, y=20)
    global listbox,medEntry,l4,l5,l6
    medName = Label(text = "Name of the product",font=("bold", 20)).place(x=100, y=250)
    medEntry = Entry(root, bd = 5, font = ('arial', 18,'bold'))
    medEntry.place(x=100, y=300)
    searchbtn = Button(root, text = "Search", width = 10, font = ('arial', 18,'bold'),command = Search).place(x=400,y=290)
    listbox = Listbox(root, width=45)
    listbox.place(x=100,y=400)


    addButton = Button(root, text = "+", width = 5, font = ('arial', 18,'bold'),command = Add).place(x=450,y=400)
    subButton = Button(root, text = "-", width = 5, font = ('arial', 18,'bold'),command = Subtract).place(x=450,y=470)
    resButton = Button(root, text = "Reset", width = 5, font = ('arial', 18,'bold'),command = reset).place(x=450,y=540)
    cart = Label(text = "Cart",font=("bold", 40)).place(x=1000, y=200)

    l1 = Label(root,text = "Item",font=("bold", 20))
    l1.place(x=800, y=270)
    l2 = Label(root,text = "Quantity",font=("bold", 20))
    l2.place(x=1200, y=270)
    l3 = Label(root,text = "Price",font=("bold", 20))
    l3.place(x=1400, y=270)

    root.mainloop()
main ()
