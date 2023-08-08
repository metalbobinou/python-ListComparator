# python-ListComparator

GUI and CLI tool for comparing lists.

Initially dedicated for comparing lists of terms, this tool can be use for any
type of lists.

This software can be extended with your own functions that takes two lists in
parameters. Just copy the *example_plugin.py* in the *plugins* folder, and
change the values (see in the __Plugins__ section later for details).

# Requirements:
- Python 3+
- csv (CSV Parser)
- Tkinter (GUI) *-- if using the GUI*
- *[Pandas (CSV Parser)] -- Very Optional*

# How to use:

## Graphical User Interface

Just call the graphical user interface by launching :

__sh ListComparator-GUI.sh__


## Command Line Interface

If you wish to automatize some comparisons, or make batchs, you can use the CLI.

__sh ListComparator-CLI.sh__

This command will show you the help. If an error occurs, make sure to remove
the plugins that would create a bug (from the *plugins* folder).
In order to use the CLI, you must give the two input CSV and some options, the
action to do, and the separator of output you wish (eventually the file where
to write, but as it's in a terminal, you can use the redirection tools for this).

Each CSV name is followed by the separator it uses and the column with the data
to compare. For example, for a first CSV named *file1.csv* that uses "," as a
separator and which data are in the 1st column , and a second CSV named
*file2.csv* that uses ";" as a separator and which data are in the 3rd column

__sh ListComparator-CLI.sh   "file1.csv" "," 0   "file2.csv" ";" 2  "UNION" ":"__

This line will execute the **UNION** operation on them and separate the output
columns with ":".

## Actions

The list of available actions is shown when you give no arguments to the CLI.
Just use the name in upper case at the left (like the "UNION", "INTERSECTION",
etc...)

# Plugins

In order to add your own operator for comparison, you can add some plugins.
To do so, just copy the *example_plugin.py* in the *plugins* folder, and
change the values.

__*classname*__ is the name of your class. You must keep the inheritance
from the **PluginLogic** in order for it to be callable later.

__name_str__ is the action for calling this function (32 chars max)

__help_str__ is the description appearing in the usage (256 chars max)

__button_str__ is the text appearing on the button in the GUI (32 chars max)

__Logic__ is the method/function that will be called. Do not change its
prototype. Just change the code, and keep in mind it must returns a list of
chars.
(You can return an answer like "True" or "False" alone in the list... but it
must be a list)

__*Do not change anything else, and do not change the name of any attribute or
method*__


# Contributors:
- BOISSIER Fabrice (Project Leader & Developper) [2023-...]
- LAUMONIER Quentin (Developper - Draft Version) [2023]
