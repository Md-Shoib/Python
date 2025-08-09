import tkinter as tk

# def great():
#     name = entry.get()
#     label.config(text=f"hello, {name}")

def login():
    print((f"username: {username.get()}, password:{password.get()}"))

root = tk.Tk()
root.title("first app")
root.geometry("400x500")

# label = tk.Label(root, text="Enter your name..")

# label.pack()

# entry = tk.Entry(root)
# entry.pack()
# button = tk.Button(root, text="greaat", command=great)
# button.pack()

tk.Label(root,text="username").grid(row=0, column=0)
tk.Label(root,text="password").grid(row=1, column=0)

username = tk.StringVar()
password = tk.StringVar()

tk.Entry(root, textvariable=username).grid(row=0, column=1)
tk.Entry(root, textvariable=password).grid(row=1, column=1)

tk.Button(root, text="Login",command=login).grid(row=2, column=1)

root.mainloop()