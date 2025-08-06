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
root = Tk()
obj = LoginSystem(root)
root.mainloop()
