import sys

# Plugin loader
from plugins_loader import PluginsImporter

# CSV loader (and saver)
from csv_manipulate import load_csv
from csv_manipulate import save_csv
from csv_manipulate import print_out_csv

# Actions
from CliClasses.actions import execute_action

# Usages & Helper
from CliClasses.usages import print_usage


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
    output_list = execute_action(list_csv_1,
                                 list_csv_2,
                                 action,
                                 MyPluginsImporter)

    # Write out the results
    if (len(sys.argv) == 10):
        out_file = sys.argv[9]
        save_csv(output_list, out_sep, out_file)
    else:
        print_out_csv(output_list, out_sep)

    return (0)

main()
