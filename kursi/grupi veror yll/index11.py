import tkinter as tk
import random
def display_funny_messages():
    messages = [
         "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I threw a boomerang a few years ago. I now live in constant fear.",
        "Why don’t skeletons fight each other? They don’t have the guts."
    ]
    message = random.choice(messages)
    label.config(text=message)
#Krijimi i window
root = tk.Tk()
root.title("Funny Messages App")
root.geometry("500x500")
root.configure(bg="#F0F0F0")
#Krijimi i Label
label = tk.Label(root, text="Click the button for a funny message!",
font=("Arial", 14), bg="#F0F0F0", fg="#C42D2D")
label.pack(pady= 20)
#Kijimi i buttonit
button = tk.Button(root, text="Make me Laugh!",
command= display_funny_messages,
font=("Arial", 14), bg="#F0F0F0", fg="#C42D2D")
button.pack(pady= 20)
root.mainloop()