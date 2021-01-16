from tkinter import *
from tkinter import messagebox


def verify_user():
    user = Username_input.get()
    passw = password_input.get()

    if user == 'rahul' and passw == 'testcode':
        messagebox.showinfo("Success", "Successfully logged In")
    else:
        messagebox.showerror('Failed', "Invalid Credentials")


# Driver Code
if __name__ == "__main__":
    # Create root window
    root = Tk()
    # Change the title
    root.title('Login Form')
    # Change the window size
    root.geometry("400x240")
    # no resize for both directions
    root.resizable(False, False)

    # set gui widgets
    lbl_username = Label(root, text="Username : ",
                         font=('Helvetica', 12, 'bold'))
    lbl_password = Label(root, text="Password : ",
                         font=('Helvetica', 12, 'bold'))
    Username_input = Entry(root, width=20, bd="2", font=(
        'Helvetica', 14), relief=RIDGE)
    password_input = Entry(root, width=20, bd="2", font=(
        'Helvetica', 14), show='*', relief=RIDGE)
    btn_login = Button(root, text='Login', width=8,
                       command=verify_user, font=('Helvetica', 14), relief=RIDGE)

    # place geometry
    lbl_username.place(x=25, y=30)
    lbl_password.place(x=25, y=100)
    Username_input.place(x=140, y=30)
    password_input.place(x=140, y=100)
    btn_login.place(x=160, y=160)

    # start mainloop
    root.mainloop()
