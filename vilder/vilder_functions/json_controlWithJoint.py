from collections import OrderedDict
import vilder.noodles as noodles
from maya import cmds
class control_with_joint():

    def layer(self):

        self.diction = OrderedDict([ 
                                                       ('Name' , ['str', 'null']), 
                                                       ('Side' , ['str', 'null']), 
                                                       ('ParentJnt' , ['str', 'selectable']),
                                                       ('ParentCtr' , ['str', 'selectable']),
                                                       ('Function' , ['str', 'null']),
                                                       ('Invert' , ['check', 'null']),
                                                       ('Position' , ['str', 'selectable'])
                                                        ])
                                           
       
        return  self.diction            
        
        
        
                                         
    def display(self):
        labeling = 'Create joint in selected position connected to a control'
        return  labeling

    def function(self, variables = [None, None, None, None, None, None, None]):
        
        control_name = variables[0]
        side = variables[1]
        ctr_parent_to = variables[2]
        jnt_parent_to = variables[3]
        jnt_usage = variables[4]
        invert = variables[5]
        position_loc = variables[6]


        def ctrJnt(control_name = variables[0]):
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
        contrl_joint_list = ctrJnt()
        if invert == True:
            contrl_joint_list_invert = ctrJnt(control_name = variables[0] + 'Dw')
            cmds.setAttr('{}.scaleY'.format(contrl_joint_list_invert[0]), -1)
            cmds.setAttr('{}.scaleY'.format(contrl_joint_list_invert[1]), -1)
