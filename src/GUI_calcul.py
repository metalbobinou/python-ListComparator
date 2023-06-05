def BN_ID_data(data, BN_ID_csv, column):
    # Fonction pour remplir le canvas avec des résultats et leur occurrence

    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du DataFrame
    for row in BN_ID_csv:
        if column < len(row):
            # Vérifier si la valeur existe déjà dans le dictionnaire
            valeur = row
            if valeur in occu:
                occu[valeur] += 1
            else:
                occu[valeur] = 1

    # Afficher les résultats dans le canevas Tkinter
    for valeur, compte in occu.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


def inter(data, BN_ID_csv_1, BN_ID_csv_2):
    # Intersection des deux CSV
    intersec_csv = [x for x in BN_ID_csv_1 if x in BN_ID_csv_2]

    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du fichier CSV
    for valeur in intersec_csv:
        if valeur in occu:
            occu[valeur] += 1
        else:
            occu[valeur] = 1

    # Afficher les résultats dans le canevas Tkinter
    for valeur, compte in occu.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)


def union(data, BN_ID_csv_1, BN_ID_csv_2):
    # Union des deux CSV
    union_csv = BN_ID_csv_1 + BN_ID_csv_2
    print(union_csv)

    # Initialiser un dictionnaire pour stocker les occurrences
    occu = {}

    # Parcourir les lignes du fichier CSV
    for row in union_csv:
        valeur = row
        if valeur in occu:
            occu[valeur] += 1
        else:
            occu[valeur] = 1

    # Afficher les résultats dans le canevas Tkinter
    for valeur, compte in occu.items():
        texte = f"{valeur} : {compte} occurrence(s)"
        data.insert(0, texte)
