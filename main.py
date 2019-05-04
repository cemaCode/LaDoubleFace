# -*- coding: utf-8 -*-
# - EL MOLGHY Chaker TS06 - M.ESCOUTE - 2018-2019 - Projet ISN - La DoubleFace - #
import cv2  # Import de cv2(opencv-python module)
from tkinter.filedialog import askopenfilename
# Fichier classificateur reconaissance faciale
CascadeVisage = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Fonction reconnaissance faciale, pas de return mais cree varible gx pour découpage 
def posRecon():
    visage = CascadeVisage.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))  # Detection du visage par OpenCv
    x, y, w, h = visage[0] #Coordonées du visage sur l'image
    global gx  # Position du centre du visage
    gx = int(x + w / 2)


# Fonction prise de photo, pas de return mais cree var H, L et img Globales
def prise():
    global img #Image future à traiter
    global H, L #Hauteur et Largeur de l'image à traiter
    cap = cv2.VideoCapture(0)  # Debut de la capture Webcam
    check, frame = cap.read()
    if check == False: #Si l'ordinateur n'est pas équipé de Webcam
        path = askopenfilename(title="Ouvrir image") # On demande de choisir une image parmi les fichiers
        img = cv2.imread(path)
        img = cv2.flip(img, 1)# Webcam inverse gauche-droite, on re-inverse
        H, L = img.shape[:2] #On récupère les dimensions de l'image
        posRecon() #
    else:
        on = True  # Boucle permettant la prise de multiples images à la suite
        while on == True:
            check, frame = cap.read()
            H, L = frame.shape[:2] #On recupère les dimensions de l'image
            
            cv2.imshow("Capture", frame)  # On affiche la prise de photo
            key = cv2.waitKey(1)  #On attend l'utilisateur
            if key == 13:  # Si user input Enter, 13 = ord("enter")
                img = frame.copy()  # Prise de l'image à l'instant(img)
                img = cv2.flip(img, 1)# Webcam inverse gauche-droite, on re-inverse
                posRecon()  # Reconnaissance du visage sur l'image prise(img)
                cv2.imshow("Image", img)  # Affichage de img pour verification
                cv2.namedWindow("Capture", cv2.WINDOW_OPENGL)
                cv2.imwrite("shot.png", img)#Enregistrement de l'image originelle (img)
            if key == ord('x') or key == ord('X'):  # Si touche "X" appuié,
                cv2.destroyWindow("Capture")  # Quitter et fermer
                cv2.destroyWindow("Image")  # Quitter et fermer
                on = False
    

    

# Fonction creation de symetrie gauche, pas de return,creation et sauvgarde de 'doublegauche.jpg'
#Il faut noter que la gauche de l'image correspond à la droite du visage! 
def gauche():
    gauche = img[0:H, 0:gx]# Découpe du côté gauche de l'image, de 0(tout à gauche) à gx(milieu duvisage)
    gauche2 = gauche.copy()  # Copie du côté gauche
    gauche2 = cv2.flip(gauche2, 1)  # Symetrie sur l'axe 1(vertical) de l'image
    gg = cv2.hconcat((gauche, gauche2)) # Concatenation des deux "demi-images"
    gg = cv2.resize(gg, (int(L*0.75),int(H*0.75))) # On redimensionne l'image légerement 
    cv2.imwrite("doublegauche.png", gg)  # Enregistrement de l'image

# Fonction creation de symetrie droite, pas de return, creation et sauvgarde de 'doubledroite.jpg'
#Il faut noter que la gauche de l'image correspond à la droite du visage! 
def droite():
    droite = img[0:H, gx:L]# Découpe du côté droit de l'image, de gx(milieux du visage) à L(tout à droite)
    droite2 = droite.copy()  # Copie du côté droit
    droite2 = cv2.flip(droite2, 1)  # Symetrie sur l'axe 1(vertical) de l'image découpée 
    dd = cv2.hconcat((droite2, droite))  # Concatenation des deux "demi-images"
    dd = cv2.resize(dd, (int(L*0.75),int(H*0.75))) # On redimensionne l'image légerement
    cv2.imwrite("doubledroite.png", dd)  # Enregistrement de l'image
    
