#FUNCIONES
from maya import cmds
from maya.api import OpenMaya
def twoInfluencesConstraint(controler, constraint, reverse = False):  #FUNCION QUE CONECTA LAS DOBLES INFLUENCIAS DE UN CONSTRAINT AL CONTROL QUE LO GESTIONA
    name = controler.split('.')[1]
    side = controler.split('_')[1]
    name_reverse = '{}_{}_rev'.format(name,side)
    rever = cmds.shadingNode('reverse', n=name_reverse, au=True)
    cmds.connectAttr(controler, '{}.inputX'.format(rever))

    looking = cmds.listAttr(constraint)

    for attr in looking:
        if 'W0' == attr[-2::]:
            W0 = attr
        elif 'W1' == attr[-2::]:
            W1 = attr  
    if reverse == False:
        cmds.connectAttr('{}.outputX'.format(rever), '{}.{}'.format(constraint, W0))
        cmds.connectAttr(controler, '{}.{}'.format(constraint, W1))
    else: 
        cmds.connectAttr('{}.outputX'.format(rever), '{}.{}'.format(constraint, W1))
        cmds.connectAttr(controler, '{}.{}'.format(constraint, W0))


def locCreator(name='locator', position=None, dad = None):

    loc = cmds.spaceLocator(n=name)[0]

    if position == None:
        pass
    else: 
        locator_pos = cmds.xform(position, ws=True, t=True, q=True)
        cmds.xform(loc, t=locator_pos, ws=True)

    if dad != None:
        cmds.parent(loc, dad)
    else:
        pass
    return '{}Shape'.format(loc) 




#Formato Rapido de Creacion de Nofos
def clampCreator(name = 'clampNode', MaxG = 0, MaxR = 0, MaxB = 0, 
                                     MinG = 0, MinR = 0, MinB = 0, 
                                     InputR = None, InputG = None, InputB = None):

    clp = cmds.shadingNode('clamp', au=True, n=name)
    clamp_dic = {'maxG':MaxG, 
                 'maxR':MaxR,
                 'maxB':MaxB,
                 'minG':MinG,
                 'minR': MinR,
                 'minB': MinB,
                 'inputR': InputR,
                 'inputG': InputG,
                 'inputB': InputB}
    for element in clamp_dic:
        input = clamp_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(clp, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(clp, element), input)
        else:
            pass
    return clp

def multiplyCreator(name = 'multiplyNode', linear = True, 
                    Input1 = 1, Input2 = 1, 
                    Input1X = 0, Input1Y = 0, Input1Z = 0,
                    Input2X = 0, Input2Y = 0, Input2Z = 0,
                    Output = None):

    mult_dic = {'input1':Input1,
                'input2':Input2,
                'input1X':Input1X,
                'input1Y':Input1Y,
                'input1Z':Input1Z,
                'input2X':Input2X,
                'input2Y':Input2Y,
                'input2Z':Input2Z}

    if linear == True:
        del mult_dic['input1X']
        del mult_dic['input1Y']
        del mult_dic['input1Z']
        del mult_dic['input2X']
        del mult_dic['input2Y']
        del mult_dic['input2Z']
        mult = cmds.shadingNode('multDoubleLinear', n=name, au=True)
    else:
        mult = cmds.shadingNode('multiplyDivide', n=name, au=True)
        del mult_dic['input1']
        del mult_dic['input2']

    for element in mult_dic:
        input = mult_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(mult, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(mult, element), input) 
        elif isinstance(input, float) == True:
            cmds.setAttr('{}.{}'.format(mult, element), input)     
        else:
            pass

    if Output != None:
        cmds.connectAttr('{}.output'.format(mult), Output)
    else:
        pass
    return mult 




