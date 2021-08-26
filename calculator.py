from tkinter import*

root = Tk()
root.title("CALCULATOR")

op = Entry(root,width = 50, borderwidth=5,bg="black",fg ="white")
op.grid(row = 0,column = 0, padx = 40,pady =50,columnspan = 3)

root.configure(background='grey')

def button_number(numbers):
     current = op.get()
     op.delete(0,END)
     op.insert(0, str(current) + numbers)

def button_clear():
    op.delete(0,END)

def button_add():
    number_1 = op.get()
    global num  #global variable to remember  the prev number(temorarary stores in memory) 
    global cal  #to store the type of operation we are performing
    cal = "+"
    num = float(number_1)
    op.delete(0,END)

def button_sub():
    number_1 = op.get()
    global num #global variable to remember  the prev number(temorarary stores in memory) 
    global cal #to store the type of operation we are performing
    cal = "-"
    num = float(number_1)
    op.delete(0,END)

def button_mul():
    number_1 = op.get()
    global num #global variable to remember  the prev number(temorarary stores in memory) 
    global cal #to store the type of operation we are performing
    cal = "*"
    num = float(number_1)
    op.delete(0,END)         

def button_div():
    number_1 = op.get()
    global num #global variable to remember  the prev number(temorarary stores in memory) 
    global cal #to store the type of operation we are performing
    cal = "/"
    num = float(number_1)
    op.delete(0,END)

def button_rem():
    number_1 = op.get()
    global num #global variable to remember  the prev number(temorarary stores in memory) 
    global cal #to store the type of operation we are performing
    cal = "%"
    num = float(number_1)
    op.delete(0,END)

def button_eq(): 
    number_2 = op.get()  # get the second number
    op.delete(0,END)  #it clears  the entry but value stays in function 

    if cal == "+":
        op.insert(0,num + float(number_2))
    elif cal == "-":
        op.insert(0,num - float(number_2))    
    elif cal == "*":
        op.insert(0,num * float(number_2))
    elif cal == "/":
        op.insert(0,num / float(number_2))
    elif cal == "%":
        op.insert(0,num % float(number_2))


 

#creating button
myb1 =Button(root,text = "1",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("1"))
myb2 =Button(root,text = "2",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("2"))
myb3 =Button(root,text = "3",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("3"))
myb4 =Button(root,text = "4",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("4"))
myb5 =Button(root,text = "5",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("5"))
myb6 =Button(root,text = "6",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("6"))
myb7 =Button(root,text = "7",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("7"))
myb8 =Button(root,text = "8",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("8"))
myb9 =Button(root,text = "9",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("9"))
myb0 =Button(root,text = "0",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command=lambda: button_number("0"))
mybC =Button(root,text = "Clear",bg ="black",fg ="white",padx = 33,font=("Algerian", 16),pady=20,command = button_clear)
mybA =Button(root,text = "+",bg ="black",fg ="white",padx = 60,pady=20,font=("Helvetica", 16),command= button_add)
mybS =Button(root,text = "-",bg ="black",fg ="white",padx = 62,pady=20,font=("Helvetica", 16),command= button_sub)
mybM =Button(root,text = "*",bg ="black",fg ="white",padx = 62,pady=20,font=("Helvetica", 16),command= button_mul)
mybD =Button(root,text = "/",bg ="black",fg ="white",padx = 65,pady=20,font=("Helvetica", 16),command= button_div)
mybR =Button(root,text = "%(rem)",bg ="black",fg ="white",padx = 28,pady=20,font=("Algerian", 16),command= button_rem)
mybE =Button(root, text ="=",bg ="black",fg ="white",padx = 62,pady=20,font=("Helvetica", 16),command= button_eq)
mybdot = Button(root,text =".",bg ="black",fg ="white",padx = 62, pady =20,font=("Helvetica", 16), command = lambda: button_number("."))


#designing on screen
myb1.grid(row = 3, column = 0)
myb2.grid(row = 3, column = 1)
myb3.grid(row = 3, column = 2)
myb4.grid(row = 2, column = 0)
myb5.grid(row = 2, column = 1)
myb6.grid(row = 2, column = 2)
myb7.grid(row = 1, column = 0)
myb8.grid(row = 1, column = 1)
myb9.grid(row = 1, column = 2)
myb0.grid(row = 4, column = 1)
mybA.grid(row = 4, column = 0)
mybS.grid(row = 4, column = 2)
mybM.grid(row = 5, column = 0)
mybD.grid(row = 5, column = 1)
mybR.grid(row = 5, column = 2)
mybC.grid(row = 6, column = 0)
mybE.grid(row = 6, column = 1)
mybdot.grid(row = 6,column = 2)
root.mainloop()
