import AutoRig.Functions_Autorig as fun
from maya import cmds


#setUp
cmds.group(em=True, n='minNull')    
cmds.setAttr('minNull.sx', -1)

cmds.spaceLocator(n='extEyelids2_l_loc')

cmds.spaceLocator(n='intEyelids2_l_loc')

cmds.spaceLocator(n='extEyelids2_r_loc')

cmds.spaceLocator(n='intEyelids2_r_loc')
for axis in 'xyz':
    cmds.connectAttr('intEyelids02_l_loc.t{}'.format(position, axis), 'intEyelids2_r_loc.t{}'.format(position, axis))   
    cmds.connectAttr('extEyelids02_l_loc.r{}'.format(position, axis), 'extEyelids2_r_loc.r{}'.format(position, axis)) 

for side in 'lr':
    for position in ['up', 'ext', 'int', 'center']:
        spaceLoc = cmds.spaceLocator(n='{}Eyelids_{}_loc'.format(position, side))
        if side == 'r':
            cmds.parent(spaceLoc, 'minNull')
            for axis in 'xyz':
                cmds.connectAttr('{}Eyelids_l_loc.t{}'.format(position, axis), '{}Eyelids_r_loc.t{}'.format(position, axis))   
                cmds.connectAttr('{}Eyelids_l_loc.r{}'.format(position, axis), '{}Eyelids_r_loc.r{}'.format(position, axis)) 

            
for i, e in ['upEyelids_l_loc', 'extEyelids2_l_loc'], ['upEyelids_l_loc', 'intEyelids2_l_loc'], ['intEyelids2_l_loc', 'intEyelids_l_loc'], ['extEyelids2_l_loc', 'extEyelids_l_loc']:
    for influenceI, influenceE in [0.75, 0.25], [0.5, 0.5], [0.25, 0.75]:
        ubic = cmds.spaceLocator(n='refLoc_dontTouch')
        pc = cmds.parentConstraint(i, e, ubic, n='parentConstraint_reference')   
        cmds.setAttr('{}.{}W0'.format(pc[0], i), influenceI)    
        cmds.setAttr('{}.{}W1'.format(pc[0], e), influenceE) 




controls_grp = cmds.group(em=True, n= 'facialEyelidsControls_c_grp')
system_grp = cmds.group(em=True, n= 'facialEyelidsSystem_c_grp')
if cmds.objExists('facialControls_c_grp') == False:
  cmds.group(em=True, n= 'facialControls_c_grp')
cmds.parent(controls_grp, 'facialControls_c_grp')
if cmds.objExists('facialRig_c_grp') == False:
  cmds.group(em=True, n= 'facialRig_c_grp')
if cmds.objExists('facialSystems_c_grp') == False:
  cmds.group(em=True, n= 'facialSystems_c_grp')
cmds.parent('facialSystems_c_grp', 'facialRig_c_grp')
cmds.parent(system_grp, 'facialSystems_c_grp')
cmds.group(em=True, n='eyelidsGeoSkin_c_grp')
cmds.group(em=True, n='eyelidsSystem_c_grp')
for side in 'rl':
    grp1 = cmds.group(em=True, n='eyelidsMainSkin_{}_grp'.format(side))
    grp2 = cmds.group(em=True, n='eyelidsSpecificSkin_{}_grp'.format(side))
    cmds.parent(grp1, grp2, system_grp)
    pop = cmds.group(em=True, n= 'eyelidsSystemJoints_{}_grp'.format(side))
    cmds.parent(pop, 'eyelidsSystem_c_grp')
cmds.group(em=True, n='eyelidsGeoSkin_c_grp')
cmds.group(em=True, n='eyelidsSystem_c_grp')
cmds.parent('eyelidsSystem_c_grp', 'eyelidsGeoSkin_c_grp', system_grp)

nurb = cmds.nurbsPlane(n='upEyelidMain_l_nurbs', ax=(0,1,0), w=True, lr= True, d = 3, u = 15, v=1, ch=1) 


#Creation

#Main Structure
cmds.duplicate('upEyelidMain_l_nurbs', n='dwEyelidMain_l_nurbs')

cmds.duplicate('upEyelidMain_l_nurbs', n='dwEyelidMain_r_nurbs')
cmds.duplicate('upEyelidMain_l_nurbs', n='upEyelidMain_r_nurbs')

inv = cmds.group(em=True)
cmds.parent('upEyelidMain_r_nurbs', 'dwEyelidMain_r_nurbs', inv)
cmds.setAttr('{}.sx'.format(inv), -1)
cmds.select(inv)
cmds.FreezeTransformations(inv)

