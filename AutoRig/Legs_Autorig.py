from maya import cmds
from maya.api import OpenMaya
import AutoRig.Functions_Autorig as fun

def createLeg(uplegJnts=8, lowlegJnts=8):
	'''''''''
	LA PIERNA


	Vas a necesitar:
	    hip_loc_l_autorig
	    knee_loc_l_autorig
	    foot_loc_l_autorig
	    endFoot_loc_l_autorig

	    LEG  LEG  LEG

	NOTAS:
	    1) Los Twist No Funcionan. He seguido el problema hasta los NonRoll. Con rascar un poco mas encontraras la solucion
	    2) Ya he encontrado varios fallos en la seccion del Twist y el Non Roll. Tal vez aclarar el codigo ayude un poco
	    3) El offset del middle blend se vuelve loco, tiene valores de rotacion por algun puto motivo
	    4) La orientacion de los Poles  no esta a MUNDO
	    5) Al aprecer hay un control llamado hip_{}_ctr que maneja el hip, independientemente de la rotacion del hip_{}_FK_ctr. Parece ser fundamental a la hora de cerrar el rig
		i) Tendra algo qeu ver con la extrana rotacion del upleg?
	    6)FALTABA UN CONTROL TODO ESTE TIEMPO! ARRRRRGGGGGGGG




	    SOLUCION DEL TWIST:
		LOS twist_skn del lowLeg van emparentados al knee_{}_jnt!!!!!! Es increible!
	    7) En Ik nos sigue dando problemas de rotacion. Es muy posible que sea otro problema  de emparentameinto
	    LA SOLUCION ESTA EN EMPARENTAR EL POLE EN EL CONTROL CENTRAL (DUH)
	'''
	####
	ctrHip = 'hip_{}_ctr'
	ctrHip_offset = 'hipCtr_{}_offset'
	for side in 'rl':
	    hip_loc = cmds.xform('hip_loc_{}_autorig'.format(side), t=True,q=True,ws=True)
	    cmds.xform(ctrHip_offset.format(side), t = hip_loc, ws=True)
	####

	'''
	8.1. CREACIoN DE LOS HUESOS
	    8.1.1 Creacion de la cadena principal: limpio
	'''
	for side in 'rl':
	    cmds.select(cl=True)
	    for part in ['hip', 'knee', 'foot']:
		loc_matrix = cmds.xform('{}_loc_{}_autorig'.format(part, side), query = True, t = True, worldSpace = True)
		joint_name = ('{}_{}_jnt'.format(part, side))
		jnt = cmds.joint(n=joint_name)
		cmds.xform(jnt, t = loc_matrix, worldSpace = True)
		if part == 'foot':
		    cmds.joint('{}_{}_jnt'.format('hip', side),e=True,zso=True, ch=True,oj='xzy',sao='zup')  
		    cmds.setAttr("foot_{}_jnt.jointOrientZ".format(side), 0) 
		    cmds.setAttr("knee_{}_jnt.preferredAngleY".format(side), 90)
		    cmds.rename(jnt, 'legEnd_{}_jnt'.format(side))


	    jnt_matrix = cmds.xform('hip_{}_jnt'.format(side), query = True, t = True, worldSpace = True)  
	    offset = cmds.group(em=True, n='legJnt_{}_offset'.format(side))
	    cmds.xform(offset, t = jnt_matrix, worldSpace = True)
	    cmds.parent('hip_{}_jnt'.format(side), offset)
	    cmds.parent(offset, 'skeleton_c_grp')


	#JNT foot    
	    cmds.select(cl=True)
	    for part in ['foot', 'ball', 'toe']:
		loc_matrix = cmds.xform('{}_loc_{}_autorig'.format(part, side), query = True, t = True, worldSpace = True)
		joint_name = ('{}_{}_jnt'.format(part, side))
		jnt = cmds.joint(n=joint_name)
		cmds.xform(jnt, t = loc_matrix, worldSpace = True)

	    cmds.joint('ball_{}_jnt'.format(side),e=True,zso=True, ch=True,oj='xyz',sao='zup') 
	    cmds.setAttr("toe_{}_jnt.jointOrientY".format(side), 0)  
	    cmds.parent('ball_{}_jnt'.format(side), w=True)
	    cmds.setAttr('foot_{}_jnt.jointOrientY'.format(side), -90)
	    cmds.setAttr('foot_{}_jnt.jointOrientX'.format(side), 90)
	    cmds.setAttr('foot_{}_jnt.jointOrientZ'.format(side), 90)
	    cmds.parent('ball_{}_jnt'.format(side), 'foot_{}_jnt'.format(side))


	    jnt_matrix = cmds.xform('foot_{}_jnt'.format(side), query = True, t = True, worldSpace = True)  
	    offset = cmds.group(em=True, n='footJnt_{}_offset'.format(side))
	    cmds.xform(offset, t = jnt_matrix, worldSpace = True)
	    cmds.parent('foot_{}_jnt'.format(side), offset)
	    cmds.parent(offset, 'skeleton_c_grp')


	# Point de LegEnd a FootGrp
	    cmds.pointConstraint('legEnd_{}_jnt'.format(side),'footJnt_{}_offset'.format(side))


	'''
	8.2. CREACION DEL IKHANDLE DE LA CADENA PRINCIPAL: limpio
	'''
	for side in 'rl':
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky', sj = 'hip_{}_jnt'.format(side), ee= 'legEnd_{}_jnt'.format(side), n='leg_{}_ikHandle'.format(side))
	    cmds.rename(ikHandle_jnt[1], 'leg_{}_eff'.format(side)) 

	for side in 'rl':  
	    offset = cmds.group(em=True, n='rig_leg_{}_grp'.format(side))
	    cmds.xform(offset, t = jnt_matrix, worldSpace = True)
	    cmds.parent('leg_{}_ikHandle'.format(side), offset)
	    cmds.parent(offset, 'bodyRig_c_grp')

	''''
	8.3. CONFIGURACION DE LOS SISTEMAS NON ROLL:
	    8.3.1 Configuracion de la cadena NonRoll del Hip: limpio
	    8.3.2 Configuracion de la cadena NonRoll del Knee: limpio
	    8.3.2 Configuracion de la cadena NonRoll del Knee: limpio
	'''    
	#nonRoll - Hip, Knee
	for side in 'rl':
	    #nonRoll - Hip---------------------------------------------------------------------------------------------------
	    nonRoll_chain = cmds.duplicate('hip_{}_jnt'.format(side), rc=True, n='hip_{}_nonRoll'.format(side))
	    cmds.delete(nonRoll_chain[2::])
	    cmds.rename(nonRoll_chain[1], 'hip_{}_nonRoll_End'.format(side))
	    cmds.setAttr('hip_{}_nonRoll.jointOrientX'.format(side), 0)
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky',
					 sj = nonRoll_chain[0], 
					 ee= 'hip_{}_nonRoll_End'.format(side), 
					 n='NonRollHip_{}_ikHandle'.format(side))
	    cmds.rename(ikHandle_jnt[1], 'nonRollHip_{}_eff'.format(side))
	    for axis in 'XYZ':
		cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
	    nonRoll_grp = cmds.group(em=True, n='hip_NonRoll_{}_grp'.format(side))
	    RollSystem_grp = cmds.group(em=True, n='upLeg_RollSystem_{}_grp'.format(side))
	    cmds.parent(nonRoll_grp, RollSystem_grp)
	    cmds.parent('upLeg_RollSystem_{}_grp'.format(side), 'rig_leg_{}_grp'.format(side))
	    cmds.parent(ikHandle_jnt[0], nonRoll_chain[0], nonRoll_grp)
		    #GLOBAL SCALE - CONNECTION TO GRP
	    for axis in 'xyz':
		cmds.connectAttr('general_c_ctr.GlobalScale', 'upLeg_RollSystem_{}_grp.s{}'.format(side, axis))



	    cmds.pointConstraint('hip_{}_jnt'.format(side), 
				  nonRoll_chain[0], 
				  n='pointConstraint_{}_from_HipJnt_To_HipNonRollJnt'.format(side))    

	    cmds.pointConstraint('knee_{}_jnt'.format(side), 
				 'NonRollHip_{}_ikHandle'.format(side), 
				 n='pointConstraint_{}_fromKneeJntTo'.format(side))


	    #nonRoll - Knee----------------------------------------------------------------------------------------------

	    nonRoll_knee = cmds.duplicate('knee_{}_jnt'.format(side), rc=True, n='knee_{}_nonRoll'.format(side))
	    cmds.delete('leg_{}_eff1'.format(side))
	    cmds.rename(nonRoll_knee[1], 'knee_{}_nonRoll_End'.format(side))
	    cmds.setAttr('knee_{}_nonRoll.jointOrientX'.format(side), 0)
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky', 
					 sj = nonRoll_knee[0], 
					 ee= 'knee_{}_nonRoll_End'.format(side), 
					 n='NonRollKnee_{}_ikHandle'.format(side))
	    cmds.rename(ikHandle_jnt[1], 'nonRollKnee_{}_eff'.format(side))
	    for axis in 'XYZ':
		cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
	    nonRoll_grp = cmds.group(em=True, n='knee_NonRoll_{}_grp'.format(side))
	    RollSystem_grp = cmds.group(em=True, n='lowLeg_RollSystem_{}_grp'.format(side))
	    cmds.parent(nonRoll_grp, RollSystem_grp)
	    cmds.parent('lowLeg_RollSystem_{}_grp'.format(side), 'rig_leg_{}_grp'.format(side))
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

	for side in 'rl':
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



	'''
	8.5. CREACIoN DE LOS CONTROLES:
	    8.5.1. Creacion del control FootIK (char_ac_lf_footIK):
	    8.5.2. Creacion del control legPole (char_ac_lf_legPole):
	'''        
	#Foot IK
	for side in 'rl':
	    foot_pos = cmds.xform('foot_{}_jnt'.format(side), q=True, t=True, ws=True)
	    cmds.xform('footIKCtr_{}_offset'.format(side), t=foot_pos, ws=True)
	    cmds.parent('footIKCtr_{}_offset'.format(side), 'center_c_ctr')

	fun.poleLocation()
	for side in 'rl':    
	    cmds.move(30, 'legPoleCtr_{}_offset'.format(side), z=True)
	for side in 'rl':
	    cmds.parent('legPoleCtr_{}_offset'.format(side), 'center_c_ctr')
	#Hip_ctr
	    pos = cmds.xform('hip_{}_jnt'.format(side), q=True, t=True, ws=True)
	    cmds.xform('hipCtr_{}_offset'.format(side), t=pos, ws=True)
	    cmds.parent('hipCtr_{}_offset'.format(side), 'pelvis_c_ctr')

	#Settings_ctr
	for side in 'rl':
	    pos = cmds.xform('foot_{}_jnt'.format(side), q=True, t=True, ws=True)
	    cmds.xform('legSettingsCtr_{}_offset'.format(side), t=pos, ws=True)
	    cmds.parent('legSettingsCtr_{}_offset'.format(side), 'center_c_ctr')



	#FK_ctr
	for side in 'rl':
	    for parte in ['hip','knee','foot']:
		pos = cmds.xform('{}_{}_jnt'.format(parte, side), q=True, t=True, ws=True)
		cmds.xform('{}FKCtr_{}_offset'.format(parte, side), t=pos, ws=True)
	    cmds.parent('hipFKCtr_{}_offset'.format(side), 'center_c_ctr')
	    cmds.parent('kneeFKCtr_{}_offset'.format(side), 'hipFK_{}_ctr'.format(side))
	    cmds.parent('footFKCtr_{}_offset'.format(side), 'kneeFK_{}_ctr'.format(side))

	#toe_ctr
	for side in 'rl':
	    pos = cmds.xform('ball_{}_jnt'.format(side), q=True, t=True, ws=True)
	    cmds.xform('toeCtr_{}_offset'.format(side), t=pos, ws=True)
	    cmds.parent('toeCtr_{}_offset'.format(side), 'center_c_ctr')





	'''''
	footRollSystem

	vas a necesitar:
	    bankExt_l_pivot
	    bankInt_l_pivot
	    heel_l_pivot
		heelParam_l_pivot -misma posicion que el heel
	    toe_l_pivot
		toeParam_l_pivot
	    ball_l_pivot
		ballParam_l_pivot
	    ankle_l_pcon

	'''
	cmds.parent('bankExt_l_pivot', 'bankInt_l_pivot', 'heel_l_pivot', 'heelParam_l_pivot', 'toe_l_pivot', 'toeParam_l_pivot', 'ball_l_pivot', 'ballParam_l_pivot', 'ankle_l_pcon', 'footIK_l_ctr')
	cmds.parent('bankInt_l_pivot','bankExt_l_pivot')
	cmds.parent('heelParam_l_pivot','bankInt_l_pivot')
	cmds.parent('heel_l_pivot','heelParam_l_pivot')
	cmds.parent('toe_l_pivot','toeParam_l_pivot')
	cmds.parent('toeParam_l_pivot', 'heel_l_pivot')
	cmds.parent('ball_l_pivot','ballParam_l_pivot')
	cmds.parent('ballParam_l_pivot', 'toe_l_pivot')
	cmds.parent('ankle_l_pcon','ball_l_pivot')

	footRollSystem = cmds.duplicate('bankExt_l_pivot', n='bankExt_r_pivot', rc=True)
	for name in footRollSystem:
	    cmds.parent(name, w=True)
	    portion = name.split('_')[0]
	    cmds.rename(name, '{}_r_pivot'.format(portion))

	cmds.rename('ankle_r_pivot','ankle_r_pcon')
	null = cmds.group(em=True)
	cmds.parent('bankExt_r_pivot', 'bankInt_r_pivot', 'heel_r_pivot', 'heelParam_r_pivot', 'toe_r_pivot', 'toeParam_r_pivot', 'ball_r_pivot', 'ballParam_r_pivot', 'ankle_r_pcon', null)
	cmds.parent('bankInt_r_pivot','bankExt_r_pivot')
	cmds.parent('heelParam_r_pivot','bankInt_r_pivot')
	cmds.parent('heel_r_pivot','heelParam_r_pivot')
	cmds.parent('toe_r_pivot','toeParam_r_pivot')
	cmds.parent('toeParam_r_pivot', 'heel_r_pivot')
	cmds.parent('ball_r_pivot','ballParam_r_pivot')
	cmds.parent('ballParam_r_pivot', 'toe_r_pivot')
	cmds.parent('ankle_r_pcon','ball_r_pivot')
	cmds.setAttr('{}.sx'.format(null), -1)
	cmds.parent('bankExt_r_pivot', 'footIK_r_ctr')



	'''
	CONFIGURACION DEL CONTROL TOE
	'''

	for side in 'rl':
	    ctrFootIK = 'footIK_{}_ctr'.format(side)
	    #configuracion del ctrToe
	    parentToe = cmds.parentConstraint('footFK_{}_ctr'.format(side), 'toe_{}_pivot'.format(side), 
					      'toeCtr_{}_offset'.format(side),mo=True, 
					      n='parentConstraint_{}_FootFKandToePivotToToe'.format(side))




	    #rever = cmds.shadingNode('reverse', n=name_reverse, au=True)
	    #cmds.connectAttr('legSettings_r_ctr.Leg_IK'.format(side), '{}.inputX'.format(rever))
	    #cmds.connectAttr('{}.outputX'.format(rever), '')




	    fun.twoInfluencesConstraint(controler = 'legSettings_{}_ctr.Leg_IK'.format(side), constraint = parentToe[0])#PUEDE QUE ALGO ESTE FALLANDO aqui

	    #Configuracion del FootTilt
		#footBankExt
	    bankExtClamp = fun.clampCreator(
			   name = 'bankExt_{}_clamp'.format(side), 
			   MaxG = 999, 
			   InputG = 'footIK_{}_ctr.footTilt'.format(side))

	    if side == 'l':
		value = -1
	    else:
		value = 1
	    bankExtMult = fun.multiplyCreator(name = 'bankExt_{}_multiply'.format(side),
				       linear = True,
				       Input1 = '{}.outputG'.format(bankExtClamp),
				       Input2 = value,
				       Output = 'bankExt_{}_pivot.rz'.format(side))

		#footBank_int
	    bankIntClamp = fun.clampCreator(
			   name = 'bankInt_{}_clamp'.format(side), 
			   MinG = -999, 
			   InputG = 'footIK_{}_ctr.footTilt'.format(side))
	    bankIntMult = fun.multiplyCreator(
			  name = 'bankInt_{}_multiply'.format(side), 
			  linear = True, 
			  Input1 = '{}.outputG'.format(bankIntClamp),
			  Input2 = -1,
			  Output = 'bankInt_{}_pivot.rz'.format(side))

		#footHeel
	    heelRollClamp = fun.clampCreator(
			    name = 'heel_{}_clamp'.format(side), 
			    MinG = -999, 
			    InputG = 'footIK_{}_ctr.FootRoll'.format(side))

	    cmds.connectAttr('{}.outputG'.format(heelRollClamp), 'heel_{}_pivot.rx'.format(side))

		#footToe_pivot
	    toeRollClamp = fun.clampCreator(
			   name = 'toeRoll_{}_clamp'.format(side), 
			   MaxG = 999, 
			   MinG = 'footIK_{}_ctr.toeBreak'.format(side), 
			   InputG = 'footIK_{}_ctr.FootRoll'.format(side))

	    toeRollMinus = fun.substractCreator(
			   name='toeRoll_{}_minus'.format(side),
			   InputX0 = '{}.outputG'.format(toeRollClamp),
			   InputX1 = 'footIK_{}_ctr.toeBreak'.format(side),
			   OutputX = 'toe_{}_pivot.rx'.format(side))
		#footBall_pivot
	    angleToeBreakMinus = fun.substractCreator(
				 name='ballPivot_{}_minus'.format(side),
				 InputX1 = '{}.toeBreak'.format(ctrFootIK),
				 InputX0 = '{}.releaseAngle'.format(ctrFootIK))

	    toeBreakRestaDiv = fun.divideCreator(
			       name='ballPivot_{}_div'.format(side),
			       Input1X='footIK_{}_ctr.toeBreak'.format(side),
			       Input2X='{}.output2Dx'.format(angleToeBreakMinus))

	    toeFactorMult = fun.multiplyCreator(
			    name='toeFactor_{}_mult'.format(side), 
			    linear = True,#Esto estaba en False por algun motivo?
			    Input1 = '{}.output2Dx'.format(toeRollMinus),
			    Input2 = '{}.outputX'.format(toeBreakRestaDiv))

	    toeRollClamped = fun.clampCreator(
			     name='toeRoll_{}_clamp'.format(side), 
			     MaxG = '{}.toeBreak'.format(ctrFootIK), 
			     InputG = '{}.output'.format(toeFactorMult))#Y este output en outputX

	    ballRollClamp = fun.clampCreator(
			    name ='ballRollClamp_{}_clamp'.format(side),
			    MaxG='{}.toeBreak'.format(ctrFootIK),
			    InputG='{}.FootRoll'.format(ctrFootIK))

	    ballRollReleaseMinus = fun.substractCreator(
				   name='ballRollRelease_{}_minus'.format(side),
				   InputY0 = '{}.outputG'.format(ballRollClamp),
				   InputY1 = '{}.outputG'.format(toeRollClamped),
				   OutputY = 'ball_{}_pivot.rx'.format(side))

	    #heelRoll, ballRoll, toeRoll, toeSlide
	    cmds.connectAttr('{}.heelRoll'.format(ctrFootIK), 'heelParam_{}_pivot.rx'.format(side))
	    cmds.connectAttr('{}.ballRoll'.format(ctrFootIK), 'ballParam_{}_pivot.rx'.format(side))
	    cmds.connectAttr('{}.toeRoll'.format(ctrFootIK), 'toeParam_{}_pivot.rx'.format(side))
	    cmds.connectAttr('{}.toeSlide'.format(ctrFootIK), 'toeParam_{}_pivot.ry'.format(side))

	# RELACIONES BASICAS ENTRE CONTROLES Y HUESOS DEL IKHANDLE

	    #Creacion PACS
	for side in 'rl':
	    ctrHip = 'hip_{}_ctr'.format(side)
	    ctrHip_offset = 'hipCtr_{}_offset'.format(side)
	    jntHip = 'hip_{}_jnt'.format(side)
	    jntKnee = 'knee_{}_jnt'.format(side)
	    ctrHipFK = 'hipFK_{}_ctr'.format(side)
	    ctrKneeFK = 'kneeFK_{}_ctr'.format(side)
	    ctrFootFK = 'footFK_{}_ctr'.format(side)
	    ctrFootIK = 'footIK_{}_ctr'.format(side)
	    ctrToe = 'ball_{}_ctr'.format(side)   
	    ctrPole = 'legPole_{}_ctr'.format(side)
	    ctrSettings = 'legSettings_{}_ctr'.format(side)
	    control_list = ['hip', 'knee', 'foot', 'footIK', 'ball']
	    for element in control_list:  
		if element == 'footIK':
		    pac_name = 'footPAC_{}_IK_jnt'.format(side)
		    PAC = cmds.duplicate('foot_{}_jnt'.format(side), po=True, n=pac_name)[0]		
		else:
		    pac_name = '{}PAC_{}_jnt'.format(element, side)
	            PAC = cmds.duplicate('{}_{}_jnt'.format(element, side), po=True, n=pac_name)[0]
		if element == 'footIK':
		    cmds.parent(PAC, 'ankle_{}_pcon'.format(side))
		elif element == 'ball':
		    cmds.parent(PAC, 'toe_{}_ctr'.format(side))
		else:    
		    cmds.parent(PAC, '{}FK_{}_ctr'.format(element, side))



	     #Relacion basica entre controles, huesos e ikHandles

	    cmds.pointConstraint('footPAC_{}_IK_jnt'.format(side), 'leg_{}_ikHandle'.format(side),  
				  mo=False, n='pointConstraint_{}_footIkCtrToIkHandle'.format(side))

	    cmds.poleVectorConstraint('legPole_{}_ctr'.format(side), 'leg_{}_ikHandle'.format(side), 
				      n='poleVectorConstraint_{}_poleCtrToLegIkHandle'.format(side))

	    cmds.orientConstraint('hipPAC_{}_jnt'.format(side), 'hip_{}_jnt'.format(side), mo=True, 
				   n='orientConstraint_{}_hipCtrToHipJnt'.format(side))

	    cmds.pointConstraint('hip_{}_ctr'.format(side), 'hip_{}_jnt'.format(side), mo=True, 
				   n='pointConstraint_{}_hipCtrToHipJnt'.format(side))

	    cmds.orientConstraint('kneePAC_{}_jnt'.format(side), 'knee_{}_jnt'.format(side), mo=True,
				   n='orientConstraint_{}_kneeCtrToKneeJnt'.format(side))

	    cmds.orientConstraint('ballPAC_{}_jnt'.format(side), 'ball_{}_jnt'.format(side), mo=True, 
				   n='orientConstraint_{}_toeCtrToToeJnt'.format(side))
	    cmds.setAttr("orientConstraint_{}_toeCtrToToeJnt.interpType".format(side), 2)
	    
            
	    if side == 'l':		
		cmds.move(25, 'legSettingsCtr_{}_offset'.format(side), x=True)
	    else:
		cmds.move(-25, 'legSettingsCtr_{}_offset'.format(side), x=True)
	
	    cmds.parentConstraint('foot_{}_jnt'.format(side), 'legSettingsCtr_{}_offset'.format(side), mo=True, 
				   n='parentConstraint_{}_footJntToLegSettings'.format(side))

	    orient_constrait_foot = cmds.orientConstraint('footPAC_{}_jnt'.format(side), 'footPAC_{}_IK_jnt'.format(side), 
							  'foot_{}_jnt'.format(side),
							  n='orientConstraint_{}_footIkAndfootFkToFootJnt'.format(side))[0]
	    # Conexiones del IK/FK

	    cmds.connectAttr('legSettings_{}_ctr.Leg_IK'.format(side), 'leg_{}_ikHandle.ikBlend'.format(side))

	    cmds.connectAttr('Leg_IK_{}_rev.outputX'.format(side), '{}.footPAC_{}_jntW0'.format(orient_constrait_foot, side))
	    cmds.connectAttr('legSettings_{}_ctr.Leg_IK'.format(side), '{}.footPAC_{}_IK_jntW1'.format(orient_constrait_foot, side))
	    ###########
	    cmds.connectAttr('footIK_{}_ctr.Knee'.format(side), 'leg_{}_ikHandle.twist'.format(side))
	    ###########
	'''
	8.8. CONFIGURACION DEL SQUASH / 
	    STRETCH:8.8.1. Creacion de los locators para medir las distancias. 
	'''
	for side in 'rl': 
	    ctrHip = 'hip_{}_ctr'.format(side)
	    ctrHip_offset = 'hipCtr_{}_offset'.format(side)
	    jntHip = 'hip_{}_jnt'.format(side)
	    jntKnee = 'knee_{}_jnt'.format(side)
	    ctrHipFK = 'hipFK_{}_ctr'.format(side)
	    ctrKneeFK = 'kneeFK_{}_ctr'.format(side)
	    ctrFootFK = 'footFK_{}_ctr'.format(side)
	    ctrFootIK = 'footIK_{}_ctr'.format(side)
	    ctrToe = 'ball_{}_ctr'.format(side)   
	    ctrPole = 'legPole_{}_ctr'.format(side)
	    ctrSettings = 'legSettings_{}_ctr'.format(side)
	    control_list = [ctrHipFK, ctrKneeFK, ctrFootFK, ctrFootIK, ctrToe]
	#Squatch And Stretch
	     #Creacion de los locators para medir las distancias

	    hipStretch_loc = fun.locCreator(
			     name='stretchHip_{}_loc'.format(side), 
			     position='hip_{}_jnt'.format(side), 
			     dad = 'hip_{}_ctr'.format(side))

	    kneeStretch_loc = fun.locCreator(
			      name='stretchKnee_{}_loc'.format(side), 
			      position='kneePAC_{}_jnt'.format(side), 
			      dad = 'legPole_{}_ctr'.format(side))

	    footStretch_loc = fun.locCreator(
			      name='stretchFoot_{}_loc'.format(side), 
			      position='footIK_{}_ctr'.format(side), 
			      dad = 'ball_{}_pivot'.format(side))#??????????

		#NODOS DISTANCE DE LOS LOCATORS
	    upLeg_distance = fun.distanceCreator(
			     name = 'upLeg_{}_distance'.format(side), 
			     Input1 = '{}.worldPosition[0]'.format(hipStretch_loc), 
			     Input2 = '{}.worldPosition[0]'.format(kneeStretch_loc)) 

	    lowLeg_distance = fun.distanceCreator(
			      name = 'lowLeg_{}_distance'.format(side), 
			      Input1 = '{}.worldPosition[0]'.format(kneeStretch_loc), 
			      Input2 = '{}.worldPosition[0]'.format(footStretch_loc)) 

	    entireLeg_distance = fun.distanceCreator(
				 name = 'entireLeg_{}_distance'.format(side), 
				 Input1 = '{}.worldPosition[0]'.format(hipStretch_loc), 
				 Input2 = '{}.worldPosition[0]'.format(footStretch_loc)) 


		#Stretch IK y normalizar
	    normalStretch_div = fun.divideCreator(
				name= 'normalStretch_{}_div'.format(side), 
				Input1X = '{}.distance'.format(entireLeg_distance),
				Input2X = '{}.distance'.format(entireLeg_distance), Extraction2X=True)

	    stretch_clamp = fun.clampCreator(
			    name = 'legStretch_{}_clamp'.format(side), 
			    MaxG = 999,  
			    MinG = 'general_c_ctr.GlobalScale', 
			    InputG = '{}.outputX'.format(normalStretch_div))

	    upLegStretch_div = fun.divideCreator(
			       name= 'upLegStretch_{}_div'.format(side), 
			       Input1X = '{}.distance'.format(upLeg_distance),
			       Input2X = '{}.distance'.format(upLeg_distance), Extraction2X=True)

	    lowLegStretch_div = fun.divideCreator(
				name= 'lowLegStretch_{}_div'.format(side), 
				Input1X = '{}.distance'.format(lowLeg_distance),
				Input2X = '{}.distance'.format(lowLeg_distance), Extraction2X=True)                           

	    iKStretch_blend = fun.blendColorsCreator(
			      Name = 'ikStretch_{}_blend'.format(side), 
			      Blender = 0,  
			      Color1G = '{}.outputX'.format(upLegStretch_div), 
			      Color1B = '{}.outputX'.format(lowLegStretch_div), 
			      Color2G = '{}.outputG'.format(stretch_clamp), 
			      Color2B = '{}.outputG'.format(stretch_clamp))


	    finalStretch_blend =  fun.blendColorsCreator(
				  Name = 'finalStretch_Leg_{}_blend'.format(side), 
				  Blender = 'legSettings_{}_ctr.Leg_IK'.format(side),  
				  Color1G = '{}.outputG'.format(iKStretch_blend), 
				  Color1B = '{}.outputB'.format(iKStretch_blend), 
				  Color2G = 1, 
				  Color2B = 1)
				  ####################################                     

		#Configuracion del AutoStretch 
	    stretchiness_blend = fun.blendColorsCreator(
				 Name = 'stretchiness_Leg_{}_blend'.format(side),  
				 Color1G = '{}.outputG'.format(finalStretch_blend), 
				 Color1B = '{}.outputB'.format(finalStretch_blend), 
				 Color2G = 'general_c_ctr.GlobalScale', 
				 Color2B = 'general_c_ctr.GlobalScale') 

	    stretchByGlobal_div = fun.divideCreator(
				  name='stretchByGlobal_{}_div'.format(side), 
				  Input1X = '{}.outputG'.format(stretchiness_blend), 
				  Input1Y = '{}.outputB'.format(stretchiness_blend), 
				  Input2X = 'general_c_ctr.GlobalScale', 
				  Input2Y = 'general_c_ctr.GlobalScale')

	    autostretchOverride_sum = fun.plusCreator(
				      name='autoStretchOverride_{}_sum'.format(side), 
				      InputX0 = 'Leg_IK_{}_rev.outputX'.format(side), 
				      InputX1 = '{}.autoStretch'.format(ctrFootIK))

	    finalStretchiness_clamp = fun.clampCreator(
				      name = 'finalStretchiness_{}_clamp'.format(side),
				      MaxG = 1,  
				      MinG = 'general_c_ctr.GlobalScale', 
				      InputG = '{}.output2D.output2Dx'.format(autostretchOverride_sum))
	    cmds.connectAttr('{}.outputG'.format(finalStretchiness_clamp), '{}.blender'.format(stretchiness_blend))
	    #Conectar las escalas de los huesos
	    cmds.connectAttr('{}.outputX'.format(stretchByGlobal_div), 'hip_{}_jnt.sx'.format(side))
	    cmds.connectAttr('{}.outputY'.format(stretchByGlobal_div), 'knee_{}_jnt.sx'.format(side))
	#Configuracion del Stretch FK

	    stretchByGlobal_hipFK_mult = fun.multiplyCreator(
					 name = 'stretchByGlobal_HipFK_{}_mult'.format(side), 
					 linear = True, 
					 Input1 = 'hipFK_{}_ctr.Stretch'.format(side), 
					 Input2 = 'general_c_ctr.GlobalScale',
					 Output = '{}.color2G'.format(finalStretch_blend))

	    cmds.pointConstraint('knee_{}_jnt'.format(side), 'kneeFKCtr_{}_offset'.format(side))

	    stretchByGlobal_kneeFK_mult = fun.multiplyCreator(
					  name = 'stretchByGlobal_KneeFK_{}_mult'.format(side), 
					  linear = True, 
					  Input1 = 'kneeFK_{}_ctr.Stretch'.format(side), 
					  Input2 = 'general_c_ctr.GlobalScale',
					  Output = '{}.color2B'.format(finalStretch_blend))

	    cmds.pointConstraint('legEnd_{}_jnt'.format(side), 'footFKCtr_{}_offset'.format(side))
	#8.8.7 twistUplegChain con el Stretch

	    uplegTwistStretch = fun.curveInfoCreator(
				Name = 'uplegTwistStretch_{}_curveInfo'.format(side), 
				Input = 'twistUpleg_{}_curveShape.worldSpace[0]'.format(side))
	    upleg_ikCurveLength = fun.divideCreator(
				  name='uplegikCurve_{}_div'.format(side), 
				  Input1X = '{}.arcLength'.format(uplegTwistStretch), 
				  Input2X = '{}.arcLength'.format(uplegTwistStretch), Extraction2X = True)
	    upleg_ikCurveLengthByGlobal = fun.divideCreator(
					  name='upleg_ikCurveLengthByGlobal_{}_div'.format(side), 
					  Input1X = '{}.outputX'.format(upleg_ikCurveLength), 
					  Input2X = 'general_c_ctr.GlobalScale') 
	    twist_chain = cmds.listRelatives('upLeg0_{}_skn'.format(side), ad=True)
	    twist_chain.remove('twistUpleg_{}_eff'.format(side))
	    twist_chain.remove(twist_chain[0])
	    twist_chain.append('upLeg0_{}_skn'.format(side))
	    for jnt in twist_chain:
		cmds.connectAttr('{}.outputX'.format(upleg_ikCurveLengthByGlobal),
				 '{}.sx'.format(jnt))
	# 8.8.8. conectar los joints del twistLowlegChain con el stretch

	    lowlegTwistStretch = fun.curveInfoCreator(
				Name = 'lowlegTwistStretch_{}_curveInfo'.format(side), 
				Input = 'twistLowleg_{}_curveShape.worldSpace[0]'.format(side))
	    lowleg_ikCurveLength = fun.divideCreator(
				   name = 'lowlegikCurve_{}_div'.format(side), 
				   Input1X = '{}.arcLength'.format(lowlegTwistStretch), 
				   Input2X = '{}.arcLength'.format(lowlegTwistStretch), Extraction2X = True)
	    lowleg_ikCurveLengthByGlobal =fun.divideCreator(
					  name='lowlegikCurveByGlobal_{}_div'.format(side), 
					  Input1X = '{}.outputX'.format(lowleg_ikCurveLength), 
					  Input2X = 'general_c_ctr.GlobalScale') 
	    twist_chain = cmds.listRelatives('lowLeg0_{}_skn'.format(side), ad=True)
	    twist_chain.remove('twistLowleg_{}_eff'.format(side))
	    twist_chain.remove(twist_chain[0])
	    twist_chain.append('lowLeg0_{}_skn'.format(side))
	    for jnt in twist_chain:
		cmds.connectAttr('{}.outputX'.format(lowleg_ikCurveLengthByGlobal),
				 '{}.sx'.format(jnt)) 

	# 8.8.9. Conectar el pinKnee
	    pinKneeByIK = fun.multiplyCreator(
			  name = 'pinKnee_{}_mult'.format(side), 
			  linear = True, 
			  Input1 = '{}.pinKnee'.format(ctrPole), 
			  Input2 = '{}.Leg_IK'.format(ctrSettings), 
			  Output = '{}.input2D[2].input2Dx'.format(autostretchOverride_sum)) 

	#8.8.10. Reposicionar el kneeStretchLoc en el ctrLegPole (antes estaba sobre el jntKnee).    
	    shapeless = kneeStretch_loc.replace('Shape', '')
	    for axis in 'xyz':
		cmds.setAttr('{}.t{}'.format(shapeless ,axis), 0)       

	# 8.8.11. Configuracion del autoSquash
	    stretchByGlobalInv = fun.divideCreator(
				 name= 'stretchByGlobalInv_{}_div'.format(side), 
				 Input1X = 1,
				 Input1Y = 1,
				 Input2X = '{}.outputX'.format(stretchByGlobal_div),
				 Input2Y = '{}.outputY'.format(stretchByGlobal_div))
	    autoSquashBlend = fun.blendColorsCreator(
			      Name = 'autoSquashBlend_{}_blend'.format(side),  
			      Blender = '{}.autoSquash'.format(ctrSettings),
			      Color1G = '{}.outputX'.format(stretchByGlobalInv), 
			      Color1B = '{}.outputY'.format(stretchByGlobalInv), 
			      Color2G = 1, 
			      Color2B = 1)

	    for floor, i in ['up','G'], ['low','B']:  
		twist_chain = cmds.listRelatives('{}Leg0_{}_skn'.format(floor, side), ad=True)
		twist_chain.remove('twist{}leg_{}_eff'.format(floor.capitalize(), side))
		twist_chain.append('{}Leg0_{}_skn'.format(floor, side))
		for jnt in twist_chain:
		    for axis in 'yz':
			cmds.connectAttr('{}.output{}'.format(autoSquashBlend, i),
					 '{}.s{}'.format(jnt, axis))

	    fun.blendSystem(
	    CurveU = 'twistUpleg_{}_curve'.format(side), 
	    CurveL = 'twistLowleg_{}_curve'.format(side), 
	    ClusterName = 'ClusterBlendSystem_Leg_{}_'.format(side), 
	    upJnt = jntHip, 
	    middleJnt = jntKnee, 
	    upBlend = 'legUpBlend_{}_ctr'.format(side), 
	    middleBlend = 'legMiddleBlend_{}_ctr'.format(side), 
	    lowBlend = 'legLowBlend_{}_ctr'.format(side))


	###8.10. CONEXION ENTRE MODULOS (pelvis)



	    cmds.parent('legJnt_{}_offset'.format(side), 'pelvis_c_skn')

	    hipFKPcon = cmds.group(em=True, n='hipFK_{}_pcon'.format(side))
	    pcon_matrix = cmds.xform('hipFKCtr_{}_offset'.format(side), ws=True, matrix = True, q=True)
	    cmds.xform(hipFKPcon, matrix=pcon_matrix, ws=True)

	    cmds.parent(hipFKPcon, 'hip_{}_ctr'.format(side)) #!!!! EN LOS APUNTES ESTEparent no tenia ningun sentido, lo he cambiado. Si sigue sin funcionar mira los videos
	    cmds.parent('legMiddleBlendCtr_{}_offset'.format(side), 'center_c_ctr')
	    cmds.pointConstraint(hipFKPcon, 'hipFKCtr_{}_offset'.format(side)) 
	    cmds.parentConstraint('hip_{}_ctr'.format(side), 'upLeg_RollSystem_{}_grp'.format(side), mo=True)

	'''
	CORRECCIONES POST SCRIPT
	    Emparentar Controles to centro
	'''
	
	
	
	for side in 'rl':
	    cmds.connectAttr('legSettings_{}_ctr.Leg_IK'.format(side), 'legPole_{}_ctr.visibility'.format(side))	
	    for part in ['foot', 'knee', 'hip']:
		cmds.connectAttr('Leg_IK_{}_rev.output.outputX'.format(side), '{}FK_{}_ctr.visibility'.format(part, side))
            cmds.connectAttr('pinKnee_{}_mult.output'.format(side), 'ikStretch_{}_blend.blender'.format(side)) 			
	    #cmds.connectAttr('legSettings_{}_ctr.Leg_IK'.format(side), 'foot_{}_FK_ctr.visibility'.format(side))

	for side in 'rl':
	    cmds.setAttr('knee_{}_twistValue.radius'.format(side), 2)
	    cmds.setAttr('foot_{}_twistValue.radius'.format(side), 2)
	    cmds.connectAttr('legSettings_{}_ctr.Leg_IK'.format(side), 'footIK_{}_ctr.visibility'.format(side))
	
        joints = cmds.ls(type='joint')
	
        for jnt in joints:
	    if '_skn_PAC' in jnt:
		newName = jnt.replace('_skn_PAC', '_PAC')
		cmds.rename(jnt, newName)
            else:
                pass	
	for axis in 'xyz':
		cmds.connectAttr('general_c_ctr.GlobalScale', 'general_c_ctr.s{}'.format(axis))
		cmds.connectAttr('general_c_ctr.GlobalScale', 'skeleton_c_grp.s{}'.format(axis))
