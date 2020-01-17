for fol in cmds.ls(sl=True):
    nurb = 'mainEyelidsDw_r_nurbShape'
    parameterU = cmds.getAttr(fol + 'Shape.parameterU')
    parameterV = cmds.getAttr(fol + 'Shape.parameterV')
    name = fol.replace('_l_', '_r_')
    transform = cmds.createNode('transform', n = name)
    follicle = cmds.createNode('follicle', n = name + 'Shape', p = transform)
    
    cmds.connectAttr(nurb + '.local', follicle + '.inputSurface')
    cmds.connectAttr(nurb + '.worldMatrix', follicle + '.inputWorldMatrix')
    
    for axis in 'XYZ':
        cmds.connectAttr(follicle + '.outTranslate' + axis, transform + '.translate' + axis)
    cmds.setAttr(follicle + '.parameterU', parameterU)    
    cmds.setAttr(follicle + '.parameterV', parameterV)
    
    zero = cmds.createNode('transform' , n='{}Skn_r_zero'.format(fol.split('_')[0]))
    jnt = cmds.createNode('joint' , n='{}_r_skn'.format(fol.split('_')[0]), parent = zero)
    
    pos = cmds.xform(transform, t=True, q=True, ws=True)
    cmds.xform(zero, t=pos, ws=True)
    
    minus = autoNoodle(node = 'plusMinusAverage', name = '{}{}'.format(fol.split('_')[0], '_r_plusMinusAverage'), 
               connections = [['input3D[0].input3Dx', '{}.translateX'.format(transform)],
                              ['input3D[0].input3Dy', '{}.translateY'.format(transform)],
                              ['input3D[0].input3Dz', '{}.translateZ'.format(transform)],
                              ['input3D[1].input3Dx', cmds.getAttr('{}.translateX'.format(transform))],
                              ['input3D[1].input3Dy', cmds.getAttr('{}.translateY'.format(transform))],
                              ['input3D[1].input3Dz', cmds.getAttr('{}.translateZ'.format(transform))],
                              ['operation', 2]          
               ])
    for axis in 'xyz':
        cmds.connectAttr('{}.output3D{}'.format(minus, axis), '{}.t{}'.format(jnt, axis))