for side in 'rl':
    for position in ['up', 'dw']:
        name = '{}EyelidSpecific_{}_nurbs'.format(position, side)
        specific = cmds.duplicate('{}EyelidMain_{}_nurbs'.format(position, side), n=name)
        bs = cmds.blendShape('{}EyelidSpecific_{}_nurbs'.format(position, side), '{}EyelidMain_{}_nurbs'.format(position, side), n='{}EyelidMain_{}_bs'.format(position, side))
        cmds.setAttr('{}.{}'.format(bs[0], specific[0]), 1)
        cmds.parent(specific, 'eyelidsSpecificSkin_{}_grp'.format(side))
        cmds.parent('{}EyelidMain_{}_nurbs'.format(position, side), 'eyelidsMainSkin_{}_grp'.format(side))
        
for side in 'rl':
    pos = cmds.xform('centerEyelids_{}_loc'.format(side), q=True, ws=True, m=True)
    for position in ['up', 'ext', 'int', 'dw']:
        if position != 'dw':
            ctrJnt = fun.createControlJoint(control_name = '{}EyelidsMain'.format(position),
                                            side = side,
                                            jnt_usage = 'jnt',
                                            position_loc = '{}Eyelids_{}_loc'.format(position, side),
                                            ctr_parent_to = 'facialEyelidsControls_c_grp',
                                            jnt_parent_to = 'eyelidsSystemJoints_{}_grp'.format(side))
        else:
            ctr = cmds.duplicate('upEyelidsMainCtr_{}_zero'.format(side), n='dwEyelidsMainCtr_{}_zero'.format(side), rc=True)       
            jnt = cmds.duplicate('upEyelidsMainJnt_{}_zero'.format(side), n='dwEyelidsMainJnt_{}_zero'.format(side), rc=True)
            
            ctr = cmds.rename(ctr[1], 'dwEyelidsMain_{}_ctr'.format(side))
            jnt = cmds.rename(jnt[1], 'dwEyelidsMain_{}_jnt'.format(side))
            
            for axis in 'xyz':
                for comm in 'trs':
                    cmds.connectAttr('{}.{}{}'.format(ctr, comm, axis), '{}.{}{}'.format(jnt, comm, axis))
                
            
            cmds.setAttr('dwEyelidsMainCtr_{}_zero.sy'.format(side), -1)   
            cmds.setAttr('dwEyelidsMainJnt_{}_zero.sy'.format(side), -1)  
            
        
        cmds.select(cl=True)                               
        nskn = cmds.joint(n='{}EyelidsMain_{}_nskn'.format(position, side))
        zero = cmds.group(em=True, n='{}EyelidsNskn_{}_zero'.format(position, side))
        cmds.parent(nskn, zero)
        cmds.xform(zero, m=pos, ws=True)
        cmds.aimConstraint('{}EyelidsMain_{}_jnt'.format(position, side), '{}EyelidsMain_{}_nskn'.format(position, side))
        cmds.parent(zero, 'eyelidsMainSkin_{}_grp'.format(side))
        
#Specific Structure

for side in 'rl':
    for loc, add in ['intEyelids_{}_loc'.format(side), 'int'], ['intEyelids2_{}_loc'.format(side), '01'], ['upEyelids_{}_loc'.format(side), '02'], ['extEyelids2_{}_loc'.format(side), '03'], ['extEyelids_{}_loc'.format(side), 'ext']:
        greg = fun.createControlJoint(control_name = 'upEyelidsSpecific{}'.format(add),
                                      side = side,
                                      jnt_usage = 'jnt',
                                      position_loc = loc,
                                      ctr_parent_to = 'facialEyelidsControls_c_grp',
                                      jnt_parent_to = 'eyelidsSystemJoints_{}_grp'.format(side))
            
        if add  == '01', '02', or '03':
            ctr = cmds.duplicate(greg[0], n='dwEyelidSpecific{}Ctr_{}_zero'.format(add, side), rc=True)       
            jnt = cmds.duplicate(greg[1], n='dwEyelidsSpecific{}Jnt_{}_zero'.format(add, side), rc=True)
            
            ctr = cmds.rename(ctr[1], 'dwEyelidsSpecific{}_{}_ctr'.format(add, side))
            jnt = cmds.rename(jnt[1], 'dwEyelidsSpecific{}_{}_jnt'.format(add, side))
            
            for axis in 'xyz':
                for comm in 'trs':
                    cmds.connectAttr('{}.{}{}'.format(ctr, comm, axis), '{}.{}{}'.format(jnt, comm, axis))
                
            
            cmds.setAttr('dwEyelidsSpecificCtr_{}_zero.sy'.format(side), -1)   
            cmds.setAttr('dwEyelidsSpecificJnt_{}_zero.sy'.format(side), -1)    
        
        pos = cmds.xform(q=True, ws=True, )
        nskn = cmds.   

