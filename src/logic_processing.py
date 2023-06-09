def inter(BN_ID_csv_1, BN_ID_csv_2):
    # Intersection des deux CSV
    intersec_liste = [x for x in BN_ID_csv_1 if x in BN_ID_csv_2]
    return intersec_liste


def union(BN_ID_csv_1, BN_ID_csv_2):
    # Union des deux CSV
    union_liste = BN_ID_csv_1 + BN_ID_csv_2
    return union_liste


def unique(BN_ID_csv_1, BN_ID_csv_2, choix):
    if choix == 1:
        unique_1 = set(BN_ID_csv_1) - set(BN_ID_csv_2)
        return list(unique_1)
    if choix == 2:
        unique_2 = set(BN_ID_csv_2) - set(BN_ID_csv_1)
        return list(unique_2)


def inv_inter(BN_ID_csv_1, BN_ID_csv_2):
    inv_inter_liste = set(union(BN_ID_csv_1, BN_ID_csv_2)) \
                      - set(inter(BN_ID_csv_1, BN_ID_csv_2))
    return list(inv_inter_liste)


def smart_union(BN_ID_csv_1, BN_ID_csv_2):
    smart_union_liste = BN_ID_csv_1 + unique(BN_ID_csv_1, BN_ID_csv_2, 2)
    return smart_union_liste


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

    return occu
