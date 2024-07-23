import tkinter as tk

root = tk.Tk()
root.geometry("325x500")
label = tk.Label(root, text="Welcome to our calculator!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3)
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text="7", font=("Arial", 16))
btn2 = tk.Button(buttonframe, text="8", font=("Arial", 16))
btn3 = tk.Button(buttonframe, text="9", font=("Arial", 16))
btnx = tk.Button(buttonframe, text="X", font=("Arial", 16))

btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btnx.grid(row=0, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 16))
btn5 = tk.Button(buttonframe, text="5", font=("Arial", 16))
btn6 = tk.Button(buttonframe, text="6", font=("Arial", 16))
btnmin = tk.Button(buttonframe, text="-", font=("Arial", 16))

btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
btnmin.grid(row=1, column=3, sticky=tk.W+tk.E)

btn7 = tk.Button(buttonframe, text="1", font=("Arial", 16))
btn8 = tk.Button(buttonframe, text="2", font=("Arial", 16))
btn9 = tk.Button(buttonframe, text="3", font=("Arial", 16))
btnplu = tk.Button(buttonframe, text="+", font=("Arial", 16))

btn7.grid(row=2, column=0, sticky=tk.W+tk.E)
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)
btnplu.grid(row=2, column=3, sticky=tk.W+tk.E)

btnbarazim = tk.Button(buttonframe, text="=", font=("Arial", 16), bg="blue", fg="white")
btnpluandmin = tk.Button(buttonframe, text="+/-", font=("Arial", 16))
btnzero = tk.Button(buttonframe, text="0", font=("Arial", 16))
btnpike = tk.Button(buttonframe, text=".", font=("Arial", 16))

btnbarazim.grid(row=3, column=3, sticky=tk.W+tk.E)
btnpluandmin.grid(row=3, column=0, sticky=tk.W+tk.E)
btnzero.grid(row=3, column=1, sticky=tk.W+tk.E)
btnpike.grid(row=3, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill="x")
root.mainloop()