def divideCreator(name=None, Input1X = 1, Input1Y = 1, Input1Z = 1, 
                  Input2X = 1, Input2Y = 1, Input2Z = 1, 
                  Extraction1X = False, Extraction1Y = False, Extraction1Z = False,
                  Extraction2X = False, Extraction2Y = False, Extraction2Z = False,
                  OutputX = None, OutputY = None, OutputZ = None):

    extract_list = [[Extraction1X, 'input1X'],[Extraction1Y, 'input1Y'],[Extraction1Z, 'input1Z'],
                   [Extraction2X, 'input2X'],[Extraction2Y, 'input2Y'],[Extraction2Z, 'input2Z']]

    div_dic = {'input1X':Input1X,
                'input1Y':Input1Y,
                'input1Z':Input1Z,
                'input2X':Input2X,
                'input2Y':Input2Y,
                'input2Z':Input2Z}

    div = cmds.shadingNode('multiplyDivide', n=name, au=True)

    cmds.setAttr('{}.operation'.format(div), 2)

    for element in extract_list:
        if element[0] == True:
            number = cmds.getAttr(div_dic.get(element[1]))
            del div_dic[element[1]]
            cmds.setAttr('{}.{}'.format(div, element[1]), number)    
        else:
            pass

    for element in div_dic:
        input = div_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(div, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(div, element), input) 
        elif isinstance(input, float) == True:
            cmds.setAttr('{}.{}'.format(div, element), input)     
        else:
            pass
    div_dic_outs = {'outputX':OutputX,
                    'outputY':OutputY,
                    'outputZ':OutputZ}

    for outs in div_dic_outs:
        output = div_dic_outs.get(outs)
        if isinstance(output, str) == True:
            cmds.connectAttr('{}.{}'.format(div, output), outs)
        else:
            pass
    return div


def substractCreator(name=None, InputX0 = 0, InputX1= 0, InputX2 = 0, 
                     InputY0 = 0, InputY1 = 0, InputY2 = 0, 
                     OutputX = None, OutputY = None):

    subs_dic = {'input2D[0].input2Dx':InputX0,
                'input2D[1].input2Dx':InputX1,
                'input2D[2].input2Dx':InputX2,
                'input2D[0].input2Dy':InputY0,
                'input2D[1].input2Dy':InputY1,
                'input2D[2].input2Dy':InputY2}

    subs = cmds.shadingNode('plusMinusAverage', n=name, au=True)
    cmds.setAttr('{}.operation'.format(subs), 2)
    for element in subs_dic:
        input = subs_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(subs, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(subs, element), input)
    if isinstance(OutputX, str) == True:
        cmds.connectAttr('{}.output2D.output2Dx'.format(subs), OutputX)
    else:
        pass
    if isinstance(OutputY, str) == True:
        cmds.connectAttr('{}.output2D.output2Dy'.format(subs), OutputY)
    else:
        pass
    return subs

def plusCreator(name=None, InputX0 = 0, InputX1= 0, InputX2 = 0, 
                     InputY0 = 0, InputY1 = 0, InputY2 = 0, 
                     OutputX = None, OutputY = None):

    plus_dic = {'input2D[0].input2Dx':InputX0,
                'input2D[1].input2Dx':InputX1,
                'input2D[2].input2Dx':InputX2,
                'input2D[0].input2Dy':InputY0,
                'input2D[1].input2Dy':InputY1,
                'input2D[2].input2Dy':InputY2}

    plus = cmds.shadingNode('plusMinusAverage', n=name, au=True)
    for element in plus_dic:
        input = plus_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(plus, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(plus, element), input)
    if isinstance(OutputX, str) == True:
        cmds.connectAttr('{}.output2D.output2Dx'.format(plus), OutputX)
    else:
        pass
    if isinstance(OutputY, str) == True:
        cmds.connectAttr('{}.output2D.output2Dy'.format(plus), OutputY)
    else:
        pass
    return plus

def distanceCreator(name = None, Input1 = None, Input2 = None):
    if name == None:
        name = '{}_{}_distanceBetween'.format(Input1.split('_')[0], Input1.split('_')[1])
    else:
        pass

    dB = cmds.shadingNode('distanceBetween', n=name, au=True)
    if Input1 != None:
        cmds.connectAttr(Input1, '{}.point1'.format(dB))
    else:
        pass
    if Input1 != None:
        cmds.connectAttr(Input2, '{}.point2'.format(dB))
    else:
        pass
    return dB


