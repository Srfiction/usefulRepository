from maya import cmds
from maya.api import OpenMaya

'''
Tio, arregla la puta nomenclatura de los locators
'''




def mainGrp():
    cmds.group(em=True, n='autoRigLocators_c_grp') 

def createHandsLocators(loc_scale = 1):
    
#problema con la escala de menos 1
    if not 'locators_Autorig':
        cmds.group(em=True, n = 'locators_Autorig')
    else:
        pass
    locators_Autorig = 'locators_Autorig'
    grp = cmds.group(em=True, n = 'handFingersLocators_r_grp')
    cmds.setAttr('{}.sx'.format(grp), -1)
    loc_list = []
    for side in 'lr':
        for finger in 'ABCDE':
            count = 0
            for falange in range(0,5):    
                loc = cmds.spaceLocator(n='hand{}0{}_{}_loc'.format(finger,falange,side))
                if count == 5:
                    pass
                elif count == 0:
                    pass
                else:
                    cmds.parent(loc, 'hand{}0{}_{}_loc'.format(finger,count-1,side))
                count += 1
                if side == 'r':
                    for i in 'tr':
                        for axis in 'xyz':
                            cmds.connectAttr('hand{}0{}_l_loc.{}{}'.format(finger,falange, i, axis), 
                                             'hand{}0{}_r_loc.{}{}'.format(finger,falange, i, axis))
                    if falange == 0:
                        cmds.parent(loc, grp)
                loc_list.append(loc)
    
        
    for i in loc_list:
        for axis in 'XYZ':
            cmds.setAttr('{}.localScale{}'.format(i[0], axis), loc_scale)
    cmds.group(em=True, n= 'handFingersLocators_c_grp')
    cmds.addAttr('handA01_l_loc', ln='handIs', max=1, dv=0, at='double', min=0)
    cmds.setAttr('handA01_l_loc.handIs', e=1, keyable=True)
    cmds.parent('handFingersLocators_r_grp', 'handFingersLocators_c_grp')     
    
    
    
    
    
    
    
    
    
def createSpineLocators():
    if not cmds.objExists('autoRigLocators_c_grp'):
        mainGrp()

    
    cmds.spaceLocator(n='spineEND_loc_c_autorig')
    cmds.spaceLocator(n='spine_loc_c_autorig')
    cmds.spaceLocator(n='neckEND_loc_c_autorig')
    cmds.spaceLocator(n='neck_loc_c_autorig')
    cmds.spaceLocator(n='head_loc_END_autorig')
    cmds.spaceLocator(n='clavicle_l_loc_END_autoRig')
    cmds.spaceLocator(n='clavicle_l_loc_autoRig')
    clav1r = cmds.spaceLocator(n='clavicle_r_loc_autoRig')
    clav2r = cmds.spaceLocator(n='clavicle_r_loc_END_autoRig')
    
    cmds.group(em=True, n='clavicleLocators_c_Autorig')
    clavGrpR = cmds.group(em=True, n='clavicleLocators_r_Autorig')
    cmds.setAttr('{}.sx'.format(clavGrpR), -1)
    
    cmds.parent(clav2r, clav1r, clavGrpR)
    for axis in 'xyz':
        for i in 'rt':   
            cmds.connectAttr('clavicle_l_loc_autoRig.{}{}'.format(i, axis), '{}.{}{}'.format(clav1r[0], i, axis))
            cmds.connectAttr('clavicle_l_loc_END_autoRig.{}{}'.format(i, axis), '{}.{}{}'.format(clav2r[0], i, axis))
 
    cmds.parent('spineEND_loc_c_autorig', 'spine_loc_c_autorig', 'neckEND_loc_c_autorig', 'neck_loc_c_autorig', 'head_loc_END_autorig', 'clavicle_l_loc_END_autoRig', 'clavicle_l_loc_autoRig', 'clavicleLocators_c_Autorig') 
    
    cmds.parent('clavicleLocators_c_Autorig', clavGrpR, 'autoRigLocators_c_grp')        







