#Guarda la asignacion de huesos
vsknList = cmds.ls(sl=True)
parentNodes = []

library = {}


for jnt in vsknList:
    try:
        parentNode = cmds.listConnections('{}.tx'.format(jnt))[0]
        skn = cmds.listConnections('{}.target[0].targetParentMatrix'.format(parentNode))[0]
        library.update({jnt:skn})
        parentNodes.append(parentNode)
    except:
        pass
#Eliminar los parents 
for nod in parentNodes:
    cmds.delete(nod)

#Parent a la asignacion de huesos 

for key, value in library.iteritems():
    try:
        cmds.parentConstraint(value, key)
    except:
        pass
