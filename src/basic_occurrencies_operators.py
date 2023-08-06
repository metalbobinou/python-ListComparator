from PluginLogic import PluginLogic

# Vector of classes containing the function and its descriptors/infos
def ListOccurrenciesOperators():
    OccOperations = []

    OccOperations.append(DisjointUnion)
    OccOperations.append(Unique_1_Occ)
    OccOperations.append(Unique_2_Occ)

    return (OccOperations)

# -- CATEGORIES / OCCURRENCIES OPERATIONS --
# The set of origin is taken into account (occurrencies are used)

# Disjoint Union (categories) (counts only one time the common elements)
class DisjointUnion(PluginLogic):
    name_str = "DISJOINT_UNION"
    help_str = "Print union of the two CSV (add occurrencies)"
    button_str = "Disjoint Union"

    def Logic(self, list1, list2):
        disjoint_union_res = list1 + list2
        return (disjoint_union_res)

# Unique elements to 1st CSV (deletes elements from the other) (occurrencies)
class Unique_1_Occ(PluginLogic):
    name_str = "UNIQUE_CSV_1"
    help_str = "Print elements unique to 1st CSV (delete occurrencies from the 2nd CSV)"
    button_str = "Unique CSV 1"

    def Logic(self, list1, list2):
        unique_1 = list1.copy()
        unique_2 = list2.copy()
        for value in list1:
            if (value in list2):
                if (value in unique_2):
                    unique_1.remove(value)
                    unique_2.remove(value)
        return (unique_1)

# Unique elements to 2nd CSV (deletes elements from the other) (occurrencies)
class Unique_2_Occ(PluginLogic):
    name_str = "UNIQUE_CSV_2"
    help_str = "Print elements unique to 2nd CSV (delete occurrencies from the 1st CSV)"
    button_str = "Unique CSV 2"

    def Logic(self, list1, list2):
        unique_1 = list1.copy()
        unique_2 = list2.copy()
        for value in list2:
            if (value in list1):
                if (value in unique_1):
                    unique_1.remove(value)
                    unique_2.remove(value)
        return (unique_2)