def createArmLocators():
    if not cmds.objExists('autoRigLocators_c_grp'):
        mainGrp()
    
    cmds.spaceLocator(n='lowerArm_l_loc_autoRig')
    cmds.spaceLocator(n='hand_loc_autoRig')

    
    
    cmds.group(em=True, n='armLocators_l_Autorig')
    
    cmds.parent('lowerArm_l_loc_autoRig', 'hand_loc_autoRig', 'armLocators_l_Autorig')
    

    cmds.parent('armLocators_l_Autorig', 'autoRigLocators_c_grp')
    createHandsLocators()



def createLegLocators():
    if not cmds.objExists('autoRigLocators_c_grp'):
        mainGrp()    
    
    cmds.spaceLocator(n='hip_loc_l_autorig')
    cmds.spaceLocator(n='knee_loc_l_autorig')
    cmds.spaceLocator(n='foot_loc_l_autorig')
    cmds.spaceLocator(n='ball_loc_l_autorig')
    cmds.spaceLocator(n='endFoot_loc_l_autorig')
    cmds.spaceLocator(n='toe_loc_l_autorig')


    cmds.spaceLocator(n='hip_loc_r_autorig')
    cmds.spaceLocator(n='knee_loc_r_autorig')
    cmds.spaceLocator(n='foot_loc_r_autorig')
    cmds.spaceLocator(n='ball_loc_r_autorig')
    cmds.spaceLocator(n='endFoot_loc_r_autorig')
    cmds.spaceLocator(n='toe_loc_r_autorig')

    
    
    cmds.group(em=True, n='legLocators_c_Autorig')
    legGrpR = cmds.group(em=True, n='legLocators_r_Autorig')
   
    for axis in 'XYZ':
        for i in ['translate', 'rotate']:   
            cmds.connectAttr('hip_loc_l_autorig.{}{}'.format(i, axis), 'hip_loc_r_autorig.{}{}'.format(i, axis))
            cmds.connectAttr('knee_loc_l_autorig.{}{}'.format(i, axis), 'knee_loc_r_autorig.{}{}'.format(i, axis))
            cmds.connectAttr('foot_loc_l_autorig.{}{}'.format(i, axis), 'foot_loc_r_autorig.{}{}'.format(i, axis))
            cmds.connectAttr('ball_loc_l_autorig.{}{}'.format(i, axis), 'ball_loc_r_autorig.{}{}'.format(i, axis))
            cmds.connectAttr('endFoot_loc_l_autorig.{}{}'.format(i, axis), 'endFoot_loc_r_autorig.{}{}'.format(i, axis))
            cmds.connectAttr('toe_loc_l_autorig.{}{}'.format(i, axis), 'toe_loc_r_autorig.{}{}'.format(i, axis))
            
            
    cmds.setAttr('{}.sx'.format(legGrpR), -1)
    
    cmds.parent('toe_loc_r_autorig', 'endFoot_loc_r_autorig', 'ball_loc_r_autorig', 'foot_loc_r_autorig', 'knee_loc_r_autorig', 'hip_loc_r_autorig', legGrpR)            
 
    cmds.parent('toe_loc_l_autorig', 'endFoot_loc_l_autorig', 'ball_loc_l_autorig', 'foot_loc_l_autorig', 'knee_loc_l_autorig', 'hip_loc_l_autorig', 'legLocators_c_Autorig')
    
    cmds.parent('legLocators_r_Autorig', 'legLocators_c_Autorig') 
    cmds.parent('legLocators_c_Autorig', 'autoRigLocators_c_grp')



