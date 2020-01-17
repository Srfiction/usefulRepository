from maya import cmds
from maya.api import OpenMaya
import AutoRig.Functions_Autorig as fun

def createArm(uparmJnts=8, lowarmJnts=8):


    """""""""""""""""""""""""""""""""
    El reto del brazo comienza. Enfrentate a el
    con denuedo y determinacion. Confia en ti mismo y todo saldra
    a pedir de Yume

    Notas: 
        rotacion Z -58.251
        Ha habido un problema con la orientacion del pole del arm_l_skn. Lo he arreglado seteand
        atributos pero no garantiza que eso vaya a ser estable. OJO
        hay que cambiar los skn por jnts para no confundirlos de los skn en el twist

    Lista de locators que vas a necesitar:
        clavicle_loc_END_autoRig
        lowerArm_loc_autoRig
        hand_loc_autoRig

           ARM~~ARM~~ARM
    """""""""""""""""""""""""""""""""
    brazo = ['shoulder', 'hand', 'elbow']
    generalC = "general_c_ctr" 
    tw='twist'
    Tv='twistValue'
    Nr='nonRoll'
    vectores=['X', 'Y', 'Z']
    shoulderLocPos = cmds.getAttr('clavicle_l_loc_END_autoRig.translate')
    elbowLocPos = cmds.getAttr('lowerArm_l_loc_autoRig.translate')
    handLocPos = cmds.getAttr('hand_loc_autoRig.translate')

    cmds.joint(n='shoulder_l_skn', rad=0.1)
    cmds.select(cl=True)
    cmds.joint(n='elbow_l_skn', rad=0.1)
    cmds.select(cl=True)
    cmds.joint(n='elbow_l_End', rad=0.1)

    cmds.xform('shoulder_l_skn', t=shoulderLocPos[0])
    cmds.xform('elbow_l_skn', t=elbowLocPos[0])
    cmds.xform('elbow_l_End', t=handLocPos[0])

    cmds.parent('elbow_l_skn', 'shoulder_l_skn')
    cmds.parent('elbow_l_End', 'elbow_l_skn')

    side=['l','r']

    uA = 'shoulder_{}_skn'.format(side[0])
    lA = 'elbow_{}_skn'.format(side[0])

    cmds.mirrorJoint(uA, myz=True, mb=True, sr=['_l_', '_r_'])

    cmds.joint(oj='xyz',sao='yup', e=True, ch=True)

    hands=['elbow_r_End', 'elbow_l_End']

    for side in 'rl':
        hnd = cmds.duplicate('elbow_{}_End'.format(side), n='hand_{}_skn'.format(side), po=True)
        cmds.parent(hnd, w=True)
        end = cmds.joint(n='hand_{}_End'.format(side), rad=0.05)
        if side == 'l':
            cmds.xform(end, t=(+0.25, 0, 0))
        else:
            cmds.xform(end, t=(-0.25, 0, 0))
        cmds.joint(hnd, oj='xyz',sao='yup', e=True, ch=True)
        cmds.pointConstraint('elbow_{}_End'.format(side), hnd)


    #####################EQUACION DE LA ANTIVIDA PARA AGRUPAR###############

    toGroup = ['hand_l_skn', 'hand_r_skn', 'shoulder_r_skn', 'shoulder_l_skn']    


    for element in toGroup:
        pos = cmds.getAttr('{}.translate'.format(element))
        grp = cmds.group(n='{}_offset'.format(str(element)), em=True)
        cmds.xform(grp, t=pos[0], r=True)
        cmds.parent(element, grp)
        cmds.parent(grp, 'skeleton_c_grp')

    #6.2. Creacion del ikHandle de la cadena principal
 
    for side in 'rl':
        cmds.select('shoulder_{}_skn'.format(side))
        cmds.select('elbow_{}_End'.format(side), add=True)
        ikH = cmds.ikHandle(n='arm_{}_ikHandle'.format(side), sol='ikRPsolver', s='sticky')
        cmds.group(n='rig_arm_{}_grp'.format(side))

    polX = cmds.getAttr('arm_r_ikHandle.poleVectorX')
    polY = cmds.getAttr('arm_r_ikHandle.poleVectorY')
    polZ = cmds.getAttr('arm_r_ikHandle.poleVectorZ')

    cmds.setAttr('arm_l_ikHandle.poleVectorX', polX)
    cmds.setAttr('arm_l_ikHandle.poleVectorY', polY)
    cmds.setAttr('arm_l_ikHandle.poleVectorZ', polZ)

    ''''''''''''''''''''''
    6.3. Configuracion de los sistemas nonRoll
    6.3.1 Configuracion de la cadena NonRoll del Shoulde
    '''

    arms=['shoulder_l_skn', 'shoulder_r_skn']
    for side in 'rl':
        arm = 'shoulder_{}_skn'.format(side)
        nonRoll = cmds.duplicate(arm, n='shoulder_{}_nonRoll'.format(side), rc=True)
        rollList = cmds.listRelatives(nonRoll, allDescendents=True)
        cmds.delete(rollList[:2])
        cmds.parent('shoulder_{}_nonRoll'.format(side), w=True)
        cmds.rename(rollList[-1], 'shoulder_{}_nonRoll_End'.format(side))
        cmds.group(n='shoulder_{}_nonRoll_grp'.format(side), em=True)
        cmds.parent('shoulder_{}_nonRoll'.format(side), 'shoulder_{}_nonRoll_grp'.format(side))
  
	
	#Creacion del Ik
	ik='shoulder_{}_nonRoll'.format(side)
        cmds.select(ik)
        cmds.select('shoulder_{}_{}_End'.format(side, Nr))
        nRH = cmds.ikHandle(n='shoulder_{}_ikHandle_{}'.format(side, Nr), sol='ikSCsolver', s='sticky')
        cmds.parent(nRH[0], 'shoulder_{}_{}_grp'.format(side, Nr))
        for a in 'XYZ':
            cmds.setAttr('shoulder_{}_ikHandle_{}.poleVector{}'.format(side, Nr, a), 0)
	
	#Creacion del pointConstraint
        cmds.pointConstraint('shoulder_{}_skn'.format(side), ik, n='pointConstraint_{}_shoulderToNonRoll'.format(side))
        cmds.pointConstraint('elbow_{}_skn'.format(side), 'shoulder_{}_ikHandle_{}'.format(side, Nr), n='pointConstraint_{}_elbowToikHandle'.format(side))

	cmds.parent('shoulder_{}_nonRoll_grp'.format(side), 'rig_arm_{}_grp'.format(side))

        p = cmds.group(n='shoulder_{}_rollSystem'.format(side), em=True)
        cmds.parent(p, 'rig_arm_{}_grp'.format(side))
        cmds.parent('shoulder_{}_nonRoll_grp'.format(side), p)

    '''
    6.3.2 Configuracion de la cadena NonRoll del Elbow
    '''
    elbow=['elbow_l_skn', 'elbow_r_skn']
    for arm in elbow:
        nonRoll = cmds.duplicate(arm, n='elbow_{}_nonRoll'.format(arm[6]), rc=True)
        rollList = cmds.listRelatives(nonRoll, allDescendents=True)
        cmds.delete(rollList[1])
        cmds.parent('elbow_{}_nonRoll'.format(arm[6]), w=True)
        cmds.rename(rollList[0], 'elbow_{}_nonRoll_End'.format(arm[6]))


    cmds.group(n='elbow_l_nonRoll_grp', em=True)
    cmds.parent('elbow_l_nonRoll', 'elbow_l_nonRoll_grp')
    cmds.group(n='elbow_r_nonRoll_grp', em=True)
    cmds.parent('elbow_r_nonRoll', 'elbow_r_nonRoll_grp')

    ik2=['elbow_r_nonRoll', 'elbow_l_nonRoll']

    for i in ik2: #Creacion del Ik
        cmds.select(i)
        cmds.select('elbow_{}_nonRoll_End'.format(i[6]))
        nRH = cmds.ikHandle(n='elbow_{}_ikHandle_{}'.format(i[6], Nr), sol='ikSCsolver', s='sticky')
        cmds.parent(nRH[0], 'elbow_{}_{}_grp'.format(i[6], Nr))
        for a in vectores:
            cmds.setAttr('elbow_{}_ikHandle_{}.poleVector{}'.format(i[6], Nr, a), 0)


    for i in ik2: #Creacion del pointConstraint
        cmds.pointConstraint('elbow_{}_skn'.format(i[6]), i, n='pointConstraint_{}_shoulderENDToNonRoll'.format(i[6]))
        cmds.pointConstraint('hand_{}_skn'.format(i[6]), 'elbow_{}_ikHandle_nonRoll'.format(i[6]), n='pointConstraint_{}_elbowENDToikHandle'.format(i[6]))


    '''''''''
    Global Sclae a los Non Roll
    grupos de rollSystem de elbow
    '''''''''

    for side in 'rl':
        k = cmds.group(n='elbow_{}_rollSystem'.format(side), em=True)
        cmds.parent(k, 'rig_arm_{}_grp'.format(side))
        cmds.parent('elbow_{}_{}_grp'.format(side, Nr), k)

    nonRollArm=['shoulder_l_rollSystem', 'elbow_l_rollSystem', 'shoulder_r_rollSystem', 'elbow_r_rollSystem']

    for r in nonRollArm:
        for a in vectores:
            cmds.connectAttr('general_c_ctr.GlobalScale', '{}.scale{}'.format(r, a))
    
    #TwistValue
    cmds.duplicate('shoulder_l_nonRoll_End', n='elbow_l_twistValue')
    tvL = 'elbow_l_twistValue'
    cmds.setAttr('elbow_l_twistValue.jointOrientX', 0)
    cmds.parent(tvL, 'elbow_l_skn')
    cmds.duplicate('shoulder_r_nonRoll_End', n='elbow_r_twistValue')
    tvR='elbow_r_twistValue'
    cmds.parent(tvR, 'elbow_r_skn')

    tiwstValues=[tvL, tvR]
    for indent in 'rl':
        cmds.aimConstraint('hand_{}_skn'.format(indent), 
		           'elbow_{}_twistValue'.format(indent),
			   aim = [1,0,0],
		           u = [0,1,0],
		           wu = [0,1,0],
		           n='elbow_{}_twistValue_elbowToHand'.format(indent), 
		           wuo='elbow_{}_nonRoll'.format(indent), 
		           wut="objectrotation",
			   mo=True)


    cmds.parentConstraint('shoulder_r_nonRoll', 'elbow_r_nonRoll_grp', mo=True, n='parentConstraint_r_nonRoll_shoulderToelbowNonRollGrp')
    cmds.parentConstraint('shoulder_l_nonRoll', 'elbow_l_nonRoll_grp', mo=True, n='parentConstraint_l_nonRoll_shoulderToelbowNonRollGrp')

    '''
    6.3.3 Configuracion de la cadena NonRoll del Hand
    '''
    for side in 'rl':
        handNonRoll = cmds.duplicate('hand_{}_skn'.format(side), n='hand_{}_nonRoll'.format(side), rc=True)

        handNonRollList = cmds.listRelatives(handNonRoll)
        cmds.rename(handNonRollList[0], 'hand_{}_nonRoll_End'.format(side))
        cmds.delete(handNonRollList[1])

        cmds.group(n='hand_{}_nonRoll_grp'.format(side),em=True,w=True)

        cmds.parent('hand_{}_nonRoll'.format(side), 'hand_{}_nonRoll_grp'.format(side))
        cmds.parent('hand_{}_nonRoll_grp'.format(side), 'elbow_{}_rollSystem'.format(side))

        cmds.select('hand_{}_nonRoll'.format(side))
        cmds.select('hand_{}_{}_End'.format(side, Nr))
        nRH = cmds.ikHandle(n='hand_{}_ikHandle_{}'.format(side, Nr), sol='ikSCsolver', s='sticky')
        cmds.parent(nRH[0], 'hand_{}_{}_grp'.format(side, Nr))
        for a in vectores:
            cmds.setAttr('hand_{}_ikHandle_{}.poleVector{}'.format(side, Nr, a), 0)
        cmds.pointConstraint('hand_{}_skn'.format(side), 'hand_{}_{}'.format(side, Nr), n='pointConstraint_{}_handNonRollToHandSkn'.format(side))
        cmds.pointConstraint('hand_{}_End'.format(side), 'hand_{}_ikHandle_{}'.format(side, Nr), n='pointConstraint_{}_handENDToHandikHandle'.format(side))

	#twistValue
	
        h = cmds.duplicate('hand_{}_skn'.format(side), n='hand_{}_{}'.format(side, Tv), rc=True)
        handList= cmds.listRelatives(h)
        cmds.delete(handList[0])
        cmds.delete(handList[1])
        cmds.parent('hand_{}_{}'.format(side, Tv), 'hand_{}_skn'.format(side))
        cmds.aimConstraint('hand_{}_End'.format(side), 
			   'hand_{}_{}'.format(side, Tv),  
			   n='aimConstraint_{}_twistValue_handTohandTwistValue'.format(side), 
			   wuo='hand_{}_nonRoll'.format(side), wut="objectrotation", mo=False)
	###
	cmds.parentConstraint('elbow_{}_skn'.format(side), 'hand_{}_nonRoll_grp'.format(side), mo=True, n='eseParentQueNosCostoEncontratTanto_{}_pc'.format(side))


    '''
        ~~~~CADENA TWIST JOINTS~~~~

        1) upperARM
            a)jointChain
                 i) Left
                ii) Right

            b)ikSpline
                 i) Left
                ii) Right

        2) foreARM
            a)jointChain
                 i) Left
                ii) Right

            b)ikSpline
                 i) Left
                ii) Right
    '''



    cmds.select(cl=True)

    #    upperARM - jointChain - LEFT
    def upperArmJointLeft(cantidad, nombre, chin, radio):


        inicio = 'clavicle_l_loc_END_autoRig'
        fin = 'lowerArm_l_loc_autoRig'
        start_point = cmds.xform(inicio, q=True, t=True)
        end_point = cmds.xform(fin, q=True, t=True)
        vector_sta = OpenMaya.MVector(start_point)
        vector_end = OpenMaya.MVector(end_point)
        i = 0
        all_joints = []
        for num in range(cantidad):
            dif_point = vector_end-vector_sta
            offset = 1.0/(cantidad-1)
            new_point=dif_point*offset
            final_point = vector_sta + new_point   
            mid_pos=dif_point*(offset*num)
            final_pos=vector_sta+mid_pos
            jnt=cmds.joint(n=nombre + str(i), p=list(final_pos), rad=radio)
            if i != 0:
                cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)
            i += 1
            all_joints.append(jnt)
            if chin==False:
                cmds.select(cl=1)
            if i == cantidad:
                return all_joints

    upperArmJointLeft(uparmJnts, 'upperArm_l_skn', chin=True, radio=0.1)
    cmds.rename('upperArm_l_skn0', 'upperArm_l_skn')
    foreArmJointList = cmds.listRelatives('upperArm_l_skn', allDescendents=True)
    foreArmJointList.append('upperArm_l_skn')
    cmds.rename(foreArmJointList[0], 'upperArm_l_End')  


    cmds.select(cl=True)


    #    upperARM - jointChain - RIGHT

    def upperArmJointRight(cantidad, nombre, chin, radio):


        inicio = 'shoulder_r_nonRoll'
        fin = 'elbow_r_nonRoll'
        start_point = cmds.xform(inicio, q=True, t=True)
        end_point = cmds.xform(fin, q=True, t=True)
        vector_sta = OpenMaya.MVector(start_point)
        vector_end = OpenMaya.MVector(end_point)
        i = 0
        all_joints = []
        for num in range(cantidad):
            dif_point = vector_end-vector_sta
            offset = 1.0/(cantidad-1)
            new_point=dif_point*offset
            final_point = vector_sta + new_point   
            mid_pos=dif_point*(offset*num)
            final_pos=vector_sta+mid_pos
            jnt=cmds.joint(n=nombre + str(i), p=list(final_pos), rad=radio)
            if i != 0:
                cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)
            i += 1
            all_joints.append(jnt)
            if chin==False:
                cmds.select(cl=1)
            if i == cantidad:
                return all_joints

    upperArmJointRight(uparmJnts, 'upperArm_r_skn', chin=True, radio=0.1)
    cmds.rename('upperArm_r_skn0', 'upperArm_r_skn')
    foreArmJointList = cmds.listRelatives('upperArm_r_skn', allDescendents=True)
    foreArmJointList.append('upperArm_r_skn')
    cmds.rename(foreArmJointList[0], 'upperArm_r_End')  

    #    upperARM - ikSpline - LEFT



    def upperArmIkSplineLeft():
        cmds.ikHandle(n='upperArm_l_ikHandle_{}'.format(tw),  sj='upperArm_l_skn', ee= 'upperArm_l_End', sol='ikSplineSolver')
        c = cmds.rename('curve1', 'upperArm_l_ikHandle_curve_{}'.format(tw))
        cmds.parent('upperArm_l_ikHandle_curve_{}'.format(tw), 'rig_arm_l_grp')
        cmds.parent('upperArm_l_ikHandle_{}'.format(tw), 'shoulder_l_rollSystem')

    upperArmIkSplineLeft()

    cmds.parent('upperArm_l_skn', 'shoulder_l_rollSystem')

    #    upperARM - ikSpline - RIGHT



    def upperArmIkSplineRight():
        cmds.ikHandle(n='upperArm_r_ikHandle_{}'.format(tw),  sj='upperArm_r_skn', ee= 'upperArm_r_End', sol='ikSplineSolver')
        cmds.rename('curve1', 'upperArm_r_ikHandle_curve_{}'.format(tw))
        cmds.parent('upperArm_r_ikHandle_curve_{}'.format(tw), 'rig_arm_r_grp')
        cmds.parent('upperArm_r_ikHandle_{}'.format(tw), 'shoulder_r_rollSystem')

    upperArmIkSplineRight()


    cmds.parent('upperArm_r_skn', 'shoulder_r_rollSystem')

    cmds.select(cl=True)


    #    foreARM - jointChain - LEFT

    def foreArmJointLeft(cantidad, nombre, chin, radio):


        inicio = 'lowerArm_l_loc_autoRig'
        fin = 'hand_loc_autoRig'
        start_point = cmds.xform(inicio, q=True, t=True)
        end_point = cmds.xform(fin, q=True, t=True)
        vector_sta = OpenMaya.MVector(start_point)
        vector_end = OpenMaya.MVector(end_point)
        i = 0
        all_joints = []
        for num in range(cantidad):
            dif_point = vector_end-vector_sta
            offset = 1.0/(cantidad-1)
            new_point=dif_point*offset
            final_point = vector_sta + new_point   
            mid_pos=dif_point*(offset*num)
            final_pos=vector_sta+mid_pos
            jnt=cmds.joint(n=nombre + str(i), p=list(final_pos), rad=radio)
            if i != 0:
                cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)
            i += 1
            all_joints.append(jnt)
            if chin==False:
                cmds.select(cl=1)
            if i == cantidad:
                return all_joints

    foreArmJointLeft(lowarmJnts, 'foreArm_l_skn', chin=True, radio=0.1)
    cmds.rename('foreArm_l_skn0', 'foreArm_l_skn')
    foreArmJointList = cmds.listRelatives('foreArm_l_skn', allDescendents=True)
    foreArmJointList.append('foreArm_l_skn')
    cmds.rename(foreArmJointList[0], 'foreArm_l_End')  
    cmds.parent('foreArm_l_skn', 'elbow_l_skn')	

    #    foreARM - jointChain - RIGHT


    cmds.select(cl=True)

    def foreArmJointRight(cantidad, nombre, chin, radio):


        inicio = 'elbow_r_nonRoll'
        fin = 'hand_r_nonRoll'
        start_point = cmds.xform(inicio, q=True, t=True)
        end_point = cmds.xform(fin, q=True, t=True)
        vector_sta = OpenMaya.MVector(start_point)
        vector_end = OpenMaya.MVector(end_point)
        i = 0
        all_joints = []
        for num in range(cantidad):
            dif_point = vector_end-vector_sta
            offset = 1.0/(cantidad-1)
            new_point=dif_point*offset
            final_point = vector_sta + new_point   
            mid_pos=dif_point*(offset*num)
            final_pos=vector_sta+mid_pos
            jnt=cmds.joint(n=nombre + str(i), p=list(final_pos), rad=radio)
            if i != 0:
                cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)
            i += 1
            all_joints.append(jnt)
            if chin==False:
                cmds.select(cl=1)
            if i == cantidad:
                return all_joints

    foreArmJointRight(lowarmJnts, 'foreArm_r_skn', chin=True, radio=0.1)
    cmds.rename('foreArm_r_skn0', 'foreArm_r_skn')
    foreArmJointList = cmds.listRelatives('foreArm_r_skn', allDescendents=True)
    foreArmJointList.append('foreArm_r_skn')
    cmds.rename(foreArmJointList[0], 'foreArm_r_End') 
    cmds.parent('foreArm_r_skn', 'elbow_r_skn')	

    #    foreARM - ikSpline - LEFT

    def foreArmIkSplineLeft():
        cmds.ikHandle(n='foreArm_l_ikHandle_{}'.format(tw),  sj='foreArm_l_skn', ee= 'foreArm_l_End', sol='ikSplineSolver')
        cmds.rename('curve1', 'foreArm_l_ikHandle_curve_{}'.format(tw))
        cmds.parent('foreArm_l_ikHandle_curve_{}'.format(tw), 'rig_arm_l_grp')
        cmds.parent('foreArm_l_ikHandle_{}'.format(tw), 'elbow_l_rollSystem')

    foreArmIkSplineLeft()


    #    foreARM - ikSpline - RIGHT
    side='rl'
    def foreArmIkSplineRight():
        cmds.ikHandle(n='foreArm_r_ikHandle_{}'.format(tw),  sj='foreArm_r_skn', ee= 'foreArm_r_End', sol='ikSplineSolver')
        cmds.rename('curve1', 'foreArm_r_ikHandle_curve_{}'.format(tw))
        cmds.parent('foreArm_r_ikHandle_curve_{}'.format(tw), 'rig_arm_r_grp')
        cmds.parent('foreArm_r_ikHandle_{}'.format(tw), 'elbow_r_rollSystem')

    foreArmIkSplineRight()


    # twistUpperArm - nodos

    def twistUpperArm():
        for i in side:
            elbowValeu = 'elbow_{}_{}'.format(i, Tv)
            shoulderHandle = 'upperArm_{}_ikHandle_twist'.format(i)

            multMenusUno = cmds.shadingNode('multDoubleLinear', n='{}_{}_{}_multMenusUno'.format('Shoulder', Tv, i), au=True)
            cmds.connectAttr('{}.rotateX'.format(elbowValeu), '{}.input1'.format(multMenusUno))
            cmds.setAttr('{}.input2'.format(multMenusUno), -1)
            cmds.connectAttr('{}.output'.format(multMenusUno), '{}.twist'.format(shoulderHandle))


    twistUpperArm()

    def twistForeArm():
        for i in side:
            handValeu = 'hand_{}_{}'.format(i, Tv)
            shandHandle = 'foreArm_{}_ikHandle_twist'.format(i)

            multMenusUno = cmds.shadingNode('multDoubleLinear', n='{}_{}_{}_multMenusUno'.format('Elbow', Tv, i), au=True)
            cmds.connectAttr('{}.rotateX'.format(handValeu), '{}.input1'.format(multMenusUno))
            cmds.setAttr('{}.input2'.format(multMenusUno), -1)
            cmds.connectAttr('{}.output'.format(multMenusUno), '{}.twist'.format(shandHandle))


    twistForeArm()

    '''
    Colocacion de controles:
        Hand_l_IK
        FKs
        Pole
    '''
    for i in 'rl':
        ikOff = 'handIKCtr_{}_offset'.format(i)
        handOff =  'handFKCtr_{}_offset'.format(i)
        shoulderOff = 'shoulderFKCtr_{}_offset'.format(i)
        elbowOff = 'elbowFKCtr_{}_offset'.format(i)
        armSettingsOff = 'armSettingsCtr_{}_offset'.format(i)
        
        handPos = cmds.xform('hand_{}_nonRoll'.format(i), ws=True, q=True, t=True)
        shouldePos=cmds.xform('shoulder_{}_nonRoll'.format(i), ws=True, q=True, t=True)
        elbowPos=cmds.xform('elbow_{}_nonRoll'.format(i), ws=True, q=True, t=True)
        
        cmds.xform(ikOff, ws=True, t=handPos)
        cmds.xform(handOff, ws=True, t=handPos)
        cmds.xform(shoulderOff, ws=True, t=shouldePos)
        cmds.xform(elbowOff, ws=True, t=elbowPos)
        
        
        

        cmds.parent(armSettingsOff, 'hand_{}_nonRoll_End'.format(i))
        for a in vectores:
            cmds.setAttr('{}.translate{}'.format(armSettingsOff, a), 0)
        if i == 'l':
            cmds.setAttr('{}.translateX'.format(armSettingsOff), 30)
        else:
            cmds.setAttr('{}.translateX'.format(armSettingsOff), -30)
        cmds.parentConstraint('hand_{}_skn'.format(i), armSettingsOff, mo=True, n='parentConstraint_{}_ArmSettingsParent')

