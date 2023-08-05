import sys

# Plugin loader
from plugins_loader import PluginsImporter


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
