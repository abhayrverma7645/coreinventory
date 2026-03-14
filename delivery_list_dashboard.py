import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("CoreInventory - Delivery List")
root.geometry("900x500")
root.configure(bg="#111")

# Top Navigation
nav = tk.Frame(root, bg="#222", height=50)
nav.pack(fill="x")

menu_items = ["Dashboard", "Operations", "Products", "Move History", "Settings"]

for item in menu_items:
    btn = tk.Button(nav, text=item, bg="#333", fg="white", width=15)
    btn.pack(side="left", padx=5, pady=10)

# Title
title = tk.Label(root, text="Delivery", fg="white", bg="#111",
                 font=("Arial", 20))
title.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#111")
button_frame.pack(pady=5)

tk.Button(button_frame, text="NEW").pack(side="left", padx=5)
tk.Button(button_frame, text="Search").pack(side="left", padx=5)

# Table
columns = ("Reference", "From", "To", "Contact", "Schedule Date", "Status")

table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

table.pack(pady=20)

# Sample Data
data = [
    ("WH/OUT/0001", "WH/Stock1", "Vendor", "Azure Interior", "Today", "Ready"),
    ("WH/OUT/0002", "WH/Stock1", "Vendor", "Azure Interior", "Tomorrow", "Ready")
]

for row in data:
    table.insert("", tk.END, values=row)

root.mainloop()
