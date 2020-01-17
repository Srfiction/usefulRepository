from maya import cmds
from maya.api import OpenMaya
def createControls(size = 1):
    controlList = [u'armLowBlendCtr_l_offset',
 u'armLowBlendCtr_r_offset',
 u'armMiddleBlendCtr_l_offset',
 u'armMiddleBlendCtr_r_offset',
 u'armPoleCtr_l_offset',
 u'armPoleCtr_r_offset',
 u'armSettingsCtr_l_offset',
 u'armSettingsCtr_r_offset',
 u'armUpBlendCtr_l_offset',
 u'armUpBlendCtr_r_offset',
 u'centerCtr_c_offset',
 u'chestCtr_c_offset',
 u'clavicleCtr_l_offset',
 u'clavicleCtr_r_offset',
 u'elbowFKCtr_l_offset',
 u'elbowFKCtr_r_offset',
 u'footFKCtr_l_offset',
 u'footFKCtr_r_offset',
 u'footIKCtr_l_offset',
 u'footIKCtr_r_offset',
 u'generalCtr_c_offset',
 u'handFKCtr_l_offset',
 u'handFKCtr_r_offset',
 u'handIKCtr_l_offset',
 u'handIKCtr_r_offset',
 u'headCtr_c_offset',
 u'hipCtr_l_offset',
 u'hipCtr_r_offset',
 u'hipFKCtr_l_offset',
 u'hipFKCtr_r_offset',
 u'kneeFKCtr_l_offset',
 u'kneeFKCtr_r_offset',
 u'legLowBlendCtr_l_offset',
 u'legLowBlendCtr_r_offset',
 u'legMiddleBlendCtr_l_offset',
 u'legMiddleBlendCtr_r_offset',
 u'legPoleCtr_l_offset',
 u'legPoleCtr_r_offset',
 u'legSettingsCtr_l_offset',
 u'legSettingsCtr_r_offset',
 u'legUpBlendCtr_l_offset',
 u'legUpBlendCtr_r_offset',
 u'middleNeckCtr_c_offset',
 u'middleSpineCtr_c_offset',
 u'neckCtr_c_offset',
 u'pelvisCtr_c_offset',
 u'shoulderFKCtr_l_offset',
 u'shoulderFKCtr_r_offset',
 u'spineFK1Ctr_c_offset',
 u'spineFK2Ctr_c_offset',
 u'spineFK3Ctr_c_offset',
 u'spineIK1Ctr_c_offset',
 u'spineIK2Ctr_c_offset',
 u'spineIK3Ctr_c_offset',
 u'toeCtr_l_offset',
 u'toeCtr_r_offset',
 u'upperBodyCtr_c_offset']
    #Generate Controls
    def offset(ctrl):
        name1=ctrl[:-6]
        side = ctrl[-5]
        grp = cmds.group(em=True, n='{}Ctr_{}_offset'.format(name1, side, ctrl))
        cmds.parent(ctrl, grp)

    def attr(ctr):
        cmds.addAttr(ctr, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(ctr), e=1, keyable=True) 

    def oneFloat(ctr, name):
        cmds.addAttr(ctr, ln=name, max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.{}'.format(ctr, name), e=1, keyable=True)
    def infiniteFloat(ctr=None, name=None, dv=1, minim = 0):
        cmds.addAttr(ctr, ln=name, dv=dv, at='double', min=minim)
        cmds.setAttr('{}.{}'.format(ctr, name), e=1, keyable=True) 
    def flip(ctrl):
        cmds.setAttr('{}.ry'.format(ctrl), 180)
        cmds.setAttr('{}.sz'.format(ctrl), -1)
        
    #general_
    general = cmds.curve(n= 'general_c_ctr',p=[(-3.60402e-07, 0, 16.506927), (3.736972, 0, 11.501218), (7.108143, 0, 9.78352), (9.78352, 0, 7.108143), (11.501217, 0, 3.736972), (12.093095, 0, 0), (11.501225, 0, -3.736974), (9.783525, 0, -7.108147), (7.108147, 0, -9.783525), (3.736974, 0, -11.501223), (0, 0, -12.093101), (-3.736974, 0, -11.501222), (-7.108146, 0, -9.783523), (-9.783523, 0, -7.108145), (-11.50122, 0, -3.736973), (-12.093098, 0, 0), (-11.50122, 0, 3.736973), (-9.783522, 0, 7.108144), (-7.108144, 0, 9.783521), (-3.736973, 0, 11.501219), (-3.60402e-07, 0, 16.506927)])
    cmds.color(general, rgb=(1,1,0))    

    cmds.addAttr(general, ln="__", en="attr:", at="enum")
    cmds.setAttr('{}.__'.format(general), e=1, keyable=True)

    cmds.addAttr(general, ln="GlobalScale", dv=0, at='double', min=1)
    cmds.setAttr('{}.GlobalScale'.format(general), e=1, keyable=True)
    offset(general)


    #center_
    center = cmds.circle(n='center_c_ctr', c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=11, tol=0.01, nr=(0, 1, 0))[0]
    cmds.color(center, rgb=(124,1,0.322))
    offset(center)



    #upperBody_
    upperBody=cmds.curve(n= 'upperBody_c_ctr', p=[(-5.456046, 0.814589, 1.799444), (-5.456046, -0.814589, 1.799444), (-9.136292, 8.15695e-06, 1.799444), (-9.136292, 8.15695e-06, -1.799444), (-5.456046, -0.814589, -1.799444), (-5.456046, 0.814589, -1.799444), (-9.136292, 8.15695e-06, -1.799444), (-5.456046, -0.814589, -1.799444), (-5.456046, -0.814589, 1.799444), (-9.136292, 8.15695e-06, 1.799444), (-5.456046, 0.814589, 1.799444), (-5.456046, 0.814589, -1.799444)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], d=1)
    s1 = cmds.duplicate('upperBody_c_ctr', rc=True)[0]
    cmds.setAttr('{}.rz'.format(s1), 180)
    s2 = cmds.duplicate('upperBody_c_ctr', rc=True)[0]
    cmds.setAttr('{}.ry'.format(s2), 90)
    s3 = cmds.duplicate('upperBody_c_ctr', rc=True)[0]
    cmds.setAttr('{}.ry'.format(s3), 270)


    cmds.select('upperBody_c_ctr1', r=1)
    cmds.select('upperBody_c_ctr2', add=1)
    cmds.select('upperBody_c_ctr3', add=1)
    cmds.FreezeTransformations()
    cmds.makeIdentity(n=0, s=1, r=1, t=1, apply=True, pn=1)


    for i in range(1,4):
        shap=cmds.listRelatives('upperBody_c_ctr{}'.format(i))[0]
        cmds.select(shap, r=1)
        cmds.select('upperBody_c_ctr', add=1)
        cmds.parent(s=1, r=1)
        cmds.select(cl=True)



    cmds.color(upperBody, rgb=(0.237,0.67,0))
    offset(upperBody)
    
    cmds.delete('upperBody_c_ctr1')
    cmds.delete('upperBody_c_ctr2')
    cmds.delete('upperBody_c_ctr3')



    #SpineFK1_
    FK1 = cmds.curve(n='spineFK1_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    cmds.color(FK1, rgb=(0.124,0.171,0.057))
    offset(FK1)

    #SpineFK2_
    FK2 = cmds.curve(n='spineFK2_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    cmds.color(FK2, rgb=(0.124,0.171,0.057))
    offset(FK2)
    #SpineFK3_
    FK3 = cmds.curve(n='spineFK3_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    cmds.color(FK3, rgb=(0.124,0.171,0.057))
    offset(FK3)


    #SpineIK1_
    IK1 = cmds.curve(n='spineIK1_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    
    cmds.color(IK1, rgb=(0.193,0,0.134))
    offset(IK1)
    cmds.scale(0.82, 0.82, 0.82, r=1)
    cmds.FreezeTransformations()
    
    
    
    #SpineIK2_
    IK2 = cmds.curve(n='spineIK2_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    
    cmds.color(IK2, rgb=(0.193,0,0.134))
    offset(IK2)
    cmds.scale(0.82, 0.82, 0.82, r=1)
    cmds.FreezeTransformations()
    
    #SpineIK3_
    IK3 = cmds.curve(n='spineIK3_c_ctr', p=[(4, 0, -2), (4, 0, 2), (2, 0, 4), (-2, 0, 4), (-4, 0, 2), (-4, 0, -2), (-2, 0, -4), (2, 0, -4), (4, 0, -2)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8], d=1)
    
    cmds.color(IK3, rgb=(0.193,0,0.134))
    offset(IK3)
    cmds.scale(0.82, 0.82, 0.82, r=1)
    cmds.FreezeTransformations()

    #clavicle_
    for side in 'rl':
        clavicle = cmds.curve(n='clavicle_{}_ctr'.format(side), p=[(0.283729, 0.0269286, 0.0197059), (4.098398, 3.848887, 0.0197059), (3.951907, 4.080857, 0.0197059), (3.912054, 4.496839, 0.0197059), (4.067499, 4.827763, 0.0197059), (4.340684, 5.034158, 0.0197059), (4.779773, 5.084596, 0.0197059), (5.055588, 4.970695, 0.0197059), (5.272609, 4.743701, 0.0197059), (5.378483, 4.432506, 0.0197059), (5.349377, 4.138987, 0.0197059), (5.13119, 3.799315, 0.0197059), (4.911814, 3.666104, 0.0197059), (4.66533, 3.61421, 0.0197059), (4.340089, 3.678139, 0.0197059), (4.110373, 3.836357, 0.0197059)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], d=1)
        cmds.color(clavicle, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(clavicle, rgb=(0.696,0.035,0.027))
        offset(clavicle)


    #spineBend_
    mSpine = cmds.curve(n='middleSpine_c_ctr', p=[(-1.76176e-07, 0, 6.960704), (0.919123, 0, 5.76591), (1.826749, 0, 5.622156), (3.474683, 0, 4.782492), (4.782491, 0, 3.474684), (5.622156, 0, 1.826749), (5.911484, 0, 0), (5.622159, 0, -1.82675), (4.782495, 0, -3.474685), (3.474685, 0, -4.782494), (1.82675, 0, -5.622159), (0, 0, -5.911487), (-1.82675, 0, -5.622158), (-3.474685, 0, -4.782493), (-4.782493, 0, -3.474684), (-5.622157, 0, -1.826749), (-5.911486, 0, 0), (-5.622157, 0, 1.826749), (-4.782492, 0, 3.474684), (-3.474684, 0, 4.782492), (-0.909281, 0, 5.767469), (-1.76176e-07, 0, 6.960704)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], d=1)
    cmds.color(mSpine, rgb=(1,1,0))
    offset(mSpine)

    #Pelvis_
    pelvis = cmds.curve(n='pelvis_c_ctr', p=[(-1.76176e-07, 0, 6.960704), (0.919123, 0, 5.76591), (1.826749, 0, 5.622156), (3.474683, 0, 4.782492), (4.782491, 0, 3.474684), (5.622156, 0, 1.826749), (5.911484, 0, 0), (5.622159, 0, -1.82675), (4.782495, 0, -3.474685), (3.474685, 0, -4.782494), (1.82675, 0, -5.622159), (0, 0, -5.911487), (-1.82675, 0, -5.622158), (-3.474685, 0, -4.782493), (-4.782493, 0, -3.474684), (-5.622157, 0, -1.826749), (-5.911486, 0, 0), (-5.622157, 0, 1.826749), (-4.782492, 0, 3.474684), (-3.474684, 0, 4.782492), (-0.909281, 0, 5.767469), (-1.76176e-07, 0, 6.960704)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], d=1)
    cmds.color(pelvis, rgb=(1,1,0))
    offset(pelvis)
    
    #Chest_
    chest = cmds.curve(n='chest_c_ctr', p=[(-1.76176e-07, 0, 6.960704), (0.919123, 0, 5.76591), (1.826749, 0, 5.622156), (3.474683, 0, 4.782492), (4.782491, 0, 3.474684), (5.622156, 0, 1.826749), (5.911484, 0, 0), (5.622159, 0, -1.82675), (4.782495, 0, -3.474685), (3.474685, 0, -4.782494), (1.82675, 0, -5.622159), (0, 0, -5.911487), (-1.82675, 0, -5.622158), (-3.474685, 0, -4.782493), (-4.782493, 0, -3.474684), (-5.622157, 0, -1.826749), (-5.911486, 0, 0), (-5.622157, 0, 1.826749), (-4.782492, 0, 3.474684), (-3.474684, 0, 4.782492), (-0.909281, 0, 5.767469), (-1.76176e-07, 0, 6.960704)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], d=1)
    cmds.color(chest, rgb=(1,1,0))
    attr(chest)
    oneFloat(chest, 'Stretch')
    offset(chest)


    #middleNeck_
    neck = cmds.curve(n='middleNeck_c_ctr', p=[(-8.04265e-08, 0, 3.348198), (0.705864, 0, 2.566583), (1.586235, 0, 2.183265), (2.183265, 0, 1.586235), (2.566582, 0, 0.833933), (2.566584, 0, -0.833934), (2.183267, 0, -1.586236), (1.586236, 0, -2.183267), (0.833934, 0, -2.566584), (0, 0, -2.698666), (-0.833934, 0, -2.566584), (-1.586236, 0, -2.183266), (-2.183266, 0, -1.586236), (-2.566583, 0, -0.833933), (-2.698665, 0, 0), (-2.566583, 0, 0.833933), (-2.183266, 0, 1.586235), (-1.586235, 0, 2.183266), (-0.705864, 0, 2.566583), (-8.04265e-08, 0, 3.348198)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], d=1)
    cmds.color(neck, rgb=(1,1,0))
    offset(neck)


    #neck_
    neck = cmds.curve(n='neck_c_ctr', p=[(-0.0236117, -0.579849, 3.051797), (0.556132, -0.543993, 3.021964), (1.564183, -0.280184, 2.751003), (1.891835, -0.112346, 2.545789), (2.202836, 0.137449, 2.198635), (2.368464, 0.376225, 1.820412), (2.469395, 0.670483, 1.28204), (2.497413, 0.935618, 0.689188), (2.487877, 1.22312, -0.341578), (2.495273, 1.260285, -0.901292), (2.470548, 1.153544, -1.790652), (2.058997, 0.820408, -2.813104), (1.419097, 0.619051, -3.250979), (0.547066, 0.48674, -3.492416), (-0.27585, 0.46946, -3.520623), (-0.679163, 0.499126, -3.471573), (-1.020082, 0.543254, -3.394076), (-1.448504, 0.625809, -3.237648), (-1.813154, 0.726739, -3.0275), (-2.235576, 0.913696, -2.57878), (-2.440164, 1.101842, -2.000811), (-2.497589, 1.252444, -1.111214), (-2.488046, 1.205677, -0.234155), (-2.479171, 0.724489, 1.171893), (-2.192182, 0.126004, 2.215618), (-1.908258, -0.102077, 2.532492), (-1.522392, -0.297605, 2.77096), (-1.030855, -0.45566, 2.939425), (-0.550777, -0.544679, 3.022562), (0.072374, -0.579295, 3.051373)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29], d=1)
    cmds.color(neck, rgb=(1,1,0))
    offset(neck)
    cmds.addAttr('|neckCtr_c_offset|neck_c_ctr', ln="_", en="spaces:", at="enum", nn="_")
    cmds.setAttr('|neckCtr_c_offset|neck_c_ctr._', e=1, keyable=True)
    cmds.addAttr('|neckCtr_c_offset|neck_c_ctr', nn="Chest Space", min=0, ln="ChestSpace", max=1, at='double', dv=0)
    cmds.setAttr('|neckCtr_c_offset|neck_c_ctr.ChestSpace', e=1, keyable=True)


    #head_
    head = cmds.curve(n='head_c_ctr', p=[(-0.00906063, 5.526615, 3.361025), (0.478086, 5.481356, 3.355838), (0.911797, 5.370075, 3.330879), (1.497082, 5.129095, 3.232043), (1.881461, 4.91998, 3.095281), (2.288036, 4.657815, 2.839404), (2.77769, 4.275056, 2.249158), (3.063701, 3.974647, 1.605423), (3.203855, 3.740685, 0.986747), (3.237927, 3.583737, 0.502827), (3.216215, 3.466163, 0.0938863), (3.09009, 3.306699, -0.544166), (2.87474, 3.186459, -1.114592), (2.555016, 3.090213, -1.662183), (2.075523, 3.015602, -2.202819), (1.682184, 2.984319, -2.506999), (1.133468, 2.963139, -2.796757), (0.456747, 2.955356, -2.987936), (-0.0508068, 2.954841, -3.024241), (-0.699389, 2.956716, -2.938583), (-1.289291, 2.967291, -2.72798), (-1.954601, 3.00397, -2.306779), (-2.419711, 3.063198, -1.840186), (-2.794448, 3.156418, -1.27432), (-3.032777, 3.266216, -0.725741), (-3.195144, 3.42339, -0.066752), (-3.23727, 3.559171, 0.421018), (-3.190395, 3.772169, 1.076635), (-3.084388, 3.94732, 1.538761), (-2.960554, 4.095773, 1.884312), (-2.727912, 4.319052, 2.330119), (-2.525038, 4.484544, 2.604414), (-2.237044, 4.692971, 2.880361), (-1.839103, 4.944897, 3.114344), (-1.278531, 5.230458, 3.280868), (-0.769742, 5.413263, 3.342256), (-0.0482781, 5.526144, 3.361002)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], d=1)
    cmds.color(head, rgb=(1,1,0))
    offset(head)
    cmds.select('headCtr_c_offset|head_c_ctr', r=1, sym=1)
    cmds.addAttr('headCtr_c_offset|head_c_ctr', ln="__", en="attr:", at="enum", nn="__")
    cmds.setAttr('headCtr_c_offset|head_c_ctr.__', e=1, keyable=True)
    cmds.addAttr('headCtr_c_offset|head_c_ctr', nn="Neck  Follow", min=0, ln="FollowHead", max=1, at='double', dv=0)
    cmds.setAttr('headCtr_c_offset|head_c_ctr.FollowHead', e=1, keyable=True)
    cmds.select('headCtr_c_offset|head_c_ctr', r=1, sym=1)
    cmds.addAttr('headCtr_c_offset|head_c_ctr', ln="_", en="spaces:", at="enum", nn="_")
    cmds.setAttr('headCtr_c_offset|head_c_ctr._', e=1, keyable=True)
    cmds.select('headCtr_c_offset|head_c_ctr', r=1, sym=1)
    cmds.addAttr('headCtr_c_offset|head_c_ctr', nn="Neck Space", min=0, ln="neckSpace", max=1, at='double', dv=0)
    cmds.setAttr('headCtr_c_offset|head_c_ctr.neckSpace', e=1, keyable=True)
    
    
    #amrBlendLow_
    for side in 'rl':
        bend = cmds.circle(n='armLowBlend_{}_ctr'.format(side))
        armBend = bend[0]
        nodoCircle = bend[1]
        cmds.setAttr('{}.normalX'.format(nodoCircle), 600)
        cmds.setAttr('{}.radius'.format(nodoCircle), 3)
        cmds.color(armBend, rgb=(230,140,162))
        offset(armBend)
        if side == 'l':
            cmds.color(armBend, rgb=(40,1,0.322))
        
        
    #amrBlendUp_
    for side in 'rl':
        bend = cmds.circle(n='armUpBlend_{}_ctr'.format(side))
        armBend = bend[0]
        nodoCircle = bend[1]
        cmds.setAttr('{}.normalX'.format(nodoCircle), 600)
        cmds.setAttr('{}.radius'.format(nodoCircle), 3)
        cmds.color(armBend, rgb=(230,140,162))
        offset(armBend)
        if side == 'l':
            cmds.color(armBend, rgb=(40,1,0.322))
        
        
    #amrBlendUp_
    for side in 'rl':
        bend = cmds.circle(n='armMiddleBlend_{}_ctr'.format(side))
        armBend = bend[0]
        nodoCircle = bend[1]
        cmds.setAttr('{}.normalX'.format(nodoCircle), 600)
        cmds.setAttr('{}.radius'.format(nodoCircle), 3)
        cmds.color(armBend, rgb=(230,140,162))
        offset(armBend)
        if side == 'l':
            cmds.color(armBend, rgb=(40,1,0.322))
        
        
        
    #handIK_
    for side in 'rl':
        handIK = cmds.curve(n='handIK_{}_ctr'.format(side), p=[(-2.4, 0, -2.400001), (-0.4, 0, -2.400001), (-0.4, 0, -3.2), (-0.8, 0, -3.2), (0, 0, -4), (0.8, 0, -3.2), (0.400001, 0, -3.2), (0.400001, 0, -2.400001), (2.400001, 0, -2.400001), (2.400001, 0, -0.400001), (3.2, 0, -0.400001), (3.2, 0, -0.8), (4, 0, 0), (3.2, 0, 0.8), (3.2, 0, 0.4), (2.400001, 0, 0.4), (2.400001, 0, 2.4), (0.400001, 0, 2.4), (0.400001, 0, 3.2), (0.8, 0, 3.2), (0, 0, 4), (-0.8, 0, 3.2), (-0.4, 0, 3.2), (-0.4, 0, 2.4), (-2.4, 0, 2.4), (-2.4, 0, 0.4), (-3.2, 0, 0.4), (-3.2, 0, 0.8), (-4, 0, 0), (-3.2, 0, -0.8), (-3.2, 0, -0.400001), (-2.4, 0, -0.400001), (-2.4, 0, -2.400001)], k=[0, 2, 2.8, 3.2, 4.331371, 5.462743, 5.862742, 6.662741, 8.662741, 10.662741, 11.462741, 11.86274, 12.994111, 14.125482, 14.525483, 15.325482, 17.325483, 19.325483, 20.125482, 20.525482, 21.656853, 22.788224, 23.188225, 23.988225, 25.988225, 27.988226, 28.788225, 29.188226, 30.319597, 31.450968, 31.850968, 32.650967, 34.650967], d=1)
        cmds.addAttr(handIK, ln="AutoStretch", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.AutoStretch'.format(handIK), e=1, keyable=True)
        cmds.addAttr(handIK, ln="Elbow", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.Elbow'.format(handIK), e=1, keyable=True)
        cmds.addAttr(handIK, ln="__", en="spaces:", at="enum", nn="_")
        cmds.setAttr('{}.__'.format(handIK), e=1, keyable=True)
        cmds.addAttr(handIK, ln="ChestSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.ChestSpace'.format(handIK), e=1, keyable=True)
        cmds.addAttr(handIK, ln="HeadSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.HeadSpace'.format(handIK), e=1, keyable=True)
        cmds.addAttr(handIK, ln="HipSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.HipSpace'.format(handIK), e=1, keyable=True)
        cmds.setAttr("{}.rotateZ".format(handIK), 90)
        cmds.FreezeTransformations()
        cmds.color(handIK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(handIK, rgb=(0.696,0.035,0.027))
        offset(handIK)
        
        
    #handFK_
    for side in 'rl':
        handFK = cmds.curve(n='handFK_{}_ctr'.format(side), p=[(-0.259275, -0.609001, 0.0506822), (-0.234091, -0.609001, 0.391155), (-0.188739, -0.609, 1.004282), (0.321094, -0.609005, 1.814125), (0.802455, -0.608988, 2.496939), (1.580395, -0.609037, 2.920006), (2.348253, -0.608824, 2.943054), (3.079394, -0.609465, 2.91513), (3.689918, -0.607617, 2.921027), (4.156881, -0.601368, 2.945297), (4.771137, -0.451005, 3.021692), (4.37332, 0.107051, 3.057296), (3.986368, 0.421548, 3.032682), (3.496317, 0.797613, 2.970597), (2.929086, 1.166058, 2.832916), (2.259701, 1.52244, 2.499926), (1.692881, 1.664249, 1.773714), (1.405117, 1.651421, 0.954272), (1.300889, 1.654143, 0.107301), (1.437982, 1.65373, -0.707674), (1.766817, 1.652377, -1.50542), (2.353143, 1.485484, -2.199832), (3.155077, 1.03384, -2.536645), (3.87377, 0.533626, -2.647418), (4.343223, 0.101103, -2.669442), (4.610485, -0.178534, -2.662925), (4.619725, -0.456838, -2.625233), (4.173317, -0.627303, -2.561208), (3.497501, -0.599402, -2.524434), (2.680465, -0.610351, -2.556114), (1.953051, -0.608693, -2.549997), (1.376307, -0.609078, -2.451596), (0.758123, -0.608965, -2.05187), (0.313857, -0.60901, -1.421943), (-0.134986, -0.608999, -0.703776), (-0.216538, -0.609001, -0.191973), (-0.257984, -0.609001, 0.0681321)], k=[0, 0, 0, 1.005467, 1.810656, 2.827175, 3.475035, 4.384375, 5.076924, 5.69692, 6.164592, 6.614238, 7.102291, 7.641101, 8.27345, 8.909288, 9.724758, 10.687152, 11.589565, 12.305711, 13.225604, 14.033625, 14.872881, 15.897006, 16.876257, 17.507297, 17.82684, 18.003996, 18.237687, 19.088355, 20.117208, 20.655982, 21.278534, 21.839667, 22.811908, 23.568098, 24.349547, 24.349547, 24.349547], d=3)
        cmds.addAttr(handFK, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(handFK), e=1, keyable=True)
        cmds.addAttr(handFK, ln="Stretch", dv=1, at='double', min=1)
        cmds.setAttr('{}.Stretch'.format(handFK), e=1, keyable=True) 
        cmds.addAttr(handFK, ln="__", en="spaces:", at="enum", nn="_")
        cmds.setAttr('{}.__'.format(handFK), e=1, keyable=True)
        cmds.addAttr(handFK, ln="ChestSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.ChestSpace'.format(handFK), e=1, keyable=True)
        cmds.color(handFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(handFK, rgb=(0.696,0.035,0.027))
        offset(handFK)        
    
    #shoulderFK_
    for side in 'rl':
        shoulderFK = cmds.curve(n='shoulderFK_{}_ctr'.format(side), p=[(1.688088, 9.540492, 0.218075), (1.685252, 9.524145, -0.288581), (1.679158, 9.489025, -1.377095), (1.604738, 9.005682, -2.933156), (1.509863, 8.310913, -4.251953), (1.409628, 7.498418, -5.33675), (1.311428, 6.615752, -6.229291), (1.202582, 5.504096, -7.071173), (1.092557, 4.172465, -7.813566), (0.998019, 2.6606, -8.384802), (0.925129, 0.815671, -8.803185), (0.914941, -1.028145, -8.904794), (0.978368, -2.835165, -8.688532), (1.060526, -4.226463, -8.337305), (1.158355, -5.483304, -7.857968), (1.266686, -6.646646, -7.256909), (1.394836, -7.837439, -6.435374), (1.511819, -8.793585, -5.514369), (1.627448, -9.660447, -4.399367), (1.72322, -10.318687, -3.236948), (1.806214, -10.843026, -1.719658), (1.842957, -11.052653, -0.163254), (1.818063, -10.911948, 1.345093), (1.757055, -10.535766, 2.688382), (1.679403, -10.021738, 3.79766), (1.593241, -9.407548, 4.74934), (1.505696, -8.741728, 5.563551), (1.416593, -8.010798, 6.268205), (1.322574, -7.172727, 6.912802), (1.236499, -6.329365, 7.434885), (1.152327, -5.399207, 7.893292), (1.08565, -4.549064, 8.22262), (1.027693, -3.676631, 8.486085), (0.981797, -2.829378, 8.676878), (0.941674, -1.80475, 8.824108), (0.919225, -0.672763, 8.881454), (0.926193, 0.448731, 8.814538), (0.955435, 1.617002, 8.637666), (1.00365, 2.722148, 8.358536), (1.078944, 3.953199, 7.901634), (1.161986, 5.030544, 7.359324), (1.252761, 6.027375, 6.69951), (1.347916, 6.955555, 5.921777), (1.452368, 7.85978, 4.918948), (1.552803, 8.632069, 3.712418), (1.633742, 9.198328, 2.378751), (1.679025, 9.48596, 1.197119), (1.685589, 9.525502, 0.433734), (1.687833, 9.539025, 0.172664)], k=[0, 0, 0, 1.515517, 3.25598, 4.832826, 5.978654, 7.321218, 8.596241, 10.162856, 11.890487, 13.433899, 15.828838, 17.382842, 18.88197, 20.128518, 21.421389, 22.814534, 24.472435, 25.394824, 27.060655, 28.462099, 30.196341, 31.727403, 32.973407, 34.36931, 35.384476, 36.374286, 37.529391, 38.433357, 39.554459, 40.510005, 41.551009, 42.292773, 43.248008, 44.156912, 45.397685, 46.641722, 47.520042, 48.940869, 50.054727, 51.460621, 52.557078, 53.644627, 55.096666, 56.602824, 57.929527, 59.437223, 60.22082, 60.22082, 60.22082], d=3)
        cmds.addAttr(shoulderFK, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(shoulderFK), e=1, keyable=True)   
        cmds.addAttr(shoulderFK, ln="Stretch", dv=1, at='double', min=1)
        cmds.setAttr('{}.Stretch'.format(shoulderFK), e=1, keyable=True) 
        cmds.color(shoulderFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(shoulderFK, rgb=(0.696,0.035,0.027))
        offset(shoulderFK)   
        
    #elbowFK_
    for side in 'rl':
        elbowFK = cmds.curve(n='elbowFK_{}_ctr'.format(side), p=[(4.129111, 7.854407, -0.0407905), (4.113892, 7.826445, -0.455747), (4.08408, 7.771675, -1.268559), (3.863644, 7.348506, -2.596092), (3.533071, 6.683087, -3.801825), (3.101685, 5.76421, -4.884898), (2.614848, 4.679748, -5.796564), (2.073295, 3.345059, -6.552269), (1.604232, 1.890156, -7.071696), (1.285953, 0.462149, -7.353418), (1.147109, -0.917909, -7.425824), (1.212299, -2.310535, -7.294252), (1.439245, -3.689909, -6.966817), (1.787462, -4.967158, -6.45491), (2.219242, -6.163041, -5.758762), (2.679539, -7.193291, -4.913765), (3.108707, -7.995942, -3.961492), (3.503778, -8.652965, -2.881524), (3.807029, -9.099569, -1.747788), (3.996249, -9.346781, -0.333735), (3.925825, -9.260761, 1.219374), (3.558087, -8.744108, 2.755472), (3.072206, -7.939422, 4.072042), (2.573173, -6.975259, 5.131788), (2.093973, -5.849053, 5.978482), (1.716366, -4.723539, 6.567478), (1.433218, -3.612159, 6.983158), (1.23074, -2.446305, 7.275798), (1.141997, -1.090827, 7.431117), (1.275843, 0.472798, 7.372701), (1.626203, 1.974319, 7.061261), (2.070655, 3.314211, 6.553748), (2.590903, 4.63191, 5.840367), (3.189817, 5.963468, 4.763747), (3.718639, 7.064667, 3.234162), (4.067286, 7.74132, 1.58713), (4.108742, 7.817148, 0.480845), (4.129016, 7.854232, -0.0601744)], k=[0, 0, 0, 1.243318, 2.435398, 4.191646, 5.454182, 6.869722, 8.66605, 10.306058, 11.691, 13.117145, 14.44291, 15.867075, 17.403668, 18.679979, 20.203287, 21.610917, 22.611564, 24.168307, 25.340366, 26.92148, 28.755198, 30.250617, 31.749238, 33.281605, 34.693325, 35.709386, 36.934043, 38.337766, 39.783977, 41.611304, 43.018762, 44.270373, 46.360771, 48.400786, 50.090186, 51.707125, 51.707125, 51.707125], d=3)
        cmds.addAttr(elbowFK, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(elbowFK), e=1, keyable=True)
        cmds.addAttr(elbowFK, ln="Stretch", dv=1, at='double', min=1)
        cmds.setAttr('{}.Stretch'.format(elbowFK), e=1, keyable=True) 
        cmds.addAttr(elbowFK, ln="__", en="spaces:", at="enum", nn="_")
        cmds.setAttr('{}.__'.format(elbowFK), e=1, keyable=True)
        cmds.addAttr(elbowFK, ln="ChestSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.ChestSpace'.format(elbowFK), e=1, keyable=True)
        cmds.color(elbowFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(elbowFK, rgb=(0.696,0.035,0.027))
        offset(elbowFK)   
        
        
        
    cmds.select('shoulderFK_l_ctr', 'elbowFK_r_ctr', 'elbowFK_l_ctr', 'shoulderFK_r_ctr', r=1)
    cmds.scale(0.297576, 0.297576, 0.297576, r=1)     
    cmds.FreezeTransformations()   
    cmds.select(cl=True)
  
    #armPole_
    for side in 'rl':
        armPole = cmds.curve(n='armPole_{}_ctr'.format(side), p=[(0, 1, 0), (-2.98023e-08, 0, 1), (0, -1, 0), (0, 0, -1), (0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (-2.98023e-08, 0, 1), (1, 0, 0), (0, 0, -1), (-1, 0, 0)], k=[0, 1.414214, 2.828427, 4.242641, 5.656855, 7.071069, 8.485282, 9.899496, 11.31371, 12.727924, 14.142138, 15.556351, 16.970565, 18.384779, 19.798993], d=1)


        cmds.addAttr(armPole, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(armPole), e=1, keyable=True)
        
        
        cmds.addAttr(armPole, ln="PinElbow", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.PinElbow'.format(armPole), e=1, keyable=True)


        cmds.addAttr(armPole, ln="__", en="spaces:", at="enum", nn="_")
        cmds.setAttr('{}.__'.format(armPole), e=1, keyable=True)

        cmds.addAttr(armPole, ln="ChestSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.ChestSpace'.format(armPole), e=1, keyable=True)
        
        
        cmds.addAttr(armPole, ln="HandSpace", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.HandSpace'.format(armPole), e=1, keyable=True)


        cmds.color(armPole, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(armPole, rgb=(0.696,0.035,0.027))
        offset(armPole)           
  
  
  
    #armSettings_
    for side in 'rl':
        armSettings = cmds.curve(n='armSettings_{}_ctr'.format(side), p=[(-0.269231, 0, -0.192308), (-0.269231, 0, 0.192308), (-0.230769, 0, 0.192308), (-0.230769, 0, 0.230769), (-0.192308, 0, 0.230769), (-0.192308, 0, 0.269231), (0.192308, 0, 0.269231), (0.192308, 0, 0.230769), (0.230769, 0, 0.230769), (0.230769, 0, 0.192308), (0.269231, 0, 0.192308), (0.269231, 0, -0.192308), (0.230769, 0, -0.192308), (0.230769, 0, -0.230769), (0.192308, 0, -0.230769), (0.192308, 0, -0.269231), (-0.192308, 0, -0.269231), (-0.192308, 0, -0.230769), (-0.230769, 0, -0.230769), (-0.230769, 0, -0.192308), (-0.269231, 0, -0.192308)], k=[0, 0.384615, 0.423077, 0.461538, 0.5, 0.538462, 0.923077, 0.961538, 1, 1.038462, 1.076923, 1.461538, 1.5, 1.538462, 1.576923, 1.615385, 2, 2.038462, 2.076923, 2.115385, 2.153846], d=1)
        
        attr(armSettings)
        oneFloat(armSettings, 'Arm_IK')
        infiniteFloat(armSettings, 'Stretch')
        
        cmds.color(armSettings, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(armSettings, rgb=(0.696,0.035,0.027))           
        offset(armSettings)       




    #legBends_
    for side in 'rl':
        blen = cmds.circle(n='legUpBlend_{}_ctr'.format(side),c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]    

        nodeRadius = cmds.listConnections('legUpBlend_{}_ctrShape.create'.format(side))[0]
        cmds.setAttr("{}.radius".format(nodeRadius), 3)    
        cmds.color(blen, rgb=(230,140,162))
        offset(blen)
        if side == 'l':
            cmds.color(blen, rgb=(40,1,0.322))
        
    for side in 'rl':
        blen = cmds.circle(n='legLowBlend_{}_ctr'.format(side),c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]    

        nodeRadius = cmds.listConnections('legLowBlend_{}_ctrShape.create'.format(side))[0]
        cmds.setAttr("{}.radius".format(nodeRadius), 3)    
        cmds.color(blen, rgb=(230,140,162))
        offset(blen)
        if side == 'l':
            cmds.color(blen, rgb=(40,1,0.322))
            
    for side in 'rl':
        blen = cmds.circle(n='legMiddleBlend_{}_ctr'.format(side),c=(0, 0, 0), ch=1, d=3, ut=0, sw=360, s=8, r=1, tol=0.01, nr=(0, 1, 0))[0]    

        nodeRadius = cmds.listConnections('legMiddleBlend_{}_ctrShape.create'.format(side))[0]
        cmds.setAttr("{}.radius".format(nodeRadius), 3)    
        cmds.color(blen, rgb=(230,140,162))
        offset(blen)
        if side == 'l':
            cmds.color(blen, rgb=(40,1,0.322))
            
    #legSettings_
    for side in 'rl':
        legSettings = cmds.curve(n='legSettings_{}_ctr'.format(side), p=[(-0.269231, 0, -0.192308), (-0.269231, 0, 0.192308), (-0.230769, 0, 0.192308), (-0.230769, 0, 0.230769), (-0.192308, 0, 0.230769), (-0.192308, 0, 0.269231), (0.192308, 0, 0.269231), (0.192308, 0, 0.230769), (0.230769, 0, 0.230769), (0.230769, 0, 0.192308), (0.269231, 0, 0.192308), (0.269231, 0, -0.192308), (0.230769, 0, -0.192308), (0.230769, 0, -0.230769), (0.192308, 0, -0.230769), (0.192308, 0, -0.269231), (-0.192308, 0, -0.269231), (-0.192308, 0, -0.230769), (-0.230769, 0, -0.230769), (-0.230769, 0, -0.192308), (-0.269231, 0, -0.192308)], k=[0, 0.384615, 0.423077, 0.461538, 0.5, 0.538462, 0.923077, 0.961538, 1, 1.038462, 1.076923, 1.461538, 1.5, 1.538462, 1.576923, 1.615385, 2, 2.038462, 2.076923, 2.115385, 2.153846], d=1)
        
        attr(legSettings)
        oneFloat(legSettings, 'Leg_IK')
        infiniteFloat(legSettings, 'Stretch')
        oneFloat(legSettings, 'autoSquash')
        
        cmds.color(legSettings, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(legSettings, rgb=(0.696,0.035,0.027))
        offset(legSettings)  
        
        
    #legPole_
    for side in 'rl':
        legPole = cmds.curve(n='legPole_{}_ctr'.format(side), p=[(0, 1, 0), (-2.98023e-08, 0, 1), (0, -1, 0), (0, 0, -1), (0, 1, 0), (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (-2.98023e-08, 0, 1), (1, 0, 0), (0, 0, -1), (-1, 0, 0)], k=[0, 1.414214, 2.828427, 4.242641, 5.656855, 7.071069, 8.485282, 9.899496, 11.31371, 12.727924, 14.142138, 15.556351, 16.970565, 18.384779, 19.798993], d=1)


        cmds.addAttr(legPole, ln="_", en="attr:", at="enum")
        cmds.setAttr('{}._'.format(legPole), e=1, keyable=True)
        
        
        cmds.addAttr(legPole, ln="pinKnee", max=1, dv=0, at='double', min=0)
        cmds.setAttr('{}.pinKnee'.format(legPole), e=1, keyable=True)

        cmds.color(legPole, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(legPole, rgb=(0.696,0.035,0.027))
        offset(legPole)           
          
          
    #legsFK_
    for side in 'rl':
        hipFK = cmds.circle(n='hipFK_{}_ctr'.format(side), c=(0, 0, 0), ch=1, d=1, ut=0, sw=360, s=4, r=4, tol=0.01, nr=(0, 1, 0))[0]
        attr(hipFK)
        infiniteFloat(hipFK, 'Stretch')
        cmds.color(hipFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(hipFK, rgb=(0.696,0.035,0.027))
        offset(hipFK)  

        footFK = cmds.circle(n='footFK_{}_ctr'.format(side), c=(0, 0, 0), ch=1, d=1, ut=0, sw=360, s=4, r=4, tol=0.01, nr=(0, 1, 0))[0]
        attr(footFK)
        infiniteFloat(footFK, 'Stretch')
        cmds.color(footFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(footFK, rgb=(0.696,0.035,0.027))
        offset(footFK)  

        kneeFK = cmds.circle(n='kneeFK_{}_ctr'.format(side), c=(0, 0, 0), ch=1, d=1, ut=0, sw=360, s=4, r=4, tol=0.01, nr=(0, 1, 0))[0]
        attr(kneeFK)
        infiniteFloat(kneeFK, 'Stretch')
        cmds.color(kneeFK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(kneeFK, rgb=(0.696,0.035,0.027))
        offset(kneeFK)    
 
    for side in 'rl':        
        footIK = cmds.curve(n= 'footIK_{}_ctr'.format(side), p=[(0.566299, -3.880927, 21.713182), (1.837053, -4.058588, 21.158397), (2.953511, -4.283378, 20.286933), (3.955646, -4.534353, 19.026532), (4.77056, -4.77923, 17.288891), (5.27501, -4.967409, 15.192199), (5.560398, -5.120419, 12.487461), (5.633768, -5.30664, 5.64772), (5.641498, -5.352313, 1.818756), (5.612919, -5.362869, 0.382069), (5.415954, -5.372748, -1.84411), (5.003885, -5.37574, -3.561784), (4.308392, -5.376176, -5.016165), (3.147246, -5.376176, -6.372168), (1.755069, -5.376176, -7.378785), (0.158534, -5.376176, -8.064733), (-1.319097, -5.376176, -8.29854), (-2.683442, -5.376176, -8.036416), (-3.603767, -5.376176, -7.33164), (-4.283822, -5.376176, -6.18606), (-4.685533, -5.376176, -4.774477), (-4.851187, -5.376176, -3.119194), (-4.799923, -5.376176, -1.627533), (-4.543374, -5.375271, 0.0227815), (-4.223456, -5.370166, 1.475157), (-4.002616, -5.362054, 2.5561), (-3.84186, -5.35064, 3.595026), (-3.708708, -5.315671, 5.866787), (-3.835515, -5.261153, 8.457159), (-3.930724, -5.230366, 9.588987), (-4.082882, -5.174329, 11.262225), (-4.168681, -5.134427, 12.239974), (-4.2697, -5.069638, 13.565502), (-4.340733, -4.984205, 14.960778), (-4.354258, -4.900239, 16.055283), (-4.29572, -4.779176, 17.289364), (-4.004736, -4.551549, 18.925134), (-3.376602, -4.264604, 20.367713), (-2.715385, -4.064416, 21.138262), (-1.66976, -3.876326, 21.725955), (-0.567287, -3.81623, 21.882808), (0.566197, -3.880916, 21.713211)], k=[0, 1.397914, 2.83195, 4.461635, 6.396434, 8.561151, 11.285204, 18.127872, 21.957117, 23.394127, 25.629024, 27.395436, 29.007558, 30.792776, 32.51075, 34.248406, 35.744421, 37.133718, 38.292902, 39.625128, 41.092759, 42.75631, 44.248852, 45.918988, 47.40619, 48.509491, 49.560843, 51.836771, 54.430818, 55.567061, 57.248137, 58.230454, 59.561403, 60.961097, 62.058901, 63.300286, 64.977257, 66.576608, 67.611513, 68.825636, 69.940831, 71.088757], d=1)
        cmds.color(footIK, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(footIK, rgb=(0.696,0.035,0.027))
        offset(footIK)          
        attr(footIK)
        infiniteFloat(footIK, 'Knee')
        oneFloat(footIK, 'autoStretch')
        infiniteFloat(footIK, 'FootRoll', dv=0, minim = -900)
        infiniteFloat(footIK, 'toeBreak', dv=0, minim = -900)
        infiniteFloat(footIK, 'releaseAngle', dv=0, minim = -900)
        infiniteFloat(footIK, 'footTilt', dv=0, minim = -900)
        infiniteFloat(footIK, 'toeRoll', dv=0, minim = -900)
        infiniteFloat(footIK, 'toeSlide', dv=0, minim = -900)
        infiniteFloat(footIK, 'heelRoll', dv=0, minim = -900)
        infiniteFloat(footIK, 'ballRoll', dv=0, minim = -900)

        cmds.scale(0.429166, 0.429166, 0.429166, r=1)
        cmds.FreezeTransformations()
        
        
        hip = cmds.curve(n='hip_{}_ctr'.format(side), p=[(11.46422, 0, 0), (17.196333, 0, 0), (22.928444, 0, 0), (28.63073, 0, 0), (28.658184, 0.348822, 0), (28.739866, 0.689056, 0), (28.873768, 1.012323, 0), (29.056591, 1.310662, 0), (29.283833, 1.576729, 0), (29.5499, 1.803972, 0), (29.84824, 1.986795, 0), (30.171507, 2.120697, 0), (30.860563, 2.229832, 0), (31.209387, 2.202379, 0), (31.54962, 2.120697, 0), (31.872887, 1.986795, 0), (32.171227, 1.803972, 0), (32.437294, 1.576729, 0), (32.664536, 1.310662, 0), (32.847359, 1.012323, 0), (32.981258, 0.689056, 0), (33.062943, 0.348822, 0), (33.090397, 0, 0), (33.062943, -0.348822, 0), (32.981258, -0.689056, 0), (32.847359, -1.012323, 0), (32.664536, -1.310662, 0), (32.437294, -1.576729, 0), (32.171227, -1.803972, 0), (31.872887, -1.986795, 0), (31.54962, -2.120697, 0), (31.209387, -2.202379, 0), (30.860563, -2.229832, 0), (30.51174, -2.202379, 0), (30.171507, -2.120697, 0), (29.84824, -1.986795, 0), (29.5499, -1.803972, 0), (29.283833, -1.576729, 0), (29.056591, -1.310662, 0), (28.873768, -1.012323, 0), (28.739866, -0.689056, 0), (28.658184, -0.348822, 0), (28.63073, 0, 0)], k=[0, 5.732113, 11.464224, 17.16651, 17.516411, 17.866312, 18.216213, 18.566115, 18.916015, 19.265917, 19.615818, 19.96572, 20.663365, 21.013267, 21.363168, 21.71307, 22.062971, 22.412873, 22.762773, 23.112674, 23.462575, 23.812477, 24.162378, 24.512279, 24.862181, 25.212081, 25.561983, 25.911883, 26.261785, 26.611686, 26.961588, 27.311488, 27.661391, 28.011293, 28.361193, 28.711095, 29.060996, 29.410898, 29.760798, 30.1107, 30.460601, 30.810502, 31.160403], d=1)
        cmds.color(hip, rgb=(0.027, 0.188, 0.678))
        if side == 'r':
            cmds.color(hip, rgb=(0.696,0.035,0.027))
        offset(hip) 
        cmds.scale(0.429166, 0.429166, 0.429166, r=1)
        cmds.FreezeTransformations()

        toe  = cmds.curve(n='toe_{}_ctr'.format(side), p=[(-0.0385215, 3.957414, 0.718801), (0.205524, 3.934804, 0.733309), (0.729687, 3.886242, 0.764471), (1.459415, 3.605437, 1.045553), (2.187278, 3.219955, 1.479569), (2.916797, 2.723655, 2.102098), (3.397958, 2.235792, 3.082272), (3.394273, 1.981778, 4.381794), (3.102841, 1.91104, 5.668804), (2.523822, 1.92142, 7.069801), (1.708564, 2.009793, 8.208151), (0.752163, 2.104869, 8.834095), (-0.191018, 2.157225, 9.010093), (-1.121942, 2.143878, 8.674219), (-1.912478, 2.10903, 7.934674), (-2.459396, 2.091758, 7.154354), (-2.88106, 2.096313, 6.300734), (-3.22482, 2.134239, 5.303357), (-3.417225, 2.226477, 4.277463), (-3.407479, 2.415846, 3.329943), (-3.175681, 2.697319, 2.546391), (-2.640559, 3.090211, 1.866215), (-1.864957, 3.520306, 1.279832), (-0.98733, 3.885767, 0.830041), (-0.313255, 3.93729, 0.750355), (-0.0485848, 3.957521, 0.719067)], k=[0, 0, 0, 0.730603, 1.569196, 2.440623, 3.525249, 4.778448, 5.879079, 7.412875, 8.71545, 10.409304, 11.54359, 12.05069, 13.246686, 14.31901, 15.275676, 16.089115, 17.168215, 18.43406, 19.207572, 20.043584, 20.97382, 22.007629, 23.237581, 24.032715, 24.032715, 24.032715], d=3)
        cmds.color(toe, rgb=(0.027, 0.188, 0.678))
        offset(toe) 
        if side == 'r':
            cmds.color(toe, rgb=(0.696,0.035,0.027))
        cmds.scale(0.429166, 0.429166, 0.429166, r=1)
        cmds.FreezeTransformations()

        
        
        
        
        flip('clavicleCtr_r_offset')
        flip('kneeFKCtr_r_offset')
        flip('hipFKCtr_r_offset')
        flip('footFKCtr_r_offset')
        flip('hipCtr_r_offset')
        flip('footIKCtr_r_offset')
        flip('handIKCtr_r_offset')
        flip('handFKCtr_r_offset')
        flip('shoulderFKCtr_r_offset')
        flip('elbowFKCtr_r_offset')
        
    if size != 1:
        cmds.group(em=True, n='controlScale')
        for i in controlList:
            cmds.parent(i, 'controlScale')
        for axis in 'xyz':
            cmds.setAttr('controlScale.s{}'.format(axis), size)
        cmds.makeIdentity('controlScale', apply=True, s=1, n=0)
    '''        
        for ctrl in controlList:
            ctrl = cmds.listRelatives(ctrl)[0]
            if ctrl[-5] == 'r':
                cmds.color(ctrl, rgb=(0.696,0.035,0.027))
            elif ctrl[-5] == 'l':
                cmds.color(ctrl, rgb=(0.027, 0.188, 0.678))
    '''        
        
    listBend = ['armUpBlend_l_ctr',  'armUpBlend_r_ctr', 'armMiddleBlend_r_ctr', 
                   'armMiddleBlend_l_ctr', 'armLowBlend_r_ctr', 'armLowBlend_l_ctr',
                   'legMiddleBlend_l_ctr', 'legLowBlend_l_ctr', 'legUpBlend_l_ctr', 
                   'legMiddleBlend_r_ctr', 'legLowBlend_r_ctr', 'legUpBlend_r_ctr']
    for ctrl in listBend:
        if ctrl[-5] == 'r':
            cmds.color(ctrl, rgb=(0.384,0.120,0.356))
        elif ctrl[-5] == 'l':
            cmds.color(ctrl, rgb=(0.091, 0.358, 0.358))
        
        
        
        
        