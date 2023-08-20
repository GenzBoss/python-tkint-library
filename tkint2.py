from tkinter import *

root= Tk()


def var_states():
    print("Warrior: %d, \nMage: %d" % (var1.get(), var2.get()))


Label(root,root.title("Adventure Game"),text=">>>>>>Your adventure role<<<<<<").grid(row=0, sticky=N)
var1 = IntVar()
Checkbutton(root,text="Warrior", variable=var1).grid(row=1,sticky=W)
var2 = IntVar()

Checkbutton(root, text = "Mage", variable=var2).grid(row=2, sticky=W)
Button(root,text='QUIT', command=root.destroy).grid(row=3,sticky=W,pady=4)
Button(root,text = 'Show', command= var_states).grid(row=3,sticky=E,pady=4)



#v = IntVar()
#Label(root,root.title("Options"),text="""Choose a preferred language:""", justify= LEFT, padx= 20).pack()
#Radiobutton(root,text="Python", padx = 20, variable=v, value=1).pack(anchor=W)

#Radiobutton(root, text="C++",padx = 20, variable=v,value=2).pack(anchor=W)


#logo = PhotoImage(file="sundevil.gif")
#w1 = Label(root, root.title("Python Fun"), image = logo).pack(side="right")
#content = """ I am new to being an independent learner i want to become a master coder and make great things"""

#w2 = Label(root,justify=LEFT,padx=10, text=content).pack(side="left")


mainloop()
