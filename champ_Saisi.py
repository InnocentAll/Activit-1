from tkinter import *
import tkinter as tkinter
from tkinter import *
fenetre=Tk()
fenetre.title("PLATEFORME D'ORIENTATION")
fenetre.geometry("900x550+180+50")
#**Tkinter** fournit de nombreuses methodes; l'une d'elles est **la méthode geometry()**. cette methode est utilisée pour définir la dimension de la fénetre tkinter, et est utilisée pour definir la position de la fenetre principale sur le bureau de l'utilisateur
#ma contribution
canvas=Canvas(fenetre,width=950,height=550,bg="pink")
canvas.place(x=0,y=0)
label=Label(canvas,bg="blue",text="BIENVENUE SUR VOTRE PLATREFORME D'ORIENTATION UNIVERSITAIRE EN LIGNE",font=('ariel',19,'bold'))
label.place(x=0,y=0)
identifiant=Label(canvas,text="Email ou numéro de telephone",font=('times new Roman',12))
identifiant.place(x=350,y=200)
champ=Entry(canvas,width=20,relief=FLAT,font=('times new Roman',10))
champ.place(x=380,y=250)
identifiant=Label(canvas,text="Votre mot de Pass",font=('times new Roman',12))
identifiant.place(x=382,y=300)
champ1=Entry(canvas,show="*",width=15,relief=FLAT,font=('times new Roman',10))
champ1.place(x=395,y=350)
