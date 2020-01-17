cmds.spaceLocator(n='septum_c_autoRig')
cmds.spaceLocator(n='nose_c_autoRig')
cmds.spaceLocator(n='noseTip_c_autoRig')

cmds.spaceLocator(n='nose_l_autoRig')
cmds.spaceLocator(n='nose_r_autoRig')

import AutoRig.Functions_Autorig as fun
reload(fun)


sys = cmds.group(em=True, n='facialExtrasSystem_c_grp')


hold = fun.createHold(n='Extras', side='c')
cmds.parent(hold, sys)

septum = fun.createControlJoint(control_name = 'septum',
                       side = 'c',
                       jnt_usage = 'skn',
                       position_loc = 'septum_c_autoRig',
                       ctr_parent_to = None,
                       jnt_parent_to = sys)
                       
                       
nose = fun.createControlJoint(control_name = 'nose',
                       side = 'c',
                       jnt_usage = 'skn',
                       position_loc = 'nose_c_autoRig',
                       ctr_parent_to = septum[2],
                       jnt_parent_to = septum[3])                       

     

noseTip = fun.createControlJoint(control_name = 'noseTip',
                       side = 'c',
                       jnt_usage = 'skn',
                       position_loc = 'noseTip_c_autoRig',
                       ctr_parent_to = nose[2],
                       jnt_parent_to = nose[3]) 
                                             

for side in 'rl':
    fun.createControlJoint(control_name = 'nose',
                       side = side,
                       jnt_usage = 'skn',
                       position_loc = 'nose_{}_autoRig'.format(side),
                       ctr_parent_to = nose[2],
                       jnt_parent_to = nose[3]) 
