import maya.cmds as cmds
from maya.api import OpenMaya
def zero():
    list = cmds.ls(sl=True)

    for element in list:
        el = element.split('_')
        if len(el) == 3:
            function = element.split('_')[2]
            function = function.capitalize()
            first = '{}{}'.format(element.split('_')[0], function)
            second = element.split('_')[1]
            name = '{}_{}_zero'.format(first, second)
        else:     
            name = '{}_zero'.format(element)
        dad = cmds.listRelatives(element, c=False, p=True)   
        zero = cmds.group(em=True, n=name)
        pos = cmds.xform(element, m=True, q=True, ws=True)
        cmds.xform(zero, m=pos, ws=True)
        cmds.parent(element, zero)
        if dad:
            cmds.parent(zero, dad[0])   
        else:
            pass 
        return zero


def chainJoint(cantidad, nombre, lado, chin, radio, inicio, fin, unparent):

    start_point = cmds.xform(inicio, q=True, t=True, ws=True)
    end_point = cmds.xform(fin, q=True, t=True, ws=True)
    vector_sta = OpenMaya.MVector(start_point)
    vector_end = OpenMaya.MVector(end_point)
    i = 0
    all_joints = []
    for num in range(cantidad):
        name = '{}{}_{}_skn'.format(nombre, i, lado)
        nameEnd = '{}{}_{}_End'.format(nombre, i, lado)
        dif_point = vector_end-vector_sta
        offset = 1.0/(cantidad-1)
        new_point=dif_point*offset
        final_point = vector_sta + new_point   
        mid_pos=dif_point*(offset*num)
        final_pos=vector_sta+mid_pos
        jnt=cmds.joint(n=name, p=list(final_pos), rad=radio)
        all_joints.append(jnt)
        if i != 0:
            cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)  
        i += 1
        
        if chin==False:
            cmds.select(cl=1)
        if i == cantidad:
            jnt = cmds.rename(jnt, nameEnd)
            all_joints[-1] = jnt
            break
    if unparent == True:
        for jnt in all_joints:
            try:
                cmds.parent(jnt, w=True)
            except: 
                cmds.select(jnt)
                zero()
                pass
            zero()   
    return all_joints
    
def makeRibbon(point1, point2, width, module, side, u, v):
    #crear curva
    
    point1 = cmds.xform(point1, ws=True, q=True, t=True)
    point2 = cmds.xform(point2, ws=True, q=True, t=True)
    
    
    cur = cmds.curve(p=[point1, point2], degree=1)    
    
        #crear NURBS
    cur1 = cmds.duplicate(cur)
    cmds.move(width, cur1, x=True)
    
    cur2 = cmds.duplicate(cur)   
    cmds.move(width*(-1), cur2, x=True) 
    
    nurb = cmds.loft(cur1, cur2)
    cmds.delete(nurb[1])
    nurb = cmds.rename(nurb[0], '{}_{}_nurbs'.format(module, side))
    for c in [cur1, cur2, cur]:
        cmds.delete(c)
        #rebuild NURBS
    reb = cmds.rebuildSurface(nurb, su=u, sv=v)    
    return reb
    
def attachBones(nurb, side, system):
    jnt_list = cmds.ls(sl=True)
    follicle_list = []
    c=0
    for jnt in jnt_list:
         follicle_name = '{}{}_{}_fol'.format(system, c, side)
         follicle = cmds.createNode('transform', name = follicle_name)
         follicle_shape = cmds.createNode('follicle', name = '{}Shape'.format(follicle_name), parent = follicle)
         cmds.connectAttr('{}.local'.format(nurb), '{}.inputSurface'.format(follicle_shape), force = True)
         cmds.connectAttr('{}.worldMatrix[0]'.format(nurb), '{}.inputWorldMatrix'.format(follicle_shape), force = True)
         for axis in 'XYZ':
             cmds.connectAttr('{}.outTranslate{}'.format(follicle_shape, axis), '{}.translate{}'.format(follicle, axis), force = True)
         follicle_list.append(follicle)
        
        
        
         closestPoint = cmds.createNode('closestPointOnSurface', name = 'temp_closest')
         cmds.connectAttr('{}.local'.format(nurb), '{}.inputSurface'.format(closestPoint), force = True)
         jnt_position = cmds.xform(jnt, query = True, translation = True, worldSpace = True)
         cmds.setAttr('{}.inPosition'.format(closestPoint), jnt_position[0], jnt_position[1], jnt_position[2])
         parameter_U = cmds.getAttr('{}.parameterU'.format(closestPoint))
         parameter_V = cmds.getAttr('{}.parameterV'.format(closestPoint))
    
         cmds.setAttr('{}.parameterU'.format(follicle_shape), parameter_U)
         cmds.setAttr('{}.parameterV'.format(follicle_shape), parameter_V)
         cmds.delete(closestPoint)
         cmds.parentConstraint(follicle, jnt, skipRotate=['z', 'x', 'y'])
         c += 1 
         #aim joints
    c=0     
    for fol in follicle_list:         
         if c == len(jnt_list):
             pass
         else:    
             aim = cmds.aimConstraint(jnt_list[c+1], jnt_list[c], n='{}{}_{}_aimCon'.format(system, c, side), 
                                      aimVector=(1,0,0), 
                                      upVector=(0,0,1), worldUpType='vector', 
                                      worldUpVector = (0,0,1))[0]
             cmds.connectAttr('{}Shape.outNormal'.format(fol), '{}.upVector'.format(aim))
         c += 1    
    