def blendColorsCreator(Name = 'blendColor', Blender = None, Color1R = None, Color1G = None, Color1B = None, 
                       Color2R = None, Color2G = None, Color2B = None):

    blend_dic = {'blender':Blender,
                'color1R':Color1R,
                'color1G':Color1G,
                'color1B':Color1B,
                'color2R':Color2R,
                'color2G':Color2G,
                'color2B':Color2B}
    blen = cmds.shadingNode('blendColors', au=True, n=Name)
    for element in blend_dic:
        input = blend_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(blen, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(blen, element), input)
        else:
            pass       
    return blen    

def curveInfoCreator(Name = 'curveInfo', Input = None, Length = None, Output = None):
    iC = cmds.shadingNode('curveInfo', n=Name, au=True)    
    cmds.connectAttr(Input, '{}.inputCurve'.format(iC))  
    arcLength = cmds.getAttr('{}.arcLength'.format(iC)) 
    if Length:
        cmds.setAttr(Length, arcLength)
    else:
        pass
    if Output != None:
        cmds.connectAttr('{}.arcLength'.format(iC), Output)  
    else:
        pass
    return iC
#Blend function

def clusterCreator(Name = 'None', CV1 = None, CV2 = None, Double = False):
    cmds.select(CV1)
    if Double == True:
        cmds.select(CV2, add=True)

    clust = cmds.cluster(n=Name)

    cmds.select(cl=True)

    return clust



def blendSystem(CurveU = None, CurveL = None, ClusterName = 'ClusterBlendSystem', 
                upJnt = None, middleJnt = None,
                upBlend = None, middleBlend = None, lowBlend = None):
    
    upName=upBlend[:-6]
    lowName = lowBlend[:-6]
    midName = middleBlend[:-6]
    side= upBlend[-5]
   
    upOff = '{}Ctr_{}_offset'.format(upName, side) 
    midOff= '{}Ctr_{}_offset'.format(midName, side) 
    lowOff = '{}Ctr_{}_offset'.format(lowName, side) 
    
    
    
    CV0U = ['{}.cv[0]'.format(CurveU)]
    CV1U = ['{}.cv[1]'.format(CurveU)]
    CV2U = ['{}.cv[2]'.format(CurveU)]
    CV3U = ['{}.cv[3]'.format(CurveU)]
    CV0L = ['{}.cv[0]'.format(CurveL)]
    CV1L = ['{}.cv[1]'.format(CurveL)]
    CV2L = ['{}.cv[2]'.format(CurveL)]
    CV3L = ['{}.cv[3]'.format(CurveL)]

    A = clusterCreator(
        Name='{}A'.format(ClusterName),
        CV1 = CV0U)
    cmds.parent(A, upJnt)


    B = clusterCreator(
        Name = '{}B'.format(ClusterName),
        Double = True, 
        CV1 = CV1U,
        CV2 = CV2U)
    clusterMatrix = cmds.xform(B, q=1, ws=1, rp=1)
    cmds.xform(upOff, t=clusterMatrix, ws=True)
    cmds.parent(B, upBlend)
    cmds.parent(upOff, upJnt)

    C = clusterCreator(
        Name='{}C'.format(ClusterName),
        Double = True, 
        CV1 = CV3U,
        CV2 = CV0L)
    clusterMatrix = cmds.xform(C, q=1, ws=1, rp=1)
    cmds.xform(midOff, t=clusterMatrix, ws=True)
    cmds.parent(C, middleBlend)
    cmds.parentConstraint(upJnt, middleJnt, midOff, mo=True)


    D = clusterCreator(
        Name='{}D'.format(ClusterName),
        Double = True, 
        CV1 = CV1L,
        CV2 = CV2L)

    clusterMatrix = cmds.xform(D, q=1, ws=1, rp=1)
    cmds.xform(lowOff, t=clusterMatrix, ws=True)
    cmds.parent(D, lowBlend)
    cmds.parent(lowOff, middleJnt)

    E = clusterCreator(
        Name='{}E'.format(ClusterName),
        CV1 = CV3L)
    cmds.parent(E, middleJnt)

