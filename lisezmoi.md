La DoubleFace:

Présentation:
Programme fait par Chaker El Molghy dans le cadre des épreuves du BAC d'Informatique et Sciences du Numérique avec le professeur M.ESCOUTE du lycée Georges Clémenceau.
Codé en Python 3.6.5 en utilisant le module externe opencv-python (cv2).
Idée du programme issue de M.ESCOUTE et un professeur de philosophie du lycée.
Autres membres du groupe: Arthur Boulis, Hugo Dardalhon

Ce programme est une expérience vous permettant de constater ce que la symétrie de votre visage donne, ainsi que des explications à propos de quelques traits du visage en rapport avec votre personnalité. Il est possible de classer cela dans le domaine de la morphopsychologie. Les différentes personnalités d'une personne devraient être visibles par la symétrie de leurs visages (hémisphères du cerveau qui contrôlent différentes régions du corps et de l'esprit).

Comment utiliser le programme?
-Avoir installé Python(www.python.org/, 3) et le Module Opencv-python (cv2)(pypi.org/project/opencv-python/)
-Si les images 'doubledroite.png' et 'doublegauche.png' n'existent pas, lancez 'setup.exe'(à faire si c'est la première utilisation.)
-Double cliquer sur le fichier "GUI.py" du dossier ou l'exécuter depuis l'interpréteur.
-Suivre les instructions à l'écran

Bugs que vous pourriez rencontrer:
0)J'ai lancé le programme mais ça ne marche pas/je ne vois rien
    Vérifiez que la fenêtre du programme ne s'est pas caché sur la barre de tâches.
    Si vous ne le trouvez pas, vérifiez que vous avez ouvert GUI.py avec Python ou son interpréteur. Vérifiez aussi que vous avez Python 3.X au minimum.
    Si ca ne marche toujours pas, vérifiez que vous avez les modules nécessaires(modules hors-default; voir plus haut pour Opencv-python, modules par défaut; csv, random, tkinter).
    Si le problème n'est toujours pas résolu, essayez de lire le message d'erreur s'il y en a un et faites une recherche sur internet. 
    Sinon abandonnez.
1)L'onglet "Capture" gèle quand je prend une image
    Il est possible que durant la prise d'image l'onglet 'Capture' gèle, dans ce cas fermer l'onglet 'Capture' seulement, puis relancer la prise de photo. Si cela se répète, essayez de prendre une photo sous meilleures conditions(meilleur lumière par exemple)
2)J'ai pris mon image mais je n'arrive pas a la fermer
    Si cela vous arrive vous avez surement mal compris les instructions(qui peuvent en effet être un peu confuses). Une fois que votre image est prise et que vous avez la prévisualisation, il suffit d'appuyer sur la touche "X" de votre clavier. 
3)J'appuie sur 'Voir mes résultats mais rien n'apparait
    Cela peut arriver lorsque l'algorithme de reconnaissance faciale ne reconnaît pas de visage dans la photo(manque de lumière, mouvement, image floue). Il suffit de reprendre une image sous de meilleures conditions.
4)Les phrases d'explication sont coupées
    Votre écran est peut être trop petit pour le programme, essayez d'agrandir la fenêtre (carré à côté de la croix pour fermer la fenêtre). Si ca ne résout pas le problème et que vous voulez à tout prix consulter les phrases, vous pouvez ouvrir le fichier 'Phrases.csv' dans le dossier, je vous conseille de l'ouvrir avec Bloc-Notes plutôt qu'en tableur.
5) J'ai fermé le programme mais la lumière de la Webcam est resté allumée
    Commencez par vérifier que tous les onglets du programme sont fermés. Si le problème persiste suivez les instructions suivantes:
        -Faites un clic droit sur la barre de tâches Windows
        -Ouvrez "Gestionnaire des tâches"
        -Dans l'onglet "Processus", cherchez "Python" 
        -Faites un clic droit sur le processus et "Fin de tâche"

Toutes les images utilisées sont miennes.
Seul le fichier du classificateur 'haarcascade_frontalface_alt.xml', appartient à 
Copyright (C) 2000, Intel Corporation, tous les droits sont réservés, sous une licence Open Source(voir entête du fichier en question).

