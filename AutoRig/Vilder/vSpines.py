import Vilder.vFunctions as vFun
import Vilder.vSetUp as vSet
reload(vSet)

creative = vSet.refAutorig('spineRibbon', 'c')
creative.referenceChain(mod='spineRibbon', sid='c', quantity=2)


class spines:
    def __init__(self, name, sknNumber, position1, position2):
        self.name = name
        self.sknNumber = sknNumber
        self.position1 = position1
        self.position2 = position2 
    def ribbonSpine(self, width):
        joints = vFun.chainJoint(cantidad=self.sknNumber, nombre=self.name, lado='c', 
                                 chin=True, radio=1, inicio=self.position1, 
                                 fin=self.position2, unparent=True)        
        nurbs = vFun.makeRibbon(point1=self.position1, point2=self.position2, 
                                width=width, module=self.name, side='c', u=1, v=7)[0] 
        cmds.select(cl=True)
        for jnt in joints:
            cmds.select(jnt, add=True)                   
        vFun.attachBones(nurb = nurbs, side='c', system='spine')     
        
    def splineSpine(self):        
        joints = vFun.chainJoint(cantidad=self.sknNumber, nombre=self.name, lado='c', 
                                 chin=True, radio=1, inicio=self.position1, 
                                 fin=self.position2, unparent=False)
        ik = cmds.ikHandle(sj= joints[0], ee=joints[-1], 
                      sol='ikSplineSolver', n='{}_c_ikHandle'.format(self.name))
        cmds.rename(ik[1], '{}_c_effector'.format(self.name)) 
        cmds.rename(ik[2], '{}IkCurve_c_curve'.format(self.name))               
        
        
        
spine = spines('spine', 10, 'position0Spine_c_vilder', 'position1Spine_c_vilder')
spine.ribbonSpine(5)  

spine = spines('spine', 10, 'position0Spineribbon_c_vilder', 'position1Spineribbon_c_vilder')
spine.splineSpine()  
          