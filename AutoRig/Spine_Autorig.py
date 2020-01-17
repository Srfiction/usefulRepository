from maya import cmds
from maya.api import OpenMaya
import AutoRig.Functions_Autorig as fun

def createSpine(spineJnts=8, neckJnts=8):



    cmds.group(n='bodyRig_c_grp', em=True)
    
    
    
    def spinePositions():
   
        cmds.parent('centerCtr_c_offset', 'generalCtr_c_offset')
        
        
        upPos= cmds.getAttr('spine_loc_c_autorig.translate')
        downPos= cmds.getAttr('spineEND_loc_c_autorig.translate')
        
        
        FK1 = 'spineFK1Ctr_c_offset'
        FK2 = 'spineFK2Ctr_c_offset'
        FK3 = 'spineFK3Ctr_c_offset'
        IK3 = 'spineIK3Ctr_c_offset'
        IK2 = 'spineIK2Ctr_c_offset'
        IK1 = 'spineIK1Ctr_c_offset'
        
        
        
        list = [FK1, FK2, FK3, IK1, IK2, IK3]
        
        pelvis = 'pelvisCtr_c_offset'
        chest = 'chestCtr_c_offset'
        
        middle = 'middleSpineCtr_c_offset'
        
        
        cmds.xform(pelvis, t=downPos[0])
        cmds.xform(chest, t=upPos[0])
        cmds.pointConstraint(pelvis, chest, middle, mo=False, n='del')
        cmds.delete('del')
        for i in list:
            if i[7] == '1':
                cmds.xform(i, t=upPos[0])
            elif i[7] == '2':
                cmds.parentConstraint('spine_loc_c_autorig', 'spineEND_loc_c_autorig', i, n='del')
                cmds.delete('del')
            else:
                cmds.xform(i, t=downPos[0]) 
        
        cmds.parent(FK3, 'spineFK2_c_ctr')
        cmds.parent(FK2, 'spineFK1_c_ctr')
        cmds.parent(IK1, 'spineIK2_c_ctr')
        cmds.parent(IK2, 'spineIK3_c_ctr')
        
        cmds.select(cl=True)
        
        
        cmds.parentConstraint('spineFK3_c_ctr', 'pelvisCtr_c_offset', n='parentConstraint_spineFKtoPelvis')
        cmds.parentConstraint('spineIK1_c_ctr', 'chestCtr_c_offset', n='parentConstraint_spineIKtoChest')
        
       
        
        
              
    spinePositions()
    
    '''''''''''''''''''''''''''''''''''''''''
    Notas:
        los skn se agrupan en body rig en vez de skeleton
        hay que renombrar los ends
        hay un nodo que falta llamado spine_c_blendColors_autoSquach cuya funcion no consigo entender. a ver que es y que hace y como lo metemos
        
    Lista de locators que vas a necesitar:
        spine_loc_END_autoRig
        spine_loc_autoRig
        
    '''''''''''''''''''''''''''''''''''''''
    fun.chainJoint(cantidad=spineJnts, 
                   nombre='spine', 
                   lado='c', 
                   chin=True, 
                   radio=0.5, 
                   ini= 'spineEND', 
                   fin='spine')
    
    spineSkn0 = 'spine0_c_skn'
    spineJointList = cmds.listRelatives(spineSkn0, allDescendents=True)
    spineJointList.append(spineSkn0)
    
    
    
    def spineIK(chestControl, middleControl, pelvisControl):
        cmds.ikHandle(n='spine_c_ikHandle', sj=spineSkn0, ee= spineJointList[0], sol='ikSplineSolver')
        cmds.rename('curve1', 'spine_c_ikHandle_curve')
        spineCurve = 'spine_c_ikHandle_curve'
       
        
        spineHandle = 'spine_c_ikHandle'
        
        ############################CLUSTER UBICATION####################
        c1 = cmds.select(spineCurve+'.cv[2:3]')
        cmds.cluster()
        cmds.parent('cluster1Handle',chestControl)
        c2 = cmds.select(spineCurve+'.cv[0:1]')
        cmds.cluster()
        cmds.select(cl=True)
        cmds.parent('cluster2Handle', pelvisControl) 
    
        #############################NODAL - AUTOSTRETCH#####################
        curveInfo1 = cmds.shadingNode('curveInfo', n='spine_c_ikHandle_curve_curveInfo', au=True)
        cmds.connectAttr(spineCurve+'Shape.worldSpace[0]', curveInfo1+'.inputCurve')
        lengthCurve = cmds.getAttr(curveInfo1+'.arcLength')
        divideNorm = cmds.shadingNode('multiplyDivide', n=spineCurve+'DivideNormalice', au=True)
        cmds.setAttr(divideNorm+'.operation', 2)
        cmds.setAttr(divideNorm+'.input2Y', lengthCurve)
        ####Correccion
        diviByGlobal = fun.divideCreator(name='divideByGlob_c_div', 
                                         Input1X = 'spine_c_ikHandle_curveDivideNormalice.outputY',
                                         Input2X = 'general_c_ctr.GlobalScale')
        
        blendByGlobal = fun.blendColorsCreator(Name = 'blendColorByGlobal_c_blend', 
                                              Blender = 'chest_c_ctr.Stretch', 
                                              Color1R = '{}.outputX'.format(diviByGlobal), 
                                              Color2R = 1)
         
        cmds.connectAttr(curveInfo1+'.arcLength', divideNorm+'.input1Y')
        #AQUI HAY QUE Anadir EL GLOBAL SCALE(divideGlobal)!!!!!
        for bone in spineJointList:
            cmds.connectAttr(blendByGlobal+'.outputR', bone+'.scaleX')
        #Recuerda que aque no se que que cambiarlo por divideGlobal
        
        ##########################TWIST CONFIGURATION############################
        cmds.setAttr(spineHandle+'.dTwistControlEnable', 1)
        cmds.setAttr(spineHandle+'.dWorldUpType', 4)
        cmds.setAttr(spineHandle+'.dWorldUpAxis', 3)
        cmds.setAttr(spineHandle+'.dWorldUpVectorY', 0)
        cmds.setAttr(spineHandle+'.dWorldUpVectorZ', 1) 
        cmds.setAttr(spineHandle+'.dWorldUpVectorEndZ', 1)
        cmds.setAttr(spineHandle+'.dWorldUpVectorEndY', 0)
        cmds.connectAttr(pelvisControl+'.worldMatrix[0]', spineHandle+'.dWorldUpMatrix')
        cmds.connectAttr(chestControl+'.worldMatrix[0]', spineHandle+'.dWorldUpMatrixEnd')
        
    
    
    spineIK('chest_c_ctr', 'middleSpine_c_ctr', 'pelvis_c_ctr')    
    ########################CURVA BEND#####################################
    
    cmds.duplicate('spine_c_ikHandle_curve', n='spine_c_ikHandle_curveBend')
    cmds.delete('spine_c_ikHandle_curveBendShapeOrig')
    
    cmds.select('{}.cv[1]'.format('spine_c_ikHandle_curveBend'))
    cmds.cluster()
    cmds.select(cl=True)
    cmds.select('{}.cv[2]'.format('spine_c_ikHandle_curveBend'))
    cmds.cluster()
    cmds.select(cl=True)
    cmds.parent('cluster3Handle', 'middleSpine_c_ctr')
    cmds.parent('cluster4Handle', 'middleSpine_c_ctr')
    
    
    cmds.group(n='middleSpine_c_bend_grp', em=True)
    middleSpinePos = cmds.getAttr('middleSpineCtr_c_offset.translate')
    cmds.xform('middleSpine_c_bend_grp', t=middleSpinePos[0])
    cmds.parent('cluster3Handle', 'cluster4Handle', 'middleSpine_c_bend_grp')
    
    cmds.parent('middleSpine_c_bend_grp', 'bodyRig_c_grp')
    
    
    cmds.group(n='middleSpine_c_bend_grp_offset', em=True)
    cmds.xform('middleSpine_c_bend_grp_offset', t=middleSpinePos[0])
    cmds.parent('middleSpine_c_bend_grp_offset', 'bodyRig_c_grp')
    cmds.parent('middleSpine_c_bend_grp', 'middleSpine_c_bend_grp_offset')
    
    for axis in 'XYZ':
        cmds.connectAttr('middleSpine_c_ctr.translate{}'.format(axis), 'middleSpine_c_bend_grp.translate{}'.format(axis))
        cmds.connectAttr('middleSpine_c_ctr.rotate{}'.format(axis), 'middleSpine_c_bend_grp.rotate{}'.format(axis))
    
    cmds.blendShape('spine_c_ikHandle_curveBend', 'spine_c_ikHandle_curve', n='spine_c_ikHandle_curvebs', foc=True)
    cmds.setAttr("spine_c_ikHandle_curvebs.spine_c_ikHandle_curveBend", 1)
    
    ###########################DIOS MALDITA LA PUTA CURVA BEND#######################
    def chestAndPelvis():
        pos1 = cmds.getAttr('{}.translateY'.format('spine_loc_c_autorig'))
        chest= cmds.duplicate(spineJointList[0], n='chest_c_skn', po=True)
        cmds.parent(chest, w=True)    
        cmds.setAttr('{}.translateY'.format('chest_c_skn'), pos1+0.01)
        pos2 = cmds.getAttr('{}.translateY'.format('spineEND_loc_c_autorig'))
        chest= cmds.duplicate(spineJointList[-1], n='pelvis_c_skn', po=True)    
        cmds.setAttr('{}.translateY'.format('pelvis_c_skn'), pos2-0.01)
    
    chestAndPelvis()
    
    
    
    def controlPosicionamiento():
        pelvis = 'pelvis_c_ctr'
        chest = 'chest_c_ctr'
        middle = 'middleSpine_c_ctr'
        
        
        cmds.parentConstraint(pelvis, 'pelvis_c_skn', mo=True)
        cmds.parentConstraint(chest, 'chest_c_skn', mo=True)
        
    controlPosicionamiento()
    
    cmds.parent('spine_c_ikHandle', 'spine_c_ikHandle_curve', 'spine_c_ikHandle_curveBend', 'bodyRig_c_grp')
    
    
    """""""""""""""""""""""""""""""""
    
    Notas:
    
    Lista de locators que vas a necesitar:
        neck_loc_END_autoRig
        neck_loc_autoRig
        head_loc_END_autoRig
           
           NECK~~~~NECK~~~~NECK
    """""""""""""""""""""""""""""""""
    
    cmds.select(cl=True)
    
    neckLoc= cmds.getAttr('{}.translate'.format('neck_loc_c_autorig'))
    headLoc= cmds.getAttr('{}.translate'.format('neckEND_loc_c_autorig'))
    
    cmds.xform('{}'.format('neckCtr_c_offset'), t=neckLoc[0])
    cmds.xform('{}'.format('headCtr_c_offset'), t=headLoc[0])
    
    cmds.parentConstraint('neckCtr_c_offset', 'headCtr_c_offset', 'middleNeckCtr_c_offset', mo=False)
    cmds.delete('middleNeckCtr_c_offset_parentConstraint1')
    cmds.Parent('middleNeckCtr_c_offset', 'neck_c_ctr')
    cmds.select(cl=True)
    
    fun.chainJoint(cantidad=neckJnts, 
                   nombre='neck', 
                   lado='c', 
                   chin=True, 
                   radio=0.1, 
                   ini='neck', 
                   fin='neckEND')
        
     
    neckSkn0 = 'neck0_c_skn'
    neckJointList = cmds.listRelatives(neckSkn0, allDescendents=True)
    neckJointList.append(neckSkn0)
    
    def headCreation():
        cmds.setAttr('{}.jointOrientX'.format(neckSkn0), 0)
        jointHead = cmds.duplicate(neckJointList[0], n='head_c_skn')
        cmds.parent('head_c_skn', w=True)
        cmds.setAttr('head_c_skn.jointOrientY', 0)
        endHead = cmds.objExists('head_loc_END_autoRig')
        if endHead==True:
            pos = cmds.getAttr('head_loc_END_autoRig.translate')
            cmds.joint(n='head_c_END', p=pos[0], rad=0.1)
        else:
            pass
        cmds.parentConstraint('head_c_ctr', jointHead, n='parentConstrain_c_fromHeadControl', mo=True)
    
    headCreation()
    
    def neckIK(headControl, middleControl, neckControl):
        cmds.ikHandle(n='neck_c_ikHandle', sj=neckSkn0, ee= neckJointList[0], sol='ikSplineSolver')
        cmds.rename('curve1', 'neck_c_ikHandle_curve')
        neckCurve = 'neck_c_ikHandle_curve'
        centerCurve = 'neck_c_ikHandle_deform_curve'
        neckHandle = 'neck_c_ikHandle'
        cmds.group(n='neck_rig', p='bodyRig_c_grp')
        cmds.parent('neck_c_ikHandle_curve', 'neck_rig')
            
            ############################CLUSTER UBICATION
        
        cmds.select(neckCurve+'.cv[0]')
        c1 = cmds.cluster(n='neck_cluster1')
        cmds.select(cl=True)
        cmds.parent(c1, neckControl)
        cmds.select(neckCurve+'.cv[3]')
        c2 = cmds.cluster(n='neck_cluster2')
        cmds.select(cl=True)
        cmds.parent(c2, headControl) 
        cmds.select(neckCurve+'.cv[1:2]')
        c3 = cmds.cluster(n='neck_cluster3')
        cmds.parent(c3, middleControl)
        cmds.select(cl=True)
        
            ##########################TWIST CONFIGURATION############################
            
        cmds.setAttr(neckHandle+'.dTwistControlEnable', 1)
        cmds.setAttr(neckHandle+'.dWorldUpType', 4)
        cmds.setAttr(neckHandle+'.dWorldUpAxis', 3)
        cmds.setAttr(neckHandle+'.dWorldUpVectorY', 0)
        cmds.setAttr(neckHandle+'.dWorldUpVectorZ', 1) 
        cmds.setAttr(neckHandle+'.dWorldUpVectorEndZ', 1)
        cmds.setAttr(neckHandle+'.dWorldUpVectorEndY', 0)
        cmds.connectAttr(neckControl+'.worldMatrix[0]', neckHandle+'.dWorldUpMatrix')
        cmds.connectAttr(headControl+'.worldMatrix[0]', neckHandle+'.dWorldUpMatrixEnd')
        
        #############################CONEXIoN NODAL - AUTOSTRETCH#####################
        
        curveInfo1 = cmds.shadingNode('curveInfo', n='neck_c_ikHandle_curve_curveInfo', au=True)
        cmds.connectAttr(neckCurve+'Shape.worldSpace[0]', curveInfo1+'.inputCurve')
        lengthCurve = cmds.getAttr(curveInfo1+'.arcLength')
        divideNorm = cmds.shadingNode('multiplyDivide', n=neckCurve+'divideNormalice', au=True)
        cmds.setAttr(divideNorm+'.operation', 2)
        cmds.setAttr(divideNorm+'.input2Y', lengthCurve)
        cmds.connectAttr(curveInfo1+'.arcLength', divideNorm+'.input1Y')
        divideGlob = cmds.shadingNode('multiplyDivide', n=neckCurve+'divideGlobal', au=True)
        cmds.setAttr(divideGlob+'.operation', 2)
        cmds.connectAttr(divideNorm+'.outputY', divideGlob+'.input1Y')
        cmds.connectAttr('general_c_ctr.GlobalScale', divideGlob+'.input2Y')
        for bone in neckJointList:
            cmds.connectAttr(divideGlob+'.outputY', bone+'.scaleX')
            
        
     
    neckIK('head_c_ctr', 'middleNeck_c_ctr', 'neck_c_ctr')    
    
    
    
    def neckSpaces():
        neckPos = cmds.getAttr('{}.translate'.format(neckSkn0))
        
        cmds.group(n='neck_c_pCon', em=True)
        cmds.xform('neck_c_pCon', t=neckPos[0])
        cmds.parent('neck_c_pCon','chest_c_ctr')
        cmds.pointConstraint('neck_c_pCon', 'neckCtr_c_offset', n='constrainPoint_neckSpaceToChest', mo=True)
        
        
        gS = cmds.group(n='neck_c_chestSpace', p='chest_c_ctr', em=True)
        gW = cmds.group(n='neck_c_worldSpace', p='center_c_ctr', em=True)
        cmds.xform('neck_c_chestSpace', t=neckPos[0])
        cmds.xform('neck_c_worldSpace', t=neckPos[0])
        cmds.orientConstraint(gS, gW, 'neckCtr_c_offset', n='constrainOrient_neckSpaceToChest', mo=True)
    
        rev = cmds.shadingNode('reverse', n=gS+'_reverse', au=True)
        cmds.connectAttr('neck_c_ctr.ChestSpace', 'constrainOrient_neckSpaceToChest.neck_c_chestSpaceW0')
        cmds.connectAttr('neck_c_ctr.ChestSpace', rev+'.inputY')
        cmds.connectAttr(rev+'.outputY', 'constrainOrient_neckSpaceToChest.neck_c_worldSpaceW1')
    
    neckSpaces()
    
    def headSpaces():
        headPos = cmds.getAttr('head_c_skn.translate')
        head = 'head_c_ctr' 
        neck = 'neck_c_ctr' 
        Pc = 'pointConstraint' 
        Oc = 'orientConstraint' 
        nS = 'neckSpace'
        
        ############################### FOLLOW NECK ########################
        
        gS = cmds.group(n='head_c_neckpCon', em=True)
        gW = cmds.group(n='head_c_worldpCon', em=True)
        cmds.xform(gS, t=headPos[0])
        cmds.parent(gS, 'neck_c_ctr')
        cmds.xform(gW, t=headPos[0])
        cmds.parent(gW, 'center_c_ctr')
        cmds.pointConstraint(gS, gW, 'headCtr_c_offset', n='{}_headFollowToNeck'.format(Pc), mo=True)
    
        rev = cmds.shadingNode('reverse', n=gS+'_reverse', au=True)
        cmds.connectAttr('{}.FollowHead'.format(head), '{}_headFollowToNeck.{}W0'.format(Pc, gS))
        cmds.connectAttr('{}.FollowHead'.format(head), rev+'.inputY')
        cmds.connectAttr(rev+'.outputY', '{}_headFollowToNeck.{}W1'.format(Pc, gW))
        
        ############################# NECK SPACE #############################
        
        
        fS = cmds.group(n='head_c_neckFollow', em=True)
        fW = cmds.group(n='head_c_worldFollow', em=True)
        cmds.xform(fS, t=headPos[0])
        cmds.parent(fS, 'neck_c_ctr')
        cmds.xform(fW, t=headPos[0])
        cmds.parent(fW, 'center_c_ctr')
        cmds.orientConstraint(fS, fW, 'headCtr_c_offset', n='{}_headFollowToNeck'.format(Oc), mo=True)
    
        rev = cmds.shadingNode('reverse', n=fS+'_reverse', au=True)
        cmds.connectAttr('{}.{}'.format(head, nS), '{}_headFollowToNeck.{}W0'.format(Oc, fS))
        cmds.connectAttr('{}.{}'.format(head, nS), rev+'.inputY')
        cmds.connectAttr(rev+'.outputY', '{}_headFollowToNeck.{}W1'.format(Oc, fW))
        
        
        
    headSpaces()
    
    cmds.parent('middleNeckCtr_c_offset', 'neck_c_ctr')
    
    renNeckEnd = cmds.listRelatives(neckSkn0, allDescendents=True)
    
    cmds.rename(renNeckEnd[0], 'neck_c_END')
    
    """""""""""""""""""""""""""""""""
    Lista de locators que vas a necesitar:
        clavicle_loc_END_autoRig
        clavicle_loc_autoRig
           
           CLAVICLE~~CLAVICLE~~CLAVICLE
    """""""""""""""""""""""""""""""""
    
    for side in 'rl':
        clavicleOff = 'clavicleCtr_{}_offset'.format(side)
        ctr = 'clavicle_{}_ctr'.format(side)
        clavicle = 'clavicle_{}_loc_autoRig'.format(side)
        clavicleEND = 'clavicle_{}_loc_END_autoRig'.format(side)
        
        clavLocPos = cmds.xform(clavicle, ws=True, q=True, t=True)
        clavLocPosEnd = cmds.xform(clavicleEND, ws=True, q=True, t=True)
        
        skn = cmds.joint(n='clavicle_{}_skn'.format(side), p=clavLocPos, rad=0.1)
        sknE = cmds.joint(n='clavicle_{}_END'.format(side), p=clavLocPosEnd, rad=0.1)
        
        cmds.joint(skn, oj='xyz', sao='yup', e=True)
        
        cmds.xform(clavicleOff, ws=True, t=clavLocPos)
        
        cmds.parent(skn, 'chest_c_skn')
    
        cmds.parentConstraint(ctr, skn, n='parentConstrain_{}_fromControlClavicle'.format(side), mo=True)
        
    
    '''''''''''''''''''''
    
    retoques finales
    
    organizacion de emparentacion 
    
    
    '''''''''
    #Nomenclatura para futuro
    
    
    headSkn = 'head_c_skn'
    pelvisSkn = 'pelvis_c_skn'
    chestSkn = 'chest_c_skn'
    skeletonGroup = cmds.group(n='skeleton_c_grp', em=True)
    cmds.parent('neckCtr_c_offset', 'headCtr_c_offset', 'center_c_ctr')
    
    valorUpperBody = cmds.getAttr('spineEND_loc_c_autorig.translate')
    cmds.xform('upperBodyCtr_c_offset', t=valorUpperBody[0])
    
    cmds.parent('pelvisCtr_c_offset', 'chestCtr_c_offset', 'middleSpineCtr_c_offset', 'spineFK1Ctr_c_offset', 'spineIK3Ctr_c_offset', 'upperBody_c_ctr')
    cmds.parent(spineSkn0, neckSkn0, headSkn, pelvisSkn, chestSkn, skeletonGroup)
    
    cmds.parent('centerCtr_c_offset', 'general_c_ctr')
    cmds.parent('upperBodyCtr_c_offset', 'center_c_ctr')
    
    for side in 'rl':
        cmds.parent('clavicleCtr_{}_offset'.format(side), 'chest_c_ctr')
