def createFingers():
    from maya import cmds
    from maya.api import OpenMaya
    hand_skn = 'hand_{}_skn'

    
    for side in 'rl':
        handFingers_grp = cmds.group(em=True, n='handFingers_{}_grp'.format(side))
        cmds.parentConstraint(hand_skn.format(side), handFingers_grp)
    
    for finger in 'ABCDE':
        cmds.select(cl=True)
        for side in 'rl':
            cmds.select(cl=True)
            count = 0
            for falange in range(0,4):
                name = 'finger{}0{}_{}_'.format(finger, falange, side)
                loc_position = cmds.xform('hand{}0{}_{}_loc'.format(finger, falange, side), 
                                           t=True, ws=True, q=True)
                zero = cmds.group(em=True, n='{}zero'.format(name))
                ctr = cmds.circle(n = '{}ctr'.format(name))
                cmds.xform(ctr, t=loc_position)
                cmds.xform(zero, t=loc_position)
                cmds.parent(ctr, zero)

    jnt_list = []
    for finger in 'ABCDE':
        for side in 'rl':
            cmds.select(cl=True)
            count = 0
            for falange in range(0,5):
                name = 'finger{}0{}_{}_skn'.format(finger, falange, side)
                loc_position = cmds.xform('hand{}0{}_{}_loc'.format(finger, falange, side), 
                                           t=True, ws=True, q=True)
                jnt = cmds.joint(n = name)
                cmds.xform(jnt, t=loc_position, ws=True)
                jnt_list.append(jnt)
                if falange == 4:
                    pass
                else:
                    cmds.parent(jnt, 'finger{}0{}_{}_ctr'.format(finger, falange, side))
        
        count += 1
    for side in 'rl':
        for finger in 'ABCDE':
            count = 1
            for i in range(0,4):
                if count < 4:
                    cmds.parent('finger{}0{}_{}_zero'.format(finger, count, side), 'finger{}0{}_{}_skn'.format(finger, count-1, side))
                    count += 1
                else:
                    pass
            cmds.parent('finger{}00_{}_zero'.format(finger, side), 'handFingers_{}_grp'.format(side))

    for jnt in jnt_list:
        cmds.setAttr('{}.drawStyle'.format(jnt), 2)
