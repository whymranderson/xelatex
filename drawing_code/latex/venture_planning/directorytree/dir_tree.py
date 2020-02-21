import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def list_files_menukeys(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        if level < 3:
            indent = '\>' * (level)
            print('{}{}{}/{}\\\\'.format(indent,r'\nixpath{', os.path.basename(root),'}'))
            subindent = '\>' * (level + 1)
            for f in files:
                print('{}{}{}{}\\\\'.format(subindent,r'\nixfile{',f,'}'))

#listpath = r"C:\Documents and Settings\The One\My Documents\tony\Scripts\GyroSoft Simulation\1_Demo_Examples"
listpath = r"C:\texlive\2018"

#list_files(listpath)
list_files_menukeys(listpath)
