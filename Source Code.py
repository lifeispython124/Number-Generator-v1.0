import tkinter as tk
import tkinter.font as tkFont
import random

VER = "1.0"

app = tk.Tk()
app.title("Random Number Generator v" +VER)
app.geometry("500x250")

font_style = tkFont.Font(family="Segoe UI Bold", size=50)
font_style2 = tkFont.Font(family="Segoe UI Bold", size=40)

label = tk.Label(app, text="", font=font_style)
label.pack(pady=20)

def gen():
    number = random.randint(1, 250)
    label.config(text=str(number))

btn = tk.Button(app, text="Generate", command=gen, font=("Segoe UI", 16))
btn.pack(pady=20)


app.mainloop()
