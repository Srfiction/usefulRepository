from PySide2 import QtCore, QtGui, QtWidgets
import functools
import random

from maya import cmds
from maya.api import OpenMaya
from collections import OrderedDict
from vilder_functions.json_chain import joint_chain
from vilder_functions.json_nonRoll import nonRoll_system
from vilder_functions.json_ctrFolFollow import control_follow_folicle
from vilder_functions.json_scaleJointCurve import joint_scale_curve
from vilder_functions.json_controlWithJoint import control_with_joint

from maya.api import OpenMaya

class Ui_Dialog():
    def __init__(self):
        self.modular_layout = None
        self.diccionario_try = {} 
        self.ventanaNombre = 'fockingWut'
        self.Titulo = 'Vilder'
        self.Alto = 350
        self.Ancho = 500
        self.VENTANA = cmds.window(self.ventanaNombre, title='AutorigBuilder', width=self.Alto, height = self.Ancho)
    
    
    def vilder_layout(self, type_element = None, *pArgs): 
         
        
        self.main_layout = cmds.columnLayout('main_layout',  w= 1000, h=700)
        
        self.center_layout = cmds.columnLayout('center_layout0', parent = self.main_layout,  w= 1000, h=700)
        
        self.three_windows_layout = cmds.rowLayout('three_windows_layout', parent = self.center_layout, nc=3,  w= 1000, h=700)
        
        ###
        self.list_functions_layout = cmds.columnLayout('list_functions_layout', parent = self.three_windows_layout,  w= 200, h=700)
        
        self.trocecitos_layout = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5, parent = self.list_functions_layout, w= 200, h=700)
        self.functions_list()
        
        self.vilder_rebild_layout = cmds.columnLayout('vilder_rebuilder_layout', parent = self.three_windows_layout, bgc = (0,0,0),  w= 460, h=700)
        
        self.hold_modular_layout = cmds.columnLayout('modular_container_layout', parent = self.three_windows_layout,  w= 330, h=700)
        #self.layout_creator()
        
        ###
        cmds.showWindow()
    
    def changeTextFld(self, boton=None, *pArgs):
        selection = cmds.ls(sl=True)[0]
        cmds.textField('textField{}_selectinText'.format(boton), edit=True, tx=selection)
    
        
    def functions_list(self, *pArgs):

        self.trocitos = cmds.columnLayout('trocitos', parent = self.trocecitos_layout)
        self.trocitos_list()
        
        self.elementos = cmds.columnLayout('full_elements', parent = self.trocecitos_layout)
        self.elementos_list()
        
        
        cmds.tabLayout( self.trocecitos_layout, edit=True, tabLabel=((self.trocitos, 'Trocecitos'), (self.elementos, 'Compuestos')) )
        
    def trocitos_list(self, *pArgs):
        #Anadir aqui los botones con las funciones
        cmds.button(label= 'Joint Chain', command= functools.partial(self.layout_creator, joint_chain()), w= 200 )      
        cmds.button(label= 'NonRoll Chain', command= functools.partial(self.layout_creator, nonRoll_system()), w= 200)     
        cmds.button(label= 'Connect Fol to Ctr', command= functools.partial(self.layout_creator, control_follow_folicle()), w= 200) 
        cmds.button(label= 'Connect Curve Scale to Chain', command= functools.partial(self.layout_creator, joint_scale_curve()), w= 200)    
        cmds.button(label= 'Control with Joint', command= functools.partial(self.layout_creator, control_with_joint()), w= 200)     
            
    def elementos_list(*pArgs):
        cmds.button()      
        cmds.button()                

    def layout_creator(self, import_function = None, *pArgs):
        
        if self.modular_layout:
            cmds.deleteUI(self.modular_layout, layout=True)
        
        self.modular_layout = cmds.rowColumnLayout(numberOfColumns=1, columnOffset=[(1, 'right', 3) ], parent = self.hold_modular_layout) 
        
        #import import_function
        #from import_function import layer, display
        import_layout = import_function.layer()
        import_display = import_function.display()
        input_list = []
        for element in import_layout:
            self.generated_layout = cmds.rowColumnLayout('{}_layout'.format(element), numberOfColumns=4, columnOffset = [(1, 'left', 3), (2, 'left', 3), (3, 'left', 0)], parent = self.modular_layout, ut=True, w= 330, h=50)  
            input_type = import_layout[element][0]
            addition = import_layout[element][1]
            cmds.text(label = element)
            if input_type == 'int':
                input = cmds.intField('{}_layout'.format(element), v = addition )
            elif input_type == 'flaot':
                input = cmds.floatField( v = addition )
            elif input_type == 'str':
                text_code = random.randint(1,21)
                input = cmds.textField('textField{}_selectinText'.format(element))
                if addition == 'selectable':
                    cmds.button('{}_selectinBotton'.format(element), label = 'Select', command = functools.partial(self.changeTextFld, element))
                else:
                    pass
            elif input_type == 'check':
                input = cmds.checkBox( v=False )                      
                if addition == 'checked':
                    cmds.checkBox(input, edit=True, v=True)
            input_list.append([input, input_type]) 
                   
        def execute_function(*pArgs): 
            value_list =[]                   
            for input in input_list:
                input_type = input[1]
                input = input[0]
                if input_type == 'int':
                    value = cmds.intField( input, q=True, value = True )
                elif input_type == 'flaot':
                    value = cmds.floatField( input, q=True, value = True )
                elif input_type == 'str':
                    value = cmds.textField( input, q=True, text = True )
                elif input_type == 'check':
                    value = cmds.checkBox( input, q=True, value = True )                      
                value_list.append(value)   
                
            import_function.function(value_list)
        self.description_layout = cmds.rowColumnLayout('description_layout', numberOfColumns=4, columnOffset = [(1, 'left', 3), (2, 'left', 3), (3, 'left', 0)], parent = self.modular_layout, ut=True, w= 330, h=50, bgc = (0.1, 0.1,0.2))    
        cmds.text(label = import_display)
        self.description_layout = cmds.rowColumnLayout('execute_layout', numberOfColumns=4, columnOffset = [(1, 'left', 3), (2, 'left', 3), (3, 'left', 0)], parent = self.modular_layout, ut=True, w= 330, h=50)
        cmds.button(label = 'Execute', command = execute_function)
          

test = Ui_Dialog()
test.vilder_layout()