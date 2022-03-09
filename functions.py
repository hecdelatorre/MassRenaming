from bullet import Input, colors, YesNo
from colored import fg, attr
from os import listdir, rename
from os.path import isdir, isfile
from getpass import getuser

colorRed = fg('#CC0000')
colorGreen = fg('#73D216')
colorBlue = fg('#338CFF')
res = attr('reset')

def err():
    print(f'{colorRed}Wrong data{res}')
    exit()

def validateDir(directory): 
    if not isdir(directory): err()
    else: return directory 

def enterDirectory():
    directory = Input(f'{colorGreen}Enter the directory {res}', default = f"/home/{getuser()}/Downloads", word_color = colors.foreground["yellow"]).launch()
    directory = validateDir(directory)
    return directory

def traverseDirectory(directory):
    newName = Input(f'{colorGreen}Login in new name {res}', default = 'default', word_color = colors.foreground["yellow"]).launch()
    newExtension = Input(f'{colorGreen}Login in new extension {res}', default = 'default', word_color = colors.foreground["yellow"]).launch()

    directoryArray = listdir(directory)
    directorys = []
    
    print(f'Current name {colorBlue}::{res} New name')
    c = 0

    for dFile in directoryArray: 
        if isfile(f'{directory}/{dFile}'): 
            print(f'{dFile} {colorRed}::{res} {newName}-{c}.{newExtension}')
            c += 1
            directorys.append(dFile)

    return directorys, newName, newExtension

def renameDirectory(directory, directorys, newName, newExtension):
    renameQuestion = YesNo(f'{colorGreen}Do you want to rename the folders? {res}', default = 'n', word_color = colors.foreground["yellow"]).launch()
    
    c=  0

    if renameQuestion: 
        for name in directorys: 
            rename(f'{directory}/{name}', f'{directory}/{newName}-{c}.{newExtension}')
            c += 1
        print(f'{colorBlue}Renamed directories{res}')
    else: print(f'{colorRed}Directories not renamed{res}')