####
    def poleLocation():
        from maya import cmds , OpenMaya
        import math
        for i in side:

            start = cmds.xform('shoulder_{}_skn'.format(i) ,q= 1 ,ws = 1,t =1 )
            mid = cmds.xform('elbow_{}_skn'.format(i) ,q= 1 ,ws = 1,t =1 )
            end = cmds.xform('elbow_{}_End'.format(i) ,q= 1 ,ws = 1,t =1 )

            startV = OpenMaya.MVector(start[0] ,start[1],start[2])
            midV = OpenMaya.MVector(mid[0] ,mid[1],mid[2])
            endV = OpenMaya.MVector(end[0] ,end[1],end[2])

            startEnd = endV - startV
            startMid = midV - startV

            dotP = startMid * startEnd
            proj = float(dotP) / float(startEnd.length())
            startEndN = startEnd.normal()
            projV = startEndN * proj

            arrowV = startMid - projV
            arrowV*= 0.5 
            finalV = arrowV + midV

            cross1 = startEnd ^ startMid
            cross1.normalize()

            cross2 = cross1 ^ arrowV
            cross2.normalize()
            arrowV.normalize()

            matrixV = [arrowV.x , arrowV.y , arrowV.z , 0 , 
            cross1.x ,cross1.y , cross1.z , 0 ,
            cross2.x , cross2.y , cross2.z , 0,
            0,0,0,1]

            matrixM = OpenMaya.MMatrix()

            OpenMaya.MScriptUtil.createMatrixFromList(matrixV , matrixM)

            matrixFn = OpenMaya.MTransformationMatrix(matrixM)

            rot = matrixFn.eulerRotation()

            loc = 'armPoleCtr_{}_offset'.format(i)
            cmds.xform(loc , ws =1 , t= (finalV.x , finalV.y ,finalV.z))

            cmds.xform ( loc , ws = 1 , rotation = ((rot.x/math.pi*180.0),
            (rot.y/math.pi*180.0),
            (rot.z/math.pi*180.0)))




    poleLocation()
    '''
    Parent de Controles:
        PACs
        Parent Constrains
        PoleVector Constraints
        Orient Cosntraints (FK)
    '''

    for i in 'rl':
        for partes in brazo:
            PAC = cmds.duplicate('{}_{}_skn'.format(partes, i), n='{}_{}_skn_PAC'.format(partes, i), rc=True)
            PAClist = cmds.listRelatives(PAC, ad=True)
            for huesoDeParent in PAClist:
                cmds.delete(huesoDeParent)
            cmds.parent('{}_{}_skn_PAC'.format(partes, i), '{}FK_{}_ctr'.format(partes, i))
        PACdeIK = cmds.duplicate('hand_{}_skn_PAC'.format(i), n='hand_IK_{}_skn_PAC'.format(i))
        cmds.parent(PACdeIK, 'handIK_{}_ctr'.format(i))
        cmds.pointConstraint(PACdeIK, 'arm_{}_ikHandle'.format(i), n='pointConstraint_{}_PACofTheArmIK'.format(i))
        cmds.poleVectorConstraint('armPole_{}_ctr'.format(i), 'arm_{}_ikHandle'.format(i), n='poleVectorConstraint_{}_PoleofTheArmIK'.format(i))
        for partes in brazo:
            if partes != 'hand':
                cmds.orientConstraint('{}_{}_skn_PAC'.format(partes, i), '{}_{}_skn'.format(partes, i), n='orientConstraint_{}_{}PACto{}sknFK'.format(i, partes, partes))
            else:
                cmds.orientConstraint('{}_{}_skn_PAC'.format(partes, i), '{}_IK_{}_skn_PAC'.format(partes, i), '{}_{}_skn'.format(partes, i), n='orientConstraint_{}_{}PACto{}sknFKandIK'.format(i, partes, partes))


    '''
    Nodos:
        Switch FK/IK
    '''
    for i in 'rl':
        armSettings='armSettings_{}_ctr'.format(i)
        ikH= 'arm_{}_ikHandle'.format(i)
        cmds.connectAttr('{}.Arm_IK'.format(armSettings), '{}.ikBlend'.format(ikH))
        reverse = cmds.shadingNode('reverse', au=True, n='armSettings_{}_reverse'.format(i))
        cmds.connectAttr('{}.Arm_IK'.format(armSettings), '{}.inputY'.format(reverse))
        cmds.connectAttr('{}.outputY'.format(reverse),'orientConstraint_{}_handPACtohandsknFKandIK.hand_{}_skn_PACW0'.format(i, i))
        cmds.connectAttr('{}.Arm_IK'.format(armSettings),'orientConstraint_{}_handPACtohandsknFKandIK.hand_IK_{}_skn_PACW1'.format(i, i))
        cmds.connectAttr('{}.Arm_IK'.format(armSettings),'handIK_{}_ctr.visibility'.format(i))
        for segmentos in brazo:
            cmds.connectAttr('{}.outputY'.format(reverse), '{}FK_{}_ctr.visibility'.format(segmentos, i))

    '''
    Nodos:
        Stretch
    '''
    for i in 'rl':
        for partes in brazo:
            loc=cmds.spaceLocator(n='stretch{}_{}_loc'.format(partes, i))
            cmds.parent(loc, '{}_{}_skn'.format(partes, i))
            for a in vectores:
                cmds.setAttr('{}.translate{}'.format(loc[0], a), 0)
            if partes == 'shoulder':
                cmds.parent(loc, 'clavicle_{}_END'.format(i))
            elif partes == 'elbow':
                cmds.parent(loc, 'armPole_{}_ctr'.format(i))    
            else:
                cmds.parent(loc, 'handIK_{}_ctr'.format(i))





    def stretchArm():
        for i in 'rl':
            shoulder = 'stretchshoulder_{}_locShape'.format(i)
            elbow = 'stretchelbow_{}_locShape'.format(i)
            hand = 'stretchhand_{}_locShape'.format(i)

            up = cmds.shadingNode('distanceBetween', n='upArm_{}_distance'.format(i), au=True)
            entire = cmds.shadingNode('distanceBetween', n='entireArm_{}_distance'.format(i), au=True)
            low = cmds.shadingNode('distanceBetween', n='lowArm_{}_distance'.format(i), au=True)

            cmds.connectAttr('{}.worldPosition'.format(shoulder), '{}.point1'.format(up))
            cmds.connectAttr('{}.worldPosition'.format(elbow), '{}.point2'.format(up))

            cmds.connectAttr('{}.worldPosition'.format(shoulder), '{}.point1'.format(entire))
            cmds.connectAttr('{}.worldPosition'.format(hand), '{}.point2'.format(entire))

            cmds.connectAttr('{}.worldPosition'.format(elbow), '{}.point1'.format(low))
            cmds.connectAttr('{}.worldPosition'.format(hand), '{}.point2'.format(low))

            nod = [up, entire, low]
            for o in nod:
                div = cmds.shadingNode('multiplyDivide', n='{}_{}_normalStretch'.format(o[:-11], i), au=True)
                cmds.setAttr('{}.operation'.format(div), 2)
                cmds.connectAttr('{}.distance'.format(o), '{}.input1Y'.format(div))
                dis= cmds.getAttr('{}.distance'.format(o))
                cmds.setAttr('{}.input2Y'.format(div), dis)

            clamp = cmds.shadingNode('clamp', n='armStretch_{}_clamp'.format(i), au=True)
            cmds.setAttr('{}.maxG'.format(clamp), 999)
            cmds.connectAttr('{}_{}_normalStretch.outputY'.format(entire[:-11],i), '{}.inputG'.format(clamp))
            cmds.connectAttr('general_c_ctr.GlobalScale', '{}.minG'.format(clamp))

            blen = cmds.shadingNode('blendColors', n='armStretch_pinElbow_{}_blend'.format(i), au=True)
            blenF = cmds.shadingNode('blendColors', n='armStretch_FINAL_{}_blend'.format(i), au=True)
            blenS = cmds.shadingNode('blendColors', n='armStretch_stretchiness_{}_blend'.format(i), au=True)
            dive = cmds.shadingNode('multiplyDivide', n='armStretch_stretchByGlobal_{}_div'.format(i), au=True)
            rever = 'armSettings_{}_reverse'.format(i)


            #Blen

            cmds.connectAttr('{}_{}_normalStretch.{}'.format('upArm', i, 'outputY'), '{}.color1G'.format(blen)) 
            cmds.connectAttr('{}.{}'.format(clamp, 'outputG'), '{}.color2G'.format(blen)) 
            cmds.connectAttr('{}.{}'.format(clamp, 'outputG'), '{}.color2B'.format(blen)) 
            cmds.connectAttr('{}_{}_normalStretch.{}'.format('lowArm', i, 'outputY'), '{}.color1B'.format(blen)) 

            #BlenF

            cmds.connectAttr('{}.outputG'.format(blen), '{}.color1G'.format(blenF))
            cmds.connectAttr('{}.outputB'.format(blen), '{}.color1B'.format(blenF))  
            cmds.connectAttr('armSettings_{}_ctr.Arm_IK'.format(i), '{}.blender'.format(blenF)) 

            #BlenS

            cmds.connectAttr('{}.outputG'.format(blenF), '{}.color1G'.format(blenS))
            cmds.connectAttr('{}.outputB'.format(blenF), '{}.color1B'.format(blenS))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.color2G'.format(blenS))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.color2B'.format(blenS))

            #Dive

            cmds.setAttr('{}.operation'.format(dive), 2)
            cmds.connectAttr('{}.outputG'.format(blenS), '{}.input1Y'.format(dive))
            cmds.connectAttr('{}.outputB'.format(blenS), '{}.input1Z'.format(dive))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.input2Y'.format(dive))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.input2Z'.format(dive))

            cmds.connectAttr('{}.outputY'.format(dive), 'shoulder_{}_skn.scaleX'.format(i)) 
            cmds.connectAttr('{}.outputZ'.format(dive), 'elbow_{}_skn.scaleX'.format(i))

           ############################## Conexion Control Blender de BlenS

            plusMinus = cmds.shadingNode('plusMinusAverage', n='arm_autoStretchOverride_{}_sum'.format(i), au=True) 
            clampPlusMinus = cmds.shadingNode('clamp', n='arm_autoStretchOverride_{}_clamp'.format(i), au=True)
            cmds.setAttr('{}.maxG'.format(clampPlusMinus), 1) 
            cmds.connectAttr('{}.outputY'.format(rever),'{}.input2D[0].input2Dy'.format(plusMinus))
            cmds.connectAttr('handIK_{}_ctr.AutoStretch'.format(i),'{}.input2D[1].input2Dy'.format(plusMinus))

            cmds.connectAttr('{}.output2Dy'.format(plusMinus),'{}.inputG'.format(clampPlusMinus))
            cmds.connectAttr('{}.outputG'.format(clampPlusMinus), '{}.blender'.format(blenS))

            ############################## Conexion Control de ColorG y colorB de BlenF

            multDivUp = cmds.shadingNode('multiplyDivide', n='armShoulder_{}_StretchByGlobal_mult'.format(i),au=True)
            multDivLow = cmds.shadingNode('multiplyDivide', n='armElbow_{}_StretchByGlobal_mult'.format(i),au=True)

            cmds.connectAttr('shoulderFK_{}_ctr.Stretch'.format(i), '{}.input1Y'.format(multDivUp))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.input2Y'.format(multDivUp))

            cmds.connectAttr('elbowFK_{}_ctr.Stretch'.format(i), '{}.input1Y'.format(multDivLow))
            cmds.connectAttr('{}.GlobalScale'.format(generalC), '{}.input2Y'.format(multDivLow))

            cmds.connectAttr('{}.outputY'.format(multDivUp), '{}.color2G'.format(blenF))
            cmds.connectAttr('{}.outputY'.format(multDivLow), '{}.color2B'.format(blenF))

            ######################## Blender Blen

            multDivPin = cmds.shadingNode('multiplyDivide', n='armShoulder_{}_PinElbow_mult'.format(i),au=True)
            cmds.connectAttr('armPole_{}_ctr.PinElbow'.format(i), '{}.input1Y'.format(multDivPin))
            cmds.connectAttr('armSettings_{}_ctr.Arm_IK'.format(i), '{}.input2Y'.format(multDivPin))
            cmds.connectAttr('{}.outputY'.format(multDivPin), '{}.blender'.format(blen))
            cmds.connectAttr('{}.outputY'.format(multDivPin), '{}.input2D[2].input2Dy'.format(plusMinus))

    stretchArm()


    def stretchTwistArm():
        for i in side:
            cvUp = 'upperArm_{}_ikHandle_curve_twist'.format(i)
            cvLow = 'foreArm_{}_ikHandle_curve_twist'.format(i)
            cvInfUp = cmds.shadingNode('curveInfo', n='upArm_stretchTwitch_{}_info'.format(i), au=True)
            cvInfLow = cmds.shadingNode('curveInfo', n='lowArm_stretchTwitch_{}_info'.format(i), au=True)


            cmds.connectAttr('{}.worldSpace'.format(cvUp), '{}.inputCurve'.format(cvInfUp))
            cmds.connectAttr('{}.worldSpace'.format(cvLow), '{}.inputCurve'.format(cvInfLow))

            divUp = cmds.shadingNode('multiplyDivide', n='lowArm_stretchTwitch_{}_div'.format(i), au=True)
            divGlobUp = cmds.shadingNode('multiplyDivide', n='lowArm_stretchTwitchbuGlobal_{}_div'.format(i), au=True)
            divLow = cmds.shadingNode('multiplyDivide', n='upArm_stretchTwitch_{}_div'.format(i), au=True)
            divGlobLow = cmds.shadingNode('multiplyDivide', n='upArm_stretchTwitchbbyGlobal_{}_div'.format(i), au=True)
            u = [divUp, divGlobUp, divLow, divGlobLow]
            for indent in u:
                cmds.setAttr('{}.operation'.format(indent), 2)

            lenghtUp = cmds.getAttr('{}.arcLength'.format(cvInfUp))
            lengthLow = cmds.getAttr('{}.arcLength'.format(cvInfLow))

            cmds.connectAttr('{}.arcLength'.format(cvInfUp), '{}.input1Y'.format(divUp))
            cmds.connectAttr('{}.arcLength'.format(cvInfLow), '{}.input1Y'.format(divLow))
            cmds.setAttr('{}.input2Y'.format(divUp), lenghtUp)
            cmds.setAttr('{}.input2Y'.format(divLow), lengthLow)
            cmds.connectAttr('{}.outputY'.format(divUp),'{}.input1Y'.format(divGlobUp))
            cmds.connectAttr('{}.outputY'.format(divLow), '{}.input1Y'.format(divGlobLow))
            cmds.connectAttr('{}.GlobalScale'.format('general_c_ctr'),'{}.input2Y'.format(divGlobUp))
            cmds.connectAttr('{}.GlobalScale'.format('general_c_ctr'), '{}.input2Y'.format(divGlobLow))

            k = ['upper', 'fore']

            for part in k:
                huesosTwist = cmds.listRelatives('{}Arm_{}_skn'.format(part, i), ad=True)
                huesosTwist.append('{}Arm_{}_skn'.format(part, i))
                for hueso in huesosTwist:
                    if part == 'upper':
                        cmds.connectAttr('{}.outputY'.format(divGlobUp), '{}.scaleX'.format(hueso))
                    else:
                        cmds.connectAttr('{}.outputY'.format(divGlobLow), '{}.scaleX'.format(hueso))


    stretchTwistArm()

    for side in 'rl':
        cmds.pointConstraint('elbow_{}_skn'.format(side), 'elbowFKCtr_{}_offset'.format(side), n='pointConstraint_{}_elbowStretchFK'.format(side))
        cmds.pointConstraint('hand_{}_skn'.format(side), 'handFKCtr_{}_offset'.format(side), n='pointConstraint_{}_handStretchFK'.format(side))
    ''''
    ordenar el outliner
    '''
    cmds.parent('rig_arm_l_grp', 'rig_arm_r_grp', 'bodyRig_c_grp')

    for side in 'rl':
        PolePosition = cmds.getAttr('armPoleCtr_{}_offset.translateZ'.format(side))
        cmds.setAttr('armPoleCtr_{}_offset.translateZ'.format(side), (PolePosition -1))
    
        jntClavicle = 'clavicle_{}_skn'.format(side)
        jntClavicleEnd = 'clavicle_{}_END'.format(side)
        grpShoulderRollSystem = 'shoulder_{}_rollSystem'.format(side)
        jntShoulderOffset = 'shoulder_{}_skn_offset'.format(side)
        ctrShoulderFKOffset = 'shoulderFKCtr_{}_offset'.format(side)


        fun.blendSystem(
        CurveU = 'upperArm_{}_ikHandle_curve_twist'.format(side), 
        CurveL = 'foreArm_{}_ikHandle_curve_twist'.format(side), 
        ClusterName = 'ClusterBlendSystem_Arm_{}_'.format(side), 
        upJnt = 'shoulder_{}_skn'.format(side), 
        middleJnt = 'elbow_{}_skn'.format(side), 
        upBlend = 'armUpBlend_{}_ctr'.format(side), 
        middleBlend = 'armMiddleBlend_{}_ctr'.format(side), 
        lowBlend = 'armLowBlend_{}_ctr'.format(side))

        shoulderFKPcon = cmds.group(em=True, n='shoulderFK_{}_pcon'.format(side))
        pconShoulderMatrix = cmds.xform(ctrShoulderFKOffset, q=True, matrix=True, ws=True)
        cmds.xform(shoulderFKPcon, ws=True, matrix = pconShoulderMatrix)
        cmds.parent(shoulderFKPcon, jntClavicleEnd)

        cmds.parentConstraint(jntClavicle, grpShoulderRollSystem, mo=True)
        cmds.pointConstraint(jntClavicleEnd, jntShoulderOffset , mo=False)
        cmds.pointConstraint(shoulderFKPcon,  ctrShoulderFKOffset, mo=False)

        cmds.move(-50, 'armPoleCtr_{}_offset'.format(side), z=True)
        cmds.connectAttr('armSettings_{}_ctr.Arm_IK'.format(side), 'armPole_{}_ctr.visibility'.format(side))
        cmds.parent('armPoleCtr_{}_offset'.format(side), 'center_c_ctr')

        cmds.rename('shoulder_{}_skn'.format(side), 'shoulder_{}_jnt'.format(side))
        cmds.rename('elbow_{}_skn'.format(side), 'elbow_{}_jnt'.format(side))
	
        cmds.parent('handFKCtr_{}_offset'.format(side), 'elbowFK_{}_ctr'.format(side))   
	cmds.parent('elbowFKCtr_{}_offset'.format(side), 'shoulderFK_{}_ctr'.format(side))
    
    #Configuracion de los spaces
    for side in 'rl':
	pos = cmds.xform('handIK_{}_ctr'.format(side), ws=True, m=True, q=True)	
	w = cmds.group(em=True, n='handIK_{}_worldSpace'.format(side))	
	h = cmds.group(em=True, n='handIK_{}_headSpace'.format(side))	
	c = cmds.group(em=True, n='handIK_{}_chestSpace'.format(side))	
	p = cmds.group(em=True, n='handIK_{}_pelvisSpace'.format(side))	
	for i in [w, h, c, p]:
	    cmds.xform(i, ws=True, m=pos)
	cmds.parent(w, 'general_c_ctr')
	cmds.parent(h, 'head_c_ctr')
	cmds.parent(c, 'chest_c_ctr')
	cmds.parent(p, 'pelvis_c_ctr')
	cmds.parentConstraint(w,h,c,p, 'handIKCtr_{}_offset'.format(side), mo=False, n='spaceParentIKHand_{}_cns'.format(side))
	cmds.connectAttr('handIK_{}_ctr.ChestSpace'.format(side), 'spaceParentIKHand_{}_cns.handIK_{}_chestSpaceW2'.format(side, side))
	cmds.connectAttr('handIK_{}_ctr.HeadSpace'.format(side), 'spaceParentIKHand_{}_cns.handIK_{}_headSpaceW1'.format(side, side))
	cmds.connectAttr('handIK_{}_ctr.HipSpace'.format(side), 'spaceParentIKHand_{}_cns.handIK_{}_pelvisSpaceW3'.format(side, side))
	
	
	
	clampSpace = fun.clampCreator(name = 'handIKSpace_{}_clamp'.format(side),  
				      MaxR = 1,
				      MinR = 0)
	
	
	
	fun.plusCreator(name='handIKSpace_{}_sum'.format(side), 
			InputX0 = 'handIK_{}_ctr.ChestSpace'.format(side), 
			InputX1= 'handIK_{}_ctr.HeadSpace'.format(side), 
			InputX2 = 'handIK_{}_ctr.HipSpace'.format(side),  
                        OutputX = '{}.inputR'.format(clampSpace))
	
	
	reverseSpace = cmds.shadingNode('reverse', au=True, n='handIKSpace_{}_rev'.format(side))
	cmds.connectAttr('{}.outputR'.format(clampSpace), '{}.inputX'.format(reverseSpace))
	
	
	
	cmds.connectAttr('{}.outputX'.format(reverseSpace), 'spaceParentIKHand_{}_cns.handIK_{}_worldSpaceW0'.format(side, side))
     #Correccion del fallo del twist del brazo
    cmds.setAttr("elbow_l_twistValue_elbowToHand.offsetX", 0)
    cmds.setAttr("elbow_l_twistValue.jointOrientX", 0)
	
    cmds.parent('armMiddleBlendCtr_r_offset', 'skeleton_c_grp') 
    cmds.parent('armMiddleBlendCtr_l_offset', 'skeleton_c_grp') 	
    cmds.parent('shoulderFKCtr_l_offset', 'handIKCtr_l_offset', 'center_c_ctr') 
    cmds.parent('shoulderFKCtr_r_offset', 'handIKCtr_r_offset', 'center_c_ctr') 
    for part in ['foreArm', 'upperArm']:
        for side in 'rl': 
            foreArmList = cmds.listRelatives('{}_{}_skn'.format(part, side), ad=True)
            foreArmList.reverse()
            i=1
            for element in foreArmList:
                if 'skn' in element:
                    cmds.rename(element, '{}{}_{}_skn'.format(part, i, side))
                    i += 1
                else:
                    pass

    joints = cmds.ls(type='joint')

    for jnt in joints:
	if '_skn_PAC' in jnt:
		newName = jnt.replace('_skn_PAC', '_PAC')
		cmds.rename(jnt, newName)
        else:
            pass
                
