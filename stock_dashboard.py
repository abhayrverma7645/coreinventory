import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("CoreInventory - Stock Dashboard")
app.geometry("1000x600")

# ===== Sidebar =====
sidebar = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(sidebar, text="CoreInventory", font=("Arial",20,"bold"))
title.pack(pady=30)

menu_items = ["Dashboard","Operations","Products","Move History","Settings"]

for item in menu_items:
    btn = ctk.CTkButton(sidebar, text=item, width=160)
    btn.pack(pady=10)

# ===== Main Frame =====
main_frame = ctk.CTkFrame(app)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

header = ctk.CTkLabel(main_frame, text="Stock", font=("Arial",24,"bold"))
header.pack(anchor="w", pady=10)

# ===== Table Frame =====
table_frame = ctk.CTkFrame(main_frame)
table_frame.pack(fill="both", expand=True, pady=20)

columns = ("Product", "Per Unit Cost", "On Hand", "Free to Use")

table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, anchor="center", width=150)

table.pack(fill="both", expand=True)

# ===== Sample Data =====
data = [
    ("Desk", "3000 Rs", "50", "45"),
    ("Table", "3000 Rs", "50", "50")
]

for item in data:
    table.insert("", "end", values=item)

# ===== Update Stock Section =====
update_frame = ctk.CTkFrame(main_frame)
update_frame.pack(fill="x", pady=10)

product_label = ctk.CTkLabel(update_frame, text="Product")
product_label.grid(row=0,column=0,padx=10,pady=10)

product_entry = ctk.CTkEntry(update_frame)
product_entry.grid(row=0,column=1,padx=10)

qty_label = ctk.CTkLabel(update_frame, text="Update Quantity")
qty_label.grid(row=0,column=2,padx=10)

qty_entry = ctk.CTkEntry(update_frame)
qty_entry.grid(row=0,column=3,padx=10)

def update_stock():
    product = product_entry.get()
    qty = qty_entry.get()
    table.insert("", "end", values=(product,"-",qty,qty))

update_button = ctk.CTkButton(update_frame, text="Update Stock", command=update_stock)
update_button.grid(row=0,column=4,padx=20)

app.mainloop()
