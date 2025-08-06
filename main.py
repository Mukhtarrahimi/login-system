from tkinter import  *
from tkinter import ttk
from PIL import Image, ImageTk
# class login
class LoginSystem():
    def __init__(self, root):
        print('Hello programer world')
        self.root = root
        self.root.title('Login System')
        self.root.geometry('1350x700+0+0')

        #  All image
        self.bg_icon = ImageTk.PhotoImage(file="images\bg.jpg") 
        self.user_icon = PhotoImage(file="images\user.png")
        self.password_icon = PhotoImage(file="images\password.png")
        
        bg_label = Label(self.root, image=self.bg_icon). pack()
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"),bg='yellow', fg='red', bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=0)
        
        
        login_frame = Frame(self.root, bg='white')
        login_frame.place(x = 400, y = 150)
        
        logo_label = Label(login_frame, image=self.user_icon).grid(row=0, column=0, pady=20)
        
        user_label = Label(login_frame, text="Username", compound=LEFT, font=("times new roman", 15, "bold"), bg='white').grid(row = 1, column=0, padx=20, pady=20)
        user_input = Entry(login_frame, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"), bg='light').grid(row=1, column=1, padx=20)
        
        password_label = Label(login_frame, text="Password", compound=LEFT, font=("times new roman", 15, "bold"))
        password_input = Entry(login_frame, bd=5, relief=GROOVE, font=("times new roman", 15, "bold"), bg='light').grid(row=2, column=1, padx=20)
        
        
        
        
root = Tk()
obj = LoginSystem(root)
root.mainloop()