def createFootLocators():
    if not cmds.objExists('autoRigLocators_c_grp'):
        mainGrp()
        
    cmds.spaceLocator(n='bankExt_l_pivot')
    cmds.spaceLocator(n='bankInt_l_pivot')
    cmds.spaceLocator(n='heelParam_l_pivot')
    cmds.spaceLocator(n='heel_l_pivot')
    cmds.spaceLocator(n='toeParam_l_pivot')
    cmds.spaceLocator(n='toe_l_pivot')
    cmds.spaceLocator(n='ballParam_l_pivot')
    cmds.spaceLocator(n='ball_l_pivot')
    cmds.spaceLocator(n='ankle_l_pcon')
    
    
    cmds.parent('toeParam_l_pivot', 'toe_l_pivot')
    cmds.parent('ballParam_l_pivot', 'ball_l_pivot')
    cmds.parent('heelParam_l_pivot', 'heel_l_pivot')
    
    
    cmds.group(em=True, n='footLocators_l_grp')
    
    cmds.parent('bankExt_l_pivot', 'bankInt_l_pivot', 'heel_l_pivot', 'toe_l_pivot', 'ball_l_pivot', 'ankle_l_pcon', 'footLocators_l_grp')

    cmds.parent('footLocators_l_grp', 'autoRigLocators_c_grp')

