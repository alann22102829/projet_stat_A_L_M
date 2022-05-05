# Importation des modules
from random import uniform , randint
import tkinter as tk
from math import sqrt
import os as os
import pandas

# Création des fonctions
# PARTIE 1

def creer_fichier_alea(nb, nomfichier):
    """
    Fonction qui prend un nb en entier et un nomfichier en string.
    Fonction quiva créer un fichier texte avec commme nom
    l'argument nomfichier, avec nbr de lignes correspondant a
    l'argument nb.
    Chaque ligne contiendra deux nbrs aleatoires flottants
    """
    file = open(nomfichier, "w", encoding="Utf-8")
    i = 0
    while i != nb:
        file.write(f"{uniform(0, 500)} {uniform(0, 500)}\n")
        i += 1
    file.close()


def lit_fichier(nomfic):
    """
    Fonction qui prend en argument un nom de fichier en string.
    Fichier qui contient deux coordonées par lignes séparés d'un espace
    Fonction va lire le fichier et renvoyer la liste des X et liste Y
    """
    if nomfic == "Fichier_alea":
        creer_fichier_alea(50, "Fichier_alea")
    file = open(nomfic, "r")
    listeX, listeY, = [], []

    for ligne in file:
        a = ligne.split()
        listeX.append(float(a[0]))
        listeY.append(float(a[1]))

    file.close()
    return listeX, listeY


def trace_Nuage(nomf):
    """
    Fonction qui prend en argument le nom d'un fichier en string.
    Fichier qui contient les coordonées des points d'un nuage.
    Fonction va appeler la fonction lit_fichier puis va représenter
    le nuage de points correspondant.Puis renverra le nombre de points
    dessinés.
    """
    global height, liste_y, liste_x, liste_tracer_droite
    canvas.delete("all")
    # Création des axes du graphique
    canvas.create_line(5, 595, 5, 10, fill="blue")
    canvas.create_line(5, 595, width-10, 595, fill="blue")
    liste_points = lit_fichier(nomf)
    for i in range(len(liste_points[0])):
        canvas.create_oval(float(liste_points[0][i]) + 5,  (height-5) - float(liste_points[1][i]),
                           float(liste_points[0][i]) + 9, ((height- 5) - float(liste_points[1][i])) + 4,
                           fill="red")

    nbr_points = len(liste_points[0])   # ou de liste_points[1]
    # récupère les deux listes de coordonées
    liste_x = liste_points[0].copy()
    liste_y = liste_points[1].copy()
    
    j = droite_reg(liste_x,liste_y)
    liste_tracer_droite.insert(0, j[1])
    liste_tracer_droite.insert(0, j[0])
    return nbr_points


def trace_droite(a, b):
    """
    Fonction qui prend duex flottants en arguments
    a = coefficient directeur et b =l'ordonée à l'origine.
    Tracer une droitye entre l'ordonée à l'origine et
    le coefficient directeur
    """
    global height, width, couleur, liste, peut_tracer, liste_x, liste_y, liste_tracer_droite
    #calcule de la correlation
    if len(liste_x) != 0:
        peut_tracer = forteCorrelation(liste_x, liste_y)
    
        
    if peut_tracer == True:
        fonction_lineaire = a * width + b
        x0 = 5
        y0 = b
        x1 = width       # longueur max de la droite
        y1 = fonction_lineaire
        ligne = canvas.create_line(x0, y0, x1, y1, fill= couleur, width=3)
        liste.append(ligne)


# Série de test partie 1
#creer_fichier_alea(50, "Fichier_alea")
#print(lit_fichier("Fichier_alea"))
# Les 2 tests si dessous s'éxécutent vers la fin du programme
#tk.Button(ecran, text="Graphique", command=lambda:print(trace_Nuage("Fichier_alea"))).grid()
#tk.Button(ecran, text="Trace_droite", command=lambda:(trace_droite(5, 4))).grid()


# PARTIE 2

def moyenne(serie):
    somme = 0
    for elt in serie:
        somme += float(elt)
    moyenne = somme / len(serie)
    return moyenne


