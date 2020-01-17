from maya import cmds
import AutoRig.Functions_Autorig as fun
reload(fun)


controls_grp = cmds.group(em=True, n= 'facialMouthControls_c_grp')
system_grp = cmds.group(em=True, n= 'facialMouthSystem_c_grp')

locator_mouth = cmds.spaceLocator(n='centralMouth_c_loc')
locator_mouth_l = cmds.spaceLocator(n='centralMouth_l_loc')
locator_mouthCorner = cmds.spaceLocator(n='centralMouthCorner_l_loc')


if cmds.objExists('facialControls_c_grp') == False:
  cmds.group(em=True, n= 'facialControls_c_grp')
cmds.parent(controls_grp, 'facialControls_c_grp')
if cmds.objExists('facialRig_c_grp') == False:
  cmds.group(em=True, n= 'facialRig_c_grp')
cmds.parent(system_grp, 'facialRig_c_grp')


head = cmds.duplicate('headReference_c_geo', 'headFacialMouth_c_geo')
cmds.parent(head, system_grp)

 
specificSkn_grp = cmds.group(em=True, n= 'mouthSpecificNurbsSkin_c_grp') 
specificCtr_grp = cmds.group(em=True, n= 'mouthSpecificControls_c_grp')  


#################################



fun.createControlJoint(control_name = 'upLip',
                       side = 'c',
                       jnt_usage = 'nskn',
                       position_loc = locator_mouth,
                       ctr_parent_to = specificCtr_grp,
                       jnt_parent_to = specificSkn_grp)
                       
                                              
upLip_l = fun.createControlJoint(control_name = 'upLip',
                                 side = 'l',
                                 jnt_usage = 'nskn',
                                 position_loc = locator_mouth_l,
                                 ctr_parent_to = specificCtr_grp,
                                 jnt_parent_to = specificSkn_grp)                       
                       
                      
upLip_r_ctr = fun.duplicateFlip(element=upLip_l[0], 
                            descendent=True, 
                            side = 'r', dad=specificCtr_grp)

upLip_r_nskn = fun.duplicateFlip(element=upLip_l[1], 
                                 descendent=True, 
                                 side = 'r', dad=specificSkn_grp, 
                                 axis= 'x')
fun.conElement(source=upLip_r_ctr[1], subject = upLip_r_nskn[0])


test = 'upLipNskn_l_zero'

test.replace('up', 'dw')


for nskn, ctr in ['upLipNskn_c_zero', 'upLipCtr_c_zero'], ['upLipNskn_l_zero', 'upLipCtr_l_zero'], ['upLipNskn_r_zero', 'upLipCtr_r_zero']:
    for element in [nskn, ctr]:
        duplic = cmds.duplicate(element, rc=True)
        cmds.setAttr('{}.sy'.format(duplic[0]), -1)
       
        name = duplic[0].replace('up', 'dw')
        name = name.replace(name[-1], '')
       
        child = cmds.rename(duplic[1], name)
        
        name = duplic[1].replace('up', 'dw')
        name = name.replace(name[-1], '')
        
        cmds.rename(duplic[0], name)
        if element == ctr:
            ctr = child 
        else:
            nskn = child    
    fun.conElement(source=ctr, subject=nskn)


corner = fun.createControlJoint(control_name = 'corner',
                               side = 'l',
                               jnt_usage = 'nskn',
                               position_loc = locator_mouthCorner,
                               ctr_parent_to = specificCtr_grp,
                               jnt_parent_to = specificSkn_grp)


corner_r_nskn = fun.duplicateFlip(element=corner[1], 
                                 descendent=True, 
                                 side = 'r', dad=specificSkn_grp, 
                                 axis= 'x')
                              
corner_r_ctr = fun.duplicateFlip(element=corner[0], 
                                  descendent=True, 
                                  side = 'r', dad=specificSkn_grp, 
                                  axis= 'x')

fun.conElement(source=corner_r_ctr[1], subject = corner_r_nskn[0])    


#Ahora la NURB
upNurb = cmds.nurbsPlane(n='upLip_c_nurbs', ax=(0,1,0), w=True, lr= True, d = 3, u = 9, v=1, ch=1)
print 'Colocamos cada loop sobre cada hueso Specific y el intermedio a mitad de cada uno de ellos siguiendo la forma de la union de los labios Recordad que las Nurbs tienen un loop invisible a cada extremo, los colocamos ligeramente al lado de cada corner Ayudaos de unos locators de referencia para aseguraros que la Nurbs es completamente simétrica igual que hicimos en el sistema Brows'        
dwNurb = cmds.duplicate(upNurb, n='dwLip_c_nurbs')

cmds.parent(dwNurb, upNurb, 'mouthSpecificNurbsSkin_c_grp')


######
######
######
######





fol_number = 19
nurbs = 'dwLipMain_c_nurbs'
system_name = 'dwLip'
vertex_list = [u'headBase_c_geo.vtx[1352]', u'headBase_c_geo.vtx[1353]', u'headBase_c_geo.vtx[1354]', u'headBase_c_geo.vtx[1355]', u'headBase_c_geo.vtx[1356]', u'headBase_c_geo.vtx[1363]', u'headBase_c_geo.vtx[1364]', u'headBase_c_geo.vtx[1712]', u'headBase_c_geo.vtx[2037]', u'headBase_c_geo.vtx[2417]', u'headBase_c_geo.vtx[3891]', u'headBase_c_geo.vtx[3892]', u'headBase_c_geo.vtx[3893]', u'headBase_c_geo.vtx[3894]', u'headBase_c_geo.vtx[3895]', u'headBase_c_geo.vtx[3902]', u'headBase_c_geo.vtx[3903]', u'headBase_c_geo.vtx[4251]', u'headBase_c_geo.vtx[4576]']

#Reorder vertex list
vertex_list_ordered = []
vertex_list_disordered = vertex_list[::]
vertex_list_disordered_x_positions = []
for vtx in vertex_list_disordered:
    vtx_x_position = cmds.xform(vtx, query = True, translation = True, worldSpace = True)[0]
    vertex_list_disordered_x_positions.append(vtx_x_position)

while len(vertex_list_disordered)>0:
    vtx_lower_pos = 100000000000000
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
nurbs_shape = cmds.listRelatives(nurbs, shapes = True, noIntermediate = True)
left_follicles_list = []
right_follicle_list = []
nurbs_shape = [x for x in nurbs_shape if not 'Orig' in x][0]
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


                      
