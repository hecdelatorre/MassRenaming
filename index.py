from functions import enter_directory, traverse_directory, rename_directory

def main():
    en_directory = enter_directory()
    (directorys, new_name) = traverse_directory(en_directory)
    rename_directory(en_directory, directorys, new_name)

if __name__ == '__main__': main()
