from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("600x400")
        self.root.configure(bg="#FACC15")  # رنگ پس‌زمینه

        # Variables
        self.name = StringVar()
        self.password = StringVar()

        # Logo
        self.log_icon = ImageTk.PhotoImage(
            Image.open("images/logo.png").resize((80, 80))
        )
        logo_label = Label(self.root, image=self.log_icon, bg="#FACC15")
        logo_label.pack(pady=20)

        # Main Frame
        main_frame = Frame(self.root, bg="#FACC15")
        main_frame.pack(pady=10)

        # اندازه فرم‌ها و Input ها
        frame_width = 450
        frame_height = 50  # ارتفاع بیشتر برای کاربر پسند

        # Username Frame
        username_frame = Frame(
            main_frame, bg="#E5E7EB", width=frame_width, height=frame_height
        )
        username_frame.pack(pady=10)
        username_frame.pack_propagate(False)  # جلوگیری از تغییر اندازه فرم
        self.user_icon = ImageTk.PhotoImage(
            Image.open("images/user.png").resize((25, 25))  # کمی بزرگتر
        )
        Label(username_frame, image=self.user_icon, bg="#E5E7EB").pack(
            side=LEFT, padx=5
        )
        self.user_input = Entry(
            username_frame,
            textvariable=self.name,
            font=("times new roman", 14),  # فونت کمی بزرگتر
            bg="#E5E7EB",
            fg="#4B4F54",
        )
        self.user_input.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        # Password Frame
        password_frame = Frame(
            main_frame, bg="#E5E7EB", width=frame_width, height=frame_height
        )
        password_frame.pack(pady=10)
        password_frame.pack_propagate(False)
        self.password_icon = ImageTk.PhotoImage(
            Image.open("images/password.png").resize((25, 25))
        )
        Label(password_frame, image=self.password_icon, bg="#E5E7EB").pack(
            side=LEFT, padx=5
        )
        self.password_input = Entry(
            password_frame,
            textvariable=self.password,
            font=("times new roman", 14),
            bg="#E5E7EB",
            fg="#4B4F54",
            show="*",
        )
        self.password_input.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        # Login Button
        login_btn = Button(
            main_frame,
            text="Login",
            bg="#262F3E",
            fg="white",
            font=("times new roman", 14, "bold"),
            width=30,
            height=2,
            command=self.login,
        )
        login_btn.pack(pady=20)

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
