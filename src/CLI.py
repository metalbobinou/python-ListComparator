import sys
from logic_processing import union
from logic_processing import inter
from logic_processing import occurence
from csv_manipulate import load_csv
from csv_manipulate import save_csv


def process_csv(file_path_1,
                separator1,
                column1,
                file_path_2,
                separator2,
                column2,
                action,
                nom_csv,
                separator3):
    BN_ID_csv_1 = load_csv(file_path_1,
                           separator1,
                           column1)
    BN_ID_csv_2 = load_csv(file_path_2,
                           separator2,
                           column2)

    if action == "CSV_1":
        occu_csv_1 = occurence(BN_ID_csv_1)
        dict_save = occu_csv_1
        print("\nBN_ID du premier CSV :\n")
        for key, value in occu_csv_1.items():
            print(f"{key} : {value} occurrence(s)")

    if action == "CSV_2":
        occu_csv_2 = occurence(BN_ID_csv_2)
        dict_save = occu_csv_2
        print("\nBN_ID du deuxième CSV :\n")
        for key, value in occu_csv_2.items():
            print(f"{key} : {value} occurrence(s)")

    if action == "INTERSECTION":
        intersection = occurence(inter(BN_ID_csv_1,
                                       BN_ID_csv_2))
        dict_save = intersection
        print("\nIntersection des BN_ID des deux CSV :\n")
        for key, value in intersection.items():
            print(f"{key} : {value} occurrence(s)")

    if action == "UNION":
        union_result = occurence(union(BN_ID_csv_1,
                                       BN_ID_csv_2))
        dict_save = union_result
        print("\nUnion des BN_ID des deux CSV :\n")
        for key, value in union_result.items():
            print(f"{key} : {value} occurrence(s)")

    save_csv(dict_save, separator3, nom_csv)


if __name__ == "__main__":
    if len(sys.argv) < 10:
        print("Usage: python CLI.py <file_path_1> <separator1> <column1> <file_path_2> <separator2> <column2> <action> <nom_csv> <separator3>")
        print("Différentes action :\nBN_ID du premier csv : CSV_1\nBN_ID du deuxième csv : CSV_2\nBN_ID de l\'intersection des 2 csv : INTERSECTION\nBN_ID de l'union des 2 csv : UNION")
        sys.exit(1)

    file_path_1 = sys.argv[1]
    separator1 = sys.argv[2]
    column1 = int(sys.argv[3])
    file_path_2 = sys.argv[4]
    separator2 = sys.argv[5]
    column2 = int(sys.argv[6])
    action = sys.argv[7]
    nom_csv = sys.argv[8]
    separator3 = sys.argv[9]

    process_csv(file_path_1,
                separator1,
                column1,
                file_path_2,
                separator2,
                column2,
                action,
                nom_csv,
                separator3)
