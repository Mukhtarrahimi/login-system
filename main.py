from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#FACC15")  # Background color

        # Images (resize icons smaller)
        self.user_icon = ImageTk.PhotoImage(
            Image.open("images/user.png").resize((20, 20))
        )
        self.password_icon = ImageTk.PhotoImage(
            Image.open("images/password.png").resize((20, 20))
        )
        self.log_icon = ImageTk.PhotoImage(
            Image.open("images/logo.png").resize((80, 80))
        )

        # Variables
        self.name = StringVar()
        self.password = StringVar()

        # Title
        title = Label(
            self.root,
            text="Login System",
            font=("times new roman", 40, "bold"),
            bg="#FACC15",
            fg="red",
            bd=10,
            relief=GROOVE,
        )
        title.pack(pady=20)

        # Login Frame (centered)
        login_frame = Frame(self.root, bg="#FACC15")
        login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Logo
        logo_label = Label(login_frame, image=self.log_icon, bd=0, bg="#FACC15")
        logo_label.grid(row=0, columnspan=2, pady=20)

        # Username
        user_label = Label(login_frame, image=self.user_icon, bg="#FACC15")
        user_label.grid(row=1, column=0, padx=10, pady=10)
        user_input = Entry(
            login_frame,
            textvariable=self.name,
            bd=2,
            relief=GROOVE,
            font=("times new roman", 14),
            bg="#E5E7EB",
            fg="#4B5563",  # کمی تیره‌تر
            width=25,
        )
        user_input.grid(row=1, column=1, padx=10, pady=10)

        # Password
        password_label = Label(login_frame, image=self.password_icon, bg="#FACC15")
        password_label.grid(row=2, column=0, padx=10, pady=10)
        password_input = Entry(
            login_frame,
            textvariable=self.password,
            bd=2,
            relief=GROOVE,
            font=("times new roman", 14),
            bg="#E5E7EB",
            fg="#4B5563",  # کمی تیره‌تر
            width=25,
            show="*",
        )
        password_input.grid(row=2, column=1, padx=10, pady=10)

        # Login Button
        login_btn = Button(
            login_frame,
            text="Login",
            font=("times new roman", 14, "bold"),
            bg="#262F3E",
            fg="white",
            width=25,
            height=2,
            command=self.login,
        )
        login_btn.grid(row=3, columnspan=2, pady=20)

    def login(self):
        if self.name.get() == "admin" and self.password.get() == "admin":
            messagebox.showinfo("Success", "Login Success")
        elif self.name.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            messagebox.showerror("Error", "Invalid username or password")


root = Tk()
obj = LoginSystem(root)
root.mainloop()
