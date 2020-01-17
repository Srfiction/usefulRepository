    
from maya import cmds
import AutoRig.Functions_Autorig as fun


def setUpBrows():
    controls_grp = cmds.group(em=True, n= 'facialBrowsControls_c_grp')
    system_grp = cmds.group(em=True, n= 'facialBrowsSystem_c_grp')
    nurbs_grp = cmds.group(em=True, n= 'browsMainNurbsSkin_c_grp')
    Snurbs_grp = cmds.group(em=True, n= 'browsSpecificNurbsSkin_c_grp')
    Scontrols_grp = cmds.group(em=True, n= 'facialBrowsSpecificControls_c_grp')
    geo_grp = cmds.group(em=True, n= 'browsGeoSkin_c_grp')
    
    cmds.duplicate('headReference_c_geo', n='headFacialBrows_c_geo')

    mNurb = cmds.nurbsPlane(n='browsMain_c_nurbs', ax=(0,1,0), w=True, lr= True, d = 3, u = 24, v=1, ch=1)
    cmds.parent(mNurb, nurbs_grp)

    mainBrows_l_loc = cmds.spaceLocator(n='mainBrows_l_loc')
    brow_c_loc = cmds.spaceLocator(n='brow_c_loc')
    brow01_l_loc = cmds.spaceLocator(n='brow01_l_loc')
    brow02_l_loc = cmds.spaceLocator(n='brow02_l_loc')
    brow03_l_loc = cmds.spaceLocator(n='brow03_l_loc')

    brow01_r_loc = cmds.spaceLocator(n='brow01_r_loc')
    brow02_r_loc = cmds.spaceLocator(n='brow02_r_loc')
    brow03_r_loc = cmds.spaceLocator(n='brow03_r_loc')


    fun.conElement(source=brow01_l_loc[0], subject = brow01_r_loc[0])
    fun.conElement(source=brow02_l_loc[0], subject = brow02_r_loc[0])
    fun.conElement(source=brow03_l_loc[0], subject = brow03_r_loc[0])



    if cmds.objExists('facialControls_c_grp') == False:
      cmds.group(em=True, n= 'facialControls_c_grp')
    cmds.parent(controls_grp, 'facialControls_c_grp')
    cmds.parent(Scontrols_grp, 'facialControls_c_grp')
    if cmds.objExists('facialRig_c_grp') == False:
      cmds.group(em=True, n= 'facialRig_c_grp')
    if cmds.objExists('facialSystems_c_grp') == False:
      cmds.group(em=True, n= 'facialSystems_c_grp')
      cmds.parent('facialSystems_c_grp', 'facialRig_c_grp')  
    cmds.parent(system_grp, 'facialRig_c_grp')
    cmds.parent(nurbs_grp, system_grp)
    cmds.parent(Snurbs_grp, system_grp)
    for i, e in ['brow_c_loc', 'brow01_l_loc'], ['brow01_l_loc', 'brow02_l_loc'], ['brow02_l_loc', 'brow03_l_loc']:
        for influenceI, influenceE in [0.75, 0.25], [0.5, 0.5], [0.25, 0.75]:
            ubic = cmds.spaceLocator(n='refLoc_dontTouch')
            pc = cmds.parentConstraint(i, e, ubic, n='parentConstraint_reference')   
            cmds.setAttr('{}.{}W0'.format(pc[0], i), influenceI)    
            cmds.setAttr('{}.{}W1'.format(pc[0], e), influenceE)   

def set2Brows():
    controls_grp='facialBrowsControls_c_grp'
    system_grp='facialBrowsSystem_c_grp'
    nurbs_grp='browsMainNurbsSkin_c_grp'
    Snurbs_grp = 'browsSpecificNurbsSkin_c_grp'
    Scontrols_grp = 'facialBrowsSpecificControls_c_grp'
    mNurb = 'browsMain_c_nurbs'
    Snurbs_grp = 'browsSpecificNurbsSkin_c_grp'
    mainCtr = fun.createControlJoint(control_name = 'browMain',
                                       side = 'l',
                                       jnt_usage = 'nskn',
                                       position_loc = 'mainBrows_l_loc',
                                       ctr_parent_to = controls_grp,
                                       jnt_parent_to = nurbs_grp)
    for side in 'lr':
      fun.createControlJoint(control_name = 'brow01',
                             side = side,
                             jnt_usage = 'nskn',
                             position_loc = 'brow01_{}_loc'.format(side),
                             ctr_parent_to = Scontrols_grp,
                             jnt_parent_to = Snurbs_grp)
      fun.createControlJoint(control_name = 'brow02',
                             side = side,
                             jnt_usage = 'nskn',
                             position_loc = 'brow02_{}_loc'.format(side),
                             ctr_parent_to = Scontrols_grp,
                             jnt_parent_to = Snurbs_grp)
      fun.createControlJoint(control_name = 'brow03',
                             side = side,
                             jnt_usage = 'nskn',
                             position_loc = 'brow03_{}_loc'.format(side),
                             ctr_parent_to = Scontrols_grp,
                             jnt_parent_to = Snurbs_grp)
    fun.createControlJoint(control_name = 'brow',
                           side = 'c',
                           jnt_usage = 'nskn',
                           position_loc = 'brow_c_loc',
                           ctr_parent_to = Scontrols_grp,
                           jnt_parent_to = Snurbs_grp)

    fun.duplicateFlip(element=mainCtr[0], 
                      descendent=True, 
                      side = 'r', dad=controls_grp)
    fun.duplicateFlip(element=mainCtr[1], 
                      descendent=True, 
                      side = 'r', dad=system_grp)
    
    sNurb = cmds.duplicate(mNurb, n='browsSpecific_c_nurbs')
    cmds.parent(sNurb, Snurbs_grp)
    bs = cmds.blendShape(sNurb, mNurb, n='browsMain_c_bs')
    cmds.setAttr('{}.{}'.format(bs[0], sNurb[0]), 1)

