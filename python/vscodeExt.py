from subprocess import call
from subprocess import check_output

curExtList = check_output("code --list-extensions", shell=True).split()
#get regular extensions from a file called exts.txt
extsToAdd = [ext.rstrip('\n') for ext in open('exts.txt')]
#get rid of all strings common to each list
setOfCurExt = set(curExtList)
toInstall = [ext for ext in extsToAdd if ext not in setOfCurExt]
#install any extensions that are in the list but not currently installed
if toInstall:
    for ext in toInstall:
        call('code --install-extension ' + ext, shell=True)
    print 'sucessfully installed vscode extensions'