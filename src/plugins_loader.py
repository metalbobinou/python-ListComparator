import os
import sys

# Tools for loading modules and inspecting classes
import importlib
import inspect


# The parent class of the plugins
from plugins.PluginLogic import PluginLogic


# The directory containing the plugins
g_plugins_directory = "plugins"


class PluginsImporter:
    # List of classes imported from the plugins
    classes_list = []
    nb_classes = 0

    # State of the plugins
    nb_files = 0
    loaded = False

    def __init__(self):
        self.classes_list = []
        self.nb_classes = 0
        self.nb_files = 0
        self.loaded = False

    def LoadPlugins(self):
        # Do not reload plugins if they are already loaded
        if (self.loaded == True):
            return (-1)

        # Check if plugins directory exists
        directory = g_plugins_directory
        if (not (self.__dir_exists_and_not_empty(directory))):
            return (None)

        # List all the files in the "plugins" directory, and process them
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if (not os.path.isfile(filepath)):
                continue

            # Avoid the non python files / Filenames that do not ends by ".py"
            if (not (filename.split(".")[-1] == "py")):
                continue

            # Avoid the Parent class that could be loaded by every plugin
            if (filename == "PluginLogic.py"):
                continue

            # Count one more file loaded
            self.nb_files += 1

            # Build the name of module in python format : Dir.Class
            submodulename = os.path.splitext(filename)[0]
            modulename = directory + "." + submodulename

            # Import the module
            module = importlib.import_module(modulename)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                #print(obj)
                #print(obj.__name__)

                # Avoid loading the PluginLogic class
                if (obj.__name__ == "PluginLogic"):
                    continue

                # Add the class to the class container
                self.classes_list.append(obj)

        # Count how many classes were loaded
        self.nb_classes = len(self.classes_list)

        # Set the state as "loaded"
        self.loaded = True

        return (self.nb_classes)


    # Test if a directory exists and is not empty
    def __dir_exists_and_not_empty(self, directory):
        res = False
        if (os.path.exists(directory)):
            if (os.listdir(directory)):
                res = True
        return (res)

    # Return the list of loaded classes
    def GetClasses(self):
        return (self.classes_list)

    # Return the number of loaded classes
    def GetNbClasses(self):
        return (len(self.classes_list))

    # Return the number of files read
    def GetNbPluginsLoaded(self):
        return (self.nb_files)

    # Return the state of the loader
    def IsAlreadyLoaded(self):
        return (self.loaded)