def chainJoint(cantidad, nombre, lado, chin, radio, ini, fin):

   
    inicio = '{}_loc_{}_autorig'.format(ini, lado)
    fin = '{}_loc_{}_autorig'.format(fin, lado)
    start_point = cmds.xform(inicio, q=True, t=True, ws=True)
    end_point = cmds.xform(fin, q=True, t=True, ws=True)
    vector_sta = OpenMaya.MVector(start_point)
    vector_end = OpenMaya.MVector(end_point)
    i = 0
    all_joints = []
    for num in range(cantidad):
        name = '{}{}_{}_skn'.format(nombre, i, lado)
        nameEnd = '{}{}_{}_End'.format(nombre, i, lado)
        dif_point = vector_end-vector_sta
        offset = 1.0/(cantidad-1)
        new_point=dif_point*offset
        final_point = vector_sta + new_point   
        mid_pos=dif_point*(offset*num)
        final_pos=vector_sta+mid_pos
        jnt=cmds.joint(n=name, p=list(final_pos), rad=radio)
        all_joints.append(jnt)
        if i != 0:
            cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup', rad=radio)  
        i += 1
        
        if chin==False:
            cmds.select(cl=1)
        if i == cantidad:
            jnt = cmds.rename(jnt, nameEnd)
            all_joints[-1] = jnt
            break
           
    return all_joints
    
def posToControl(offset, part = None, X = None, Y = None, Z = None):
    if part == None:
        part = offset.split('_')[0]
    lado = offset.split('_')[1]
    jnt_pos = '{}_{}_jnt'.format(part, lado)
    cmds.parent(offset, jnt_pos)
    cmds.setAttr('{}.rx'.format(offset), X)
    cmds.setAttr('{}.ry'.format(offset), Y)
    cmds.setAttr('{}.rz'.format(offset), Z)
    for axis in 'xyz':
        cmds.setAttr('{}.t{}'.format(offset, axis), 0)
    cmds.parent(offset, 'general_c_ctr')

def poleLocation():
    from maya import cmds , OpenMaya
    import math
    for side in 'rl':

        start = cmds.xform('hip_{}_jnt'.format(side) ,q= 1 ,ws = 1,t =1 )
        mid = cmds.xform('knee_{}_jnt'.format(side) ,q= 1 ,ws = 1,t =1 )
        end = cmds.xform('legEnd_{}_jnt'.format(side) ,q= 1 ,ws = 1,t =1 )

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

        loc = 'legPoleCtr_{}_offset'.format(side)
        cmds.xform(loc , ws =1 , t= (finalV.x , finalV.y ,finalV.z))

        cmds.xform ( loc , ws = 1 , rotation = ((rot.x/math.pi*180.0),
        (rot.y/math.pi*180.0),
        (rot.z/math.pi*180.0)))
        
        
        
        
        
############################################FACIAL FUNCTIONS AUTORIG####################################################


def chainJointFacial(cantidad, nombre, chin, ini, fin):

   
    inicio = ini
    fin = fin
    start_point = cmds.xform(inicio, q=True, t=True, ws=True)
    end_point = cmds.xform(fin, q=True, t=True, ws=True)
    vector_sta = OpenMaya.MVector(start_point)
    vector_end = OpenMaya.MVector(end_point)
    i = 0
    all_joints = []
    for num in range(cantidad):
        name = '{}{}_c_skn'.format(nombre, i)
        nameEnd = '{}{}_c_End'.format(nombre, i)
        dif_point = vector_end-vector_sta
        offset = 1.0/(cantidad-1)
        new_point=dif_point*offset
        final_point = vector_sta + new_point   
        mid_pos=dif_point*(offset*num)
        final_pos=vector_sta+mid_pos
        jnt=cmds.joint(n=name, p=list(final_pos))
        all_joints.append(jnt)
        if i != 0:
            cmds.joint(all_joints[i-1],e=True,zso=True,oj='xyz',sao='yup')  
        i += 1
        
        if chin==False:
            cmds.select(cl=1)
        if i == cantidad:
            jnt = cmds.rename(jnt, nameEnd)
            all_joints[-1] = jnt
            break
           
    return all_joints


