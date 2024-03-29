from PluginLogic import PluginLogic

# Vector of classes containing the function and its descriptors/infos
def ListSetOperators():
    SetOperations = []

    SetOperations.append(Union)
    SetOperations.append(Intersection)
    #SetOperations.append(Inv_Intersection)
    SetOperations.append(Unique_Both_Set)
    SetOperations.append(Unique_1_Set)
    SetOperations.append(Unique_2_Set)

    return (SetOperations)

# -- SETS OPERATIONS --
# Each element is taken into account only one time (occurrencies are not used)

# Union (set version)
class Union(PluginLogic):
    name_str = "UNION"
    help_str = "Print all of the elements of the two CSV"
    button_str = "Union"

    def Logic(self, list1, list2):
        union_res = set(list1).union(set(list2))
        return (union_res)

# Intersection (set version)
class Intersection(PluginLogic):
    name_str = "INTERSECTION"
    help_str = "Print only the common elements of the two CSV"
    button_str = "Intersection"

    def Logic(self, list1, list2):
        intersection_res = set(list1).intersection(set(list2))
        ## intersection_res = [x for x in list1 if x in list2]
        return (intersection_res)

# Inverse of Intersection (set version) [SYMMETRIC DIFFERENCE]
#class Inv_Intersection(PluginLogic):
#    name_str = "INV_INTERSECTION"
#    help_str = "Print the inverse of the intersection (union - intersection)"
#    button_str = "Inverse Intersection"
#
#    def Logic(self, list1, list2):
#        union = set(list1).union(set(list2))
#        intersection = set(list1).intersection(set(list2))
#        inv_intersection_res = set(union) - set(intersection)
#        return (inv_intersection_res)

# Unique elements to both CSV (delete commons elements)
class Unique_Both_Set(PluginLogic):
    name_str = "UNIQUE_SET_CSV_BOTH"
    help_str = "Print elements unique to both CSV / Symmetric difference"
    button_str = "Unique Both / Symmetric Diff"

    def Logic(self, list1, list2):
        unique_both_res = set(list1).symmetric_difference(set(list2))
        return (unique_both_res)

# Unique elements to 1st CSV (delete elements from the other) (set version)
class Unique_1_Set(PluginLogic):
    name_str = "UNIQUE_SET_CSV_1"
    help_str = "Print elements unique to 1st CSV / Difference CSV1 - CSV2"
    button_str = "Unique CSV 1 / Difference"

    def Logic(self, list1, list2):
        unique_1_res = set(list1).difference(set(list2))
        return (unique_1_res)

# Unique elements to 2nd CSV (delete elements from the other) (set version)
class Unique_2_Set(PluginLogic):
    name_str = "UNIQUE_SET_CSV_2"
    help_str = "Print elements unique to 2nd CSV / Difference CSV2 - CSV1"
    button_str = "Unique CSV 2 / Difference"

    def Logic(self, list1, list2):
        unique_2_res = set(list2).difference(set(list1))
        return (unique_2_res)
