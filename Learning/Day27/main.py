# Exercitiul 1

# import tkinter

# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()


# my_label["text"] = "Apasa te rog Butonul"



# # Button

# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)
    
# button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()

# # Entry

# input = tkinter.Entry(width=10)
# input.pack()
# print(input.get())


# window.mainloop()

# Exercitiul 2

# Mile to Km Converter

import tkinter

window = tkinter.Tk()
window.title("Km to Mile Converter")
window.minsize(width=400, height=40)

# Label
my_label1 = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
my_label1.grid(column=0, row=1)

# Entry

input = tkinter.Entry(width=10, font=("Arial", 16))
input.grid(column=1, row=0)


# Label
my_label2 = tkinter.Label(text=" KM", font=("Arial", 24, "bold"))
my_label2.grid(column=2, row=0)

# Label
my_label3 = tkinter.Label(text="0", font=("Arial", 24, "bold"))
my_label3.grid(column=1, row=1)

# Button

def button_clicked():
    km = float(input.get())
    calc = round(km / 1.609, 1)
    my_label3.config(text=calc)
    
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Label
my_label4 = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
my_label4.grid(column=2, row=1)


window.mainloop()