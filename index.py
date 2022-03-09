from functions import enterDirectory, traverseDirectory, renameDirectory

def main():
    enDirectory = enterDirectory()
    (directorys, newName, newExtension) = traverseDirectory(enDirectory)
    renameDirectory(enDirectory, directorys, newName, newExtension)

if __name__ == '__main__': main()
