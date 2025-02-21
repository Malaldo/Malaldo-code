import tkinter as tk
from tkinter import scrolledtext, messagebox
from nltk.chat.util import Chat, reflections
import re 
from tkinter import ttk


paires = [
    (r"bonjour|salut|coucou", 
     [
        "Bonjour ! Comment puis-je vous aider ?",
        "Bonjour ! Je suis chargé de répondre aux questions concernant One Piece"
          ]),

      (r"comment (vas tu|vas-tu|tu vas) ?", ["Je vais bien 😀. Et vous ?"]),    

    (r"qui (cree|crée) (ce|le) chatbot|qui te (cree|crée)|qui est ton (createur|créateur) ?", 
     [
        "Ce chatbot est en train d'être créé par Malaldo"
          ]),

    (r"(qui es tu|qui es-tu|tu es qui|t'es qui|qu'es tu|qu'es-tu) ?", 
     [
        "Je suis un chatbot destiné à répondre aux questions concernant One Piece."
          ]),

    (r"comment (ça va|allez-vous) ?", 
     [
        "Je vais bien, merci ! Et vous ?"
          ]),


    (r"au revoir|bye", 
     [
        "Au revoir ! Passez une bonne journée."
          ]),

    (r"quel est le meilleur (manga|anime) (au monde|de tous les temps) ?", 
     [
        "Il s'agit de ONE PIECE."
          ]),

    (r"qui est le (personnage|perso) principal (de|dans) one piece ?", 
     [
        "Le personnage principal de One Piece est Monkey D. Luffy."
          ]),

    (r"qui est (Luffy|Monkey D luffy) ?", 
     [
       "Monkey D Luffy est le personnage principal du manga One Piece d'Eiichiro Oda.",
       "Luffy est le capitaine des Chapeaux de Paille.",
       "Monkey D. Luffy est un pirate qui rêve de devenir le roi des pirates.",
       "Luffy est le personnage principal de One Piece."
          ]),

(r"quel est le (rêve|reve) de Luffy ?", 
 [     
    "Le rêve de Luffy est de devenir le roi des pirates. Cependant, le véritable rêve de Luffy reste un mystère, non encore dévoilé par l'auteur."
        ]),

(r"(qui|quels) sont les membres de l'(équipage|equipage) (de luffy|au chapeau de paille) ?", 
 [
        "Les actuels membres de l'équipage au chapeau de paille sont : Luffy, Zoro, Nami, Usopp, Sanji, Chopper, Robin, Franky, Brook et Jinbei."
        ]),

(r"quel est le (reve|rêve) de (Zoro|Roronoa|Roronoa Zoro) ?", 
 [
    "Le rêve de Zoro est de devenir le meilleur sabreur au monde."
        ]),

(r"(qui sont les (freres|frères)|comment s'appellent les (freres|frères)) de luffy ?", 
 [
    "Les frères de Luffy sont Ace et Sabo."
        ]),

(r"quel est (l'arc|l'histoire|le chapitre) (le plus long|le plus court) dans one piece ?", 
 [
    "L'arc le plus long de One Piece est l'arc Wano. L'arc le plus court est souvent considéré comme l'arc Loguetown."
        ]),

(r"(peux-tu|pourrais-tu) me résumer l'arc marineford ?", 
 [
    "L'arc Marineford raconte la bataille entre Barbe Blanche et la Marine pour sauver Ace."
        ]),

(r"(peux-tu|pourrais-tu|peux tu|pourrais tu) me (résumer|resumer) l'arc dressrosa ?", 
 [
    "L'arc Dressrosa explore la chute de Doflamingo et le combat de l'équipage pour libérer le royaume."
        ]),

(r"(peux-tu|pourrais-tu|peux tu|pourrais tu) me (résumer|resumer) l'arc alabasta ?", 
 [
    "L'arc Alabasta est centré sur la guerre civile dans le royaume de Vivi et le combat contre Crocodile."
        ]),

(r"(peux-tu|pourrais-tu|peux tu|pourrais tu) me (résumer|resumer) l'arc wano ?", 
 [
    "L'arc Wano raconte la révolte contre Kaido et Orochi pour libérer le pays des samouraïs."
        ]),

(r"(qui est|comment s'appelle) le roi des pirates ?", 
 [
    "Gol D Roger est considéré comme le roi des pirates."
        ]),

(r"Qui est le mentor de Luffy ?", 
 [
    "Le mentor de Luffy s'appelle Shanks."
        ]),

(r"Qui sont les (quatre|4) empereurs", 
 [
    "Autrefois le groupe des 4 empereurs était composé de Edward Newgate(Barbe blanche), Kaido, Sharlotte Linlin(Big mom) et Shanks. Mais après la chute de Barbe blanche à Marineford et de Kaido et Big mom à Wano on assiste à la naissance de 3 nouveaux empereurs: Marshall D Teach(Barbe noire), Luffy et Baggy."
        ]),

(r"qui a produit One Piece|qui a (écrit|ecrit) One Piece|qui est le (créateur|createur) de One Piece ?", 
 [
    "Le mangaka qui écrit One Piece s'appelle Eiichiro Oda."
        ]),

(r"(qui est|comment s'appelle) le (pere|père) de luffy ?", 
 [
    "Le père de Luffy s'appelle Monkey D Dragon. C'est le commandant de l'armée révolutionnaire."
       ]),

(r"(c'est quoi le one piece|qu'est ce que le one piece|qu'est ce le one piece) ?",
   [
    "inconnu"
       ]),

(r"qui sont les grands corsaires ?", 
  [
    "inconnu"
      ]),

(r"(comment s'appelle|qui est) le grand (pere|père) de luffy ?",  
  [
    "Le grand-père de Luffy s'appelle Monkey D Garp"
      ]),

(r"quel est l'arc le plus long de one piece ?",  
  [ 
    "inconnu"
      ]),

(r"(Qui est le plus fort|quel est le personnage le plus puissant|qui est le plus puissant) (de|dans) one piece ?", 
 [
    "inconnu"
      ]),

(r"(quels|quelles) sont les (objectifs|buts|ambitions) des membres de l'équipage (de luffy|au chapeau de paille)", 
 [
     "inconnu"
     ]),

(r"Quand a (débuté|commencé|debute|commence) one piece|one piece a (commence|commencé|debute|débuté) quand ?", 
 [
    "inconnu"
      ]),

(r"(pourquoi zoro ne (rit|rie|ris) (pas|plus))|depuis quand zoro a (arrete|arrêté|arreté) de rire|depuis quand zoro ne (rit|ris|rie) (pas|plus)|quelle est la raison pour laquelle zoro ne (rit|ris|rie) (pas|plus) ?",
 [
    "inconnu"
      ]), 

(r"zoro (a|possede|posséde) combien de (sabres|sabre)|zoro se bat avec combien de (sabres|sabre)|combien de (sabres|sabre) (a|possede|posséde) zoro ?",
 [
    "inconnu"
      ]),

(r"qui est vegapunk|vegapunk est qui ?",
 [
    "inconnu"
      ]),

(r"comment sont les cheveux de sanji|les cheveux de sanji sont comment|de (quelle|quel) couleur sont les cheveux de sanji ?",
  [
    "inconnu"
      ]),

(r"quel était la prime de luffy à Arlong Park ?", 
 [
    "30 millions de berrys"
      ]),

(r"quel était la prime de luffy après alabasta ?",
  [
    "100 millions de berrys"
      ]),

(r"((a|à) combien s'(eleve|élève|éleve|éléve) la (premiere|première) prime|(quel|quelle) est la (premiere|première) prime) de Zoro ?",
  [
      "60 millions de berrys"
        ]),
                   
(r"Quel est le nom du premier bateau de l'équipage de Luffy ?", 
 [
    "Le Going Merry"
     ]),      

(r"Qui a (donné|donne) (son|le) chapeau de paille (à|a) Luffy ?",
 [
    "Shanks le Roux"
      ]),

(r"Quel (était|etait) le nom du sabre que Zoro a perdu contre Mihawk ?",
 [
     "Yubashiri"
      ]),

(r"Quelle est la prime actuelle de Luffy après l'arc de Wano ?",
 [
    "3 milliards de berrys"
      ]),

(r"Qui est le navigateur de l’(équipage|equipage) du Chapeau de Paille ?",
 [
    "Nami"
      ]),

(r" Qui a enseigné le Haki à Luffy ?",
 [
    "Silvers Rayleigh"
      ]),                                 
(r"Quel est le nom de l’arme antique qui repose sous l’(île|ile) des Hommes-Poissons ?",
 [
    "Poséidon"
      ]),

(r"Comment s’appelle la jeune fille riche qu’Usopp essaye de protéger ?",
 [
    "Kaya"
      ]),

(r"Comment s’appelle le majordome de Kaya qui est en réalité un pirate déguisé ?",
 [
    "Klahadoll (Capitaine Kuro)"    
      ]),

(r"Quel est le nom du village où Usopp vit au début de l’histoire ?",
 [
    "Village de Syrup"  
      ]),

(r"Comment s’appelle la sœur adoptive de Nami ?",
 [
    "Nojiko"
      ]),

(r"Qui est la princesse d’Alabasta ?", 
 [
    "Nefertari Vivi"
      ]),

(r"(qui est le plus fort entre (shanks|mihawk) et (mihawk|shanks))|((shanks|mihawk) vs (mihawk|shanks)) ?", 
 [
    "Mihawk bat Shanks à l'épée."
      ]),

(r"(quel est le (reve|rêve)|c'est quoi le (reve|rêve)) de Nami ?",
 [
     "Le rêve de Nami est de cartographier la terre entière."
      ]),

(r"(quel est le (reve|rêve)|c'est quoi le (reve|rêve)) de Sanji ?",
 [
    "Le rêve de Sanji est de découvrir All Blue."
      ]),

(r"(qui est vivi|vivi est qui) ?",
 [
    "Vivi est la princesse d'Alabasta."
     ]),

(r"qui a battu Arlong ?",
 [
    "Arlong a été battu par Luffy"
      ]),

(r"qui est le plus grand (epeiste|épéiste|sabreur|manieur de sabre) (au monde|(de|dans)one piece|) ?",
 [
    "Le plus grand sabreur de One Piece est Dracule Mihawk."
     ]),

(r"Quel est le concept du Davy Back Fight ?", ["Un jeu de pirates où l’équipage gagnant peut voler des membres de l’équipage adverse"]),

(r" Quel fruit du (démon|demon) possède Foxy ?", ["Le Noro Noro no Mi (Fruit du Ralentissement)"]),

(r"Quel membre de l’(équipage|equipage) de Luffy est (capturé|capture) en premier lors du Davy Back Fight ?", ["Chopper"]),

(r"Quel pirate (mystérieux|mysterieux) apparaît (à|a) la fin de l’arc Davy Back Fight ?", ["Aokiji"]),

(r"Quelle est la (spécialité|specialite) de la ville de Water 7 ?", ["La construction navale"]),

(r"Quel est le nom de l’entreprise de charpentiers la plus (célèbre|celebre) de Water 7 ?", ["Galley-La Company"]),

(r"Qui est le maire de Water 7 (et chef de Galley-La Company|) ?", ["Iceburg"]),

(r"Quel est le nom du groupe d’assassins infiltré dans Water 7 ?", ["CP9"]),

(r"Quel est le nom du chef du CP9|Qui déclenche le Buster Call sur Enies Lobby ?", ["Spandam"]),

(r"Quel est le véritable objectif du CP9 à Water 7 ?", ["Récupérer les plans de Pluton"]),

(r"Quel charpentier de Galley-La rejoint l’(équipage|equipage) de Luffy|Qui est la vraie (identité|identite) de Cutty Flam ?", ["Franky"]),

(r"Quel est le fruit du (démon|demon) de Rob Lucci ?", ["Neko Neko no Mi, modèle Léopard"]),

(r" Quel est le vrai but de Nico Robin en suivant le CP9 ?", ["Protéger l’équipage de Luffy en se livrant à la Marine"]),

(r"Qui sont les (quatre|4) membres du CP9 (infiltrés|infiltres) chez Galley-La ?", ["Rob Lucci, Kaku, Kalifa, Blueno"]),

(r"Quel est le nom du train qui relie Water 7 à Enies Lobby ?", ["Le Puffing Tom"]),

(r"Quel est l’objectif principal de l’équipage de Luffy à Enies Lobby ?", ["Sauver Nico Robin"]),

(r"Quelle phrase Robin dit-elle avant que l’(équipage|equipage) ne vienne la sauver ?", ["Je veux vivre !"]),

(r"Comment s’appelle la porte massive qui(sépare|separe)Enies Lobby d’Impel Down et Marineford ?", ["La Porte de la Justice"]),

(r"Qui Luffy affronte en duel à Enies Lobby ?", ["Rob Lucci"]),

(r"Quelle nouvelle transformation Luffy dévoile dans cet arc ?", ["Gear Second et Gear Third"]),

(r"Qui combat Kaku du CP9|Qui est la personne qui affronte Kuma pour protéger les Mugiwara|(qui est le deuxieme membre de l'(equipage|équipage) de luffy|qui a rejoint luffy en premier|(quel|qui) est la (premiere|première|premier) recrue de luffy) ?", ["Roronoa Zoro"]),

(r"Quelle est la dernière attaque que Luffy utilise pour vaincre Rob Lucci ?", ["Gomu Gomu no Jet Gatling"]),

(r"Comment Sanji aide-t-il l’équipage pendant la mission ?", ["Il coupe les communications du CP9 et ferme la Porte de la Justice"]),

(r"Quelle est la prime de Luffy après Enies Lobby ?", ["300 millions de berrys"]),

(r"Quel est le fruit du démon de Gecko Moria ?", ["Kage Kage no Mi (Fruit de l’Ombre)"]),

(r"Comment Moria utilise-t-il son pouvoir contre ses ennemis ?", ["Il leur vole leur ombre et l’insère dans des cadavres pour créer des zombies"]),

(r"Quel personnage de l’équipage rejoint officiellement Luffy à Thriller Bark ?", ["Brook"]),

(r"Quel est le nom du gigantesque zombie que Moria utilise comme arme ultime ?", ["Oars"]),

(r"Comment l’équipage est-il piégé sur Thriller Bark ?", ["Ils sont attirés par une mystérieuse barque en détresse et piégés par une brume étrange"]),

(r"Quel est le nom du scientifique fou travaillant pour Moria ?", ["Dr. Hogback"]),

(r"Quelle est la particularité du corps de Brook qui lui permet de survivre après la mort ?", ["Son Fruit du Démon, le Yomi Yomi no Mi"]),

(r"Qui combat Absalom et le bat ?", ["Sanji"]),

(r"Quel personnage mystérieux apparaît après la défaite de Moria ?", ["Bartholomew Kuma"]),

(r" Comment Zoro sauve-t-il Luffy après l’attaque de Kuma ?", ["Il prend toute la douleur et la fatigue de Luffy sur lui"]),

(r"Quelle phrase célèbre Zoro prononce après avoir pris la douleur de Luffy ?", ["Rien… rien ne s’est passé."]),

(r"Quel est le lien entre Brook et Laboon ?", ["Brook faisait partie de l’équipage qui avait promis de revenir voir Laboon"]),

(r"Quel est le secret derrière les zombies de Hogback ?", ["Ils sont créés en combinant des ombres volées et des cadavres"]),


(r"(.*)", ["Désolé, je ne suis pas en mesure de répondre. Essayez de reformuler autrement !!!."])
]