def createControlJoint(control_name = None,
                       side = None,
                       jnt_usage = 'skn',
                       position_loc = None,
                       ctr_parent_to = None,
                       jnt_parent_to = None):


    
    #Crear hueso
    jnt_name = '{}_{}_{}'.format(control_name, side, jnt_usage)
    jnt = cmds.createNode('joint', n= jnt_name)
    jnt_zero_name = '{}{}_{}_zero'.format(control_name, jnt_usage.capitalize(), side)
    jnt_zero = cmds.createNode('transform', n=jnt_zero_name)
    cmds.parent(jnt, jnt_zero)[0]
    
    #Crear control
    ctr_name = '{}_{}_ctr'.format(control_name, side)
    ctr = cmds.circle(name= ctr_name, constructionHistory=False)
    ctr_zero_name = '{}Ctr_{}_zero'.format(control_name, side)
    ctr_zero = cmds.createNode('transform', name=ctr_zero_name)
    cmds.parent(ctr, ctr_zero)[0]
    
    #Engarzar Control y Hueso
    for attr in 'trs':
        for axis in 'xyz':
            cmds.connectAttr('{}.{}{}'.format(ctr[0], attr, axis),
                             '{}.{}{}'.format(jnt, attr, axis),
                             force = True)
                             
    #Reposicionar zero
    position_loc_matrix = cmds.xform(position_loc, query=True, matrix=True, worldSpace=True)
    cmds.xform(jnt_zero, matrix=position_loc_matrix)
    cmds.xform(ctr_zero, matrix=position_loc_matrix)
    
    #Parent elements
    if ctr_parent_to:
        ctr_zero = cmds.parent(ctr_zero, ctr_parent_to)[0] 
    if jnt_parent_to:
        jnt_zero = cmds.parent(jnt_zero, jnt_parent_to)[0] 
    return [ctr_zero, jnt_zero, ctr[0], jnt]    



def createHold(n=None, side=None, skin = 'skn'):
    
    zeroName = 'facial{}Hold{}_{}_zero'.format(n, skin.capitalize(), side)
    holdName = 'facial{}Hold_{}_{}'.format(n, side, skin)
    grp = cmds.group(em=True, n=zeroName)
    jnt = cmds.joint(n=holdName)
    return grp

def duplicateFlip(element=None, descendent=True, side = 'r', dad=None, axis= 'x'):
    null = cmds.group(em=True)
    first = element.split('_')[0]
    third = element.split('_')[2]
    name = '{}_{}_{}'.format(first, side, third)
    duplic = cmds.duplicate(element, name, rc=True)
    duplic = cmds.rename(duplic[0], name)
    if descendent == True:
        relatives = cmds.listRelatives(duplic)
        for relative in relatives:
            first = relative.split('_')[0]
            third = relative.split('_')[2]
            third = third.replace(third[-1], '')
            name = '{}_{}_{}'.format(first, side, third)  
            cmds.rename(relative, name)
    cmds.parent(duplic, null)
    cmds.setAttr('{}.s{}'.format(null, axis), -1)
    
    if dad:
        cmds.parent(duplic, dad)
    else:
        cmds.parent(duplic, w=True)
    
    cmds.delete(null)
    result = cmds.listRelatives(duplic, ad=True, s=False)
    return result
        
def conElement(source=None, subject = None):
    for attr in 'trs':
        for axis in 'xyz':
            cmds.connectAttr('{}.{}{}'.format(source, attr, axis),
                             '{}.{}{}'.format(subject, attr, axis),
                             force = True)
        
        
