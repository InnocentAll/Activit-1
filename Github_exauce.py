from tkinter import*
import tkinter as tkinter


root=Tk()
root.title("plateforme d'orientation")
root.geometry("950*550+180+50")
#**Tkinter** fournit de nombreuses methodes; l'une d'elles est **la méthode geometry()**. cette methode est utilisée pour définir la dimension de la fénetre tkinter, et est utilisée pour definir la position de la fenetre principale sur le bureau de l'utilisateur

logo= Canvas(root, width=950, height=550, bg="#46B8E1")
logo.place(x=0, y=10)

logo=Label(logo, text="plateforme d'orientation", font=('arial', '19', 'blod'))
logo.place(x=20, y=10)

identifiant=Label(logo, text="E-mail ou telephone", bg="#46B8E1", font=('arial', 15, 'blod'), fg="#fff")
identifiant.place(x=400, y=140)

mdp=Label(logo, text="Mot de passer", bg="#46B8E1", font=('arial', 15, 'blod'), fg="#fff")
mdp.place(x=430, y=200)

identifiantEntry=Entry(logo, width=50, relief=PLAT, font=('arial', 12))
identifiantEntry.Entry(x=260, y=170)

mdpEntry=Entry(logo, width=50, show="*", relief=PLAT, font=('arial', 12))
mdpEntry.Entry(x=260, y=230)

root.mainloop()
