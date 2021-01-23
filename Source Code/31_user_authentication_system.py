from tkinter import *
from tkinter import messagebox
import mysql.connector as my


class signup_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up Window")
        self.root.geometry("500x340")
        self.root.resizable(False, False)

        lbl_title = Label(self.root, text="SIGN UP FORM", font=(
            "helvetica", 16, "bold"), fg="black").place(x=160, y=10)

        # ----------row 1---------
        lbl_fname = Label(self.root, text="First Name", font=(
            "helvetica", 12), fg="grey").place(x=20, y=50)
        self.txt_fname = Entry(self.root, font=("helvetica", 13),
                               bg="light grey")
        self.txt_fname.place(x=20, y=80, width=180)

        lbl_lname = Label(self.root, text="Last Name", font=(
            "helvetica", 12), fg="grey").place(x=250, y=50)
        self.txt_lname = Entry(self.root, font=("helvetica", 13),
                               bg="light grey")
        self.txt_lname.place(x=250, y=80, width=180)

        # ----------row 2---------
        lbl_contact = Label(self.root, text="Contact Number", font=(
            "helvetica", 12), fg="grey").place(x=20, y=120)
        self.txt_contact = Entry(self.root, font=("helvetica", 13),
                                 bg="light grey")
        self.txt_contact.place(x=20, y=150, width=180)

        lbl_email = Label(self.root, text="Email", font=(
            "helvetica", 12), fg="grey").place(x=250, y=120)
        self.txt_email = Entry(self.root, font=("helvetica", 13),
                               bg="light grey")
        self.txt_email.place(x=250, y=150, width=180)

        # ----------row 3---------
        lbl_pass = Label(self.root, text="Password", font=(
            "helvetica", 12), fg="grey").place(x=20, y=190)
        self.txt_pass = Entry(self.root, font=("helvetica", 13),
                              bg="light grey", show="*")
        self.txt_pass.place(x=20, y=220, width=180)

        lbl_cpass = Label(self.root, text="Confirm Password", font=(
            "helvetica", 12), fg="grey").place(x=250, y=190)
        self.txt_cpass = Entry(self.root, font=("helvetica", 13),
                               bg="light grey", show="*")
        self.txt_cpass.place(x=250, y=220, width=180)

        # ----------row 4---------
        btn_signup = Button(self.root, text="Sign Up", width=8, command=self.signup, font=(
            "helvetica", 13), relief=RIDGE, bd=2, cursor="hand2").place(x=20, y=265)

        lbl_msg = Label(self.root, text="Already, have an account login here ➤ ", font=(
            "helvetica", 12)).place(x=110, y=270)

        btn_login = Button(self.root, text="Login", width=8, command=self.login_window, font=(
            "helvetica", 13), relief=RIDGE, bd=2, cursor="hand2").place(x=385, y=265)

    def login(self):
        if self.txt_email.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror(
                "error", "All field are required", parent=self.root)
        else:

            try:
                # connection to the database
                con = my.connect(host='localhost', user='root',
                                 password='your password', database='students')
                cur = con.cursor()
                cur.execute("select * from students where email=%s and password= %s",
                            (self.txt_email.get(), self.txt_pass.get()))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror(
                        "error", "INVALID USERNAME AND PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo(
                        "Success", "Login successfully", parent=self.root)
                con.close()
                self.clear_login()
            except Exception as es:
                messagebox.showerror(
                    "error", f"error due to {es}", parent=self.root)

    def clear_login(self):
        self.txt_email.delete(0, END)
        self.txt_pass.delete(0, END)

    def login_window(self):
        login = Toplevel()
        self.root = login
        self.root.title("Login Window")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        lbl_title = Label(self.root, text="LOGIN HERE", font=(
            "helvetica", 16, "bold"), fg="black").place(x=120, y=10)

        lbl_email = Label(self.root, text="Email :", font=(
            "helvetica", 14), fg="black").place(x=40, y=70)
        self.txt_email = Entry(self.root, font=("helvetica", 12),
                               bg="light grey")
        self.txt_email.place(x=170, y=70, width=190, height=25)

        # ----------row 3---------
        lbl_pass = Label(self.root, text="Password :", font=(
            "helvetica", 14), fg="black").place(x=40, y=140)
        self.txt_pass = Entry(self.root, font=("helvetica", 14),
                              bg="light grey", show="*")
        self.txt_pass.place(x=170, y=140, width=190)

        btn_login = Button(self.root, text="Login", width=8, font=(
            "helvetica", 14), relief=RIDGE, bd=2, command=self.login, cursor="hand2").place(x=160, y=195)

    def clear_signup(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_cpass.delete(0, END)

    def signup(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_email.get() == "" or self.txt_contact.get() == "" or self.txt_pass.get() == "" or self.txt_cpass.get() == "":
            messagebox.showerror(
                "error", "All field are required", parent=self.root)
        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror(
                "error", "Password didn't matched", parent=self.root)
        else:
            try:
                # connection to the database
                con = my.connect(host='localhost', user='root',
                                 password='your password', database='students')
                cur = con.cursor()
                cur.execute("select * from students where email=%s",
                            (self.txt_email.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "error", "Already User Exists, Try with another email", parent=self.root)
                else:
                    cur.execute(
                        """insert into students (first_name,last_name,contact_number,email,password) values(%s,%s,%s,%s,%s)""", (self.txt_fname.get(), self.txt_lname.get(), self.txt_contact.get(), self.txt_email.get(), self.txt_pass.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Sign Up successfully", parent=self.root)
                self.clear_signup()
            except Exception as es:
                messagebox.showerror(
                    "error", f"error due to {es}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = signup_window(root)
    root.mainloop()