def createNurb(uNumber=5, vNumber=5, side=None, name=None, mX=0, mY=0, mZ=0):
    name= '{}_{}_nurb'.format(name, side)
    
    try:
        crv = cmds.polyToCurve(n='deletableCurve', form=2, degree=3, conformToSmoothMeshPreview=1)[0]

        degs = cmds.getAttr( '{}.degree'.format(crv) )
        spans = cmds.getAttr( '{}.spans'.format(crv) )

        cvs = degs+spans
        #
        #crv1 = cmds.duplicate(crv, n='deletableCurve1')[0]
        #cmds.select('{}.cv[0:{}]'.format(crv1, cvs))

        #cmds.move(mX, mY, mZ, r=True, os=True, wd=True)

        #crv2 = cmds.duplicate(crv, n='deletableCurve2')[0]
        #cmds.select('{}.cv[0:{}]'.format(crv2, cvs))

        #mX= mX*(-1)
        #mY= mY*(-1)
        #mZ= mZ*(-1)
        
        #cmds.move(mX, mY, mZ, r=True, os=True, wd=True)	
        mnX= mX*(-1)
        offst_curve1 = cmds.offsetCurve(crv, d=mX)[0]
        offst_curve2 = cmds.offsetCurve(crv, d=mnX)[0]
        
        
        surf = cmds.loft(offst_curve1, offst_curve2, ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=0, rsn=True, n=name)[0]	
        cmds.rebuildSurface(surf, ch=1, rpo=1, rt=0, end=1, kr=0, kcp=0, kc=0, su=uNumber, du=3, sv=vNumber, dv=3, tol=0.01, fr=0, dir=2)
        cmds.delete(surf, ch=True)
        for c in [crv, offst_curve1, offst_curve2]:
            cmds.delete(c)

    except:  
        cmds.nurbsPlane(n=name, ax=(0,1,0), w=True, lr= True, d = 3, u = uNumber, v = vNumber, ch=1) 



def referenceLocators(cuantity = 1, reflection = True, between = 0):
    reflectionLocators = []
    if cuantity == 1:
        loc = cmds.spaceLocator(n = 'generatingLocator')[0]
        if reflection == True:
            flip = cmds.group(em=True, n='locReferenceReflection_builder')
            ref = cmds.spaceLocator(n = 'reflectLocator')[0]
            cmds.parent(ref, flip)
            for axis in 'xyz':
                for trs in 'trs':
                    cmds.connectAttr('{}.{}{}'.format(loc, trs, axis), '{}.{}{}'.format(ref, trs, axis))   
            cmds.setAttr('{}.sx'.format(flip), -1)            
            return loc                
    elif cuantity > 1:
        referencedLocators = []
        for c in range(cuantity):
            loc = cmds.spaceLocator(n = 'generatingLocator{}'.format(c))[0]
            referencedLocators.append(loc)
            reflectionLocators.append(loc)
        if between > 0:
            i = 0
            while len(referencedLocators) != 0:
                value = float(1)/(between+1)
                for number in range(between):
                    value1 = value * (number+1)
                    value2 = 1-value1
                    influence1 = referencedLocators[0]
                    influence2 = referencedLocators[1]
                    bet = cmds.spaceLocator(n='betweenLocator{}'.format(i))
                    pC = cmds.parentConstraint(influence1, influence2, bet)[0]
                    cmds.setAttr('{}.{}W0'.format(pC, influence1), value1)
                    cmds.setAttr('{}.{}W1'.format(pC, influence2), value2)
                i += 1
                referencedLocators.remove(referencedLocators[0])
                if len(referencedLocators) == 1:
                    break
        if reflection == True:
            flip = cmds.group(em=True, n='locReferenceReflection_builder')
            for locator in reflectionLocators:
                reverse = cmds.duplicate(locator, n='reverseLocator')
                cmds.parent(reverse, flip)
                for axis in 'xyz':
                    for trs in 'trs':
                        cmds.connectAttr('{}.{}{}'.format(locator, trs, axis), '{}.{}{}'.format(reverse[0], trs, axis))
            cmds.setAttr('{}.sx'.format(flip), -1)   
 



