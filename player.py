import tkinter as tk

# widgets............
# Labels -- used to display text and images, display purpose only
#        -- can't be edited, kinda like print function
# Buttons
# Entry
# Text
# Frame
# ...................
# widget common parameters
# background, bd, bg, borderwidth, class,
#         colormap, container, cursor, height, highlightbackground,
#         highlightcolor, highlightthickness, menu, relief, screen, takefocus,
#         use, visual, width

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