def quickPos():
    cmds.setAttr('spineEND_loc_c_autorig.ty', 118.973)
    cmds.setAttr('spine_loc_c_autorig.ty', 161.552)
    cmds.setAttr('neckEND_loc_c_autorig.ty', 190.885)
    cmds.setAttr('neckEND_loc_c_autorig.tz', 3.194)
    cmds.setAttr('neck_loc_c_autorig.ty', 179.048)
    cmds.setAttr('head_loc_END_autorig.ty', 257)
    cmds.setAttr('clavicle_l_loc_END_autoRig.tx', 12.009)
    cmds.setAttr('clavicle_l_loc_END_autoRig.ty', 171.031)
    cmds.setAttr('clavicle_l_loc_autoRig.tx', 2.541)
    cmds.setAttr('clavicle_l_loc_autoRig.tz', 3.855)
    cmds.setAttr('clavicle_l_loc_autoRig.ty', 168.235)
    
    cmds.setAttr('lowerArm_l_loc_autoRig.tx', 44.958)
    cmds.setAttr('lowerArm_l_loc_autoRig.ty', 171.031)
    
    cmds.setAttr('hand_loc_autoRig.tx', 70.221)
    cmds.setAttr('hand_loc_autoRig.ty', 171.031)
    
    
    cmds.setAttr('hip_loc_l_autorig.tx', 10.112)
    cmds.setAttr('hip_loc_l_autorig.ty', 114.916)
    
    cmds.setAttr('knee_loc_l_autorig.tx', 10.112)
    cmds.setAttr('knee_loc_l_autorig.ty', 68.339)
    
    cmds.setAttr('foot_loc_l_autorig.tx', 10.112)
    cmds.setAttr('foot_loc_l_autorig.ty', 7.445)
    
    cmds.setAttr('endFoot_loc_l_autorig.tx', 10.112)
    cmds.setAttr('endFoot_loc_l_autorig.ty', -8.686)
    
    cmds.setAttr('ball_loc_l_autorig.tx', 9.813)
    cmds.setAttr('ball_loc_l_autorig.tz', 11.522)
    
    cmds.setAttr('toe_loc_l_autorig.tx', 9.383)
    cmds.setAttr('toe_loc_l_autorig.tz', 23.33)
    
    
    
    ####
    
    
    cmds.setAttr('bankExt_l_pivot.tx', 14.295)
    cmds.setAttr('bankExt_l_pivot.tz', 11.374)
    
    
    cmds.setAttr('bankInt_l_pivot.tx', 4.91)
    cmds.setAttr('bankInt_l_pivot.tz', 14.449)
    
    cmds.setAttr('heel_l_pivot.tx', 9.384)
    cmds.setAttr('heel_l_pivot.tz', -4.099)
    
    cmds.setAttr('toe_l_pivot.tx', 9.376)
    cmds.setAttr('toe_l_pivot.tz', 23.326)
    
    cmds.setAttr('ball_l_pivot.tx', 9.189)
    cmds.setAttr('ball_l_pivot.tz', 12.221)
    
    cmds.setAttr('ankle_l_pcon.tx', 9.879)
    cmds.setAttr('ankle_l_pcon.ty', 0.633)
    
    ###Hands
    
    #A
    cmds.setAttr('handA00_l_loc.tx', 75.123)
    cmds.setAttr('handA00_l_loc.ty', 170.16)
    cmds.setAttr('handA00_l_loc.tz', 0.373)
    
    cmds.setAttr('handA01_l_loc.tx', 1.385)
    cmds.setAttr('handA01_l_loc.ry', 3.506)
    
    cmds.setAttr('handA02_l_loc.tx', 2.354)
    cmds.setAttr('handA02_l_loc.tz', 2.513)
    
    cmds.setAttr('handA03_l_loc.tx', 2.994)
    cmds.setAttr('handA03_l_loc.tz', 3.606)
    
    cmds.setAttr('handA03_l_loc.tx', 4.346)
    
    
    
    
    #B
    cmds.setAttr('handB00_l_loc.tx', 77.698)
    cmds.setAttr('handB00_l_loc.ty', 172.166)
    cmds.setAttr('handB00_l_loc.tz', 1.658)
    
    cmds.setAttr('handB01_l_loc.tx', 6.192)
    cmds.setAttr('handB01_l_loc.tz', -0.528)
    cmds.setAttr('handB01_l_loc.ry', -2.436)
    
    cmds.setAttr('handB02_l_loc.tx', 4.452)
    
    cmds.setAttr('handB03_l_loc.tx', 2.889)
    
    cmds.setAttr('handB03_l_loc.tx', 4.346)
    
    #C
    cmds.setAttr('handC00_l_loc.tx', 77.678)
    cmds.setAttr('handC00_l_loc.ty', 172.166)
    cmds.setAttr('handC00_l_loc.tz', -1.812)
    cmds.setAttr('handC00_l_loc.ry', 2.178)
    
    cmds.setAttr('handC01_l_loc.tx', 6.78)
    cmds.setAttr('handC01_l_loc.tz', 0.213)
    
    cmds.setAttr('handC02_l_loc.tx', 4.437)
    
    cmds.setAttr('handC03_l_loc.tx', 3.796)
    
    cmds.setAttr('handC04_l_loc.tx', 4.876)  
    
    #D
    cmds.setAttr('handD00_l_loc.tx', 76.715)
    cmds.setAttr('handD00_l_loc.ty', 172.166)
    cmds.setAttr('handD00_l_loc.tz', -3.838)
    cmds.setAttr('handD00_l_loc.rx', 0.078)
    cmds.setAttr('handD00_l_loc.ry', 2.042)
    cmds.setAttr('handD00_l_loc.rz', 2.192)
    
    cmds.setAttr('handD01_l_loc.tx', 6.696)
    cmds.setAttr('handD01_l_loc.tz', 0.245)
    
    cmds.setAttr('handD02_l_loc.tx', 4.349)
    
    cmds.setAttr('handD03_l_loc.tx', 3.098)
    
    cmds.setAttr('handD04_l_loc.tx', 4.803)      
    
    #E
    cmds.setAttr('handE00_l_loc.tx', 76.715)
    cmds.setAttr('handE00_l_loc.ty', 172.166)
    cmds.setAttr('handE00_l_loc.tz', -5.072)
    cmds.setAttr('handE00_l_loc.rx', 0.24)
    cmds.setAttr('handE00_l_loc.ry', 6.629)
    cmds.setAttr('handE00_l_loc.rz', 2.08)
    
    cmds.setAttr('handE01_l_loc.tx', 4.979)
   
    cmds.setAttr('handE02_l_loc.tx', 3.421)
    
    cmds.setAttr('handE03_l_loc.tx', 2.752)
    
    cmds.setAttr('handE04_l_loc.tx', 3.121)  
    
    
    cmds.disconnectAttr('handA00_l_loc.ry', 'handA00_r_loc.ry')  
    cmds.setAttr('handA00_r_loc.ry', -90)
    
