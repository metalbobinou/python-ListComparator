def occurrence(liste):
    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du fichier CSV
    for row in liste:
        valeur = row
        if valeur in occu:
            occu[valeur] += 1
        else:
            occu[valeur] = 1

    return occu
