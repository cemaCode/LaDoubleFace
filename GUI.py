# -*- coding: utf-8 -*-
from tkinter import *
import main
from random import choice
import csv

#Initialisation/Preparation
fenetre = Tk()
#Configuration de la fenetre (titre/dimensions)
fenetre.title('La DoubleFace') 
fenetre.configure(width = 800, height = 600, bg = "ivory") 
fenetre.geometry("800x600")
#Mise en place de l'image de fond
BGimg = PhotoImage(file="fondBlur.png")
BGimg = BGimg.zoom(2) 
BG = Label(fenetre, image=BGimg)
BG.place(x=0, y=0,relwidth=1, relheight=1)

#Fonction qui met à jour les images traités à affihcer et leur légande
def refresh():  
    #Appel aux fonctions creatrices d'image(droite() et gauche())
    main.droite() 
    main.gauche() 
    #Récupération et actualisation des images sur les Labels ainsi que légendes 
    RdroiteN = PhotoImage(file="doubledroite.png") 
    RgaucheN = PhotoImage(file="doublegauche.png")
    droiteLab.configure(image=RdroiteN, text="Votre symétrie de droite")
    gaucheLab.configure(image=RgaucheN,text="Votre symétrie de gauche")
    droiteLab.image= RdroiteN
    gaucheLab.image= RgaucheN

#Fonction qui génère des phrases généralistes au hasard prises dans un fichier csv 
#Renvoie deux phrases (en une seule chaine) après avoir verifé que ce ne sont pas les mêmes
def phraseGen():
    with(open("Phrases.csv", encoding = 'utf-8', newline = '') ) as phrases:
        lecteur = csv.reader(phrases, delimiter = ';', )
        for phrase in lecteur:
            p1 = choice(phrase)
            p2 = choice(phrase)
            while p2 == p1:
                p2 = choice(phrase)
    p = p1 + "\n" +p2
    PhraseLab.configure(text = p)
    return p

#Présentations/Instructions + Button de prise de l'image
Titre = Label( text= "Bienvenu(e) dans La DoubleFace, retrouvez votre personnalité caché.", font = ('Calibri', 16,'bold')).pack(pady = 5)
FInstruc = Frame(fenetre)
instruc = Label(FInstruc,font = ("Calibri", 11), text="Instructions:\nCliquez sur 'Prendre une image', tenez vous droit(e) face à la webcam et appuiez sur la touche 'Entrée' du clavier.").pack()
instruc2 = Label(FInstruc,font = ("Calibri", 11), text="Vous aurez un aperçu de votre image, si elle est correcte appuiez sur la touche 'X' du clavier. Sinon appuiez sur 'Entrée' à nouveau. ").pack()
FInstruc.pack()
prisePhoto = Button(fenetre,font = ("Calibri", 11), text="Prendre une image", command=main.prise)
prisePhoto.pack()
instruc3 = Label(fenetre,font = ("Calibri", 11), text="Une fois que l'image est prise appuiez sur 'Voir le résultat'. Si cela ne marche pas reprenez une image.").pack()
#Boutton pour voir les résultats + Affichage des images
result = Button(text="Voir le résultat", font = ("Calibri", 11),command=refresh)
result.pack()
#Frame contenant images 
RFrame = Frame(fenetre)
RFrame.pack()
Rdroite = PhotoImage(file="doubledroite.png") # R pour résultat
Rgauche = PhotoImage(file="doublegauche.png")
#Légendes des images
droiteLab = Label(RFrame, image=Rdroite, text="Dernier utilisateur", compound=BOTTOM)
droiteLab.pack(side=RIGHT)
gaucheLab = Label(RFrame, image=Rgauche, text="Dernier utilisateur", compound=BOTTOM)
gaucheLab.pack(side=LEFT, expand = True)
#Button et Label pour les phrases explicatives
PhraseLab = Label(fenetre,font = ("Calibri", 11),text= "Demandez une explication pour certains caractères!" , width = 600)
PhraseLab.pack(fill ='x')
NewPhrase = Button(text= "Nouvelle Explication", command = phraseGen)
NewPhrase.pack()
#Button pour quitter le programme
quit = Button(fenetre, text="Quitter", command=fenetre.destroy)
quit.pack(side=BOTTOM)

fenetre.mainloop()
