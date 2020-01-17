from collections import OrderedDict
import vilder.noodles as noodles
from maya import cmds
reload(noodles)
class joint_scale_curve():

    def layer(self):

        self.scale_curve = OrderedDict([ 

                                                       ('Curve' , ['str', 'selectable']),
                                                       ('Scale Axis' , ['str', 'selectable'])
                                                       ])
                                           
       
        return  self.scale_curve            
        
        
        
                                         
    def display(self):
        labeling = 'Select joints that you want to connect to the scale of the curve'
        return  labeling

    def function(self, variables = [None, None]):
        
        joints = cmds.ls(sl=True)
        
        selected_curve = variables[0]
        scale_axis = variables[1].upper()
        
        name = selected_curve.split('_')[0]
        side = selected_curve.split('_')[1]
        
        curve_info = cmds.shadingNode('curveInfo', au=True, name = '{}_{}_curveInfo'.format(name, side))
        cmds.connectAttr('{}.local'.format(selected_curve), '{}.inputCurve'.format(curve_info))
        
        curve_div = noodles.createMultDiv(name='{}_{}_div'.format(name, side), 
                                         inputX1 = '{}.arcLength'.format(curve_info), 
                                         inputX2 = cmds.getAttr('{}.arcLength'.format(curve_info)), 
                                         operation='Divide')
        
        for jnt in joints:
            cmds.connectAttr('{}.outputX'.format(curve_div), '{}.scale{}'.format(jnt, scale_axis))
            
    

  
    