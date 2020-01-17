from collections import OrderedDict
import vilder.noodles as noodles
from maya import cmds
class control_follow_folicle():

    def layer(self):

        self.control_follow = OrderedDict([ 
                                                       ('Control' , ['str', 'selectable']), 
                                                       ('Folicle' , ['str', 'selectable']), 
                                                       ])
                                           
       
        return  self.control_follow            
        
        
        
                                         
    def display(self):
        labeling = 'Connect the translation of a folicle to a control without affecting performance'
        return  labeling

    def function(self, variables = [None, None]):
        
        ctr = variables[0]
        fol = variables[1]
        n=ctr.split('_')[0]
        side=ctr.split('_')[1]
        
        namePos='{}_{}_pos'.format(n, side)
        namePosZero='{}Pos_{}_zero'.format(n, side)
        nameRev='{}_{}_rev'.format(n, side)
        nameRevZero='{}Rev_{}_zero'.format(n, side)
        
        for grp in [namePos, namePosZero, nameRev, nameRevZero]:
            pos=cmds.xform(ctr, m=True, ws=True, q=True)
            grpPos = cmds.group(em=True, n=grp)
            cmds.xform(grpPos, m=pos, ws=True)
        cmds.parent(namePos, namePosZero)
        cmds.parent(nameRev, nameRevZero)
        cmds.parent(nameRevZero, namePos)           
        zero = cmds.listRelatives(ctr, parent=True)[0]
        cmds.parent(namePosZero, zero)
        cmds.parent(ctr, nameRev)
        
        plusMinusName = '{}_{}_sub'.format(n, side)
        cmds.shadingNode('plusMinusAverage', n=plusMinusName, au=True)
        multDivName = '{}_{}_mult'.format(n, side)
        cmds.shadingNode('multiplyDivide', n=multDivName, au=True)
        
        cmds.setAttr('{}.operation'.format(plusMinusName), 2)
        
        for axis in 'xyz':
            set = cmds.getAttr('{}.t{}'.format(fol, axis))
        
            cmds.setAttr('{}.input3D[1].input3D{}'.format(plusMinusName, axis), set)
            cmds.connectAttr('{}.t{}'.format(fol, axis), '{}.input3D[0].input3D{}'.format(plusMinusName, axis))
            cmds.connectAttr('{}.output3D.output3D{}'.format(plusMinusName, axis), '{}.t{}'.format(namePos, axis))
        
            cmds.connectAttr('{}.t{}'.format(ctr, axis), '{}.input1.input1{}'.format(multDivName, axis.upper()))   
            cmds.connectAttr('{}.output{}'.format(multDivName, axis.upper()), '{}.t{}'.format(nameRev, axis)) 
            
            cmds.setAttr('{}.input2{}'.format(multDivName, axis.upper()), -1)
            
            #from zero to RevZero
            
            rotate_zero = cmds.getAttr('{}.r{}'.format(zero, axis))
            scale_zero = cmds.getAttr('{}.s{}'.format(zero, axis))
            cmds.setAttr('{}.s{}'.format(nameRevZero, axis), scale_zero)
            cmds.setAttr('{}.r{}'.format(nameRevZero, axis), rotate_zero)
            
            cmds.setAttr('{}.s{}'.format(zero, axis), 1)
            cmds.setAttr('{}.r{}'.format(zero, axis), 0)            