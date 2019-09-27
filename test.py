#get Control Number Joint

 

 

 

 

 


###Arbol Nodal

 

 

 

def trunkTreeNode(ctr = None, jntZero = None, jntNumber = None, name = None): 
     
    byTen = '{}ByTen_c_mult'.format(ctr)
     
    
    
    #ahora conectas al numberJoint del control
    
     
    
    #difurcacion negativa
    falloff_positionMinus = createSubsPlus(name='{}falloffPosition_c_subs'.format(name), 
                                       inputX1 = '{}.outputY'.format(byTen), 
                                       inputX2 = '{}.outputX'.format(byTen))
    
     
    
    falloff_posJnt = createSubsPlus(name='{}falloffPositionJnt_c_subs'.format(name), 
                                    inputX1 = '{}.output3Dx'.format(falloff_positionMinus), 
                                    inputX2 = '{}.position'.format(jntZero))#input2 requiere de jntPosition
    
     
    
    falloff_posCtr = createSubsPlus(name='{}falloffPositionCtr_c_subs'.format(name), 
                                    inputX1 = '{}.output3Dx'.format(falloff_positionMinus), 
                                    inputX2 = '{}.outputY'.format(byTen))#input2 requiere de ctrPosition
    
     
    
    
    rotMuliply_minus = createMultDiv(name='{}rotMultiply_c_div'.format(name), 
                                     inputX1= '{}.output3Dx'.format(falloff_posJnt), 
                                     inputX2= '{}.output3Dx'.format(falloff_posCtr), 
                                     whantToDive=True)
    
     
    
    
    #difurcacion positiva
    
     
    
    falloff_positionPlus = createSubsPlus(name='{}falloffPosition_c_subs'.format(name), 
                                      inputX1 = '{}.outputY'.format(byTen), 
                                      inputX2 = '{}.outputX'.format(byTen), 
                                      whantToSubs=False)
    
     
    
    falloff_posJnt = createSubsPlus(name='{}falloffPositionJnt_c_subs'.format(name), 
                                    inputX1 = '{}.output3Dx'.format(falloff_positionPlus), 
                                    inputX2 = '{}.position'.format(jntZero))#input2 requiere de jntPosition
    
     
    
    falloff_posCtr = createSubsPlus(name='{}falloffPositionCtr_c_subs'.format(name), 
                                    inputX1 = '{}.output3Dx'.format(falloff_positionPlus), 
                                    inputX2 = '{}.outputY'.format(byTen))#input2 requiere de ctrPosition
    
     
    
    
    rotMuliply_plus = createMultDiv(name='{}rotMultiply_c_div'.format(name), 
                                    inputX1= '{}.output3Dx'.format(falloff_posJnt), 
                                    inputX2= '{}.output3Dx'.format(falloff_posCtr), 
                                    whantToDive=True)
    
     
    
    #condicional
    
     
    
    cond = cmds.shadingNode('condition', au=True, n='{}influenceCondition_c_con'.format(name))
    cmds.setAttr('{}.operation'.format(cond), 3)
    cmds.connectAttr('{}.outputY'.format(byTen), '{}.firstTerm'.format(cond))
    cmds.connectAttr('{}.position'.format(jntZero), '{}.secondTerm'.format(cond))
    
     
    
    cmds.connectAttr( '{}.output.outputX'.format(rotMuliply_minus), '{}.colorIfTrueR'.format(cond)) #ifTrue el minus
    cmds.connectAttr( '{}.output.outputX'.format(rotMuliply_plus), '{}.colorIfFalseR'.format(cond),) #ifFalse el plus
    
     
    
    
    #number of joints affected
    
     
    
    numberJointsByOne_div = createMultDiv(name='{}numberJointsByOne_c_div'.format(name), 
                                            inputX1= 1, 
                                            inputX2= '{}.numberJoints'.format(ctr),#aqui cambiar por el number of joints 
                                            whantToDive=True)
    
     
    
     
    
    
    ctrRotation_mult = createMultDiv(name='{}ctrRotationTimes_c_mult'.format(name), 
                                     inputX1= '{}.outColorR'.format(cond), 
                                     inputX2= '{}.rx'.format(ctr),#rotacion x del control
                                     inputY1 = '{}.outColorR'.format(cond),
                                     inputY2 = '{}.ry'.format(ctr),#rotacion y del control
                                     inputZ1 = '{}.outColorR'.format(cond),
                                     inputZ2 = '{}.rz'.format(ctr))#rotacion z del control
    
     
    
     
    
     
    
    xConnumberJoints_div = createMultDiv(name='{}xConnumberJoints_c_div'.format(name), 
                                           inputX1= '{}.outputX'.format(numberJointsByOne_div), 
                                           inputX2= '{}.outputX'.format(ctrRotation_mult),
                                           inputY1 = '{}.outputX'.format(numberJointsByOne_div),
                                           inputY2 = '{}.outputY'.format(ctrRotation_mult),
                                           inputZ1 = '{}.outputX'.format(numberJointsByOne_div),
                                           inputZ2 = '{}.outputZ'.format(ctrRotation_mult),
                                           whantToDive = False)
    
     
    
    numberJoints_mult = createMultDiv(name='{}rotMultiply_c_mult'.format(name), 
                                     inputX1= '{}.outputX'.format(xConnumberJoints_div), 
                                     inputX2= 2,
                                     inputY1 = '{}.outputX'.format(xConnumberJoints_div),
                                     inputY2 = 2,
                                     inputZ1 = '{}.outputX'.format(xConnumberJoints_div),
                                     inputZ2 = 2)
                                     
                                     
    #condicional rotacion
    #AQUI VA A HABER ALGO
    
     
    
    cond = cmds.shadingNode('condition', au=True, n='{}rotateCondition_c_con'.format(name))
    cmds.setAttr('{}.operation'.format(cond), 5)
    cmds.connectAttr('{}.outputX'.format(byTen), '{}.secondTerm'.format(cond))
    cmds.connectAttr('{}.position'.format(jntZero), '{}.firstTerm'.format(cond))
    
     
    for axis, col in ['X', 'R'], ['Y', 'G'], ['Z', 'B']:
        cmds.connectAttr( '{}.output.output{}'.format(numberJoints_mult, axis), '{}.colorIfTrue{}'.format(cond, col)) #ifTrue el minus
        cmds.setAttr('{}.colorIfFalse{}'.format(cond, col), 0)

 

 

 

    
    
        cmds.connectAttr('{}.outColor{}'.format(cond, col), '{}.rotate{}'.format(jntZero, axis))
