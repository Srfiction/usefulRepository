

def setUpNose():
  from maya import cmds
  import AutoRig.Functions_Autorig as fun
  reload(fun)
  cmds.spaceLocator(n='septum_c_autoRig')
  cmds.spaceLocator(n='nose_c_autoRig')
  cmds.spaceLocator(n='noseTip_c_autoRig')
  cmds.spaceLocator(n='noseSquetch_c_autoRig')
  cmds.spaceLocator(n='nose_l_autoRig')
  cmds.spaceLocator(n='nose_r_autoRig')



  sys = cmds.group(em=True, n='facialNoseSquetchSystem_c_grp')
  sysC = cmds.group(em=True, n='facialNoseSquetchControls_c_grp')



  if cmds.objExists('facialControls_c_grp') == False:
    cmds.group(em=True, n= 'facialControls_c_grp')
  cmds.parent(sysC, 'facialControls_c_grp')

  if cmds.objExists('facialRig_c_grp') == False:
    cmds.group(em=True, n= 'facialRig_c_grp')
  if cmds.objExists('facialSystems_c_grp') == False:
    cmds.group(em=True, n= 'facialSystems_c_grp')
    cmds.parent('facialSystems_c_grp', 'facialRig_c_grp')  
  cmds.parent(sys, 'facialRig_c_grp')



def closeNose(nNumber = 5):
  from maya import cmds
  import AutoRig.Functions_Autorig as fun
  reload(fun)
  sys = 'facialNoseSquetchSystem_c_grp'
  sysC = 'facialNoseSquetchControls_c_grp'
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



  squetch = fun.createControlJoint(control_name = 'noseSquetch',
                                   side = 'c',
                                   jnt_usage = 'cskn',
                                   position_loc = 'noseSquetch_c_autoRig',
                                   ctr_parent_to = sysC,
                                   jnt_parent_to = sys)

  chain = fun.chainJointFacial(cantidad= nNumber, 
                               nombre = 'noseSquetch', 
                               chin = True, 
                               ini = 'septum_c_ctr', 
                               fin = 'noseSquetch_c_ctr')

  pos = cmds.xform(chain[0], q=True, m=True, ws=True)
  z = cmds.group(em=True, n= 'noseSquetch01Skn_c_zero')
  cmds.xform(z, m=pos, ws=True)                             
  cmds.parent(chain[0], z)  

  ikHan = cmds.ikHandle(sj = chain[0], ee = chain[-1], sol='ikSplineSolver', n='noseSquetch_c_iks')
  chain.remove(chain[-1])
  cmds.rename(ikHan[2], 'noseSquetchIk_c_crv')

  #Advanced Twist Controls
  cmds.setAttr('{}.dTwistControlEnable'.format(ikHan[0]), 1)
  cmds.setAttr('{}.dWorldUpType'.format(ikHan[0]), 4)
  cmds.setAttr('{}.dForwardAxis'.format(ikHan[0]), 0)
  cmds.setAttr('{}.dWorldUpAxis'.format(ikHan[0]), 3)
  cmds.setAttr('{}.dWorldUpVectorZ'.format(ikHan[0]), 1)
  cmds.setAttr('{}.dWorldUpVectorY'.format(ikHan[0]), 0)
  cmds.setAttr('{}.dWorldUpVectorEndZ'.format(ikHan[0]), 1)
  cmds.setAttr('{}.dWorldUpVectorEndY'.format(ikHan[0]), 0)
  cmds.connectAttr('noseSquetchCskn_c_zero.worldMatrix', '{}.dWorldUpMatrix'.format(ikHan[0]))
  cmds.connectAttr('noseSquetch_c_cskn.worldMatrix', '{}.dWorldUpMatrixEnd'.format(ikHan[0]))



  norm = fun.divideCreator(name='noseSquetch_c_norm')
  cuInf = fun.curveInfoCreator(Name = 'noseSquetch_c_cinfo', 
                           Input = '{}.worldSpace[0]'.format('noseSquetchIk_c_crv'), 
                           Length = '{}.input2.input2X'.format(norm), 
                           Output = '{}.input1.input1X'.format(norm))

  for jnt in chain:
    cmds.connectAttr('{}.outputX'.format(norm), '{}.sx'.format(jnt))


  subZero = fun.substractCreator(name='noseSquetch_c_sub', 
                                 InputX0 = '{}.outputX'.format(norm), 
                                 InputX1= -1, 
                                 OutputX = None, 
                                 OutputY = None)

  for jnt in chain:
    name = jnt.split('_')[0]
    nameM = '{}_c_mult'.format(name)
    nameP= '{}_c_sum'.format(name)
    mult = fun.multiplyCreator(name = nameM, 
                               linear = False,  
                               Input1Y = '{}.output3Dx'.format(subZero), 
                               Input1Z = '{}.output3Dx'.format(subZero),
                               Input2Y = 0, 
                               Input2Z = 0)

    plus = fun.plusCreator(name = nameP, 
                           InputX1 = '{}.input2X'.format(mult), 
                           InputX2 = 1, 
                           InputY1 = '{}.input2Y'.format(mult), 
                           InputY2 = 1)


    cmds.connectAttr('{}.output2D.output2Dx'.format(plus), '{}.sy'.format(jnt))
    cmds.connectAttr('{}.output2D.output2Dy'.format(plus), '{}.sz'.format(jnt))



  fun.createHold(n='NoseSquetch', side='c', skin = 'cskn')
  fun.createHold(n='NoseSquetch', side='c', skin = 'skn')
