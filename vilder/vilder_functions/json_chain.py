from collections import OrderedDict
from maya import cmds
from maya.api import OpenMaya
class joint_chain():
    def __init__(self):
        self.execute = 'not executable'
    def layer(self):
        self.joint_chain_layout = OrderedDict([
                                                           ('Number' , ['int', 5]), 
                                                           ('Connected_Chain' , ['check', 'checked']), 
                                                           ('Name' , ['str', 'null']), 
                                                           ('Side' , ['str', 'null']), 
                                                           ('Start' , ['str', 'selectable']), 
                                                           ('End' , ['str', 'selectable']),
                                                           ('Function' , ['str', 'null'])
                                                           ])
                                   
       
        return  self.joint_chain_layout                                             
    def display(self):
        labeling = 'Generate a bone chain between points.'
        return  labeling
    def function(self, variables = [None, False, None, None, None, None, None], *pArgs ):
        self.number = variables[0]
        self.parent = variables[1]
        self.name = variables[2]
        self.side = variables[3]
        self.ini = variables[4]
        self.end = variables[5]
        self.function = variables[6]
        inicio = self.ini
        fin = self.end
        start_point = cmds.xform(inicio, q=True, t=True, ws=True)
        end_point = cmds.xform(fin, q=True, t=True, ws=True)
        vector_sta = OpenMaya.MVector(start_point)
        vector_end = OpenMaya.MVector(end_point)
        all_joints = []
        for count in range(self.number):            
            name = '{}{}_{}_{}'.format(self.name, str(count).zfill(2), self.side, self.function)
            nameEnd = '{}{}End_{}_{}'.format(self.name, str(count).zfill(2), self.side, self.function)
            dif_point = vector_end-vector_sta
            offset = 1.0/(self.number-1)
            new_point=dif_point*offset
            final_point = vector_sta + new_point   
            mid_pos=dif_point*(offset*count)
            final_pos=vector_sta+mid_pos
            jnt=cmds.joint(n=name, p=list(final_pos))
            all_joints.append(jnt)
            if count != 0:
                cmds.joint(all_joints[count-1],e=True,zso=True,oj='xyz',sao='yup')  
            
            if self.parent == False:
                cmds.select(cl=1)
            if count == self.number:
                jnt = cmds.rename(jnt, nameEnd)
                all_joints[-1] = jnt
                break
               
        return all_joints    
        