def variance(serie):
    moyenne_serie = moyenne(serie)
    somme = 0
    for elt in serie:
        somme += (float(elt) - moyenne_serie)**2
    variance_serie = somme / len(serie)
    return variance_serie


def covariance(serieX, serieY):
    moyenne_serieX = moyenne(serieX) 
    moyenne_serieY = moyenne(serieY)
    produit = 0
    for i in range(len(serieX)):
        produit += (float(serieX[i]) - moyenne_serieX)*((float(serieY[i]) - moyenne_serieY))
    covariance_series = produit / len(serieX)
    return covariance_series


def correlation(serieX, serieY):
    variance_serieX = variance(serieX) 
    variance_serieY = variance(serieY)
    covariance_series = covariance(serieX, serieY)
    correlation_series = covariance_series / (sqrt(variance_serieX * variance_serieY))
    return correlation_series


def forteCorrelation(serieX, serieY):
    
    corr = correlation(serieX, serieY)
    if corr < 0.8 and corr > -0.8:
        return True
    else :
        return False
 
def droite_reg(serieX, serieY):
    a = covariance(serieX,serieY)/variance(serieX)
    b= moyenne(serieY) - a * moyenne(serieX)
    return (a,b)


def aide():
    os.system("start https://google.fr")


# Série de test partie 2
#print(moyenne([4, 6, 5, 6, 8, 4, 6, 5, 10, 5]))
#print(moyenne([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(variance([7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(covariance([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(correlation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(forteCorrelation([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))
#print(droite_reg([4, 6, 5, 6, 8, 4, 6, 5, 10, 5], [7, 5, 9, 6, 10, 8,9, 7, 8, 7]))


# PARTIE 3

def changer_couleur():
    global couleur, liste_couleur
    couleur = liste_couleur[randint(0, len(liste_couleur)-1)]

def desactiver():
    """
    Va retirer la fonctionalité d'ajouter des points manuellements.
    """
    global dessin
    dessin = False

def activer():
    """ 
    Va activer la fonctionalité d'ajouter des points manuellements.
    """
    global dessin
    dessin = True

def ajout_point(event):
    """ 
    Ajoute des points dès que l'on clique.
    """
    global liste_x, liste_y, dessin, liste
    if dessin == True:
        canvas.create_oval(event.x ,  event.y,
                           event.x + 4,  event.y + 4,
                           fill="red")
        liste_x.append(event.x)
        liste_y.append(event.y)
        if len(liste_x) > 2:                        # peut pas tracer de droites tant que l'on a pas plus de deux points
            if len(liste) != 0:                     # supprime la ligne précédante 
                canvas.delete(liste[-1])
            j = droite_reg(liste_x,liste_y)
            liste_tracer_droite.insert(0, j[1])
            liste_tracer_droite.insert(0, j[0])       

        
def extraire_info_fichier():
    """Préciser qu on a trouver cette idée sur internet totalist()"""
    global liste_x, liste_y, nombre_choisi
    canvas.delete("all")
    if nombre_choisi != 0:
        info_villes = pandas.read_csv("villes_virgule.csv")
        a = info_villes.loc[(info_villes["nb_hab_2010"] <= 500) & (info_villes["nb_hab_2012"] <= 500) , ["nb_hab_2010", "nb_hab_2012"]]
        # tolist() va permettre de récupérer les valeurs de la colone choisis dans la base qu'on a récupérer à la ligne précedante
        nb_2010 = a["nb_hab_2010"].tolist()             
        nb_2012 = a["nb_hab_2012"].tolist()
        
        file = open("donnees_villes_hab", "w")
        for i in range(nombre_choisi):
            file.write(f"{int(nb_2010[i])} {int(nb_2012[i])}\n")
        file.close()
        file_2 = open("donnees_villes_hab", "r")
        for i in range(nombre_choisi):
            ligne = file_2.readline()
            coords = ligne.split()
            liste_x.append(coords[0])
            liste_y.append(coords[1])
        file_2.close()
        for i in range(nombre_choisi):
            canvas.create_oval(float(liste_x[(i)]) ,  float(liste_y[i]),
                                float(liste_x[i]) + 4,  float(liste_y[i]) + 4,
                                fill="red")

        j = droite_reg(liste_x,liste_y)
        liste_tracer_droite.insert(0, j[1])
        liste_tracer_droite.insert(0, j[0])    



