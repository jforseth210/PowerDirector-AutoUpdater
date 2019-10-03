# PowerDirector-AutoUpdater
A tool to automatically make Cyberlink PowerDirector reopen a file if it changes on disk. 
I created this tool to make using CyberLink PowerDirector 16 with git easier. Doing this offers a number of benefits in the form of branches, commits, etc. This works because PowerDirector's savefiles are basically just .txt files (You can even run git diff, though it isn't always human readable). However, the process can be somewhat combersome because you have to run your git command, then reopen the filesince PowerDirector doesn't detect changes on disk.

This script checks if the save file has changed, and if so, reopens it in PowerDirector. To get started simply clone my repo, and run the python file. Select the parent folder of your save file.

If you create a repo for your PowerDirector project, running a git command that modifies any "\*.pds" in the selected folder will automatically reopen the most recent file in PowerDirector. This is done by finding the file button, clicking it, and pressing the necessary combination of keystrokes to open the most recent file. 

This script could also be used to detect changes on shared network drives or the like.

_Disclaimers_

I am an amatuer. 
This was designed to be a solution for my specific version and configuration. It may require some tweaking to make it work for you. 
This software comes with absolutely NO WARRANTY. It uses the GUI automation tool pyautogui and may have unintended side effects. If you experience issues, feel free to add an issue or create a pull request.
Don't trust this script. It works for me, but I can't garauntee it will for you. 

Planned features (stuff I might add I if get a chance):
-Auto commit upon save. 
-Exe file
-Simple gui
