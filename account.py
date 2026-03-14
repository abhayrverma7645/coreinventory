import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# ---------------- DATABASE SETUP ----------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login_id TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT UNIQUE
)
""")

conn.commit()

# ---------------- VALIDATION FUNCTIONS ----------------

def validate_signup():

    login_id = entry_login.get()
    email = entry_email.get()
    password = entry_pass.get()
    confirm = entry_confirm.get()

    # Login ID validation
    if len(login_id) < 6 or len(login_id) > 12:
        messagebox.showerror("Error","Login ID must be between 6 and 12 characters")
        return

    # Email format check
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        messagebox.showerror("Error","Invalid email format")
        return

    # Password length
    if len(password) < 8:
        messagebox.showerror("Error","Password must be more than 8 characters")
        return

    # Password lowercase check
    if not re.search("[a-z]", password):
        messagebox.showerror("Error","Password must contain lowercase letter")
        return

    # Password uppercase check
    if not re.search("[A-Z]", password):
        messagebox.showerror("Error","Password must contain uppercase letter")
        return

    # Password special character check
    if not re.search("[!@#$%^&*()_+]", password):
        messagebox.showerror("Error","Password must contain special character")
        return

    # Confirm password check
    if password != confirm:
        messagebox.showerror("Error","Passwords do not match")
        return

    # Database uniqueness check
    cursor.execute("SELECT * FROM users WHERE login_id=?",(login_id,))
    if cursor.fetchone():
        messagebox.showerror("Error","Login ID already exists")
        return

    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    if cursor.fetchone():
        messagebox.showerror("Error","Email already exists")
        return

    try:
        cursor.execute("INSERT INTO users(login_id,email,password) VALUES(?,?,?)",
                       (login_id,email,password))
        conn.commit()

        messagebox.showinfo("Success","User Registered Successfully")

        entry_login.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        entry_pass.delete(0,tk.END)
        entry_confirm.delete(0,tk.END)

    except:
        messagebox.showerror("Error","Password already used")

# ---------------- GUI DESIGN ----------------

root = tk.Tk()
root.title("CoreInventory Sign Up")
root.geometry("420x520")
root.configure(bg="#1f3c88")

# Logo / Title
title = tk.Label(root,text="CoreInventory",font=("Arial",26,"bold"),
                 bg="#1f3c88",fg="white")
title.pack(pady=20)

subtitle = tk.Label(root,text="Create Your Account",
                    font=("Arial",14),
                    bg="#1f3c88",
                    fg="white")
subtitle.pack(pady=5)

# Frame
frame = tk.Frame(root,bg="white",padx=30,pady=30)
frame.pack(pady=20)

# Login ID
tk.Label(frame,text="Login ID",bg="white",font=("Arial",11)).pack(anchor="w")
entry_login = tk.Entry(frame,width=30)
entry_login.pack(pady=5)

# Email
tk.Label(frame,text="Email ID",bg="white",font=("Arial",11)).pack(anchor="w")
entry_email = tk.Entry(frame,width=30)
entry_email.pack(pady=5)

# Password
tk.Label(frame,text="Password",bg="white",font=("Arial",11)).pack(anchor="w")
entry_pass = tk.Entry(frame,width=30,show="*")
entry_pass.pack(pady=5)

# Confirm Password
tk.Label(frame,text="Re-enter Password",bg="white",font=("Arial",11)).pack(anchor="w")
entry_confirm = tk.Entry(frame,width=30,show="*")
entry_confirm.pack(pady=5)

# Signup Button
signup_btn = tk.Button(root,
                       text="Sign Up",
                       font=("Arial",12,"bold"),
                       bg="#ff6b6b",
                       fg="white",
                       width=15,
                       command=validate_signup)

signup_btn.pack(pady=20)

# Footer
footer = tk.Label(root,
                  text="Inventory Management System",
                  bg="#1f3c88",
                  fg="white",
                  font=("Arial",9))
footer.pack(side="bottom",pady=10)

root.mainloop()
