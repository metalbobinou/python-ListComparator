def inter(data, BN_ID_csv_1, BN_ID_csv_2):
    # Intersection des deux CSV
    intersec_csv = [x for x in BN_ID_csv_1 if x in BN_ID_csv_2]
    return intersec_csv


def union(data, BN_ID_csv_1, BN_ID_csv_2):
    # Union des deux CSV
    union_csv = BN_ID_csv_1 + BN_ID_csv_2
    return union_csv


def occurence(liste):
    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du fichier CSV
    for row in liste:
        valeur = row
        if valeur in occu:
            occu[valeur] += 1
        else:
            occu[valeur] = 1