def extraire_info_fichier_2():
    """Préciser qu on a trouver cette idée sur internet totalist()"""
    global liste_x, liste_y, nombre_choisi
    canvas.delete("all")
    if nombre_choisi != 0:
        info_pourboires = pandas.read_csv("pourboire.csv")
        a = info_pourboires.loc[(info_pourboires["TOTBILL"] < 50) & (info_pourboires["TIP"] < 5) , ["TOTBILL", "TIP"]]
        # tolist() va permettre de récupérer les valeurs de la colone choisis dans la base qu'on a récupérer à la ligne précedante
        addition = a["TOTBILL"].tolist()             
        prix_pourboire =  a["TIP"].tolist()
        
        file = open("donnees_pourboires", "w")
        for i in range(nombre_choisi):
            file.write(f"{int(addition[i])} {int(prix_pourboire[i])}\n")
        file.close()
        file_2 = open("donnees_pourboires", "r")
        for i in range(nombre_choisi):
            ligne = file_2.readline()
            prix = ligne.split()
            liste_x.append(prix[0])
            liste_y.append(prix[1])
        file_2.close()
        for i in range(nombre_choisi):
            canvas.create_oval(float(liste_x[(i)]*10) ,  float(liste_y[i]*100),
                                float(liste_x[i]*10) + 4,  float(liste_y[i]*100) + 4,
                                fill="red")

        j = droite_reg(liste_x,liste_y)
        liste_tracer_droite.insert(0, j[1])
        liste_tracer_droite.insert(0, j[0])    

def valeur_entrer():
    global nombre_choisi
    nombre_choisi = int(entry.get())
    

# Programme Principale

# Constantes et Variables globale
width , height = 600, 600               # Taille de la fenêtre
liste = []
liste_couleur = ["green", "red", "yellow", "orange", "purple", "white", "pink"]
couleur = liste_couleur[randint(0, len(liste_couleur)-1)]
peut_tracer = True
liste_x, liste_y = [], []
dessin = False
liste_tracer_droite = [randint(0, 3), randint(5, width)]
nombre_choisi = 0




# Création de la fenêtre
ecran = tk.Tk()
ecran.geometry("1000x700")
ecran.title("Projet Statistiques descriptive à deux variables: droite de régression.")
ecran.config(bg="grey")

canvas = tk.Canvas(ecran, bg="blue", width=width, height=height)
canvas.grid(row=0 ,column=0, rowspan=11, pady=5, padx=5)


tk.Button(ecran, text="Trace_droite correlation", command=lambda:(trace_droite(liste_tracer_droite[0],liste_tracer_droite[1])))\
    .grid(row=1 ,column=1, padx=50)

tk.Button(ecran, text="Autre couleur", command=changer_couleur).grid(row=2 ,column=1, padx=50)


tk.Button(ecran, text="Nuages de points: Fichier Alea", command=lambda:trace_Nuage("Fichier_alea")).grid(row=4 ,column=1, padx=50)
tk.Button(ecran, text="Nuages de points: Fichier exemple.txt", command=lambda:trace_Nuage("exemple.txt")).grid(row=5,column=1, padx=50)

tk.Button(ecran, text="Quitter", command=ecran.quit).grid(row=10,column=1)


tk.Button(ecran, text="villes_virgules.csv", command=extraire_info_fichier).grid(row=6,column=1)
tk.Button(ecran, text="pourboire.csv", command=extraire_info_fichier_2).grid(row=6,column=2)

# ajout des boutons pour activer et désaactiver la partie dessin
tk.Button(ecran, text="Activer", command=activer).grid(row=9, column=1)
tk.Button(ecran, text="Désactiver", command=desactiver).grid(row=9, column=2)

tk.Label(ecran, text="Entrez le nombre de points que vous voulez. Doit être différente de 0 :").grid(row=7, column=1)
entry = tk.Entry(ecran, bg="white", fg="red")
entry.grid(row=8, column=1)
tk.Button(ecran, text="Valider", command=valeur_entrer).grid(row=8, column=2)

canvas.bind("<Button>", ajout_point)
ecran.mainloop()

