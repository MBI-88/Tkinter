print('Hi from Gui init\n')
from sys import path
from pprint import pprint
from site import addsitedir
from os import getcwd, chdir, pardir

while True:
    curFull = getcwd()
    curDir = curFull.split('\\')[-1]
    if 'Cap_11' == curDir:
        addsitedir(curFull)
        addsitedir(curFull + '\Folder_1\Folder_2\Folder_3')
        break
    chdir(pardir)

pprint(path)
