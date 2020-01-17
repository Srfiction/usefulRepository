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
        elif isinstance(input, float) == True:
            cmds.setAttr('{}.{}'.format(mult, element), input) 
        elif isinstance(input, int) == True:
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
