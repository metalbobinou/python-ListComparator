import sys

# Plugin loader
from plugins_loader import PluginsImporter

# Logic operators
from basic_set_operators import ListSetOperators
from basic_occurrencies_operators import ListOccurrenciesOperators
from basic_various_operators import ListVariousOperators

# Tools for lists
from tools import occurrence


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

def get_various_actions():
    var_actions = []
    for cls in ListVariousOperators():
        name_str = str(cls.GetName(cls))
        #function = lambda l1, l2 : cls.Logic(cls, l1, l2)
        var_actions.append([name_str[0:32], lambda l1, l2 : cls.Logic(cls, l1, l2)])
    return (var_actions)

def get_plugins_actions(MyPluginsImporter):
    plugins_actions = []
    for cls in MyPluginsImporter.GetClasses():
        name_str = str(cls.GetName(cls))
        #function = lambda l1, l2 : cls.Logic(cls, l1, l2)
        plugins_actions.append([name_str[0:32], lambda l1, l2 : cls.Logic(cls, l1, l2)])
    return (plugins_actions)


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

    # Load internal functions first (set & occ & var) and search the verbs
    operations = get_set_actions() + get_occurrencies_actions() + get_various_actions()
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

    sys.exit(-3)
