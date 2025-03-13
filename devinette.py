import random
import tkinter as tk
from tkinter import messagebox

# Fonction pour démarrer une nouvelle partie
def nouvelle_partie():
    global nombre_a_deviner, essais, max_essais
    nombre_a_deviner = random.randint(1, 100)
    essais = 0
    max_essais = 10  # Limite du nombre d'essais
    label_essais.config(text=f"Essais restants: {max_essais - essais}")
    entry_nombre.delete(0, tk.END)
    label_message.config(text="Devinez un nombre entre 1 et 100")

# Fonction pour vérifier la devinette
def verifier_nombre():
    global essais
    try:
        devinette = int(entry_nombre.get())
    except ValueError:
        label_message.config(text="Veuillez entrer un nombre valide.")
        return

    essais += 1
    label_essais.config(text=f"Essais restants: {max_essais - essais}")

    if devinette < nombre_a_deviner:
        label_message.config(text="Plus grand.")
    elif devinette > nombre_a_deviner:
        label_message.config(text="Plus petit.")
    else:
        messagebox.showinfo("Félicitations !", f"Vous avez deviné le nombre en {essais} essais.")
        nouvelle_partie()
        return

    if essais >= max_essais:
        messagebox.showinfo("Dommage", f"Vous avez atteint la limite des essais. Le nombre était {nombre_a_deviner}.")
        nouvelle_partie()

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Jeu de Devinettes")

# Couleurs personnalisées
root.configure(bg='lightblue')

# Message d'acceuil
label_message = tk.Label(root, text="Devinez un nombre entre 1 et 100", bg='lightblue', fg='darkblue', font=('Helvetica', 14, 'bold'))
label_message.pack(pady=10) 

# Entree utilisateur
entry_nombre = tk.Entry(root, font=('Helvetica', 12)) 
entry_nombre.pack(pady=5) 

# Creer un bouton VERIFIER
bouton_verifier = tk.Button(root, text="Vérifier", command=verifier_nombre, bg='blue', fg='white', font=('Helvetica', 12, 'bold')) 
bouton_verifier.pack(pady=5) 

# Renseigner sur le nombre d'essais restants
label_essais = tk.Label(root, text="", bg='lightblue', fg='darkred', font=('Helvetica', 12)) 
label_essais.pack(pady=10)

# Envoi avec le bouton enter
entry_nombre.bind("<Return>", lambda event: verifier_nombre())

nouvelle_partie() 

# Lancer la fenetre
root.mainloop()