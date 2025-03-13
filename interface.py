from tkinter import *
from tkinter import ttk

# Fonction pour afficher boutons cliqués
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(enter_val.get()))
            enter_val.set(result)
        except Exception as e:
            enter_val.set("Erreur")
    elif text == "C":
        enter_val.set("")
    elif text == "⌫":
        enter_val.set(enter_val.get()[:-1])    
    else:
        enter_val.set(enter_val.get() + text)


# Interface graphique
win = Tk()
win.geometry("300x460")
win.title("Malaldo Calculator")
win.configure(bg="lightblue")

# Zone d'affichage 
enter_val = StringVar()
entry = Entry(win, textvariable=enter_val, font=("Arial", 20), justify='right')
entry.pack(fill='both', ipadx=8, ipady=8, pady=10)

# Boutons de la calculatrice
boutons = [
    ['C', '⌫', '/'],
    ['1', '2', '3', '*'],
    ['4', '5', '6', '+'],
    ['7', '8', '9', '-'],
    ['.', '0', '=' ]
]

# Conteneur
frame = Frame(win)
frame.pack()

# Acceder aux lignes de boutons
for ligne in boutons:
    cont_boutons = Frame(frame) # Conteneur de boutons
    cont_boutons.pack(side='top') # Afficher le conteneur de boutons
    for touche in ligne: # Acceder aux touches de chaque ligne
        btn = Button(cont_boutons, text=touche, font=("Calibri", 15), width=5, height=2)
        btn.pack(side='left', padx=5, pady=5) # Afficher les boutons
        btn.bind('<Button-1>', on_click)

win.mainloop()
















