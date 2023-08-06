from PluginLogic import PluginLogic

# Vector of classes containing the function and its descriptors/infos
def ListVariousOperators():
    VariousOperations = []

    VariousOperations.append(IsDisjoint)
    VariousOperations.append(IsSubset)
    VariousOperations.append(IsSuperset)

    return (VariousOperations)

# -- VARIOUS OPERATIONS --
# Various tests about the lists

# Is Disjoint
class IsDisjoint(PluginLogic):
    name_str = "IS_DISJOINT"
    help_str = "Test if the lists are disjoints (do not have any common element)"
    button_str = "Is Disjoint ?"

    def Logic(self, list1, list2):
        is_disjoint_res = set(list1).isdisjoint(set(list2))
        return ([str(is_disjoint_res)])

# Is Subset
class IsSubset(PluginLogic):
    name_str = "IS_SUBSET"
    help_str = "Test if CSV 1 is a subset of CSV 2 (CSV 1 is completely included in CSV 2)"
    button_str = "1 Is Subset of 2 ?"

    def Logic(self, list1, list2):
        is_subset_res = set(list1).issubset(set(list2))
        return ([str(is_subset_res)])

# Is Superset
class IsSuperset(PluginLogic):
    name_str = "IS_SUPERSET"
    help_str = "Test if CSV 1 is a superset of CSV 2 (CSV 1 contains the whole CSV 2)"
    button_str = "1 Is Superset of 2 ?"

    def Logic(self, list1, list2):
        is_superset_res = set(list1).issuperset(set(list2))
        return ([str(is_superset_res)])
