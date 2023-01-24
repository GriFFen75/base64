import unidecode

dico_lettre = {"A": 0,
               "B": 0,
               "C": 0,
               "D": 0,
               "E": 0,
               "F": 0,
               "G": 0,
               "H": 0,
               "I": 0,
               "J": 0,
               "K": 0,
               "L": 0,
               "M": 0,
               "N": 0,
               "O": 0,
               "P": 0,
               "Q": 0,
               "R": 0,
               "S": 0,
               "T": 0,
               "U": 0,
               "W": 0,
               "X": 0,
               "Y": 0,
               "Z": 0, }


def compteur_lettre():
    with open("FIC_les_tontons.txt", 'r') as f:
        for i in f:
            ligne_unicode = unidecode.unidecode(i)
            for j in dico_lettre.keys():
                nombre = ligne_unicode.lower().count(j.lower())
                dico_lettre[j] = dico_lettre.get(j) + nombre

    longueur = sum(dico_lettre.values())
    print(dico_lettre)
    print("nombre de lettres dans le texte :", longueur)

    for i in dico_lettre.keys():  # je l'ai fait en 2 boucles pour que ça sois plus visible à l'affichage
        dico_lettre[i] = "{:.2%}".format(dico_lettre[i] / longueur)
    print(dico_lettre)


compteur_lettre()