def makeRibbon(nurbs = '____nurb', system_name = 'brows'):
    vertex_list = cmds.ls(flatten = True, orderedSelection=True)
    fol_number = len(vertex_list)

    #vertex_list = [u'HeadBrows_c_geo.vtx[334]', u'HeadBrows_c_geo.vtx[335]', u'HeadBrows_c_geo.vtx[337]', u'HeadBrows_c_geo.vtx[341]', u'HeadBrows_c_geo.vtx[342]', u'HeadBrows_c_geo.vtx[344]', u'HeadBrows_c_geo.vtx[346]', u'HeadBrows_c_geo.vtx[348]', u'HeadBrows_c_geo.vtx[350]', u'HeadBrows_c_geo.vtx[352]', u'HeadBrows_c_geo.vtx[359]', u'HeadBrows_c_geo.vtx[360]', u'HeadBrows_c_geo.vtx[522]', u'HeadBrows_c_geo.vtx[1693]', u'HeadBrows_c_geo.vtx[1695]', u'HeadBrows_c_geo.vtx[1697]', u'HeadBrows_c_geo.vtx[1700]', u'HeadBrows_c_geo.vtx[1701]', u'HeadBrows_c_geo.vtx[1703]', u'HeadBrows_c_geo.vtx[1706]', u'HeadBrows_c_geo.vtx[1708]', u'HeadBrows_c_geo.vtx[1710]', u'HeadBrows_c_geo.vtx[1712]', u'HeadBrows_c_geo.vtx[1719]', u'HeadBrows_c_geo.vtx[1875]', u'HeadBrows_c_geo.vtx[3616]', u'HeadBrows_c_geo.vtx[3617]']

    # Recover Vertex List
    vertex_list_ordered = []
    vertex_list_disordered = vertex_list[::]
    vertex_list_disordered_x_positions = []
    for vtx in vertex_list_disordered:
        vtx_x_position = cmds.xform(vtx, query = True, translation = True, worldSpace = True)[0]
        vertex_list_disordered_x_positions.append(vtx_x_position)

    while len(vertex_list_disordered)>0:
        vtx_lower_pos =  10000000000000
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
    nurbs_shape = cmds.listRelatives(nurbs, shapes = True, noIntermediate = True)[0]
    left_follicles_list = []
    right_follicle_list = []
    for x in nurbs_shape:
        if not 'Orig' in x:
            nurbs_shape
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



    #Creacion de Huesos por foliculo
    follicles_list = left_follicles_list + right_follicle_list + [center_follicle]
    cmds.group(em=True, n='{}GeoSkin_c_grp'.format(system_name))
    cmds.group(em=True, n='{}SystemFols_c_grp'.format(system_name))
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
        cmds.parent(jnt_zero, '{}GeoSkin_c_grp'.format(system_name))
    #Hold bullshit
    if cmds.objExists('facialControls_c_grp') == False:
        cmds.group(em=True, n= 'facialControls_c_grp')
    if cmds.objExists('facialRig_c_grp') == False:
        cmds.group(em=True, n= 'facialRig_c_grp')
    if cmds.objExists('facialSystems_c_grp') == False:
        cmds.group(em=True, n= 'facialSystems_c_grp')    
    cmds.createNode('joint', n='{}_c_Hold'.format(system_name))
    cmds.createNode('transform', name = '{}Hold_c_zero'.format(system_name))
    cmds.parent('{}_c_Hold'.format(system_name), '{}Hold_c_zero'.format(system_name))
    cmds.parent('{}Hold_c_zero'.format(system_name), '{}GeoSkin_c_grp'.format(system_name))

    cmds.createNode('transform', n='{}SystemFols_c_grp'.format(system_name))
    for fol in follicles_list:
        cmds.parent(fol, '{}SystemFols_c_grp'.format(system_name))
    cmds.parent('{}SystemFols_c_grp'.format(system_name), 'facialSystems_c_grp')    
        
def colorKin(color=(0.027, 0.188, 0.678)):
    list = cmds.ls(sl=True)
    for i in list:
        cmds.color(i, rgb=color)


