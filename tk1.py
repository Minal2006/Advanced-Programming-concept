
import tkinter as tk

root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)

root.mainloop()
