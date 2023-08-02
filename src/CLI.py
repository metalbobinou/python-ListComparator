import sys

# CSV loader (and saver)
from csv_manipulate import load_csv
from csv_manipulate import save_csv
from csv_manipulate import print_out_csv

# Tools for lists
from tools import occurrence

# Logic operators
from logic_processing import union
from logic_processing import inter
from logic_processing import unique
from logic_processing import inv_inter
from logic_processing import disjoint_union
from logic_processing import unique_without_occurrence



def process_csv(file_path_1, sep1, id_col1,
                file_path_2, sep2, id_col2,
                action,
                out_sep):
                #out_csv, out_sep):
    list_1 = load_csv(file_path_1, sep1, id_col1)
    list_2 = load_csv(file_path_2, sep2, id_col2)

    if (action == "CSV_1"):
        # Print CSV 1
        occu_csv_1 = occurrence(list_1)
        dict_save = occu_csv_1

    if (action == "CSV_2"):
        # Print CSV 2
        occu_csv_2 = occurrence(list_2)
        dict_save = occu_csv_2

    if (action == "UNION"):
        # [set] Union of CSV 1 and CSV 2
        union_result = occurrence(union(list_1, list_2))
        dict_save = union_result

    if (action == "INTERSECTION"):
        # [set] Intersection of CSV 1 and CSV 2
        intersection_result = occurrence(inter(list_1, list_2))
        dict_save = intersection_result

    if (action == "INV_INTERSECTION"):
        # [set] Inverse of intersection of CSV 1 and CSV 2
        inv_intersection_result = occurrence(inter(list_1, list_2))
        dict_save = inv_intersection_result

    if (action == "UNIQUE_SET_CSV_1"):
        # [set] Unique value from CSV 1 (remove values from CSV 2)
        unique_set_1_result = occurrence(unique_without_occurrence(list_1, list_2, 1))
        dict_save = unique_set_1_result

    if (action == "UNIQUE_SET_CSV_2"):
        # [set] Unique value from CSV 2 (remove values from CSV 1)
        unique_set_2_result = occurrence(unique_without_occurrence(list_1, list_2, 2))
        dict_save = unique_set_2_result

    if (action == "UNION_DISJOINT"):
        # Union, but counts only one time the common elements
        union_disjoint_result = occurrence(disjoint_union(list_1, list_2))
        dict_save = union_disjoint_result

    if (action == "UNIQUE_CSV_1"):
        # Elements unique to CSV 1 (remove the occurrencies of CSV 2)
        unique_1_result = occurrence(unique(list_1, list_2, 1))
        dict_save = unique_1_result

    if (action == "UNIQUE_CSV_2"):
        # Elements unique to CSV 2 (remove the occurrencies of CSV 1)
        unique_2_result = occurrence(unique(list_1, list_2, 2))
        dict_save = unique_2_result

    #save_csv(dict_save, out_sep, out_csv)
    print_out_csv(dict_save, out_sep)


def print_usage():
    print("Usage: python CLI.py " \
          "<file_path_1> <separator1> <column_of_ID_1> " \
          "<file_path_2> <separator2> <column_of_ID_2> " \
          "<action> " \
          "<output_separator>")
          #"<output_file> <output_separator>")
    print("")
    print("-- Actions --")
    print("")
    print(" [set] : operation working on sets (occurrencies not used)")
    print("")
    print("CSV_1 : ")
    print("   Print only 1st CSV")
    print("CSV_2 : ")
    print("   Print only 2nd CSV")
    print("UNION : [set]")
    print("   Print all of the elements of the two CSV")
    print("INTERSECTION : [set]")
    print("   Print only the common elements of the two CSV")
    print("INV_INTERSECTION : [set]")
    print("   Print the inverse of the intersection (union - intersection)")
    print("UNIQUE_SET_CSV_1 : [set]")
    print("   Print elements unique to 1st CSV")
    print("UNIQUE_SET_CSV_2 : [set]")
    print("   Print elements unique to 2nd CSV")
    print("UNION_DISJOINT :")
    print("   Print union of the two CSV (add occurrencies)")
    print("UNIQUE_CSV_1 :")
    print("   Print elements unique to 1st CSV (delete occurrencies from the 2nd CSV)")
    print("UNIQUE_CSV_2 :")
    print("   Print elements unique to 2nd CSV (delete occurrencies from the 1st CSV)")

def main():
    #if (len(sys.argv) != 10):
    if (len(sys.argv) != 9):
        print_usage()
        sys.exit(-1)

    file_path_1 = sys.argv[1]
    sep1 = sys.argv[2]
    id_col1 = int(sys.argv[3])
    file_path_2 = sys.argv[4]
    sep2 = sys.argv[5]
    id_col2 = int(sys.argv[6])
    action = sys.argv[7]
    out_sep = sys.argv[8]

    #out_csv = sys.argv[8]
    #out_sep = sys.argv[9]

    process_csv(file_path_1, sep1, id_col1,
                file_path_2, sep2, id_col2,
                action,
                out_sep)
                #out_csv, out_sep)

    return (0)

main()
