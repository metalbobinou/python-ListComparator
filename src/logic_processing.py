# -- SETS OPERATIONS --
# Each element is taken into account only one time (occurrencies are not used)

def union(BN_ID_csv_1, BN_ID_csv_2):
    # Union au sens ensembliste
    union_liste = BN_ID_csv_1 + unique(BN_ID_csv_1, BN_ID_csv_2, 2)
    return union_liste

def inter(BN_ID_csv_1, BN_ID_csv_2):
    # Intersection des deux CSV
    intersec_liste = [x for x in BN_ID_csv_1 if x in BN_ID_csv_2]
    return intersec_liste

def inv_inter(BN_ID_csv_1, BN_ID_csv_2):
    # Inverse de l'intersection des deux CSV
    inv_inter_liste = set(union(BN_ID_csv_1, BN_ID_csv_2)) \
                      - set(inter(BN_ID_csv_1, BN_ID_csv_2))
    return list(inv_inter_liste)

def unique_without_occurrence(BN_ID_csv_1, BN_ID_csv_2, choix):
    # Elements uniques a un des CSV (suppression des elements de l'autre)
    #    (ensembliste : occurrences omises)
    if choix == 1:
        unique_1 = set(BN_ID_csv_1) - set(BN_ID_csv_2)
        return list(unique_1)
    if choix == 2:
        unique_2 = set(BN_ID_csv_2) - set(BN_ID_csv_1)
        return list(unique_2)


# -- CATEGORIES / OCCURRENCIES OPERATIONS --
# The set of origin is taken into account (occurrencies are used)

def disjoint_union(BN_ID_csv_1, BN_ID_csv_2):
    # Union (Disjointe) au sens categorie
    #   (ne compte qu'une fois chaque occurrence commune)
    disjoint_union_liste = BN_ID_csv_1 + BN_ID_csv_2
    return disjoint_union_liste

def unique(BN_ID_csv_1, BN_ID_csv_2, choix):
    # Elements uniques a un des CSV (suppression des elements de l'autre)
    #    (categorie : occurrences conservees)
    unique_values_1 = BN_ID_csv_1.copy()
    unique_values_2 = BN_ID_csv_2.copy()

    if (choix == 1):
        for value in BN_ID_csv_1:
            if (value in BN_ID_csv_2):
                if (value in unique_values_2):
                    unique_values_2.remove(value)
                    unique_values_1.remove(value)
        return unique_values_1
    if (choix == 2):
        for value in BN_ID_csv_2:
            if (value in BN_ID_csv_1):
                if (value in unique_values_1):
                    unique_values_1.remove(value)
                    unique_values_2.remove(value)
        return unique_values_2
