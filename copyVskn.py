def createMultDiv(name=None, inputX1 = None, inputX2 = None, inputY1 = None, inputY2 = None, inputZ1 = None, inputZ2 = None, whantToDive=False):
    mult = cmds.shadingNode('multiplyDivide', au=True, n=name)
    if whantToDive == True:
        cmds.setAttr('{}.operation'.format(mult), 2)
    input_dic = {'input1.input1X' : inputX1,
                 'input1.input1Y' : inputY1,
                 'input1.input1Z' : inputZ1,
                 'input2.input2X' : inputX2,
                 'input2.input2Y' : inputY2,
                 'input2.input2Z' : inputZ2}
   
    for input in input_dic:
        key = input_dic.get(input)
        if input:
            key = input_dic.get(input)
            if isinstance(key, str) == True:
                cmds.connectAttr(key, '{}.{}'.format(mult, input))
            elif isinstance(key, int) == True:
                cmds.setAttr('{}.{}'.format(mult, input), key)
            else:
                pass  
    return mult               
   
   
   
   
def createSubsPlus(name=None, inputX1 = None, inputX2 = None, inputY1 = None, inputY2 = None, inputZ1 = None, inputZ2 = None, whantToSubs=True):
    subs = cmds.shadingNode('plusMinusAverage', au=True, n=name)
    if whantToSubs == True:
        cmds.setAttr('{}.operation'.format(subs), 2)
    input_dic = {inputX1 : 'input3D[0].input3Dx',
                 inputY1 : 'input3D[0].input3Dy',
                 inputZ1 : 'input3D[0].input3Dz',
                 inputX2 : 'input3D[1].input3Dx',
                 inputY2 : 'input3D[1].input3Dy',
                 inputZ2 : 'input3D[1].input3Dz'}
   
    for input in [inputX1, inputX2, inputY1, inputY2, inputZ1, inputZ2]:
        if input:
            key = input_dic.get(input)
         
            if isinstance(input, str) == True:
                cmds.connectAttr(input, '{}.{}'.format(subs, key))
            elif isinstance(input, int) == True:
                cmds.setAttr('{}.{}'.format(subs, key), input)
            else:
                pass  
    return subs  













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
