from tkinter import *
from database import username, password
import tkinter as tk

def login():
    window = Tk()
    window.geometry("700x400")
    window.title("Login")
    window.configure(bg="#d6d6d6")

    def infocheck():
        usernameCheck = textFieldUsername.get()
        passwordCheck = textFieldPassword.get()
        
        if usernameCheck in username and passwordCheck in password:
            label1.config(text = "Login successfully.")
            print("\nUsername          : " + usernameCheck)
            print("Password          : " + passwordCheck)
            print("\nLogin successfully.")
            quit()

        window.after(1000, infocheck)

    font1 = ("poppins", 25, "normal")
    font2 = ("poppins", 15, "normal")

    labelUsername = tk.Label(window, font=font1, text="Username", bg="#d6d6d6")
    labelUsername.pack()
    textFieldUsername = tk.Entry(window, font=font1, bg="#d6d6d6")
    textFieldUsername.pack(pady=20)

    labelPassword = tk.Label(window, font=font1, text="Password", bg="#d6d6d6")
    labelPassword.pack()
    textFieldPassword = tk.Entry(window, font=font1, bg="#d6d6d6", show="*")
    textFieldPassword.pack()

    loginButton = tk.Button(window, font=("poppins", 15, "normal"), width=10, bg="#d6d6d6", text="login", command=infocheck)
    loginButton.pack(pady=20)

    label1 = tk.Label(window, font = font2, bg="#d6d6d6")
    label1.pack(pady = 20)

    window.mainloop()

def signup():
    window = Tk()
    window.geometry("700x500")
    window.title("Sign Up")
    window.configure(bg="#d6d6d6")

    def infocheck():
        usernameCheck = textFieldSignInUsername.get()
        passwordCheck = textFieldSignInPassword.get()
        confirmPasswordCheck = textFieldConfirmPassword.get()
        
        if usernameCheck not in username and passwordCheck == confirmPasswordCheck and passwordCheck != '' and confirmPasswordCheck != '':
            label1.config(text = "Sign Up successfully.")
            username.append(usernameCheck)
            password.append(passwordCheck)
            print("\nUsername          : " + usernameCheck)
            print("Password          : " + passwordCheck)
            print("Confirm Password  : " + confirmPasswordCheck)
            print("\nSign Up successfully.")
            quit()

        window.after(1000, infocheck)

    font1 = ("poppins", 25, "normal")
    font2 = ("poppins", 15, "normal")

    labelSignInUsername = tk.Label(window, font=font1, text="Username", bg="#d6d6d6")
    labelSignInUsername.pack()
    textFieldSignInUsername = tk.Entry(window, font=font1, bg="#d6d6d6")
    textFieldSignInUsername.pack(pady=20)

    labelSignInPassword = tk.Label(window, font=font1, text="Password", bg="#d6d6d6")
    labelSignInPassword.pack()
    textFieldSignInPassword = tk.Entry(window, font=font1, bg="#d6d6d6", show="*")
    textFieldSignInPassword.pack(pady=20)

    labelConfirmPassword = tk.Label(window, font=font1, text="Confirm Password", bg="#d6d6d6")
    labelConfirmPassword.pack()
    textFieldConfirmPassword = tk.Entry(window, font=font1, bg="#d6d6d6", show="*")
    textFieldConfirmPassword.pack()

    SignUpButton = tk.Button(window, font=("poppins", 15, "normal"), width=10, bg="#d6d6d6", text="sign up", command=infocheck)
    SignUpButton.pack(pady=20)

    label1 = tk.Label(window, font = font2, bg="#d6d6d6")
    label1.pack(pady = 20)

    window.mainloop()

def choice():
    window = Tk()
    window.title("Option")
    window.geometry("400x200")
    window.configure(bg="#d6d6d6")

    def loginFunc():
        window.destroy()
        login()

    def signupFunc():
        window.destroy()
        signup()

    OptionButton = tk.Button(window, font=("poppins", 15, "normal"), width=10, bg="#d6d6d6", text="Login", command=loginFunc)
    OptionButton.pack(pady=10)

    OptionButton2 = tk.Button(window, font=("poppins", 15, "normal"), width=10, bg="#d6d6d6", text="Sign Up", command=signupFunc)
    OptionButton2.pack(pady=10)

    window.mainloop()

def main():
    choice()

main()
