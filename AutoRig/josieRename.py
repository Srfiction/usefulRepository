from maya import cmds


def searchAndReplace(sear=None, rep=None, *pArgs):
    list = cmds.ls(sl=True)
    for element in list:
        try:
            name = element.replace(sear, rep)
            element = cmds.rename(element, name)   
            newName= name.split('|')[-1]
            cmds.rename(element, newName)
        except:
            list = cmds.ls(sl=True)
            
    
    
    
def prefix(prefix=None):
    list = cmds.ls(sl=True)
    for element in list:
        cmds.rename(element, '{}{}'.format(prefix, element))
        
        
def suffix(suffix=None):
    list = cmds.ls(sl=True)
    for element in list:
        element = element.split('|')[-1]
        cmds.rename(element, '{}{}'.format(element, suffix))
        
def renaming(name=None, start=0, padding=1):
    list = cmds.ls(sl=True)
    for element in list:
        cmds.rename(element, '{}{}'.format(name, start))
        start += 1    
