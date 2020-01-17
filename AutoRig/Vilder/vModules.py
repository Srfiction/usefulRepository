creative = vSet.refAutorig('leg', 'c')
creative.referenceChain(mod='leg', sid='c', quantity=3)

extremityStandard(mirror=False, moduleName='leg', upArticulation=['position0Leg_c_vilder', 'hip'], 
                                                  middleArticulation=['position1Leg_c_vilder', 'knee'], 
                                                  lowArticulation=['position2Leg_c_vilder', 'foot'])

def extremityStandard(mirror=True, moduleName=None, upArticulation=[None, None], middleArticulation=[None, None], lowArticulation=[None, None]):
	if cmds.objExists('skeleton_c_grp') == False:
	    cmds.group(em=True, name='skeleton_c_grp')
	if cmds.objExists('bodyRig_c_grp') == False:
	    cmds.group(em=True, name='bodyRig_c_grp')	
	
	for side in 'lr':
	    upArt = upArticulation[1]
	    midArt = middleArticulation[1]
	    lowArt = lowArticulation[1]
	    
	    upPos = upArticulation[0]
	    midPos = middleArticulation[0]
	    lowPos = lowArticulation[0]
	    
	    for part in [upArticulation, middleArticulation, lowArticulation]:
    		loc_matrix = cmds.xform(part[0], query = True, t = True, worldSpace = True)
    		joint_name = ('{}_{}_jnt'.format(part[1], side))
    		jnt = cmds.joint(n=joint_name)
    		cmds.xform(jnt, t = loc_matrix, worldSpace = True)
    		if part == lowArticulation:
    		    cmds.joint('{}_{}_jnt'.format(upArt, side),e=True,zso=True, ch=True,oj='xzy',sao='zup')  
    		    cmds.setAttr('{}_{}_jnt.jointOrientZ'.format(lowArt, side), 0) 
    		    cmds.setAttr('{}_{}_jnt.preferredAngleY'.format(midArt, side), 90)
    		    cmds.rename(jnt, '{}End_{}_jnt'.format(moduleName, side))


	    jnt_matrix = cmds.xform('{}_{}_jnt'.format(upArt, side), query = True, t = True, worldSpace = True)  
	    offset = cmds.group(em=True, n='{}Jnt_{}_offset'.format(moduleName, side))
	    cmds.xform(offset, t = jnt_matrix, worldSpace = True)
	    cmds.parent('{}_{}_jnt'.format(upArt, side), offset)
	    cmds.parent(offset, 'skeleton_c_grp')





    	#8.2. CREACION DEL IKHANDLE DE LA CADENA PRINCIPAL: limpio

	    ikHandle_jnt = cmds.ikHandle(s = 'sticky', sj = '{}_{}_jnt'.format(upArt, side), ee= '{}End_{}_jnt'.format(moduleName, side), 
	                                 n='{}_{}_ikHandle'.format(moduleName, side))
	    cmds.rename(ikHandle_jnt[1], '{}_{}_eff'.format(moduleName, side)) 

	    offset = cmds.group(em=True, n='rig{}_{}_grp'.format(moduleName, side))
	    cmds.xform(offset, t = jnt_matrix, worldSpace = True)
	    cmds.parent('{}_{}_ikHandle'.format(moduleName, side), offset)
	    cmds.parent(offset, 'bodyRig_c_grp')

    	#nonRoll - Hip, Knee

	    #nonRoll - Hip---------------------------------------------------------------------------------------------------
	    nonRoll_chain = cmds.duplicate('{}_{}_jnt'.format(upArt, side), rc=True, n='{}_{}_nonRoll'.format(upArt, side))
	    cmds.delete(nonRoll_chain[2::])
	    cmds.rename(nonRoll_chain[1], '{}End_{}_nonRoll'.format(upArt, side))
	    cmds.setAttr('{}_{}_nonRoll.jointOrientX'.format(upArt, side), 0)
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky',
					 sj = nonRoll_chain[0], 
					 ee= '{}End_{}_nonRoll'.format(upArt, side), 
					 n='NonRollHip_{}_ikHandle'.format(side))
	    cmds.rename(ikHandle_jnt[1], 'nonRoll{}_{}_eff'.format(upArt, side))
	    for axis in 'XYZ':
		cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
	    nonRoll_grp = cmds.group(em=True, n='{}NonRoll_{}_grp'.format(upArt, side))
	    RollSystem_grp = cmds.group(em=True, n='up{}_RollSystem_{}_grp'.format(moduleName.capitalize(), side))
	    cmds.parent(nonRoll_grp, RollSystem_grp)
	    cmds.parent('up{}_RollSystem_{}_grp'.format(moduleName.capitalize(), side), 'rig{}_{}_grp'.format(moduleName, side))
	    cmds.parent(ikHandle_jnt[0], nonRoll_chain[0], nonRoll_grp)
		    #GLOBAL SCALE - CONNECTION TO GRP
		    #PRESTARATENCIÓN
	    #for axis in 'xyz':
		    #cmds.connectAttr('general_c_ctr.GlobalScale', 'upLeg_RollSystem_{}_grp.s{}'.format(side, axis))



	    cmds.pointConstraint('{}_{}_jnt'.format(upArt, side), 
				  nonRoll_chain[0], 
				  n='{0}JntTo{0}NonRoll_{1}_pointConstraint'.format(upArt, side))    

	    cmds.pointConstraint('{}_{}_jnt'.format(midArt, side), 
				 'NonRoll{}_{}_ikHandle'.format(upArt.capitalize(), side), 
				 n='{}ToNonRoll_{}_pointConstraint'.format(midArt, side))


	    #nonRoll - Knee----------------------------------------------------------------------------------------------

	    nonRoll_knee = cmds.duplicate('{}_{}_jnt'.format(midArt, side), rc=True, n='{}_{}_nonRoll'.format(midArt, side))
	    cmds.delete('{}_{}_eff1'.format(moduleName, side))
	    cmds.rename(nonRoll_knee[1], '{}_{}_nonRoll_End'.format(midArt, side))
	    cmds.setAttr('{}_{}_nonRoll.jointOrientX'.format(midArt, side), 0)
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky', 
					 sj = nonRoll_knee[0], 
					 ee= '{}_{}_nonRoll_End'.format(midArt, side), 
					 n='NonRoll{}_{}_ikHandle'.format(midArt.capitalize(), side))
	    cmds.rename(ikHandle_jnt[1], 'nonRoll{}_{}_eff'.format(midArt.capitalize(), side))
	    for axis in 'XYZ':
		    cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
	    nonRoll_grp = cmds.group(em=True, n='{}NonRoll_{}_grp'.format(midArt, side))
	    RollSystem_grp = cmds.group(em=True, n='low{}RollSystem_{}_grp'.format(moduleName, side))
	    cmds.parent(nonRoll_grp, RollSystem_grp)
	    cmds.parent(RollSystem_grp, 'rig{}_{}_grp'.format(moduleName.capitalize(), side))
	    cmds.parent(ikHandle_jnt[0], nonRoll_knee[0], nonRoll_grp)
		#GLOBAL SCALE - CONNECTION TO GRP
	    for axis in 'xyz':
		cmds.connectAttr('general_c_ctr.GlobalScale', 'lowLeg_RollSystem_{}_grp.s{}'.format(side, axis))

	    cmds.pointConstraint('knee_{}_jnt'.format(side), 
				 nonRoll_knee[0], 
				 n='pointConstraint_{}_from_KneeJnt_To_KneeNonRollJnt'.format(side))    

	    cmds.pointConstraint('foot_{}_jnt'.format(side), 
				 ikHandle_jnt[0], 
				 n='pointConstraint_{}_from_FootJnt_To_KneeNonRollEnd'.format(side))




	    #TwistValue

	    twist_value = cmds.duplicate('knee_{}_jnt'.format(side), n='knee_{}_twistValue'.format(side), rc=True)
	    cmds.delete(twist_value[1])
	    cmds.parent(twist_value[0], 'knee_{}_jnt'.format(side))
	    cmds.aimConstraint('foot_{}_jnt'.format(side), 
			       'knee_{}_twistValue'.format(side),
				worldUpType = 'objectrotation',
				worldUpObject = 'knee_{}_nonRoll'.format(side),
				offset = [0,0,0],
				aimVector = [1,0,0],
				upVector = [0,1,0], 
				worldUpVector = [0,1,0],
				n='aimConstraint_{}_from_FootJnt_To_FootTwistValueJnt'.format(side))
	    cmds.parentConstraint('hip_{}_nonRoll'.format(side), 'knee_NonRoll_{}_grp'.format(side), mo=True)



	    #nonRoll - Foot------------------------------------------------------------------------------------------------

	    nonRoll_foot = cmds.duplicate('legEnd_{}_jnt'.format(side), rc=True, n='foot_{}_nonRoll'.format(side))[0]
	    nonRoll_end = cmds.duplicate(nonRoll_foot, n='foot_{}_nonRoll_End'.format(side))
	    footEnd_pos = cmds.xform('endFoot_loc_{}_autorig'.format(side), query = True, t = True, worldSpace = True) 
	    cmds.xform(nonRoll_end, t= footEnd_pos, worldSpace=True)
	    cmds.parent(nonRoll_end, nonRoll_foot)
	    cmds.setAttr('{}.jointOrientX'.format(nonRoll_foot), 0)

	    ikHandle_jnt = cmds.ikHandle(s = 'sticky', 
					 sj = nonRoll_foot, 
					 ee= 'foot_{}_nonRoll_End'.format(side), 
					 n='NonRollFoot_{}_ikHandle'.format(side))
	    cmds.rename(ikHandle_jnt[1], 'nonRollFoot_{}_eff'.format(side))
	    for axis in 'XYZ':
		cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
	    nonRoll_grp = cmds.group(em=True, n='foot_NonRoll_{}_grp'.format(side))
	    cmds.parent(nonRoll_grp, RollSystem_grp)
	    cmds.parent(ikHandle_jnt[0], nonRoll_foot, nonRoll_grp)

	    cmds.pointConstraint('foot_{}_jnt'.format(side), 
				 'foot_{}_nonRoll'.format(side), 
				 n='pointConstraint_{}_from_FootJnt_To_FootNonRollJnt')    

		#footNonRoll IkHandle Pcon
	    pcon_matrix = cmds.xform(nonRoll_end, query = True, t = True, worldSpace = True)
	    pcon = cmds.group(em=True, n='footNonRoll_{}_ikHandlePcon'.format(side))
	    cmds.xform(pcon, t = pcon_matrix, worldSpace = True)
	    cmds.parent(pcon, 'foot_{}_jnt'.format(side))
	    cmds.pointConstraint(pcon, 
				ikHandle_jnt[0], 
				n='pointConstraint_{}_footPconToIkHandle'.format(side))

		#TWIST VALUE
	    twist_value = cmds.duplicate('foot_{}_jnt'.format(side), 
					 n='foot_{}_twistValue'.format(side), rc=True)
	    cmds.delete(twist_value[1])
	    cmds.parent(twist_value[0], 'foot_{}_jnt'.format(side))

	    cmds.setAttr('foot_{}_twistValue.jointOrientY'.format(side), 90)

	    cmds.aimConstraint('foot_{}_nonRoll_End'.format(side), 
				'foot_{}_twistValue'.format(side),
				worldUpType = 'objectrotation',
				worldUpObject = 'foot_{}_nonRoll'.format(side),
				offset = [0,0,0],
				aimVector = [1,0,0],
				upVector = [0,1,0],  
				worldUpVector = [0,1,0],
				n='aimConstraint_{}_kneeTwistValueToFoot'.format(side))#AQUI HAY QUE SETEAR VALORES PAG 
	    cmds.parentConstraint('knee_{}_jnt'.format(side), 'foot_NonRoll_{}_grp'.format(side), mo=True, 
				  n='parentConstraint_{}_from_KneeJnt_To_FootNonTollGrp'.format(side))


    	'''
    	8.4. CREACION DE LAS CADENAS TWIST JOINTS:
    	    8.4.1 Creacion de la cadena twist del Upleg:
    	    8.4.2 Creacion de la cadena twist del Lowleg:
    	'''

	    cmds.select(cl=True)
	    twist_chain = fun.chainJoint(
			  uplegJnts, 
			  'upLeg', 
			  chin=True, 
			  radio=0.5, 
			  lado=side, 
			  ini='hip', 
			  fin='knee')

	    twist_ik = cmds.ikHandle(n='twistUpLeg_{}_ik'.format(side), 
				     sj=twist_chain[0], 
				     ee=twist_chain[-1], 
				     sol='ikSplineSolver')

	    eff = cmds.rename(twist_ik[1], 'twistUpleg_{}_eff'.format(side))
	    curv = cmds.rename(twist_ik[2], 'twistUpleg_{}_curve'.format(side))
	    cmds.parent(twist_ik[0], 'upLeg_RollSystem_{}_grp'.format(side))
	    cmds.parent(curv, 'rig_leg_{}_grp'.format(side))
	    cmds.parent(twist_chain[0], 'upLeg_RollSystem_{}_grp'.format(side))
	    upleg_twistValue_mult = fun.multiplyCreator(
				    name = 'upLegTwistValue_{}_mult'.format(side), 
				    linear = False, 
				    Input1X = 'knee_{}_twistValue.rx'.format(side), 
				    Input2X = -1)
	    cmds.connectAttr('{}.outputX'.format(upleg_twistValue_mult), 'twistUpLeg_{}_ik.twist'.format(side))

	###########################################################LowLEG    

	    cmds.select(cl=True)
	    twist_chain = fun.chainJoint(
			  lowlegJnts, 
			  'lowLeg', 
			  chin=True, 
			  radio=0.5, 
			  lado=side, 
			  ini='knee', 
			  fin='foot')

	    twist_ik = cmds.ikHandle(n='twistLowLeg_{}_ik'.format(side), 
				     sj=twist_chain[0], 
				     ee=twist_chain[-1], 
				     sol='ikSplineSolver')

	    eff = cmds.rename(twist_ik[1], 'twistLowleg_{}_eff'.format(side))
	    curv = cmds.rename(twist_ik[2], 'twistLowleg_{}_curve'.format(side))
	    cmds.parent(twist_ik[0], 'lowLeg_RollSystem_{}_grp'.format(side))
	    cmds.parent(curv, 'rig_leg_{}_grp'.format(side))
	    cmds.parent(twist_chain[0], 'knee_{}_jnt'.format(side))

	    lowleg_twistValue_mult = fun.multiplyCreator(
				     name = 'lowLegTwistValue_{}_mult'.format(side), 
				     linear = False, 
				     Input1X = 'foot_{}_twistValue.rx'.format(side), 
				     Input2X = -1)

	    cmds.connectAttr('{}.outputX'.format(lowleg_twistValue_mult), 'twistLowLeg_{}_ik.twist'.format(side))
        if mirror == False:
            break