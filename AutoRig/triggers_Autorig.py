import AutoRig.Functions_Autorig as noodles
from maya import cmds
reload(noodles)

def triggerCrr(system=None, side=None, direction=None, posTar=None, parTar=None, parPos=None):

    target = cmds.spaceLocator(n='target_{}_{}_{}_crr_loc'.format(system, side, direction))[0]
    base = cmds.spaceLocator(n='base_{}_{}_{}_crr_loc'.format(system, side, direction))[0]
    poss = cmds.spaceLocator(n='pose_{}_{}_{}_crr_loc'.format(system, side, direction))[0]
    
    cmds.addAttr(base, ln='conneAngle', at= 'double', dv=180)
    cmds.setAttr('{}.conneAngle'.format(base), k=True)
    cmds.addAttr(base, ln='result', at= 'double', dv=180)
    cmds.setAttr('{}.result'.format(base), k=True)
    
    
    angBet = cmds.shadingNode('angleBetween', n='angleBetween{}_{}_ab'.format(system, side), au=True)
    
    
    curPos = noodles.substractCreator(name='currentPosition{}{}_{}_sub'.format(system, direction, side))
    cmds.connectAttr('{}Shape.worldPosition'.format(base), '{}.input3D[0]'.format(curPos))
    cmds.connectAttr('{}Shape.worldPosition'.format(poss), '{}.input3D[1]'.format(curPos))
    cmds.connectAttr('{}.output3D'.format(curPos), '{}.vector1'.format(angBet))
    
    tarVec = noodles.substractCreator(name='targetVector{}{}_{}_sub'.format(system, direction, side))
    cmds.connectAttr('{}Shape.worldPosition'.format(target), '{}.input3D[1]'.format(tarVec))
    cmds.connectAttr('{}Shape.worldPosition'.format(base), '{}.input3D[0]'.format(tarVec))
    cmds.connectAttr('{}.output3D'.format(tarVec), '{}.vector2'.format(angBet))
    
    
    halfCore = noodles.multiplyCreator(name = 'halfConeAngle{}{}_{}_mdl'.format(system, direction, side), linear = True, 
                                       Input1 = '{}.conneAngle'.format(base), 
                                       Input2 = 0.5,
                                       Output = None)
                                       
                                       
    proportion = noodles.divideCreator(name='proportion{}{}_{}_div'.format(system, direction, side), 
                                       Input1X = '{}.axisAngle.angle'.format(angBet), 
                                       Input2X = '{}.output'.format(halfCore),
                                       OutputX = None)                                   
    
    
    
    setProp = noodles.substractCreator(name='setProportions{}_{}_sub'.format(system, side))
    cmds.setAttr('{}.input1D[0]'.format(setProp), 1)
    cmds.connectAttr('{}.outputX'.format(proportion), '{}.input1D[1]'.format(setProp))
    
    
    
    clamp = noodles.clampCreator(name = 'clamp{}_{}_dic'.format(system, side), 
                                 MaxG = 1,
                                 InputG = '{}.output1D'.format(setProp))
                                 
                                 
                                 
    cmds.connectAttr('{}.outputG'.format(clamp), '{}.result'.format(base))   
    
    
    posPos = cmds.xform(parPos, t=True, ws=True, q=True)
    posBas = cmds.xform(posTar, t=True, ws=True, q=True)
    
    cmds.xform(target, t=posPos, ws=True)
    cmds.xform(poss, t=posPos, ws=True)
    cmds.xform(base, t=posBas, ws=True)
    
    
    cmds.parent(target, base, parTar)
    cmds.parent(poss, parPos)                           
                             
