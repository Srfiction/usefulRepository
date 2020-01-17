import Vilder.vFunctions as vFun
import maya.cmds as cmds


class refAutorig:
    def __init__(self, module, side): 
        self.name = '{}_{}_vilder'.format(module, side)
    def boneCircle(self, number):
        name = self.name
        jnt = cmds.joint(n='position{}{}'.format(number, name.capitalize()))
        cir = cmds.circle(n='circle{}{}'.format(number, name.capitalize()))   
        cmds.parentConstraint(cir, jnt, n='parent{}'.format(number, name.capitalize()))
        return jnt
    def referenceChain(self, mod, sid, quantity):
        ref = refAutorig(module=mod, side=sid)
        jnt_list=[]
        for num in range(quantity):
            cmds.select(cl=True)
            jnt = ref.boneCircle(number=num)
            if num == 0:
                jnt_list.append(jnt)
            else:
                cmds.parent(jnt, jnt_list[num-1])  
                jnt_list.append(jnt)  
