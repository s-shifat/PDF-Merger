import tkinter as tk

# widgets............
# Labels
# Buttons
# Entry
# Text
# Frame
# ...................

window = tk.Tk()
window.title("Closer!")
label = tk.Label(text="Howdy?",
                 foreground="white",
                 background="blue")
button = tk.Button(text="Clicky",
                   fg="blue")
entry = tk.Entry(width=50)
entry.pack()
button.pack()
label.pack()

given = entry.get()
window.mainloop()
print(given)