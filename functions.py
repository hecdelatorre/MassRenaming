from bullet import Input, colors, YesNo
from colored import fg, attr
from os import listdir, rename
from os.path import isdir, isfile, splitext
from getpass import getuser

color_red = fg('#CC0000')
color_green = fg('#73D216')
color_blue = fg('#338CFF')
reset = attr('reset')

def error():
    print(f'{color_red}Wrong data{reset}')
    exit()

def validate_directory(directory): 
    if not isdir(directory): error()
    else: return directory 

def enter_directory():
    directory = Input(f'{color_green}Enter the directory {reset}', default = f"/home/{getuser()}/Downloads", word_color = colors.foreground["yellow"]).launch()
    directory = validate_directory(directory)
    return directory

def traverse_directory(directory):
    new_name = Input(f'{color_green}Login in new name {reset}', default = 'default', word_color = colors.foreground["yellow"]).launch()

    directory_array = listdir(directory)
    directories = []
    
    print(f'Current name {color_blue}::{reset} New name')
    c = 0

    for d_file in directory_array: 
        if isfile(f'{directory}/{d_file}'): 
            ext = splitext(d_file)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png', '.gif']:
                print(f'{d_file} {color_red}::{reset} {new_name}-{c}{ext}')
                c += 1
                directories.append(d_file)

    return directories, new_name

def rename_directory(directory, directories, new_name):
    rename_question = YesNo(f'{color_green}Do you want to rename the folders? {reset}', default = 'n', word_color = colors.foreground["yellow"]).launch()
    
    c = 0

    if rename_question: 
        for name in directories: 
            ext = splitext(name)[1]
            rename(f'{directory}/{name}', f'{directory}/{new_name}-{c}{ext}')
            c += 1
        print(f'{color_blue}Renamed directories{reset}')
    else: print(f'{color_red}Directories not renamed{reset}')
