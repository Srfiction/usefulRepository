import Vilder.vFunctions as vFun
import Vilder.vSetUp as vSet
reload(vSet)

creative = vSet.refAutorig('spineRibbon', 'c')
creative.referenceChain(mod='spine', sid='c', quantity=2)


ref = refAutorig('spine', 'r')
ref.referenceChain(mod='spine', sid='l', quantity=2)




class spines:
    def __init__(self, name, sknNumber, position1, position2):
        self.name = name
        self.sknNumber = sknNumber
        self.position1 = position1
        self.position2 = position2 
    def ribbonSpine(self, width):
        vFun.chainJoint(cantidad=self.sknNumber, nombre=self.name, lado='c', chin=True, radio=1, inicio=self.position1, fin=self.position2, unparent=True)        
        nurbs = vFun.makeRibbon(point1=position1, point2=position2, width=width, module=self.name, side='c', u=1, v=7)[0]        
        vFun.attachBones(nurb = nurbs, side='c', system='spine')     
        
spine = spines('spine', 10, 'position0Spine_c_vilder', 'position1Spine_c_vilder')
spine.ribbonSpine(5)            