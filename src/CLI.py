import sys

# Plugin loader
from plugins_loader import PluginsImporter

# CSV loader (and saver)
from csv_manipulate import load_csv
from csv_manipulate import save_csv
from csv_manipulate import print_out_csv

# Logic operators
from basic_set_operators import ListSetOperators
from basic_occurrencies_operators import ListOccurrenciesOperators

# Tools for lists
from tools import occurrence


### SEARCH ONE ACTION TO DO FROM THE LISTS OF ACTIONS ###

def execute_action(list_1, list_2, action, MyPluginsImporter):
    # Execution of the desired action
    out_dict = []

    # Fundamental actions
    if (action == "CSV_1"):
        # Print CSV 1
        csv_1 = list_1
        out_dict = occurrence(csv_1)
        return (out_dict)

    if (action == "CSV_2"):
        # Print CSV 2
        csv_2 = list_2
        out_dict = occurrence(csv_2)
        return (out_dict)

    # Load internal functions first (set & occ) and search the verbs
    operations = get_set_actions() + get_occurrencies_actions()
    for operation in operations:
        # operation == [ name/action, lambda l1, l2 : Logic(l1, l2) ]
        verb = operation[0]
        #function = operation[1] ### Contains a lambda
        if (action == verb):
            res = operation[1](list_1, list_2)
            out_dict = occurrence(res)
            return (out_dict)

    # Load plugins functions if action is not found in the integrated ones
    new_operations = get_plugins_actions(MyPluginsImporter)
    for operation in new_operations:
        verb = operation[0]
        #function = operation[1] ### Contains a lambda
        if (action == verb):
            res = operation[1](list_1, list_2)
            out_dict = occurrence(res)
            return (out_dict)

    print("!!! ERROR: ACTION NOT FOUND !!!")

    sys.exit(-2)

### USAGE PRINTERS ###

def print_usage(MyPluginsImporter):
    print_basic_usage()
    print("")
    print_set_usage()
    print("")
    print_occurrencies_usage()
    if (MyPluginsImporter.GetNbClasses() > 0):
        print("")
        print_plugins_usage(MyPluginsImporter)

def print_basic_usage():
    print("Usage: python CLI.py " \
          "<file_path_1> <separator1> <column_of_ID_1> " \
          "<file_path_2> <separator2> <column_of_ID_2> " \
          "<action> " \
          "<output_separator> [<output_file>]")
    print("")
    print("Write the output in the terminal if no <output_file> given or" \
          " if it is '-'")
    print("or write in the designated file (created if it does not exist)")
    print("")
    print("-- Actions --")
    print("CSV_1 : ")
    print("   Print only 1st CSV")
    print("CSV_2 : ")
    print("   Print only 2nd CSV")

def print_set_usage():
    print("-- Actions Set --")
    print(" [set] : operation working on sets (occurrencies not used)")
    for cls in ListSetOperators():
        name_str = str(cls.GetName(cls))
        help_str = str(cls.GetHelp(cls))
        print(name_str[0:32] + " : [set]")
        print("   " + help_str[0:256])

def print_occurrencies_usage():
    print("-- Actions Occurrencies/Categories --")
    for cls in ListOccurrenciesOperators():
        name_str = str(cls.GetName(cls))
        help_str = str(cls.GetHelp(cls))
        print(name_str[0:32] + " :")
        print("   " + help_str[0:256])

def print_plugins_usage(MyPluginsImporter):
    print("-- Actions Plugins --")
    for cls in MyPluginsImporter.GetClasses():
        name_str = str(cls.GetName(cls))
        help_str = str(cls.GetHelp(cls))
        print(name_str[0:32] + " :")
        print("   " + help_str[0:256])

### LOADS ACTIONS FROM DIFFERENT FILES ###

def get_set_actions():
    set_actions = []
    for cls in ListSetOperators():
        name_str = str(cls.GetName(cls))
        #function = lambda l1, l2 : cls.Logic(cls, l1, l2)
        set_actions.append([name_str[0:32], lambda l1, l2 : cls.Logic(cls, l1, l2)])
    return (set_actions)

def get_occurrencies_actions():
    occ_actions = []
    for cls in ListOccurrenciesOperators():
        name_str = str(cls.GetName(cls))
        #function = lambda l1, l2 : cls.Logic(cls, l1, l2)
        occ_actions.append([name_str[0:32], lambda l1, l2 : cls.Logic(cls, l1, l2)])
    return (occ_actions)

def get_plugins_actions(MyPluginsImporter):
    plugins_actions = []
    for cls in MyPluginsImporter.GetClasses():
        name_str = str(cls.GetName(cls))
        #function = lambda l1, l2 : cls.Logic(cls, l1, l2)
        plugins_actions.append([name_str[0:32], lambda l1, l2 : cls.Logic(cls, l1, l2)])
    return (plugins_actions)

### MAIN ###

def main():
    # Load the plugins
    MyPluginsImporter = PluginsImporter()
    nb_plugins_classes = MyPluginsImporter.LoadPlugins()

    # Test if enough parameters were given
    if ((len(sys.argv) < 9) or ((len(sys.argv) > 10))) :
        print_usage(MyPluginsImporter)
        sys.exit(-1)

    # Arguments assignation
    file_path_1 = sys.argv[1]
    sep1 = sys.argv[2]
    id_col1 = int(sys.argv[3])

    file_path_2 = sys.argv[4]
    sep2 = sys.argv[5]
    id_col2 = int(sys.argv[6])

    action = sys.argv[7]
    out_sep = sys.argv[8]

    # Loading CSV in memory
    list_csv_1 = load_csv(file_path_1, sep1, id_col1)
    list_csv_2 = load_csv(file_path_2, sep2, id_col2)

    # Executing the asked action
    output_list = execute_action(list_csv_1, list_csv_2, action, MyPluginsImporter)

    # Write out the results
    if (len(sys.argv) == 10):
        out_file = sys.argv[9]
        save_csv(output_list, out_sep, out_file)
    else:
        print_out_csv(output_list, out_sep)

    return (0)

main()
