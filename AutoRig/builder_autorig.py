def builder():
    from maya import cmds
    from maya.api import OpenMaya
    import os
    import functools
    
    import AutoRig.GenerateLocators_Autorig as locators
    import AutoRig.GenerateControls_Autorig as controls
    
    import AutoRig.Hands_Autorig as hands
    import AutoRig.Spine_Autorig as spine 
    import AutoRig.Legs_Autorig as legs 
    import AutoRig.Arms_Autorig as arm
    
    
    import AutoRig.systemBrows_Autorig as brows
    import AutoRig.systemNose_Autorig as nose
    
    import AutoRig.triggers_Autorig as trigers
   
    import AutoRig.Functions_Autorig as fun
    reload(fun)
    import AutoRig.josieRename as re
    
    
    def UI(applySpine):
        def colorK(a, *pArgs):
            fun.colorKin(color=a)
        def changeTextFld1(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld1', edit=True, tx=selection)
        def changeTextFld2(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld2', edit=True, tx=selection) 
        def changeTextFld3(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld3', edit=True, tx=selection)     
        
        def changeTextFld4(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld4', edit=True, tx=selection)     
        
        def changeTextFld5(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld5', edit=True, tx=selection) 
        
        def changeTextFld6(*pArgs):
            selection = cmds.ls(sl=True)[0]
            cmds.textField('nameOfTexFld6', edit=True, tx=selection) 
        
        
        ventanaNombre = 'myWindowID'
        Titulo = 'Autorig Builder'
        Alto = 350
        Ancho = 500
        if cmds.window(ventanaNombre, exists=True):
            cmds.deleteUI(ventanaNombre)
        VENTANA = cmds.window(ventanaNombre, title='AutorigBuilder', width=Alto, height = Ancho)
        scrollLayout = cmds.scrollLayout()
        tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
        child1 = cmds.rowColumnLayout(numberOfColumns=3, columnOffset=[(1, 'right', 3) ] )
        
        cmds.text(label = 'Control Size:')
        pCtrScale= cmds.floatField(v=1)
        cmds.button(label='GenerateControls', command=functools.partial(applyControls, pCtrScale), w=100, h=20)
        cmds.text(label = 'Locators:')
        cmds.button(label='Generate Locators', command=functools.partial(allLocators), w=100, h=20)
        cmds.button(label='Quick Position', command=functools.partial(posLoc), w=100, h=20)
        
        cmds.text(label = 'Spine/Neck Number:')
        pSpineNum = cmds.intField(v=10)
        pNeckNum = cmds.intField(v=10)
    
        cmds.text(label = 'UP/LOW Arms Number:')
        pUpArmNum = cmds.intField(v=10)
        pLowArmNum = cmds.intField(v=10) 
    
        cmds.text(label = 'UP/LOW Leg Number:')
        pUpLegNum = cmds.intField(v=10) 
        pLowLegNum = cmds.intField(v=10) 
        cmds.button(label='CreateArm', command=functools.partial(applyArms, pUpArmNum, pLowArmNum), w=100, h=20) 
        cmds.button(label='CreateSpine', command=functools.partial(applySpine, pSpineNum, pNeckNum), w=100, h=20) 
        cmds.button(label='CreateLeg', command=functools.partial(applyLegs, pUpLegNum, pLowLegNum), w=100, h=20)
        
        
        cmds.checkBox( label='Hand', v=False, onc=handsTrue, ofc=handsFalse, h=20)

        
        
        cmds.separator(h=20, style=None)
        cmds.separator(h=20, style=None)
        
        
        cmds.text(label = 'Extract Weight(.xtm):')
        nameFile = cmds.textField()
       
        
        cmds.button(label='ExportWeights', command=functools.partial(getXtm, nameFile), w=100, h=20)
        
        cmds.separator(h=20, style=None)
        cmds.separator(h=20, style=None)
        cmds.separator(h=20, style=None)
        
        #cmds.button(label='Save Loc Positions', command=functools.partial(savePosition), w=100, h=20)
        #cmds.button(label='Save Skn List', command=functools.partial(saveJoints), w=100, h=20)
        
        
        cmds.separator(h=20, style=None)
        cmds.separator(h=20, style=None)
        cmds.separator(h=20, style=None)        
        
        cmds.button(label='Axis Up', command=axisUp, w=100, h=20) 
        cmds.separator(h=20, style=None)
        cmds.button(label='Axis Down', command=axisDown, w=100, h=20) 
        
        
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
       
        cmds.button(label='Select _skn', command=selectSkins, w=100, h=20) 
        cmds.button(label='Quick Skin', command=skinPlanes, w=100, h=20) 
        
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        
        cmds.button(label='Close Rig', command=closeRig, w=100, h=20)
        cmds.button(label='Open Rig', command=openRig, w=100, h=20)
        
        
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        cmds.text(label = 'Builder version 1.0', align='left')
        cmds.setParent( '..' )
        
        #Facial

        child2 = cmds.rowColumnLayout(numberOfColumns=3)
        
        cmds.text(label = 'Create Nurbs', align='right', bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        
        
        cmds.text(label = 'NumberU:')
        NumberU = cmds.intField(v=9)
        cmds.separator(h=35, style=None)
        cmds.text(label = 'NumberV:')
        NumberV = cmds.intField(v=1)
        cmds.separator(h=35, style=None)
        cmds.text(label = 'Name:')
        Name = cmds.textField() 
        cmds.separator(h=35, style=None)
        cmds.text(label = 'Side:')
        Side = cmds.textField()
        cmds.separator(h=35, style=None)
        
        cmds.text(label='moveX')
        cmds.text(label='moveY')
        cmds.text(label='moveZ')
        
        mX = cmds.floatField(v=0.0)
        mY = cmds.floatField(v=0.0)
        mZ = cmds.floatField(v=0.0)
        
        cmds.button(command=functools.partial(createNurbs, NumberU, NumberV, Side, Name, mX, mY, mZ), l='Create NURBS') 
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        
                        ####
        cmds.text(label = 'Control with Jnt', align='right', bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        
        cmds.text(label = 'Name:')
        nameCJC = cmds.textField() 
        cmds.separator(h=35, style=None)
        
        cmds.text(label = 'Side:')
        sideCJC = cmds.textField() 
        cmds.separator(h=35, style=None)
        
        cmds.text(label = 'ParentJnt')
        pjCJC = cmds.textField('nameOfTexFld2') 
        cmds.button(command=changeTextFld2, l='Select Parent') 
        
        cmds.text(label = 'ParentCtr')
        pcCJC = cmds.textField('nameOfTexFld1') 
        cmds.button(command=changeTextFld1, l='Select Parent')
        
        cmds.text(label = 'Function')
        jntUsageCJC = cmds.textField() 
        cmds.separator(h=35, style=None)
        
        cmds.button(command=functools.partial(createJntCtr, nameCJC, sideCJC, jntUsageCJC, pcCJC, pjCJC), l='Create JNT-CTR') 
        
        cmds.separator(h=35, style=None)
        cmds.separator(h=35, style=None)
        
        cmds.text(label = 'Facial Ribbon', align='right', bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))        
        
        cmds.text(label = 'Nurb:')
        name = cmds.textField('nameOfTexFld3') 
        cmds.button(command=changeTextFld3, l='Select Nurb')  
 
        cmds.text(label = 'Modulo:')
        sys = cmds.textField() 
        cmds.separator(h=35, style=None)
        
        cmds.button(command=functools.partial(ribbonizar, name, sys), l='Ribbonizacion')
        
        cmds.separator(h=20, style=None) 
        cmds.separator(h=20, style=None) 
        
        cmds.text(label = 'Create Reference Locators', align='right', bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        
        
        cmds.text(label = 'Quantity')
        Beet = cmds.intField(v=3)
        cmds.separator(h=35, style=None)
        
        cmds.text(label = 'Between Locs')
        Cuant = cmds.intField(v=2)
        cmds.separator(h=35, style=None)
    
        hasRef = cmds.checkBox(l= 'reflect', v=True)
        
        cmds.button(command=functools.partial(refLocs, Cuant, hasRef, Beet), l='Create Reference Loc')
        cmds.separator(h=35, style=None)
        
        
        
        
        
        cmds.text(label = 'Side Facial Ribbon', align='right', bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))
        cmds.separator(h=35, style=None, bgc=(0.4,0.4,1))        
        
        cmds.text(label = 'Side:')
        side = cmds.textField() 
        cmds.separator(h=35, style=None)
                
        cmds.text(label = 'Module:')
        system = cmds.textField() 
        cmds.separator(h=35, style=None)
        
        cmds.text(label = 'Nurb:')
        nurbs = cmds.textField('nameOfTexFld4') 
        cmds.button(command=changeTextFld4, l='Select Nurb')  

        
        cmds.button(command=functools.partial(ribbonizarSide, side, system, nurbs), l='Ribbonizacion Simetrica')
        
        cmds.separator(h=20, style=None) 
        cmds.separator(h=20, style=None)    
        
        
        
        
        
        
        
        
        cmds.text(label = 'Build In Modules', h=75, bgc=(1,0.4,0.4))
        cmds.separator(h=75, style=None, bgc=(1,0.4,0.4))
        cmds.separator(h=35, style=None, bgc=(1,0.4,0.4))
        
        
        cmds.text(label = 'Brows:')
        cmds.separator(h=20, style=None)
        cmds.button(label = 'setUp', command=browsSetUp, w=100, h=20)
        cmds.button(label = 'step1', command=brows2, w=100, h=20)
        cmds.text(label = 'Follicle Number', align='left')
        
        follNumber = cmds.intField(v=21)
        
        cmds.button(label = 'step2', command = functools.partial(brows3, follNumber))
        

        cmds.separator(h=20, style=None) 
        cmds.separator(h=20, style=None) 
        cmds.separator(h=20, style=None) 
        
        cmds.text(label = 'Nose:')
        cmds.separator(h=20, style=None)    
        
        cmds.button(label = 'SetUp', command=noseSetUp, w=100, h=20)
        cmds.separator(h=20, style=None) 
        cmds.text(label = 'Nose Skn Number', align='left')
        
        noseNumber = cmds.intField(v=5)
        
        cmds.button(label = 'Create Nose', command = functools.partial(nose2, noseNumber))        
        
        functools.partial(savePosition)
        cmds.setParent( '..' )
        
        #Utilities
        
        child3 = cmds.rowColumnLayout(numberOfColumns=3)
        
        cmds.text(label = 'Create Offset:')
        cmds.separator(h=20, style=None)
        cmds.button(label='Zero', command=zero, w=100, h=20)
        cmds.button(label='Flip', command=fliping, w=100, h=20)
        
        cmds.separator(h=20, style=None)
        
        cmds.button(label='Loc In Spot', command=locSpot, w=100, h=20)
        
        cmds.text(label = 'Selection1:', align='left')
        selection1 = cmds.button(label='Save Selection', command=sel1, w=100, h=20) 
        cmds.button(label='Select', command=call1, w=100, h=20) 
        


        cmds.text(label = 'Selection2:', align='left')
        selection1 = cmds.button(label='Save Selection', command=sel2, w=100, h=20) 
        cmds.button(label='Select', command=call2, w=100, h=20) 


        
        cmds.text(label = 'Selection3:', align='left')
        selection1 = cmds.button(label='Save Selection', command=sel3, w=100, h=20) 
        cmds.button(label='Select', command=call3, w=100, h=20) 
        

       
        cmds.text(label = 'Selection4:', align='left')
        selection1 = cmds.button(label='Save Selection', command=sel4, w=100, h=20) 
        cmds.button(label='Select', command=call4, w=100, h=20) 

        
        cmds.text(label = 'Selection5:', align='left')
        selection1 = cmds.button(label='Save Selection', command=sel5, w=100, h=20) 
        cmds.button(label='Select', command=call5, w=100, h=20) 
        
        
        azul = (0.696,0.035,0.027)
        rojo = (0.027, 0.188, 0.678)
        purpura = (0.384,0.120,0.356)
        azulClaro = (0.091, 0.358, 0.358)
        rojoClaro = (0.384,0.120,0.356)
        verde = (0.237,0.67,0)
        
        cmds.button(label='Colorear', command=functools.partial(colorK, azul), bgc = [0.696,0.035,0.027], w=100, h=20)
        cmds.button(label='Colorear', command=functools.partial(colorK, rojo), bgc = [0.027, 0.188, 0.678], w=100, h=20)
        cmds.button(label='Colorear', command=functools.partial(colorK, purpura), bgc = [0.384,0.120,0.356],w=100, h=20)
        cmds.button(label='Colorear', command=functools.partial(colorK, azulClaro), bgc = [0.091, 0.358, 0.358], w=100, h=20)
        cmds.button(label='Colorear', command=functools.partial(colorK, rojoClaro), bgc = [0.384,0.120,0.356], w=100, h=20)
        cmds.button(label='Colorear', command=functools.partial(colorK, verde), bgc = [0.237,0.67,0],w=100, h=20)
        
        cmds.button(label='Copy Shape', command=controlCopy, w=100, h=20)
        cmds.setParent('..')         
        
        child4 = cmds.rowColumnLayout(numberOfColumns=2)
        
        cmds.text(label = 'Search:', align='left')
        searching = cmds.textField()
        cmds.text(label = 'Replace:', align='left')
        replacing = cmds.textField()
        cmds.separator(h=35, style=None)
        cmds.button(label='Search and replace', command=functools.partial(sAr, searching, replacing), w=100, h=50) 
        

        cmds.text(label = 'Suffix:', align='left')
        suffinx = cmds.textField()
        cmds.separator(h=35, style=None)
        cmds.button(label='Add Suffix', command=functools.partial(sf, suffinx), w=200, h=50)
        

        cmds.text(label = 'Prefix:', align='left')
        prefix = cmds.textField()
        cmds.separator(h=35, style=None)
        cmds.button(label='Add Prefix', command=functools.partial(pr, prefix), w=100, h=50)        

        cmds.text(label = 'Rename:', align='left')
        renaming = cmds.textField()
        
        cmds.text(label = 'Start:', align='left')
        strr = cmds.intField(v=1)
       
        cmds.text(label = 'Padding:', align='left')
        pad = cmds.intField(v=0)
    
    
        cmds.separator(h=35, style=None)
        cmds.button(label='Rename', command=functools.partial(ren, renaming, strr, pad), w=100, h=50)  
       

        cmds.setParent('..')   
        
                #Triggers
        
        child5 = cmds.rowColumnLayout(numberOfColumns=3)
        
        cmds.text(label = 'System Name', align='right')
        system = cmds.textField()
        cmds.separator(style=None)
        
        cmds.text(label = 'Side', align='right')
        side = cmds.textField()
        cmds.separator(style=None)
        
        cmds.text(label = 'Direction', align='right')
        direction = cmds.textField()
        cmds.separator(style=None)
        
        cmds.text(label = 'Target/Pose Position', align='right')
        parPos = cmds.textField('nameOfTexFld5')
        cmds.button(command=changeTextFld5, l='Select Parent') 
        
        cmds.text(label = 'Base/Target Parent', align='right')
        tarPose = cmds.textField('nameOfTexFld6')
        cmds.button(command=changeTextFld6, l='Select Parent') 
        
        cmds.text(label = 'Base Position', align='right')
        basPos = cmds.textField()
        cmds.separator(style=None)
        
        cmds.button(label='Create Trigger', command=functools.partial(triggerCrr, system, side, direction, basPos, parPos, tarPose))
        
        cmds.setParent( '..' )
        
        cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Corporal'), (child2, 'Facial'), (child3, 'Utilities'), (child4, 'Rename'), (child5, 'Triggers')) )
        
        cmds.window(VENTANA, edit=True, width=Alto, height=Ancho)
        cmds.showWindow()
    
    ctrls = [u'armLowBlend_l_ctr',
         u'armLowBlend_r_ctr',
         u'armMiddleBlend_l_ctr',
         u'armMiddleBlend_r_ctr',
         u'armPole_l_ctr',
         u'armPole_r_ctr',
         u'armSettings_l_ctr',
         u'armSettings_r_ctr',
         u'armUpBlend_l_ctr',
         u'armUpBlend_r_ctr',
         u'center_c_ctr',
         u'chest_c_ctr',
         u'clavicle_l_ctr',
         u'clavicle_r_ctr',
         u'elbowFK_l_ctr',
         u'elbowFK_r_ctr',
         u'footFK_l_ctr',
         u'footFK_r_ctr',
         u'footIK_l_ctr',
         u'footIK_r_ctr',
         u'general_c_ctr',
         u'handFK_l_ctr',
         u'handFK_r_ctr',
         u'handIK_l_ctr',
         u'handIK_r_ctr',
         u'head_c_ctr',
         u'hipFK_l_ctr',
         u'hipFK_r_ctr',
         u'hip_l_ctr',
         u'hip_r_ctr',
         u'kneeFK_l_ctr',
         u'kneeFK_r_ctr',
         u'legLowBlend_l_ctr',
         u'legLowBlend_r_ctr',
         u'legMiddleBlend_l_ctr',
         u'legMiddleBlend_r_ctr',
         u'legPole_l_ctr',
         u'legPole_r_ctr',
         u'legSettings_l_ctr',
         u'legSettings_r_ctr',
         u'legUpBlend_l_ctr',
         u'legUpBlend_r_ctr',
         u'middleNeck_c_ctr',
         u'middleSpine_c_ctr',
         u'neck_c_ctr',
         u'pelvis_c_ctr',
         u'shoulderFK_l_ctr',
         u'shoulderFK_r_ctr',
         u'spineFK1_c_ctr',
         u'spineFK2_c_ctr',
         u'spineFK3_c_ctr',
         u'spineIK1_c_ctr',
         u'spineIK2_c_ctr',
         u'spineIK3_c_ctr',
         u'toe_l_ctr',
         u'toe_r_ctr',
         u'upperBody_c_ctr']
    
    
    clusters = [u'ClusterBlendSystem_Arm_r_DHandle',
              'spine_c_ikHandle',
              u'ClusterBlendSystem_Arm_r_EHandle',
              u'ClusterBlendSystem_Leg_l_BHandle',
              u'ClusterBlendSystem_Leg_l_AHandle',
              u'ClusterBlendSystem_Leg_l_EHandle',
              u'ClusterBlendSystem_Leg_l_DHandle',
              u'ClusterBlendSystem_Leg_r_AHandle',
              u'ClusterBlendSystem_Leg_r_BHandle',
              u'ClusterBlendSystem_Leg_r_EHandle',
              u'ClusterBlendSystem_Leg_r_DHandle',
              'cluster1Handle',
              'cluster2Handle',  
              u'cluster3Handle',
              u'cluster4Handle',
              u'ClusterBlendSystem_Arm_r_AHandle',
              u'ClusterBlendSystem_Arm_r_BHandle',
              u'ClusterBlendSystem_Arm_l_DHandle',
              u'ClusterBlendSystem_Arm_l_EHandle',
              u'ClusterBlendSystem_Arm_l_AHandle',
              u'ClusterBlendSystem_Arm_l_BHandle',
              u'ClusterBlendSystem_Arm_r_CHandle',
              u'ClusterBlendSystem_Arm_l_CHandle',
             'neck_cluster3Handle', 
             'neck_cluster2Handle',
             'neck_cluster1Handle',
             'ClusterBlendSystem_Leg_l_CHandle',
             'ClusterBlendSystem_Leg_r_CHandle']    
    
    
    
###################################################################################################################    
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []

    
    #JosieRename
    
    def sAr(a, b, *pArgs):
        searching = cmds.textField(a, q=True, text=True)
        replacing = cmds.textField(b, q=True, text=True)        
        re.searchAndReplace(sear=str(searching), rep=str(replacing))
    
        
        
    
    def pr(a, *pArgs):
        prefixing = cmds.textField(a, q=True, text=True)
        re.prefix(prefix=prefixing)
        
        
    def sf(a, *pArgs):
        suffinx = cmds.textField(a, q=True, text=True)
        re.suffix(suffix=suffinx)
        
    def sf(a, *pArgs):
        suffinx = cmds.textField(a, q=True, text=True)
        re.suffix(suffix=suffinx)        
   
    def ren(a,b,c,*pArgs):
        renaming = cmds.textField(a, q=True, text=True)
        strr = cmds.intField(b, q=True, v=True) 
        pad = cmds.intField(b, q=True, v=True) 
        re.renaming(name=renaming, start=strr, padding=pad)



    #BipedRigging

    def allLocators(*pArgs):
        locators.createSpineLocators() 
        locators.createLegLocators() 
        locators.createArmLocators() 
        locators.createFootLocators()    
        cmds.select(cl=True)
    def applySpine(a, b, *pArgs):
        neckNum = cmds.intField(a, q=True, v=True)
        spineNum = cmds.intField(b, q=True, v=True)        
        spine.createSpine(spineJnts=spineNum, neckJnts=neckNum)
    
        cmds.select(cl=True)
        
    def applyArms(a, b, *pArgs):
        pUpArmNum = cmds.intField(a, q=True, v=True)
        pLowArmNum = cmds.intField(b, q=True, v=True)        
        arm.createArm(uparmJnts=pUpArmNum, lowarmJnts=pLowArmNum)
        cmds.select(cl=True)
        try:
            check = cmds.getAttr('handA01_l_loc.handIs')
            if check == 1:
                hands.createFingers()
            else:
                pass
        except:
            print("An exception occurred")    
    def axisUp(*pArgs):
        joints = cmds.ls(type='joint')

        for jnt in joints:
            cmds.setAttr('{}.displayLocalAxis'.format(jnt), 1)
        
    
    def axisDown(*pArgs):
        joints = cmds.ls(type='joint')

        for jnt in joints:
            cmds.setAttr('{}.displayLocalAxis'.format(jnt), 0)    
    
    
    def applyLegs(a, b, *pArgs):
        pUpLegNum = cmds.intField(a, q=True, v=True)
        pLowLegNum = cmds.intField(b, q=True, v=True)        
        legs.createLeg(uplegJnts=pUpLegNum, lowlegJnts=pLowLegNum)
        cmds.select(cl=True)
    def applyControls(a,*pArgs):
        ctrScale = cmds.floatField(a, q=True, v=True)
        controls.createControls(ctrScale)
        cmds.select(cl=True)
    def posLoc(*pArgs):
        locators.quickPos()
        cmds.select(cl=True)
    def sel1(*pArgs):
        if len(list1) > 0:
            del list1[:]  
        sel1 = cmds.ls(sl=True)        
        for i in sel1:
            list1.append(i)
        
    def call1(*pArgs):
        for i in list1:
            cmds.select(i, add=True)            
        
        
    def sel4(*pArgs):
        if len(list4) > 0:
            del list4[:]  
        sel4 = cmds.ls(sl=True)        
        for i in sel4:
            list4.append(i)
        
    def call4(*pArgs):
        for i in list4:
            cmds.select(i, add=True)   
        
        
        
    def sel3(*pArgs):
        if len(list3) > 0:
            del list3[:]  
        sel3 = cmds.ls(sl=True)        
        for i in sel3:
            list3.append(i)
        
    def call3(*pArgs):
        for i in list3:
            cmds.select(i, add=True)   
            
            
    def sel2(*pArgs):
        if len(list2) > 0:
            del list2[:]  
        sel2 = cmds.ls(sl=True)        
        for i in sel2:
            list2.append(i)
        
    def call2(*pArgs):
        for i in list2:
            cmds.select(i, add=True)               
            
            
        
        
    def sel5(*pArgs):
        if len(list5) > 0:
            del list5[:]  
        sel5 = cmds.ls(sl=True)        
        for i in sel5:
            list5.append(i)
        
    def call5(*pArgs):
        for i in list5:
            cmds.select(i, add=True)               
                    
        
        
        
        
        
    def getXtm(nameFile, *pArgs):
        geo = cmds.ls(sl=True)[0]
        geo = cmds.listRelatives(geo)
        for i in geo:
            if 'Orig' in i:
                pass
            elif 'Shape' in i:
                shape=i
            else:
                pass

        cmds.objectType('skinCluster1') 
        connections = cmds.listConnections(shape)
        for c in connections:
            if cmds.objectType(c) == 'skinCluster':
                skin = c
            else:
                pass
        cmds.deformerWeights('{}.xtm'.format(nameFile), export=True, deformer = skin)     
    

    def saveJoints(*pArgs):
        geo = cmds.ls(sl=True)[0]
        geo = cmds.listRelatives(geo)
        for i in geo:
            if 'Orig' in i:
                pass
            elif 'Shape' in i:
                shape=i
            else:
                pass

        cmds.objectType('skinCluster1') 
        connections = cmds.listConnections(shape)
        for c in connections:
            if cmds.objectType(c) == 'skinCluster':
                skin = c
            else:
                pass
        roll = cmds.listConnections('{}.matrix'.format(skin))    
        
        print roll
        pathAutorig = os.path.expanduser("~Documents/maya/2018/scripts/AutoRig/builderData.py")
        pathAutorig= pathAutorig.replace('\\', '/')
        builderNotes=open(pathAutorig, 'a+')
        builderNotes.write('jointsList =')
        builderNotes.write(str(roll))
        builderNotes.close()
        return roll

    def selectSkins(*pArgs):
        size=10
        nodes = cmds.ls(et='joint')
        jntList = ['foot_r_jnt', 'ball_r_jnt', 'foot_l_jnt', 'ball_l_jnt']
        for jnt in nodes:
            if '_skn' in jnt:
                jntList.append(jnt)
        for jnt in jntList:
            cmds.select(jnt, add=True)



    def skinPlanes(*pArgs):
        size=10
        nodes = cmds.ls(et='joint')
        jntList = ['foot_r_jnt', 'ball_r_jnt', 'foot_l_jnt', 'ball_l_jnt']
        for jnt in nodes:
            if '_skn' in jnt:
                jntList.append(jnt)

        selected_joints = jntList
        cmds.group(n='skinPlane_c_grp', em=True)
        for jnt in selected_joints:
            grp = 'skinPlane_c_grp'
            if '_jnt' in jnt:
                skin_plane = cmds.polyPlane(name=jnt.replace("_jnt","_skinPlane"),ch=False,w=size,h=size,ax=(1,0,0),sx=5,sy=5)[0]
            else:    
                skin_plane = cmds.polyPlane(name=jnt.replace("_skn","_skinPlane"),ch=False,w=size,h=size,ax=(1,0,0),sx=5,sy=5)[0]
            jnt_matrix =cmds.xform(jnt,worldSpace=True, q=True, matrix=True,absolute=True)
            cmds.xform (skin_plane, worldSpace=True,absolute=True, matrix=jnt_matrix)
            cmds.skinCluster([jnt],skin_plane,toSelectedBones=1,maximumInfluences=40,ignoreBindPose=1)
            cmds.parent(skin_plane, grp)
        cmds.select(cl=True)
    
    
    def savePosition(*pArgs):
        locatorsList=[u'spineEND_loc_c_autorig', u'spine_loc_c_autorig', u'neckEND_loc_c_autorig', u'neck_loc_c_autorig', u'head_loc_END_autorig', u'clavicle_l_loc_END_autoRig', u'clavicle_l_loc_autoRig', u'toe_loc_l_autorig', u'endFoot_loc_l_autorig', u'ball_loc_l_autorig', u'foot_loc_l_autorig', u'knee_loc_l_autorig', u'hip_loc_l_autorig', u'lowerArm_l_loc_autoRig', u'hand_loc_autoRig', 'bankExt_l_pivot', 'bankInt_l_pivot', 'heel_l_pivot', 'toe_l_pivot', 'ball_l_pivot', 'ankle_l_pcon']

        locatorsDict={}
        for loc in locatorsList:
            trans = cmds.getAttr('{}.t'.format(loc))
            locatorsDict.update({loc : trans})
        
        print locatorsDict
        pathAutorig = os.path.expanduser("~Documents/maya/2018/scripts/AutoRig/builderData.py")
        pathAutorig= pathAutorig.replace('\\', '/')
        builderNotes=open(pathAutorig, 'a+')
        builderNotes.write('locatorsDict =')
        builderNotes.write(str(locatorsDict))
        builderNotes.close()
        return locatorsDict
    def setSavedPositions(*pArgs):
        c=0
        for i in list:
            key = locatorsDict.keys()[c]
            pos = locatorsDict[key][0]
            cmds.setAttr('{}.t'.format(key), pos[0], pos[1], pos[2])
            c = c + 1  
    def closeRig(*pArgs):
        joints = cmds.ls(type='joint')
        handle = cmds.ls(type='ikHandle')
        transform = cmds.ls(type='transform')


        for j in joints:
            cmds.setAttr('{}.drawStyle'.format(j), 2)

        for t in transform:
            if '_curve' in t:
                cmds.setAttr('{}.visibility'.format(t), 0)

        for h in handle:
            cmds.setAttr('{}.visibility'.format(h), 0)
     
        for cc in clusters:
            cmds.setAttr('{}.visibility'.format(cc), 0)    

        for c in ctrls:
            cmds.setAttr('{}.visibility'.format(c), lock=True, keyable=False, channelBox=False)
            for axis in 'xyz':
                cmds.setAttr('{}.s{}'.format(c, axis), lock=True, keyable=False, channelBox=False)
            if 'FK' in c:
                for axis in 'xyz':
                    cmds.setAttr('{}.t{}'.format(c, axis), lock=True, keyable=False, channelBox=False)
                    
                    
    def openRig(*pArgs):
        joints = cmds.ls(type='joint')
        handle = cmds.ls(type='ikHandle')
        transform = cmds.ls(type='transform')


        for j in joints:
            cmds.setAttr('{}.drawStyle'.format(j), 0)

        for t in transform:
            if '_curve' in t:
                cmds.setAttr('{}.visibility'.format(t), 1)
            elif '_loc' in t:
                cmds.setAttr('{}.visibility'.format(t), 1)
                

        for h in handle:
            cmds.setAttr('{}.visibility'.format(h), 1)
     
            
        for cc in clusters:
            cmds.setAttr('{}.visibility'.format(cc), 1)    

        for c in ctrls:
            cmds.setAttr('{}.visibility'.format(c), lock=True, keyable=True, channelBox=True)
            for axis in 'xyz':
                cmds.setAttr('{}.s{}'.format(c, axis), lock=True, keyable=True, channelBox=True)
            if 'FK' in c:
                for axis in 'xyz':
                    cmds.setAttr('{}.t{}'.format(c, axis), lock=True, keyable=True, channelBox=True)                    
                    
    #FacialRigging
    def browsSetUp(*pArgs):
        brows.setUpBrows()
        
    def locSpot(*pArgs):
        fun.locOnSpot()
    def brows2(*pArgs):
        brows.set2Brows()
    def brows3(a, *pArgs):
        follNumber = cmds.intField(a, q=True, v=True)
        brows.set3Brows(follNumber)
    def noseSetUp(*pArgs):
        nose.setUpNose()
    def nose2(a, *pArgs):
        noseNumber = cmds.intField(a, q=True, v=True)
        nose.closeNose(noseNumber)   
    def createNurbs(a, b, c, d, e, f, g, *pArgs):
        NumberU = cmds.intField(a, q=True, v=True)
        NumberV = cmds.intField(b, q=True, v=True)
        Name = cmds.textField(c, q=True, text=True) 
        Side = cmds.textField(d, q=True, text=True)
        mX = cmds.floatField(e, q=True, v=True)
        mY = cmds.floatField(f, q=True, v=True)
        mZ = cmds.floatField(g, q=True, v=True)
        
        
        
        fun.createNurb(NumberU, NumberV, Name, Side, mX, mY, mZ) 
    def ribbonizar(a,b,*pArgs):
        name = cmds.textField(a, q=True, text=True)
        system = cmds.textField(b, q=True, text=True) 
        fun.makeRibbon(name,system)
        
        
    def ribbonizarSide(a,b,c,*pArgs):
        side = cmds.textField(a, q=True, text=True)
        system = cmds.textField(b, q=True, text=True)
        nurbs = cmds.textField(c, q=True, text=True)
        fun.folliclesSides(side = side, system_name=system, nurbs=nurbs)    
    def refLocs(a,b,c,*pArgs):
        Beet = cmds.intField(a, q=True, v=True)
        hasRef = cmds.checkBox(b, v=True, q=True)
        Cuant = cmds.intField(c, q=True, v=True)
        fun.referenceLocators(cuantity = Cuant, reflection = hasRef, between = Beet)
    def createJntCtr(a,b,c,d,e,*pArgs):
        nameCJC = cmds.textField(a, q=True, text=True)
        sideCJC = cmds.textField(b, q=True, text=True)
        jntUsageCJC = cmds.textField(c, q=True, text=True)
        selected = cmds.ls(sl=True)[0]
        cpCJC = cmds.textField(d, q=True, text=True)
        jpCJC = cmds.textField(e, q=True, text=True)
        fun.createControlJoint(control_name = nameCJC,
                               side = sideCJC,
                               jnt_usage = jntUsageCJC,
                               position_loc = selected,
                               ctr_parent_to = cpCJC,
                               jnt_parent_to = jpCJC)
    
        
        
    #Trigger    
    def triggerCrr(a, b, c, d, e, f, *pArgs):
        system = cmds.textField(a, q=True, text=True)
        side = cmds.textField(b, q=True, text=True)
        direction = cmds.textField(c, q=True, text=True)
        posTar=cmds.textField(d, q=True, text=True)
        tarPar = cmds.textField(e, q=True, text=True)
        posPar = cmds.textField(f, q=True, text=True)
        trigers.triggerCrr(system, side, direction, posTar, posPar, tarPar) 
        
    #Extra
    def controlCopy(*pArgs):
        fun.copyShape()
    def handsFalse(*pArgs):
        try:
            cmds.setAttr('handA01_l_loc.handIs', 0)
        except:
            print 'Generate the locators first'
    def handsTrue(*pArgs):
        try:
            cmds.setAttr('handA01_l_loc.handIs', 1)
        except:
            print 'Generate the locators first'
    def restorePosition(*pArgs):
        reload(data)
        data.restorePose()
    
    def fliping(*pArgs):
        objects = cmds.ls(sl=True)
        for object in objects:
            fun.duplicateFlip(element=object, descendent=True, side = 'r', dad=None, axis= 'x')
    def zero(*pArgs):
        list = cmds.ls(sl=True)

        for element in list:
            if '_ctr' in element:
                first = '{}Ctr'.format(element.split('_')[0])
                second = element.split('_')[1]
                name = '{}_{}_zero'.format(first, second)
            else:     
                name = '{}_zero'.format(element)
            dad = cmds.listRelatives(element, c=False, p=True)   
            zero = cmds.group(em=True, n=name)
            pos = cmds.xform(element, m=True, q=True, ws=True)
            cmds.xform(zero, m=pos, ws=True)
            cmds.parent(element, zero)
            if dad:
                cmds.parent(zero, dad[0])   
            else:
                pass 

    UI(applySpine)
