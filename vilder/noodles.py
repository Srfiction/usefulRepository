from maya import cmds
def createMultDiv(name=None, inputX1 = None, inputX2 = None, inputY1 = None, inputY2 = None, inputZ1 = None, inputZ2 = None, operation='Multiply'):
    mult = cmds.shadingNode('multiplyDivide', au=True, n=name)
    input_dic = {'input1.input1X' : inputX1, 
                 'input1.input1Y' : inputY1, 
                 'input1.input1Z' : inputZ1,
                 'input2.input2X' : inputX2,
                 'input2.input2Y' : inputY2,
                 'input2.input2Z' : inputZ2}
    
    operation_dic = {'Multiply' : 1, 
                     'Divide' : 2, 
                     'Power' : 3}        
    
    
    try:
        cmds.setAttr('{}.operation'.format(mult), operation_dic.get(operation))    
    except:
        print 'No operation selected'
    for input in input_dic:
        key = input_dic.get(input)
        if input:
            key = input_dic.get(input)
            if isinstance(key, str) == True:
                cmds.connectAttr(key, '{}.{}'.format(mult, input))
            elif isinstance(key, int) == True:
                cmds.setAttr('{}.{}'.format(mult, input), key)
            elif isinstance(key, float) == True:
                cmds.setAttr('{}.{}'.format(mult, input), key)    
            else:
                pass   
    return mult                
    
    
    
    
def createSubsPlus(name=None, dimensions = 3, inputX1 = None, inputX2 = None, inputY1 = None, inputY2 = None, inputZ1 = None, inputZ2 = None, operation='Sum'):
    subs = cmds.shadingNode('plusMinusAverage', au=True, n=name)
    if dimensions == 1:
            input_dic = {inputX1 : 'input1D[0]',
                         inputX2 : 'input1D[1]'
                         }     
      
      
    else:           
            input_dic = {inputX1 : 'input{0}D[0].input{0}Dx'.format(dimensions),
                         inputY1 : 'input3D[0].input3Dy',
                         inputZ1 : 'input3D[0].input3Dz',
                         inputX2 : 'input{0}D[1].input{0}Dx'.format(dimensions),
                         inputY2 : 'input3D[1].input3Dy',
                         inputZ2 : 'input3D[1].input3Dz'}
    
    operation_dic = {'Sum' : 1,
                     'Substract' : 2,
                     'Average' : 3}    
    
    
    try:
        cmds.setAttr('{}.operation'.format(subs), operation_dic.get(operation))    
    except:
        print 'No operation selected'
    for input in [inputX1, inputX2, inputY1, inputY2, inputZ1, inputZ2]:
        if input:
            key = input_dic.get(input)
            
            if isinstance(input, str) == True:
                cmds.connectAttr(input, '{}.{}'.format(subs, key))
            elif isinstance(input, int) == True:
                cmds.setAttr('{}.{}'.format(subs, key), input)
            elif isinstance(input, float) == True:
                cmds.setAttr('{}.{}'.format(subs, key), input)                
            else:
                pass   
    return subs        
    
    
def clampCreator(name = 'clampNode', MaxG = 0, MaxR = 0, MaxB = 0, 
                                     MinG = 0, MinR = 0, MinB = 0, 
                                     InputR = None, InputG = None, InputB = None,
                                     OutputR = None, OutputG = None, OutputB = None):

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
                 
    clamp_output = {'outputR' : OutputR,
                    'outputG' : OutputG,
                    'outputR' : OutputB}             
                    
    for element in clamp_dic:
        input = clamp_dic.get(element)
        if isinstance(input, str) == True:
            cmds.connectAttr(input, '{}.{}'.format(clp, element))
        elif isinstance(input, int) == True:
            cmds.setAttr('{}.{}'.format(clp, element), input)
        else:
            pass
    for element in clamp_output:
       value = clamp_output.get(element)
       if value:
           cmds.connectAttr('{}.{}'.format(clp, element), value)
       else:
           pass    
    return clp    

def autoNoodle(node = None, name = None, connections = []):
    noodele = cmds.shadingNode(node, au=True, n=name)
    for element in connections:
        input = element[0]
        value = element[1]
        if isinstance(value, str) == True:
            cmds.connectAttr(value, '{}.{}'.format(noodele, input))
        elif isinstance(value, int) == True:
            cmds.setAttr('{}.{}'.format(noodele, input), value) 
        elif isinstance(value, float) == True:
            cmds.setAttr('{}.{}'.format(noodele, input), value)     
        else:
            pass      
    return noodele        