chatbot = Chat(paires, reflections)


# Fonction pour l'envoi de messages
def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        messagebox.showwarning("Attention", "Vous ne pouvez pas envoyer un message vide.")
        return
    chat_window.insert(tk.END, f"Vous : {user_message}\n", "user") 
    response = chatbot.respond(user_message)
    chat_window.insert(tk.END, f"Chatbot : {response}\n", "bot")  
    save_conversation(f"Vous : {user_message}\nChatbot : {response}\n")
    user_input.delete(0, tk.END) 
    chat_window.see(tk.END)  
    if user_message.lower() == "quit":  
       root.quit()
    
      
# Fonction pour la sauvegarde de discussions
def save_conversation(text):
    with open("historique_chat.txt", "a", encoding="utf-8") as file:
        file.write(text)

# Fonction pour la suppression de messages
def clear_conversation():
    chat_window.delete(1.0, tk.END)  
    with open("historique_chat.txt", "w", encoding="utf-8") as file:
        file.write("")  

# Fonction pour afficher les informations

# Configuration de la fenetre graphique
root = tk.Tk()
root.title("Chatbot Otaku")
root.geometry("700x600")
root.configure(bg="#f0f0f0")

# Zone utilisateur
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="#ffffff", fg="#000000")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.tag_config("user", foreground="#1E90FF")  
chat_window.tag_config("bot", foreground="#32CD32")  

# Entrée utilisateur
user_input = tk.Entry(root, font=("Arial", 14), bg="#e6e6e6")
user_input.pack(padx=10, pady=10, fill=tk.X)

# Styliser les boutons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), background="red")
style.configure("Green.TButton", background="green")


# Bouton pour envoyer
send_button = tk.ttk.Button(root, text="Envoyer", command=send_message, style="Green.TButton")
send_button.pack(pady=5)

# Bouton pour effacer
clear_button = tk.ttk.Button(root, text="Effacer l'historique", command=clear_conversation, style="TButton")
clear_button.pack(pady=5)

# Envoi de messages avec la touche entrée
user_input.bind("<Return>", lambda event: send_message())


chat_window.insert(tk.END, "Bienvenue dans le chatbot Otaku ! Tapez 'quit' pour quitter.\n", "bot")


root.mainloop()
