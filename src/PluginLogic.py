### USE example_plugin.py FOR WRITING NEW OPERATIONS ###

###############################
### DO NOT MODIFY THIS FILE ###
###############################

### USE example_plugin.py FOR WRITING NEW OPERATIONS ###

class PluginLogic:
    # Name for calling this plugin
    name_str = "NAME_STR"

    # Text printed when calling the script with wrong parameters
    help_str = "HELP_STR"

    # Text of button in the GUI
    button_str = "BUTTON_STR"

    def __init__(self):
        return (None)

    # The main function doing something with the lists and returning a list
    def Logic(self, list1, list2):
        return (None)

    # Getter for the attributes
    def GetName(self):
        return (self.name_str)

    def GetHelp(self):
        return (self.help_str)

    def GetButton(self):
        return (self.button_str)