def locOnSpot():
    selection = cmds.ls(sl=True)
    def fg_get_center_position_of_objects(objects):
        # get the bounding box of selected list
        center_position = (0.0, 0.0, 0.0)

        if cmds.ls(objects):
            xmin, ymin, zmin, xmax, ymax, zmax = cmds.exactWorldBoundingBox(objects, ignoreInvisible=True)
            # look for center point
            center_position = (.5 * (xmax + xmin), .5 * (ymax + ymin), .5 * (zmax + zmin))

        return center_position

    def create_default_point(point_pos = (0.0, 0.0, 0.0)):
        # create locator
        default_point = cmds.spaceLocator(position=(0.0, 0.0, 0.0), name='point_c_loc')[0]
        default_point_shape = cmds.listRelatives(default_point, shapes=True)[0]

        # lock scale and set shape size
        for axis in ['X', 'Y', 'Z']:
            cmds.setAttr('{0}.scale{1}'.format(default_point, axis), lock=True)
            cmds.setAttr('{0}.localScale{1}'.format(default_point_shape, axis), 0.1)
        cmds.setAttr('{0}.translate'.format(default_point), point_pos[0], point_pos[1], point_pos[2])

        return [default_point, default_point_shape]

    def create_default_point_on_place():
        # look for the position that we wanna create the point (if nothing is selected the point will be created at origin)
        selected_list = cmds.ls(sl=True, flatten=True)
        center_selection_pos = fg_get_center_position_of_objects(selected_list)
        create_default_point(point_pos = center_selection_pos)


    def create_multiple_default_point_on_place():
        # look for the position that we wanna create the point (if nothing is selected the point will be created at origin)
        selected_list = cmds.ls(sl=True, flatten=True)
        for selected in selected_list:
            center_selection_pos = fg_get_center_position_of_objects(selected)
            create_default_point(point_pos = center_selection_pos)

    create_default_point_on_place()

    
def  copyShape():
    list = cmds.ls(sl=True)
    extract = list[0]
    inyect = list[1]
    pos = cmds.xform(inyect, m=True, ws=True, q=True)
    extract = cmds.duplicate(extract, rc=True)
    cmds.xform(extract, m=pos, ws=True)
    extShape = cmds.listRelatives(extract, typ='shape')
    inyShape = cmds.listRelatives(inyect, typ='shape')
    for shape in extShape:
        cmds.parent(shape, inyect, r=True, s=True)
    for shape in inyShape:
        cmds.delete(shape)    
    
def folliclesSides(side = 'r', system_name='dwEyelid', nurbs='dwEyelidMain_r_nurbs'):

    vertex_list = cmds.ls(flatten = True, orderedSelection = True)
    fol_number = len(vertex_list)
    
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
    
    #Invertir el orden de la lista para el side r
    if side == 'r':
        vertex_list_ordered = vertex_list_ordered[::-1]
    
    #Create Follicles
    nurbs_shape = cmds.listRelatives(nurbs, shapes = True, noIntermediate = True)
    nurbs_shape = [x for x in nurbs_shape if not 'Orig' in x][0]
    follicle_list = []
    for i in range(0,fol_number):
         follicle_name = '{}{}_{}_fol'.format(system_name, str(i+1).zfill(2), side)
         follicle = cmds.createNode('transform', name = follicle_name)
         follicle_shape = cmds.createNode('follicle', name = '{}Shape'.format(follicle_name), parent = follicle)
         cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(follicle_shape), force = True)
         cmds.connectAttr('{}.worldMatrix[0]'.format(nurbs_shape), '{}.inputWorldMatrix'.format(follicle_shape), force = True)
         for axis in 'XYZ':
             cmds.connectAttr('{}.outTranslate{}'.format(follicle_shape, axis), '{}.translate{}'.format(follicle, axis), force = True)
             #cmds.connectAttr('{}.outRotate{}'.format(follicle_shape, axis), '{}.rotate{}'.format(follicle, axis), force = True)
         follicle_list.append(follicle)
    
    for i, fol in enumerate(follicle_list):
        temp_closestSuface = cmds.createNode('closestPointOnSurface', name = 'temp_closest')
        cmds.connectAttr('{}.local'.format(nurbs_shape), '{}.inputSurface'.format(temp_closestSuface), force = True)
        vtx_position = cmds.xform(vertex_list_ordered[i], query = True, translation = True, worldSpace = True)
        cmds.setAttr('{}.inPosition'.format(temp_closestSuface), vtx_position[0], vtx_position[1], vtx_position[2])
        parameter_U = cmds.getAttr('{}.parameterU'.format(temp_closestSuface))
        parameter_V = cmds.getAttr('{}.parameterV'.format(temp_closestSuface))
        follicle_shape = cmds.listRelatives(fol, shapes = True)[0]
        cmds.setAttr('{}.parameterU'.format(follicle_shape), parameter_U)
        cmds.setAttr('{}.parameterV'.format(follicle_shape), parameter_V)
        cmds.delete(temp_closestSuface)
    
    for fol in follicle_list:
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
