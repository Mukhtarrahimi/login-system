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

root = Tk()
obj = LoginSystem(root)
root.mainloop()
