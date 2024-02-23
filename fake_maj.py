import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk


# Liste des faux messages de mise à jour
update_messages = [
    "Vérification des mises à jour disponibles...",
    "Téléchargement des mises à jour en cours...",
    "Installation des mises à jour..."
]

# Fonction pour mettre à jour le message en fonction de la progression
def update_status_message(value):
    if value <= 32:
        status_label.config(text="Vérification des mises à jour disponibles...")
    elif value <= 77:
        status_label.config(text="Téléchargement des mises à jour en cours...")
    elif value <= 99:
        status_label.config(text="Installation des mises à jour...")

# Fonction pour mettre à jour la barre de progression
def update_progress(value=0):
    if value <= 100:
        progress_bar["value"] = value
        percent_label.config(text=f"{value}%", font=("Segoe UI Variable", 18))
        update_status_message(value)
        value += 1
        delay = random.randint(300, 1200)
        root.after(delay, update_progress, value)
    else:
        status_label.config(text="Mise à jour réussie !", font=("Segoe UI Variable", 16))
        root.after(3000, root.destroy)  # Ferme la fenêtre après 3 secondes

# Fonction pour empêcher la fermeture de la fenêtre avec Alt + F4
def disable_alt_f4():
    root.protocol("WM_DELETE_WINDOW", lambda: None)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Mise à jour Windows")

# Personnalisation du style pour un aspect de vieux BIOS
root.configure(bg='#0066CC')  # Fond bleu
root.overrideredirect(True)  # Supprimer les bordures de la fenêtre

# Mettre la fenêtre au premier plan
root.attributes('-topmost', True)

# Définir la taille de la fenêtre pour qu'elle couvre tout l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

image_path = "win.png"  # Remplacez "votre_image.png" par le chemin de votre image
img = Image.open(image_path)
img = img.resize((200, 200), Image.BICUBIC)   # Redimensionner l'image selon les besoins
photo = ImageTk.PhotoImage(img)

# Créer un label pour afficher l'image
image_label = tk.Label(root, image=photo, bg='#0066CC')
image_label.image = photo  # Garder une référence pour éviter la suppression par le garbage collector
image_label.pack(pady=2)

# Créer une étiquette pour afficher le message au-dessus de la barre de progression
status_label_top = tk.Label(root, text="Mise à jour obligatoire de votre système\nN'éteignez pas votre ordinateur", font=("Segoe UI Variable", 16), bg='#0066CC', fg='#FFFFFF')
status_label_top.pack(pady=(screen_height // 5, 0))

# Créer une étiquette pour afficher le pourcentage
percent_label = tk.Label(root, text="0%", font=("Segoe UI Variable", 16), bg='#0066CC', fg='#FFFFFF')
percent_label.pack()

# Créer une barre de progression horizontale
progress_bar = ttk.Progressbar(root, orient="horizontal", length=screen_width - 100, mode="determinate", style="Custom.Horizontal.TProgressbar")
progress_bar.pack(pady=2)

# Créer une étiquette pour afficher l'état de la mise à jour
status_label = tk.Label(root, text="", font=("Segoe UI Variable", 13), bg='#0066CC', fg='#FFFFFF')
status_label.pack()

# Lancer la mise à jour de la barre de progression
update_progress()

# Empêcher la fermeture de la fenêtre avec Alt + F4
disable_alt_f4()

# Lancer l'interface graphique
root.mainloop()
