from collections import OrderedDict
import vilder.noodles as noodles
from maya import cmds
class nonRoll_system():

    def layer(self):
        self.nonRoll_layout = OrderedDict([ 
			                                           ('Name' , ['str', 'null']), 
			                                           ('Side' , ['str', 'null']), 
			                                           ('Start' , ['str', 'selectable']), 
			                                           ('End' , ['str', 'selectable']),
			                                           ('Superior_Articulation' , ['str', 'selectable']),
			                                           ('Inferior_Articulation' , ['str', 'selectable'])
			                                           ])
                               
       
        return  self.nonRoll_layout            
        
        
        
                                         
    def display(self):
        labeling = 'Create NonRoll System.'
        return  labeling
    def function(self, variables = [None, None, None, None, None, None], *pArgs ):
        #nonRoll - Hip---------------------------------------------------------------------------------------------------        
	    cmds.select(cl=True)
	    self.name = variable[0]
	    self.side = variable[1]
	    self.start = variables[2]
	    self.end = variables[3]
	    self.articulationUp = variable[4]
	    self.articulationDw = variable [5]
	    
	    self.ini_position = cmds.xform(self.start, ws=True, q=True, t=True)
	    self.end_position = cmds.xform(self.end, ws=True, q=True, t=True)
	    
	    nonRoll_chain = cmds.joint(n='{}_{}_nonRoll'.format(self.name, self.side), position = self.ini_position)
	    nonRoll_end = cmds.joint(n='{}End_{}_nonRoll'.format(self.name, self.side), position = self.end_position)

	    cmds.setAttr('{}.jointOrientX'.format(nonRoll_chain), 0)
	    
	    
	    ikHandle_jnt = cmds.ikHandle(s = 'sticky',
					 sj = nonRoll_chain, 
					 ee= nonRoll_end, 
					 n='{}NonRoll_{}_ikHandle'.format(self.name, self.side))
					 
	    cmds.rename(ikHandle_jnt[1], '{}NonRoll_{}_eff'.format(self.name, self.side))
	    for axis in 'XYZ':
    		cmds.setAttr('{}.poleVector{}'.format(ikHandle_jnt[0], axis), 0)
    	    nonRoll_grp = cmds.group(em=True, n='{}NonRoll_{}_grp'.format(self.name, self.side))
    	    
    	    cmds.parent(ikHandle_jnt[0], nonRoll_end, nonRoll_grp)
		    #GLOBAL SCALE - CONNECTION TO GRP


	    cmds.pointConstraint(self.articulationUp, 
        				     nonRoll_chain, 
        				     n='{}NonRoll_{}_pointCon'.format(self.name, self.side))    

	    cmds.pointConstraint(self.articulationDw, 
            				 ikHandle_jnt, 
            				 n='{}NonRoll_{}_pointCon'.format(self.name, self.side))
               
