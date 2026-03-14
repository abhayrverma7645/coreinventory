import tkinter as tk

root = tk.Tk()
root.title("CoreInventory - Delivery Form")
root.geometry("900x550")
root.configure(bg="#111")

# Top Navigation
nav = tk.Frame(root, bg="#222", height=50)
nav.pack(fill="x")

menu_items = ["Dashboard", "Operations", "Products", "Move History", "Settings"]

for item in menu_items:
    btn = tk.Button(nav, text=item, bg="#333", fg="white", width=15)
    btn.pack(side="left", padx=5, pady=10)

# Title
title = tk.Label(root, text="New Delivery", fg="white",
                 bg="#111", font=("Arial", 20))
title.pack(pady=10)

# Action Buttons
actions = tk.Frame(root, bg="#111")
actions.pack(pady=5)

tk.Button(actions, text="Validate").pack(side="left", padx=5)
tk.Button(actions, text="Print").pack(side="left", padx=5)
tk.Button(actions, text="Cancel").pack(side="left", padx=5)

# Form
form = tk.Frame(root, bg="#111")
form.pack(pady=20)

tk.Label(form, text="Delivery Address", fg="white", bg="#111").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(form, width=30).grid(row=0, column=1)

tk.Label(form, text="Schedule Date", fg="white", bg="#111").grid(row=0, column=2, padx=10)
tk.Entry(form, width=30).grid(row=0, column=3)

tk.Label(form, text="Responsible", fg="white", bg="#111").grid(row=1, column=0, padx=10)
tk.Entry(form, width=30).grid(row=1, column=1)

tk.Label(form, text="Operation Type", fg="white", bg="#111").grid(row=1, column=2)
tk.Entry(form, width=30).grid(row=1, column=3)

# Product Table Header
product_frame = tk.Frame(root, bg="#111")
product_frame.pack(pady=20)

tk.Label(product_frame, text="Product", fg="white", bg="#111", width=30).grid(row=0, column=0)
tk.Label(product_frame, text="Quantity", fg="white", bg="#111", width=20).grid(row=0, column=1)

# Product Row
tk.Entry(product_frame, width=30).grid(row=1, column=0, pady=5)
tk.Entry(product_frame, width=20).grid(row=1, column=1)

tk.Button(root, text="Add New Product").pack(pady=10)

root.mainloop()
