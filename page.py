from cgitb import text
from tkinter import *
from tkinter import ttk

class login_page:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.configure(background='#D5EEBB')
        self.root.title(" LOGIN PAGE")

        us=StringVar()
        ps=StringVar()

        lbl_title=Label(self.root,text='Login Page',font=('roboto',37,'bold'),bg='#7FC8A9',fg='black')
        lbl_title.place(x=-60,y=0,width=1530,height=90)

        lbl_title=Label(self.root,text="User Name",bg='#5F7A61',fg='white',font=('roboto',20,'bold'))
        lbl_title.place(x=400,y=200,width=200,height=40)

        lbl_title=Label(self.root,text="Password",bg='#5F7A61',fg='white',font=('roboto',20,'bold'))
        lbl_title.place(x=400,y=300,width=200,height=40)
        
        Entry(self.root,text=us,font=('roboto',17,'bold'),bg='#7FC8A9',fg='black').place(x=700,y=300,width=200,height=40)
        Entry(self.root,text=ps,font=('roboto',17,'bold'),bg='#7FC8A9',fg='black').place(x=700,y=200,width=200,height=40)

        Button(self.root,text="Submit",font=('roboto',27,'bold'),bg='#7FC8A9').place(x=500,y=400,width=300,height=40)




if __name__=="__main__":
    root=Tk()
    obj=login_page(root)
    root.mainloop()