def set3Brows(folicleNumber = 21):
    vertex_list = cmds.ls(flatten = True, orderedSelection=True)
    
    fol_number = folicleNumber
    nurbs = 'browsMain_c_nurbs'
    system_name = 'brows'
    #test_list = [u'HeadBrows_c_geo.vtx[334]', u'HeadBrows_c_geo.vtx[335]', u'HeadBrows_c_geo.vtx[337]', u'HeadBrows_c_geo.vtx[341]', u'HeadBrows_c_geo.vtx[342]', u'HeadBrows_c_geo.vtx[344]', u'HeadBrows_c_geo.vtx[346]', u'HeadBrows_c_geo.vtx[348]', u'HeadBrows_c_geo.vtx[350]', u'HeadBrows_c_geo.vtx[352]', u'HeadBrows_c_geo.vtx[359]', u'HeadBrows_c_geo.vtx[360]', u'HeadBrows_c_geo.vtx[522]', u'HeadBrows_c_geo.vtx[1693]', u'HeadBrows_c_geo.vtx[1695]', u'HeadBrows_c_geo.vtx[1697]', u'HeadBrows_c_geo.vtx[1700]', u'HeadBrows_c_geo.vtx[1701]', u'HeadBrows_c_geo.vtx[1703]', u'HeadBrows_c_geo.vtx[1706]', u'HeadBrows_c_geo.vtx[1708]', u'HeadBrows_c_geo.vtx[1710]', u'HeadBrows_c_geo.vtx[1712]', u'HeadBrows_c_geo.vtx[1719]', u'HeadBrows_c_geo.vtx[1875]', u'HeadBrows_c_geo.vtx[3616]', u'HeadBrows_c_geo.vtx[3617]']
    #len(test_list)
    # Recover Vertex List
    vertex_list_ordered = []
    vertex_list_disordered = vertex_list[::]
    vertex_list_disordered_x_positions = []
    for vtx in vertex_list_disordered:
        vtx_x_position = cmds.xform(vtx, query = True, translation = True, worldSpace = True)[0]
        vertex_list_disordered_x_positions.append(vtx_x_position)
    
    while len(vertex_list_disordered)>0:
        vtx_lower_pos =  10000000000000
        vtx_position_in_list = None
        for i, vtx_x_pos in enumerate(vertex_list_disordered_x_positions):
            if vtx_x_pos < vtx_lower_pos:
                vtx_lower_pos = vtx_x_pos
                vtx_position_in_list = i
        vertex_list_ordered.append(vertex_list_disordered[vtx_position_in_list])
        vertex_list_disordered_x_positions.pop(vtx_position_in_list)
        vertex_list_disordered.pop(vtx_position_in_list)
    
    
    vertex_right_list = vertex_list_ordered[:fol_number/2][::-1]
    vertex_left_list = vertex_list_ordered[(fol_number/2)+1:]
    vertex_center = vertex_list_ordered[fol_number/2]
    
    #Create Follicles
    nurbs_shape = cmds.listRelatives(nurbs, shapes = True, noIntermediate = True)[0]
    left_follicles_list = []
    right_follicle_list = []
    for x in nurbs_shape:
        if not 'Orig' in x:
            nurbs_shape
    for side in 'lr':
        for i in range(0,fol_number/2):
             follicle_name = '{}{}_{}_fol'.format(system_name, str(i+1).zfill(2), side)
             follicle = cmds.createNode('transform', name = follicle_name)
             follicle_shape = cmds.createNode('follicle', name = '{}Shape'.format(follicle_name), parent = follicle)
             cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(follicle_shape), force = True)
             cmds.connectAttr('{}.worldMatrix[0]'.format(nurbs_shape), '{}.inputWorldMatrix'.format(follicle_shape), force = True)
             for axis in 'XYZ':
                 cmds.connectAttr('{}.outTranslate{}'.format(follicle_shape, axis), '{}.translate{}'.format(follicle, axis), force = True)
                 #cmds.connectAttr('{}.outRotate{}'.format(follicle_shape, axis), '{}.rotate{}'.format(follicle, axis), force = True)
             if side == 'l':
                 left_follicles_list.append(follicle)
             elif side == 'r':
                 right_follicle_list.append(follicle)
                   
            
    center_follicle_name = '{}_c_fol'.format(system_name)
    center_follicle = cmds.createNode('transform', name = center_follicle_name)
    center_follicle_shape = cmds.createNode('follicle', name = '{}Shape'.format(center_follicle_name), parent = center_follicle)
    cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(center_follicle_shape), force = True)
    cmds.connectAttr('{}.worldMatrix[0]'.format(nurbs_shape), '{}.inputWorldMatrix'.format(center_follicle_shape), force = True)
    for axis in 'XYZ':
        cmds.connectAttr('{}.outTranslate{}'.format(center_follicle_shape, axis), '{}.translate{}'.format(center_follicle, axis), force = True)
        #cmds.connectAttr('{}.outRotate{}'.format(center_follicle_shape, axis), '{}.rotate{}'.format(center_follicle, axis), force = True)
    
        
    for i, r_fol in enumerate(right_follicle_list):
        temp_closestSuface = cmds.createNode('closestPointOnSurface', name = 'temp_closest')
        cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(temp_closestSuface), force = True)
        vtx_position = cmds.xform(vertex_right_list[i], query = True, translation = True, worldSpace = True)
        cmds.setAttr('{}.inPosition'.format(temp_closestSuface), vtx_position[0], vtx_position[1], vtx_position[2])
        parameter_U = cmds.getAttr('{}.parameterU'.format(temp_closestSuface))
        parameter_V = cmds.getAttr('{}.parameterV'.format(temp_closestSuface))
        follicle_shape = cmds.listRelatives(r_fol, shapes = True)[0]
        cmds.setAttr('{}.parameterU'.format(follicle_shape), parameter_U)
        cmds.setAttr('{}.parameterV'.format(follicle_shape), parameter_V)
        cmds.delete(temp_closestSuface)
    
       
    for i, l_fol in enumerate(left_follicles_list):
        temp_closestSuface = cmds.createNode('closestPointOnSurface', name = 'temp_closest')
        cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(temp_closestSuface), force = True)
        vtx_position = cmds.xform(vertex_left_list[i], query = True, translation = True, worldSpace = True)
        cmds.setAttr('{}.inPosition'.format(temp_closestSuface), vtx_position[0], vtx_position[1], vtx_position[2])
        parameter_U = cmds.getAttr('{}.parameterU'.format(temp_closestSuface))
        parameter_V = cmds.getAttr('{}.parameterV'.format(temp_closestSuface))
        follicle_shape = cmds.listRelatives(l_fol, shapes = True)[0]
        cmds.setAttr('{}.parameterU'.format(follicle_shape), parameter_U)
        cmds.setAttr('{}.parameterV'.format(follicle_shape), parameter_V)
        cmds.delete(temp_closestSuface)
        
    cmds.setAttr('{}.parameterU'.format(center_follicle_shape), 0.5)
    cmds.setAttr('{}.parameterV'.format(center_follicle_shape), 0.5)
    
    
    
    #Creacion de Huesos por foliculo
    follicles_list = left_follicles_list + right_follicle_list + [center_follicle]
    for fol in follicles_list:
        jnt_name = '{}_{}_skn'.format(*fol.split('_'))
        jnt_zero_name = '{}Skn_{}_zero'.format(*fol.split('_'))
        jnt = cmds.createNode('joint', name = jnt_name)
        jnt_zero = cmds.createNode('transform', name = jnt_zero_name)
        jnt = cmds.parent(jnt, jnt_zero)[0]
        fol_matrix = cmds.xform(fol, query = True, matrix = True, worldSpace= True)
        cmds.xform(jnt_zero, matrix = fol_matrix, worldSpace = True)
        subs_node_name = '{}Fol_{}_subs'.format(*fol.split('_'))
        subs_node = cmds.createNode('plusMinusAverage', name = subs_node_name)
        cmds.setAttr('{}.operation'.format(subs_node), 2)
        for axis in 'xyz':
            cmds.connectAttr('{}.t{}'.format(fol, axis), '{}.input3D[0].input3D{}'.format(subs_node, axis), force = True)
            cmds.connectAttr('{}.t{}'.format(fol, axis), '{}.input3D[1].input3D{}'.format(subs_node, axis), force = True)
            cmds.disconnectAttr('{}.t{}'.format(fol, axis), '{}.input3D[1].input3D{}'.format(subs_node, axis))
            cmds.connectAttr('{}.output3D{}'.format(subs_node, axis), '{}.t{}'.format(jnt, axis),  force = True)
        cmds.parent(jnt_zero, 'browsGeoSkin_c_grp')
    
    #Hold bullshit
    
    cmds.createNode('joint', n='brows_c_Hold')
    cmds.createNode('transform', name = 'browsHold_c_zero')
    cmds.parent('brows_c_Hold', 'browsHold_c_zero')
    cmds.parent('browsHold_c_zero', 'browsGeoSkin_c_grp')
    
    cmds.createNode('transform', n='BrowsSystemFols_c_grp')
    for fol in follicles_list:
        cmds.parent(fol, 'BrowsSystemFols_c_grp')
    cmds.parent('BrowsSystemFols_c_grp', 'facialSystems_c_grp')
