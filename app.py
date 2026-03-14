import tkinter as tk
from tkinter import messagebox

# Sample user database
users = {
    "admin": "1234",
    "user1": "password"
}

# Function to check login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", "Welcome " + username)
    else:
        messagebox.showerror("Error", "Invalid login ID or password")

# Function for sign up
def signup():
    messagebox.showinfo("Sign Up", "Redirecting to Sign-Up Page")

# Function for forgot password
def forgot_password():
    messagebox.showinfo("Forgot Password", "Redirecting to Password Reset Page")

# Create window
window = tk.Tk()
window.title("CoreInventory Login")
window.geometry("400x350")

# Logo / Title
label_logo = tk.Label(window, text="CoreInventory", font=("Arial", 20))
label_logo.pack(pady=20)

# Username
label_username = tk.Label(window, text="Login ID")
label_username.pack()

entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Password
label_password = tk.Label(window, text="Password")
label_password.pack()

entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Login button
btn_login = tk.Button(window, text="Login", width=15, command=login)
btn_login.pack(pady=10)

# Sign up button
btn_signup = tk.Button(window, text="Sign Up", command=signup)
btn_signup.pack(pady=5)

# Forgot password button
btn_forgot = tk.Button(window, text="Forgot Password", command=forgot_password)
btn_forgot.pack(pady=5)

window.mainloop()

