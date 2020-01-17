# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/pepe_/Desktop/teddy picker/piero_teddyPicker.ui'
#
# Created: Mon Sep  2 12:56:41 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!
try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance
except:
    from PySide.QtGui import * 
    from PySide.QtCore import *
    from shiboken import wrapInstance

import os
import maya.cmds as cmds
import maya.OpenMayaUI as omui
#from shiboken import wrapInstance

from PySide2 import QtWidgets as QtWidgets
from PySide2 import QtCore as QtCore
from PySide2 import QtGui as QtGui

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr:
        return wrapInstance(long(ptr), QMainWindow)

def run():
    global win       
    # Ponemos un nombre que queramos, en el caso de tener varias ventanas
    # este nombre es unico por cada una.
    win = Teddy_Picker_UI (parent=getMayaWindow())
    win.show()


class Teddy_Picker_UI(QDialog):
    def __init__(self, parent = None):
        super(Teddy_Picker_UI, self).__init__(parent)
        self.inverted_controls = {'footIK_l_ctr' : [[0], [1]], 'footIK_r_ctr' : [[0], [1]], 'footFK_l_ctr' : [[],[0]], 'footFK_r_ctr' : [[],[0]], 
        						  'kneeFK_l_ctr' : [[],[0]], 'kneeFK_r_ctr' : [[],[0]], 'hipFK_l_ctr' : [[],[0]], 
        						  'hipFK_r_ctr' : [[],[0]], 'legPole_l_ctr' : [[1],[]], 'legPole_r_ctr' : [[1],[]], 
        						  'elbowFK_l_ctr' : [[],[1]], 'elbowFK_r_ctr' : [[],[1]], 'handFK_l_ctr' : [[],[]], 'handFK_r_ctr' : [[],[]], 
        						   'shoulderFK_r_ctr' : [[],[]], 'shoulderFK_l_ctr' : [[],[]], 'handIK_l_ctr' : [[2],[0,2]], 'handIK_r_ctr' : [[2],[0,2]]}
        self.setObjectName("Dialog")
        self.resize(480, 757)
        self.setMinimumSize(QtCore.QSize(480, 757))
        self.setMaximumSize(QtCore.QSize(480, 757))

        #Correccion botones ventana
        self.setWindowFlags(Qt.Window)#int

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 481, 751))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.centralwidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.centralwidget.setContentsMargins(4, 4, 4, 4)
        self.centralwidget.setObjectName("centralwidget")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        # indicamos que es el layout principal
        self.setLayout(self.verticalLayout)#int
        
        self.horizontalLayout_Principal = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Principal.setContentsMargins(4, 4, 4, -1)
        self.horizontalLayout_Principal.setObjectName("horizontalLayout_Principal")
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Principal.addItem(spacerItem)
        
        # ruta de las imagenes
        imgPath = os.path.join(os.path.dirname(__file__),  'image_TeddyPicker')#int    

        IMG_Texto_Piero_Path = os.path.join(imgPath, 'IMG_Texto_Piero.png')
        IMG_Body_Piero_Path = os.path.join(imgPath, 'IMG_Body_Piero.png')
		
        '''
        self.IMG_Texto_Piero = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.IMG_Texto_Piero.setText("")
        self.IMG_Texto_Piero.setPixmap(QtGui.QPixmap(IMG_Texto_Piero_Path))
        self.IMG_Texto_Piero.setObjectName("IMG_Texto_Piero")	
		'''

		#NAMESPACE EDIT
        self.text_edit_name_space = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.text_edit_name_space.setMaximumSize(QtCore.QSize(300, 25))
        self.text_edit_name_space.setObjectName("text_edit_name_space")
        self.horizontalLayout_Principal.addWidget(self.text_edit_name_space)


        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Principal.addItem(spacerItem1)
        self.centralwidget.addLayout(self.horizontalLayout_Principal)

        '''
        self.name_space_layout = QtWidgets.QHBoxLayout()
        self.name_space_layout.setObjectName("name_space_layout")
        self.text_edit_name_space = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.text_edit_name_space.setMaximumSize(QtCore.QSize(300, 25))
        self.text_edit_name_space.setObjectName("text_edit_name_space")
        self.name_space_layout.addWidget(self.text_edit_name_space)
        self.label_name_space = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_name_space.setObjectName("label_name_space")
        self.name_space_layout.addWidget(self.label_name_space)
        self.centralwidget.addLayout(self.name_space_layout)
		'''
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.bodyTab_layout = QtWidgets.QWidget()
        self.bodyTab_layout.setObjectName("bodyTab_layout")
        self.IMG_Body_Piero = QtWidgets.QLabel(self.bodyTab_layout)
        self.IMG_Body_Piero.setGeometry(QtCore.QRect(-10, -10, 461, 501))
        self.IMG_Body_Piero.setText("")
        self.IMG_Body_Piero.setPixmap(QtGui.QPixmap(IMG_Body_Piero_Path))
        self.IMG_Body_Piero.setObjectName("IMG_Body_Piero")
        
        self.pushButton = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton.setGeometry(QtCore.QRect(190, 320, 16, 16))
        self.pushButton.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.SelectControl(ControlName = 'kneeFK_r_ctr', addSelection = None))
        self.pushButton = QtWidgets.QPushButton(self.bodyTab_layout)

        self.pushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='kneeFK_r_ctr', addSelection = True))


        self.pushButton_hipFK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_hipFK_R.setGeometry(QtCore.QRect(190, 230, 16, 16))
        self.pushButton_hipFK_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_hipFK_R.setText("")
        self.pushButton_hipFK_R.setObjectName("pushButton_2")
        self.pushButton_hipFK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'hipFK_r_ctr', addSelection = None))

        self.pushButton_hipFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_hipFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='hipFK_r_ctr', addSelection = True))
        
        self.pushButton_footFK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_footFK_R.setGeometry(QtCore.QRect(190, 420, 16, 16))
        self.pushButton_footFK_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_footFK_R.setText("")
        self.pushButton_footFK_R.setObjectName("pushButton_3")
        self.pushButton_footFK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'footFK_r_ctr', addSelection = None))

        self.pushButton_footFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_footFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='footFK_r_ctr', addSelection = True))

        self.pushButton_footFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_footFK_L.setGeometry(QtCore.QRect(250, 420, 16, 16))
        self.pushButton_footFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_footFK_L.setText("")
        self.pushButton_footFK_L.setObjectName("pushButton_4")
        self.pushButton_footFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'footFK_l_ctr', addSelection = None))

        self.pushButton_footFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_footFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='footFK_r_ctr', addSelection = True))
        
        self.pushButton_kneeFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_kneeFK_L.setGeometry(QtCore.QRect(250, 320, 16, 16))
        self.pushButton_kneeFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_kneeFK_L.setText("")
        self.pushButton_kneeFK_L.setObjectName("pushButton_5")
        self.pushButton_kneeFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'kneeFK_l_ctr', addSelection = None))

        self.pushButton_kneeFK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_kneeFK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='kneeFK_l_ctr', addSelection = True))

        self.pushButton_hipFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_hipFK_L.setGeometry(QtCore.QRect(250, 230, 16, 16))
        self.pushButton_hipFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_hipFK_L.setText("")
        self.pushButton_hipFK_L.setObjectName("pushButton_6")
        self.pushButton_hipFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'hipFK_l_ctr', addSelection = None))


        self.pushButton_hipFK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_hipFK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='hipFK_l_ctr', addSelection = True))

        self.pushButton_footIK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_footIK_L.setGeometry(QtCore.QRect(240, 440, 16, 16))
        self.pushButton_footIK_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_footIK_L.setText("")
        self.pushButton_footIK_L.setObjectName("pushButton_7")
        self.pushButton_footIK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'footIK_l_ctr', addSelection = None))

        self.pushButton_footIK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_footIK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='footIK_l_ctr', addSelection = True))


        self.pushButton_footIK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_footIK_R.setGeometry(QtCore.QRect(210, 440, 16, 16))
        self.pushButton_footIK_R.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_footIK_R.setText("")
        self.pushButton_footIK_R.setObjectName("pushButton_8")
        self.pushButton_footIK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'footIK_r_ctr', addSelection = None))


        self.pushButton_footIK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_footIK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='footIK_r_ctr', addSelection = True))

        self.pushButton_legPole_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_legPole_L.setGeometry(QtCore.QRect(270, 320, 16, 16))
        self.pushButton_legPole_L.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.pushButton_legPole_L.setText("")
        self.pushButton_legPole_L.setObjectName("pushButton_9")
        self.pushButton_legPole_L.clicked.connect(lambda: self.SelectControl(ControlName = 'legPole_l_ctr', addSelection = None))


        self.pushButton_legPole_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_legPole_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legPole_l_ctr', addSelection = True))

        self.pushButton_legPole_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_legPole_R.setGeometry(QtCore.QRect(170, 320, 16, 16))
        self.pushButton_legPole_R.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.pushButton_legPole_R.setText("")
        self.pushButton_legPole_R.setObjectName("pushButton_10")
        self.pushButton_legPole_R.clicked.connect(lambda: self.SelectControl(ControlName = 'legPole_r_ctr', addSelection = None))

        self.pushButton_legPole_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_legPole_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legPole_r_ctr', addSelection = True))


        self.pushButton_shoulderFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_shoulderFK_L.setGeometry(QtCore.QRect(270, 100, 16, 16))
        self.pushButton_shoulderFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_shoulderFK_L.setText("")
        self.pushButton_shoulderFK_L.setObjectName("pushButton_11")
        self.pushButton_shoulderFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'shoulderFK_l_ctr', addSelection = None))
        
        self.pushButton_shoulderFK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_shoulderFK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='shoulderFK_l_ctr', addSelection = True))


        self.pushButton_elbowFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_elbowFK_L.setGeometry(QtCore.QRect(320, 100, 16, 16))
        self.pushButton_elbowFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_elbowFK_L.setText("")
        self.pushButton_elbowFK_L.setObjectName("pushButton_12")
        self.pushButton_elbowFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'elbowFK_l_ctr', addSelection = None))

        self.pushButton_elbowFK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_elbowFK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='elbowFK_l_ctr', addSelection = True))


        self.pushButton_handFK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_handFK_L.setGeometry(QtCore.QRect(370, 100, 16, 16))
        self.pushButton_handFK_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_handFK_L.setText("")
        self.pushButton_handFK_L.setObjectName("pushButton_13")
        self.pushButton_handFK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'handFK_l_ctr', addSelection = None))

        self.pushButton_handFK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_handFK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='handFK_l_ctr', addSelection = True))


        self.pushButton_shoulderFK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_shoulderFK_R.setGeometry(QtCore.QRect(170, 100, 16, 16))
        self.pushButton_shoulderFK_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_shoulderFK_R.setText("")
        self.pushButton_shoulderFK_R.setObjectName("pushButton_14")
        self.pushButton_shoulderFK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'shoulderFK_r_ctr', addSelection = None))

        self.pushButton_shoulderFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_shoulderFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='shoulderFK_r_ctr', addSelection = True))


        self.pushButton_elbowFK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_elbowFK_R.setGeometry(QtCore.QRect(120, 100, 16, 16))
        self.pushButton_elbowFK_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_elbowFK_R.setText("")
        self.pushButton_elbowFK_R.setObjectName("pushButton_15")
        self.pushButton_elbowFK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'elbowFK_r_ctr', addSelection = None))

        self.pushButton_elbowFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_elbowFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='elbowFK_r_ctr', addSelection = True))


        self.pushButton_handFK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_handFK_R.setGeometry(QtCore.QRect(70, 100, 16, 16))
        self.pushButton_handFK_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_handFK_R.setText("")
        self.pushButton_handFK_R.setObjectName("pushButton_16")
        self.pushButton_handFK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'handFK_r_ctr', addSelection = None))
        
        self.pushButton_handFK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_handFK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='handFK_r_ctr', addSelection = True))


        self.pushButton_handIK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_handIK_L.setGeometry(QtCore.QRect(370, 80, 16, 16))
        self.pushButton_handIK_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_handIK_L.setText("")
        self.pushButton_handIK_L.setObjectName("pushButton_17")
        self.pushButton_handIK_L.clicked.connect(lambda: self.SelectControl(ControlName = 'handIK_l_ctr', addSelection = None))

        self.pushButton_handIK_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_handIK_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='handIK_l_ctr', addSelection = True))


        self.pushButton_handIK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_handIK_R.setGeometry(QtCore.QRect(70, 80, 16, 16))
        self.pushButton_handIK_R.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_handIK_R.setText("")
        self.pushButton_handIK_R.setObjectName("pushButton_18")
        self.pushButton_handIK_R.clicked.connect(lambda: self.SelectControl(ControlName = 'handIK_r_ctr', addSelection = None))

        self.pushButton_handIK_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_handIK_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='handIK_r_ctr', addSelection = True))


        self.pushButton_armPole_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_armPole_L.setGeometry(QtCore.QRect(320, 80, 16, 16))
        self.pushButton_armPole_L.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.pushButton_armPole_L.setText("")
        self.pushButton_armPole_L.setObjectName("pushButton_19")
        self.pushButton_armPole_L.clicked.connect(lambda: self.SelectControl(ControlName = 'armPole_l_ctr', addSelection = None))

        self.pushButton_armPole_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_armPole_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armPole_l_ctr', addSelection = True))


        self.pushButton_armPole_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_armPole_R.setGeometry(QtCore.QRect(120, 80, 16, 16))
        self.pushButton_armPole_R.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.pushButton_armPole_R.setText("")
        self.pushButton_armPole_R.setObjectName("pushButton_20")
        self.pushButton_armPole_R.clicked.connect(lambda: self.SelectControl(ControlName = 'armPole_r_ctr', addSelection = None))

        self.pushButton_armPole_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_armPole_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armPole_r_ctr', addSelection = True))


        self.pushButton_upperBody = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_upperBody.setGeometry(QtCore.QRect(220, 220, 21, 21))
        self.pushButton_upperBody.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_upperBody.setText("")
        self.pushButton_upperBody.setObjectName("pushButton_21")
        self.pushButton_upperBody.clicked.connect(lambda: self.SelectControl(ControlName = 'upperBody_c_ctr', addSelection = None))


        self.pushButton_upperBody.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_upperBody.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='upperBody_c_ctr', addSelection = True))

        self.pushButton_bendlow_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendlow_R.setGeometry(QtCore.QRect(90, 120, 16, 16))
        self.pushButton_bendlow_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendlow_R.setText("")
        self.pushButton_bendlow_R.setObjectName("pushButton_22")
        self.pushButton_bendlow_R.clicked.connect(lambda: self.SelectControl(ControlName = 'armLowBlend_r_ctr', addSelection = None))

        self.pushButton_bendlow_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendlow_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armLowBlend_r_ctr', addSelection = True))


        self.pushButton_bendMid_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendMid_R.setGeometry(QtCore.QRect(120, 120, 16, 16))
        self.pushButton_bendMid_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendMid_R.setText("")
        self.pushButton_bendMid_R.setObjectName("pushButton_23")
        self.pushButton_bendMid_R.clicked.connect(lambda: self.SelectControl(ControlName = 'armMiddleBlend_r_ctr', addSelection = None))

        self.pushButton_bendMid_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendMid_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armMiddleBlend_r_ctr', addSelection = True))


        self.pushButton_bendHig_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendHig_R.setGeometry(QtCore.QRect(150, 120, 16, 16))
        self.pushButton_bendHig_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendHig_R.setText("")
        self.pushButton_bendHig_R.setObjectName("pushButton_24")
        self.pushButton_bendHig_R.clicked.connect(lambda: self.SelectControl(ControlName = 'armUpBlend_r_ctr', addSelection = None))

        self.pushButton_bendHig_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendHig_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armMiddleBlend_r_ctr', addSelection = True))


        self.pushButton_bendMid_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendMid_L.setGeometry(QtCore.QRect(320, 120, 16, 16))
        self.pushButton_bendMid_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendMid_L.setText("")
        self.pushButton_bendMid_L.setObjectName("pushButton_25")
        self.pushButton_bendMid_L.clicked.connect(lambda: self.SelectControl(ControlName = 'armMiddleBlend_l_ctr', addSelection = None))
        
        self.pushButton_bendMid_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendMid_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armMiddleBlend_l_ctr', addSelection = True))



        self.pushButton_bendHig_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendHig_L.setGeometry(QtCore.QRect(290, 120, 16, 16))
        self.pushButton_bendHig_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendHig_L.setText("")
        self.pushButton_bendHig_L.setObjectName("pushButton_26")
        self.pushButton_bendHig_L.clicked.connect(lambda: self.SelectControl(ControlName = 'armUpBlend_r_ctr', addSelection = None))

        self.pushButton_bendHig_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendHig_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armUpBlend_r_ctr', addSelection = True))



        self.pushButton_bendlow_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendlow_L.setGeometry(QtCore.QRect(350, 120, 16, 16))
        self.pushButton_bendlow_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendlow_L.setText("")
        self.pushButton_bendlow_L.setObjectName("pushButton_27")
        self.pushButton_bendlow_L.clicked.connect(lambda: self.SelectControl(ControlName = 'armLowBlend_l_ctr', addSelection = None))

        self.pushButton_bendlow_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendlow_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armLowBlend_l_ctr', addSelection = True))


        self.pushButton_bendLegLow_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegLow_L.setGeometry(QtCore.QRect(230, 370, 16, 16))
        self.pushButton_bendLegLow_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegLow_L.setText("")
        self.pushButton_bendLegLow_L.setObjectName("pushButton_28")
        self.pushButton_bendLegLow_L.clicked.connect(lambda: self.SelectControl(ControlName = 'legLowBlend_l_ctr', addSelection = None))

        self.pushButton_bendLegLow_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegLow_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legLowBlend_l_ctr', addSelection = True))


        self.pushButton_bendLegMid_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegMid_L.setGeometry(QtCore.QRect(230, 320, 16, 16))
        self.pushButton_bendLegMid_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegMid_L.setText("")
        self.pushButton_bendLegMid_L.setObjectName("pushButton_29")
        self.pushButton_bendLegMid_L.clicked.connect(lambda: self.SelectControl(ControlName = 'legMiddleBlend_l_ctr', addSelection = None))

        self.pushButton_bendLegMid_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegMid_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legMiddleBlend_l_ctr', addSelection = True))


        self.pushButton_bendLegUp_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegUp_L.setGeometry(QtCore.QRect(230, 270, 16, 16))
        self.pushButton_bendLegUp_L.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegUp_L.setText("")
        self.pushButton_bendLegUp_L.setObjectName("pushButton_30")
        self.pushButton_bendLegUp_L.clicked.connect(lambda: self.SelectControl(ControlName = 'legUpBlend_l_ctr', addSelection = None))


        self.pushButton_bendLegUp_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegUp_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legUpBlend_l_ctr', addSelection = True))

        self.pushButton_bendLegUp_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegUp_R.setGeometry(QtCore.QRect(210, 270, 16, 16))
        self.pushButton_bendLegUp_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegUp_R.setText("")
        self.pushButton_bendLegUp_R.setObjectName("pushButton_31")
        self.pushButton_bendLegUp_R.clicked.connect(lambda: self.SelectControl(ControlName = 'legUpBlend_r_ctr', addSelection = None))

        self.pushButton_bendLegUp_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegUp_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legUpBlend_r_ctr', addSelection = True))


        self.pushButton_bendLegMid_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegMid_R.setGeometry(QtCore.QRect(210, 320, 16, 16))
        self.pushButton_bendLegMid_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegMid_R.setText("")
        self.pushButton_bendLegMid_R.setObjectName("pushButton_32")
        self.pushButton_bendLegMid_R.clicked.connect(lambda: self.SelectControl(ControlName = 'legMiddleBlend_l_ctr', addSelection = None))

        self.pushButton_bendLegMid_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegMid_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legMiddleBlend_l_ctr', addSelection = True))


        self.pushButton_bendLegLow_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_bendLegLow_R.setGeometry(QtCore.QRect(210, 370, 16, 16))
        self.pushButton_bendLegLow_R.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_bendLegLow_R.setText("")
        self.pushButton_bendLegLow_R.setObjectName("pushButton_33")
        self.pushButton_bendLegLow_R.clicked.connect(lambda: self.SelectControl(ControlName = 'legLowBlend_l_ctr', addSelection = None))

        self.pushButton_bendLegLow_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_bendLegLow_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legLowBlend_l_ctr', addSelection = True))


        self.pushButton_pelvis = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_pelvis.setGeometry(QtCore.QRect(190, 200, 81, 16))
        self.pushButton_pelvis.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_pelvis.setText("")
        self.pushButton_pelvis.setObjectName("pushButton_34")
        self.pushButton_pelvis.clicked.connect(lambda: self.SelectControl(ControlName = 'pelvis_c_ctr', addSelection = None))

        self.pushButton_pelvis.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_pelvis.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='pelvis_c_ctr', addSelection = True))


        self.pushButton_midSpine = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_midSpine.setGeometry(QtCore.QRect(190, 160, 81, 16))
        self.pushButton_midSpine.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_midSpine.setText("")
        self.pushButton_midSpine.setObjectName("pushButton_35")
        self.pushButton_midSpine.clicked.connect(lambda: self.SelectControl(ControlName = 'middleSpine_c_ctr', addSelection = None))

        self.pushButton_midSpine.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_midSpine.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='middleSpine_c_ctr', addSelection = True))


        self.pushButton_chest = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_chest.setGeometry(QtCore.QRect(190, 120, 81, 16))
        self.pushButton_chest.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton_chest.setText("")
        self.pushButton_chest.setObjectName("pushButton_36")
        self.pushButton_chest.clicked.connect(lambda: self.SelectControl(ControlName = 'chest_c_ctr', addSelection = None))


        self.pushButton_chest.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_chest.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='chest_c_ctr', addSelection = True))

        self.pushButton_head = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_head.setGeometry(QtCore.QRect(220, 30, 21, 21))
        self.pushButton_head.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_head.setText("")
        self.pushButton_head.setObjectName("pushButton_37")
        self.pushButton_head.clicked.connect(lambda: self.SelectControl(ControlName = 'head_c_ctr', addSelection = None))
        

        self.pushButton_head.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_head.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='head_c_ctr', addSelection = True))

        self.pushButton_neck = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_neck.setGeometry(QtCore.QRect(220, 90, 16, 16))
        self.pushButton_neck.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_neck.setText("")
        self.pushButton_neck.setObjectName("pushButton_38")
        self.pushButton_neck.clicked.connect(lambda: self.SelectControl(ControlName = 'neck_c_ctr', addSelection = None))


        self.pushButton_neck.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_neck.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='neck_c_ctr', addSelection = True))

        self.pushButton_neckBend = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_neckBend.setGeometry(QtCore.QRect(220, 70, 16, 16))
        self.pushButton_neckBend.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.pushButton_neckBend.setText("")
        self.pushButton_neckBend.setObjectName("pushButton_39")
        self.pushButton_neckBend.clicked.connect(lambda: self.SelectControl(ControlName = 'middleNeck_c_ctr', addSelection = None))

        self.pushButton_neckBend.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_neckBend.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='middleNeck_c_ctr', addSelection = True))


        self.pushButton_spineFK1 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineFK1.setGeometry(QtCore.QRect(210, 140, 16, 16))
        self.pushButton_spineFK1.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_spineFK1.setText("")
        self.pushButton_spineFK1.setObjectName("pushButton_40")
        self.pushButton_spineFK1.clicked.connect(lambda: self.SelectControl(ControlName = 'spineFK1_c_ctr', addSelection = None))

        self.pushButton_spineFK1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineFK1.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineFK1_c_ctr', addSelection = True))


        self.pushButton_spineIK1 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineIK1.setGeometry(QtCore.QRect(230, 140, 16, 16))
        self.pushButton_spineIK1.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_spineIK1.setText("")
        self.pushButton_spineIK1.setObjectName("pushButton_41")
        self.pushButton_spineIK1.clicked.connect(lambda: self.SelectControl(ControlName = 'spineIK1_c_ctr', addSelection = None))

        self.pushButton_spineIK1.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineIK1.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineIK1_c_ctr', addSelection = True))


        self.pushButton_spineIK3 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineIK3.setGeometry(QtCore.QRect(230, 180, 16, 16))
        self.pushButton_spineIK3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_spineIK3.setText("")
        self.pushButton_spineIK3.setObjectName("pushButton_42")
        self.pushButton_spineIK3.clicked.connect(lambda: self.SelectControl(ControlName = 'spineIK3_c_ctr', addSelection = None))


        self.pushButton_spineIK3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineIK3.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineIK3_c_ctr', addSelection = True))

        self.pushButton_spineIK2 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineIK2.setGeometry(QtCore.QRect(280, 160, 16, 16))
        self.pushButton_spineIK2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_spineIK2.setText("")
        self.pushButton_spineIK2.setObjectName("pushButton_43")
        self.pushButton_spineIK2.clicked.connect(lambda: self.SelectControl(ControlName = 'spineIK2_c_ctr', addSelection = None))

        self.pushButton_spineIK2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineIK2.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineIK2_c_ctr', addSelection = True))


        self.pushButton_spineFK3 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineFK3.setGeometry(QtCore.QRect(210, 180, 16, 16))
        self.pushButton_spineFK3.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_spineFK3.setText("")
        self.pushButton_spineFK3.setObjectName("pushButton_44")
        self.pushButton_spineFK3.clicked.connect(lambda: self.SelectControl(ControlName = 'spineFK3_c_ctr', addSelection = None))

        self.pushButton_spineFK3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineFK3.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineFK3_c_ctr', addSelection = True))


        self.pushButton_spineFK2 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_spineFK2.setGeometry(QtCore.QRect(170, 160, 16, 16))
        self.pushButton_spineFK2.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_spineFK2.setText("")
        self.pushButton_spineFK2.setObjectName("pushButton_45")
        self.pushButton_spineFK2.clicked.connect(lambda: self.SelectControl(ControlName = 'spineFK2_c_ctr', addSelection = None))

        self.pushButton_spineFK2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_spineFK2.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='spineFK2_c_ctr', addSelection = True))


        self.pushButton_ball_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_ball_L.setGeometry(QtCore.QRect(280, 440, 16, 16))
        self.pushButton_ball_L.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_ball_L.setText("")
        self.pushButton_ball_L.setObjectName("pushButton_46")
        self.pushButton_ball_L.clicked.connect(lambda: self.SelectControl(ControlName = 'toe_r_ctr', addSelection = None))


        self.pushButton_ball_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_ball_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='toe_r_ctr', addSelection = True))


        self.pushButton_ball_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_ball_R.setGeometry(QtCore.QRect(160, 440, 16, 16))
        self.pushButton_ball_R.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.pushButton_ball_R.setText("")
        self.pushButton_ball_R.setObjectName("pushButton_47")
        self.pushButton_ball_R.clicked.connect(lambda: self.SelectControl(ControlName = 'toe_l_ctr', addSelection = None))

        self.pushButton_ball_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.pushButton_ball_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='toe_l_ctr', addSelection = True))



        self.settingsArm_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.settingsArm_L.setGeometry(QtCore.QRect(430, 100, 16, 16))
        self.settingsArm_L.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.settingsArm_L.setText("")
        self.settingsArm_L.setObjectName("settingsArm_L")
        self.settingsArm_L.clicked.connect(lambda: self.SelectControl(ControlName = 'armSettings_l_ctr', addSelection = None))
        
        self.settingsArm_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.settingsArm_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armSettings_l_ctr', addSelection = True))


        self.armSettings_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.armSettings_R.setGeometry(QtCore.QRect(10, 100, 16, 16))
        self.armSettings_R.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.armSettings_R.setText("")
        self.armSettings_R.setObjectName("armSettings_R")
        self.armSettings_R.clicked.connect(lambda: self.SelectControl(ControlName = 'armSettings_r_ctr'))
        
        self.armSettings_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.armSettings_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='armSettings_r_ctr', addSelection = True))


        self.legSettings_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.legSettings_L.setGeometry(QtCore.QRect(240, 460, 16, 16))
        self.legSettings_L.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.legSettings_L.setText("")
        self.legSettings_L.setObjectName("legSettings_R")
        self.legSettings_L.clicked.connect(lambda: self.SelectControl(ControlName = 'legSettings_l_ctr'))
        
        self.legSettings_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.legSettings_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legSettings_l_ctr', addSelection = True))


        self.legSettings_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.legSettings_R.setGeometry(QtCore.QRect(210, 460, 16, 16))
        self.legSettings_R.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.legSettings_R.setText("")
        self.legSettings_R.setObjectName("legSettings_R_2")
        self.legSettings_R.clicked.connect(lambda: self.SelectControl(ControlName = 'legSettings_r_ctr'))


        self.legSettings_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.legSettings_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='legSettings_r_ctr', addSelection = True))

        self.clavicle_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.clavicle_L.setGeometry(QtCore.QRect(260, 70, 16, 16))
        self.clavicle_L.setStyleSheet("\n""background-color: rgb(0, 255, 0);")
        self.clavicle_L.setText("")
        self.clavicle_L.setObjectName("clavicle_L")
        self.clavicle_L.clicked.connect(lambda: self.SelectControl(ControlName = 'clavicle_l_ctr'))
        
        self.clavicle_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.clavicle_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='clavicle_l_ctr', addSelection = True))


        self.clavicle_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.clavicle_R.setGeometry(QtCore.QRect(190, 70, 16, 16))
        self.clavicle_R.setStyleSheet("\n""background-color: rgb(0, 255, 0);")
        self.clavicle_R.setText("")
        self.clavicle_R.setObjectName("clavicleR")
        self.clavicle_R.clicked.connect(lambda: self.SelectControl(ControlName = 'clavicle_r_ctr'))

        self.clavicle_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.clavicle_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='clavicle_r_ctr', addSelection = True))

        self.MATCHIK_FK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.MATCHIK_FK_R.setGeometry(QtCore.QRect(50, 13, 101, 20))
        self.MATCHIK_FK_R.setObjectName("MATCHIK_FK_R")

        self.MATCHIK_FK_R.clicked.connect(lambda: self.armMatch(s = 'r'))


        self.matchIK_FK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.matchIK_FK_L.setGeometry(QtCore.QRect(290, 13, 101, 20))
        self.matchIK_FK_L.setObjectName("matchIK_FK_L")

        self.matchIK_FK_L.clicked.connect(lambda: self.armMatch(s = 'l'))



        self.matchLegIK_FK_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.matchLegIK_FK_R.setGeometry(QtCore.QRect(30, 403, 101, 20))
        self.matchLegIK_FK_R.setObjectName("matchLegIK_FK_R")
        self.matchLegIK_FK_R.clicked.connect(lambda: self.legMatch(s = 'r'))

        self.matchLegIK_FK_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.matchLegIK_FK_L.setGeometry(QtCore.QRect(320, 403, 101, 20))
        self.matchLegIK_FK_L.setObjectName("matchLegIK_FK_L")
        self.matchLegIK_FK_L.clicked.connect(lambda: self.legMatch(s = 'l'))

        self.finger_L0_15 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_15.setGeometry(QtCore.QRect(20, 210, 16, 16))
        self.finger_L0_15.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_15.setText("")
        self.finger_L0_15.setObjectName("finger_L0_15")
        
        self.finger_L0_15.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE03_r_ctr'))

        self.finger_L0_15.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_15.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE03_r_ctr', addSelection = True))

        self.finger_L0_14 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_14.setGeometry(QtCore.QRect(20, 230, 16, 16))
        self.finger_L0_14.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_14.setText("")
        self.finger_L0_14.setObjectName("finger_L0_14")
        
        self.finger_L0_14.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE02_r_ctr'))

        self.finger_L0_14.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_14.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE02_r_ctr', addSelection = True))

        self.finger_L0_13 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_13.setGeometry(QtCore.QRect(20, 250, 16, 16))
        self.finger_L0_13.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_13.setText("")
        self.finger_L0_13.setObjectName("finger_L0_13")
        
        self.finger_L0_13.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE01_r_ctr'))

        self.finger_L0_13.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_13.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE01_r_ctr', addSelection = True))

        self.finger_L0_12 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_12.setGeometry(QtCore.QRect(40, 190, 16, 16))
        self.finger_L0_12.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_12.setText("")
        self.finger_L0_12.setObjectName("finger_L0_12")
        
        self.finger_L0_12.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerD03_r_ctr'))

        self.finger_L0_12.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_12.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerD03_r_ctr', addSelection = True))

        self.finger_L0_7 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_7.setGeometry(QtCore.QRect(80, 250, 16, 16))
        self.finger_L0_7.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_7.setText("")
        self.finger_L0_7.setObjectName("finger_L0_7")
        
        self.finger_L0_7.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB01_r_ctr'))

        self.finger_L0_7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_7.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB01_r_ctr', addSelection = True))

        self.finger_L0_8 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_8.setGeometry(QtCore.QRect(40, 220, 16, 16))
        self.finger_L0_8.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_8.setText("")
        self.finger_L0_8.setObjectName("finger_L0_8")
        
        self.finger_L0_8.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB02_r_ctr'))

        self.finger_L0_8.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_8.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB02_r_ctr', addSelection = True))

        self.finger_L0_6 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_6.setGeometry(QtCore.QRect(80, 190, 16, 16))
        self.finger_L0_6.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_6.setText("")
        self.finger_L0_6.setObjectName("finger_L0_6")
        
        self.finger_L0_6.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC03_r_ctr'))

        self.finger_L0_6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_6.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC03_r_ctr', addSelection = True))

        self.finger_L0_9 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_9.setGeometry(QtCore.QRect(80, 220, 16, 16))
        self.finger_L0_9.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_9.setText("")
        self.finger_L0_9.setObjectName("finger_L0_9")
        
        self.finger_L0_9.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB02_r_ctr'))

        self.finger_L0_9.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_9.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB02_r_ctr', addSelection = True))

        self.finger_L0_5 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_5.setGeometry(QtCore.QRect(60, 250, 16, 16))
        self.finger_L0_5.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_5.setText("")
        
        self.finger_L0_9.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB02_r_ctr'))

        self.finger_L0_9.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_9.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB02_r_ctr', addSelection = True))

        self.finger_L0_5.setObjectName("finger_L0_5")
        self.finger_L0_10 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_10.setGeometry(QtCore.QRect(60, 170, 16, 16))
        self.finger_L0_10.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_10.setText("")
        self.finger_L0_10.setObjectName("finger_L0_10")
        
        self.finger_L0_10.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC03_r_ctr'))

        self.finger_L0_10.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_10.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC03_r_ctr', addSelection = True))


        self.finger_L0_4 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_4.setGeometry(QtCore.QRect(40, 250, 16, 16))
        self.finger_L0_4.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_4.setText("")
        self.finger_L0_4.setObjectName("finger_L0_4")
        
        self.finger_L0_4.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerD01_r_ctr'))

        self.finger_L0_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_4.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerD01_r_ctr', addSelection = True))

        self.finger_L0_11 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_11.setGeometry(QtCore.QRect(60, 220, 16, 16))
        self.finger_L0_11.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_11.setText("")
        self.finger_L0_11.setObjectName("finger_L0_11")
        
        self.finger_L0_11.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC02_r_ctr'))

        self.finger_L0_11.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_11.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC02_r_ctr', addSelection = True))

        self.finger_L0 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0.setGeometry(QtCore.QRect(100, 260, 16, 16))
        self.finger_L0.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0.setText("")
        self.finger_L0.setObjectName("finger_L0")
        
        self.finger_L0.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerA01_r_ctr'))

        self.finger_L0.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerA01_r_ctr', addSelection = True))

        self.finger_L0_3 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_3.setGeometry(QtCore.QRect(110, 240, 16, 16))
        self.finger_L0_3.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_3.setText("")
        self.finger_L0_3.setObjectName("finger_L0_3")
        
        self.finger_L0_3.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerA02_r_ctr'))

        self.finger_L0_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_3.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerA02_r_ctr', addSelection = True))

        self.finger_L0_2 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_L0_2.setGeometry(QtCore.QRect(120, 220, 16, 16))
        self.finger_L0_2.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_L0_2.setText("")
        self.finger_L0_2.setObjectName("finger_L0_2")
        
        self.finger_L0_2.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerA03_r_ctr'))

        self.finger_L0_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_L0_2.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerA03_r_ctr', addSelection = True))

        self.finger_R0_14 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_14.setGeometry(QtCore.QRect(370, 170, 16, 16))
        self.finger_R0_14.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_14.setText("")
        self.finger_R0_14.setObjectName("finger_R0_14")
        
        self.finger_R0_14.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC03_l_ctr'))

        self.finger_R0_14.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_14.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC03_l_ctr', addSelection = True))

        self.finger_R0 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0.setGeometry(QtCore.QRect(320, 240, 16, 16))
        self.finger_R0.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0.setText("")
        self.finger_R0.setObjectName("finger_R0")
        
        self.finger_R0.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC03_l_ctr'))

        self.finger_R0.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC03_l_ctr', addSelection = True))

        self.finger_R0_2 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_2.setGeometry(QtCore.QRect(410, 230, 16, 16))
        self.finger_R0_2.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_2.setText("")
        self.finger_R0_2.setObjectName("finger_R0_2")
        
        self.finger_R0_2.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE02_l_ctr'))

        self.finger_R0_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_2.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE02_l_ctr', addSelection = True))

        self.finger_R0_3 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_3.setGeometry(QtCore.QRect(390, 190, 16, 16))
        self.finger_R0_3.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_3.setText("")
        self.finger_R0_3.setObjectName("finger_R0_3")
        
        self.finger_R0_3.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerD03_l_ctr'))

        self.finger_R0_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_3.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerD03_l_ctr', addSelection = True))

        self.finger_R0_4 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_4.setGeometry(QtCore.QRect(390, 250, 16, 16))
        self.finger_R0_4.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_4.setText("")
        self.finger_R0_4.setObjectName("finger_R0_4")
        
        self.finger_R0_4.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerD01_l_ctr'))

        self.finger_R0_4.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_4.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerD01_l_ctr', addSelection = True))

        self.finger_R0_5 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_5.setGeometry(QtCore.QRect(390, 220, 16, 16))
        self.finger_R0_5.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_5.setText("")
        self.finger_R0_5.setObjectName("finger_R0_5")
        
        self.finger_R0_5.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerD02_l_ctr'))

        self.finger_R0_5.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_5.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerD02_l_ctr', addSelection = True))

        self.finger_R0_6 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_6.setGeometry(QtCore.QRect(370, 250, 16, 16))
        self.finger_R0_6.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_6.setText("")
        self.finger_R0_6.setObjectName("finger_R0_6")
        
        self.finger_R0_6.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC01_l_ctr'))

        self.finger_R0_6.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_6.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC01_l_ctr', addSelection = True))

        self.finger_R00 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R00.setGeometry(QtCore.QRect(330, 260, 16, 16))
        self.finger_R00.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R00.setText("")
        self.finger_R00.setObjectName("finger_R00")
        
        self.finger_R00.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerA01_l_ctr'))

        self.finger_R00.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R00.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerA01_l_ctr', addSelection = True))

        self.finger_R0_7 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_7.setGeometry(QtCore.QRect(370, 220, 16, 16))
        self.finger_R0_7.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_7.setText("")
        self.finger_R0_7.setObjectName("finger_R0_7")
        
        self.finger_R0_7.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerC02_l_ctr'))

        self.finger_R0_7.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_7.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerC02_l_ctr', addSelection = True))

        self.finger_R0_8 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_8.setGeometry(QtCore.QRect(350, 250, 16, 16))
        self.finger_R0_8.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_8.setText("")
        self.finger_R0_8.setObjectName("finger_R0_8")
        
        self.finger_R0_8.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB01_l_ctr'))

        self.finger_R0_8.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_8.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB01_l_ctr', addSelection = True))

        self.finger_R0_9 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_9.setGeometry(QtCore.QRect(350, 220, 16, 16))
        self.finger_R0_9.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_9.setText("")
        self.finger_R0_9.setObjectName("finger_R0_9")
        
        self.finger_R0_9.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB02_l_ctr'))

        self.finger_R0_9.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_9.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB02_l_ctr', addSelection = True))

        self.finger_R0_10 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_10.setGeometry(QtCore.QRect(350, 190, 16, 16))
        self.finger_R0_10.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_10.setText("")
        self.finger_R0_10.setObjectName("finger_R0_10")
        
        self.finger_R0_10.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerB03_l_ctr'))

        self.finger_R0_10.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_10.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerB03_l_ctr', addSelection = True))

        self.finger_R0_11 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_11.setGeometry(QtCore.QRect(410, 250, 16, 16))
        self.finger_R0_11.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_11.setText("")
        self.finger_R0_11.setObjectName("finger_R0_11")
        
        self.finger_R0_11.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE01_l_ctr'))

        self.finger_R0_11.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_11.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE01_l_ctr', addSelection = True))

        self.finger_R0_12 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_12.setGeometry(QtCore.QRect(310, 220, 16, 16))
        self.finger_R0_12.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_12.setText("")
        self.finger_R0_12.setObjectName("finger_R0_12")
        
        self.finger_R0_12.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerA03_l_ctr'))

        self.finger_R0_12.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_12.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerA03_l_ctr', addSelection = True))

        self.finger_R0_13 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.finger_R0_13.setGeometry(QtCore.QRect(410, 210, 16, 16))
        self.finger_R0_13.setStyleSheet("background-color: rgb(255, 163, 15);")
        self.finger_R0_13.setText("")
        self.finger_R0_13.setObjectName("finger_R0_13")
        
        self.finger_R0_13.clicked.connect(lambda: self.SelectControl(ControlName = 'fingerE03_l_ctr'))

        self.finger_R0_13.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.finger_R0_13.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='fingerE03_l_ctr', addSelection = True))

        self.showHand_L = QtWidgets.QPushButton(self.bodyTab_layout)
        self.showHand_L.setGeometry(QtCore.QRect(350, 280, 51, 20))
        self.showHand_L.setStyleSheet("background-color: rgb(255, 0, 0);\n""color: rgb(255, 255, 255);")
        self.showHand_L.setObjectName("showHand_L")
        self.showHand_L.clicked.connect(lambda: self.hideSomething(n='handRig_l_grp'))


        self.showHand_R = QtWidgets.QPushButton(self.bodyTab_layout)
        self.showHand_R.setGeometry(QtCore.QRect(40, 280, 51, 20))
        self.showHand_R.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.showHand_R.setObjectName("showHand_R")
        self.showHand_R.clicked.connect(lambda: self.hideSomething(n='handRig_r_grp'))




        self.pushButton_48 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_48.setGeometry(QtCore.QRect(50, 40, 101, 23))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_48.clicked.connect(lambda: self.SwitchIKFK(attr = 'armSettings_r_ctr.Arm_IK'))
    
        self.pushButton_49 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_49.setGeometry(QtCore.QRect(290, 40, 101, 23))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_49.clicked.connect(lambda: self.SwitchIKFK(attr = 'armSettings_l_ctr.Arm_IK'))

        self.pushButton_50 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_50.setGeometry(QtCore.QRect(320, 430, 101, 23))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_50.clicked.connect(lambda: self.SwitchIKFK(attr = 'legSettings_l_ctr.Leg_IK'))


        self.pushButton_51 = QtWidgets.QPushButton(self.bodyTab_layout)
        self.pushButton_51.setGeometry(QtCore.QRect(30, 430, 101, 23))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_51.clicked.connect(lambda: self.SwitchIKFK(attr = 'legSettings_r_ctr.Leg_IK'))

        self.tabWidget.addTab(self.bodyTab_layout, "")
        self.faceTab_layout = QtWidgets.QWidget()
        self.faceTab_layout.setObjectName("faceTab_layout")


        imgPath = os.path.join(os.path.dirname(__file__),  'image_TeddyPicker')#int    

        IMG_Face_Piero_Path = os.path.join(imgPath, 'IMG_Face_Piero.png')

        self.IMG_Face_Piero = QtWidgets.QLabel(self.faceTab_layout)
        self.IMG_Face_Piero.setGeometry(QtCore.QRect(-20, 10, 451, 491))
        self.IMG_Face_Piero.setText("")
        self.IMG_Face_Piero.setPixmap(QtGui.QPixmap(IMG_Face_Piero_Path))
        self.IMG_Face_Piero.setObjectName("IMG_Face_Piero")

        self.eyeUp_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUp_R.setGeometry(QtCore.QRect(160, 140, 21, 16))
        self.eyeUp_R.setText("")
        self.eyeUp_R.setObjectName("eyeUp_R")

        self.eyeUp_R.clicked.connect(lambda: self.SelectControl(ControlName = 'upEyelidsMain_r_ctr'))        
        self.eyeUp_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.eyeUp_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='upEyelidsMain_r_ctr', addSelection = True))


        self.eyeUp_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUp_L.setGeometry(QtCore.QRect(270, 140, 20, 16))
        self.eyeUp_L.setText("")
        self.eyeUp_L.setObjectName("eyeUp_L")

        self.eyeUp_L.clicked.connect(lambda: self.SelectControl(ControlName = 'upEyelidsMain_l_ctr'))       
        self.eyeUp_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.eyeUp_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='upEyelidsMain_l_ctr', addSelection = True))


        self.eyeDw_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDw_L.setGeometry(QtCore.QRect(270, 170, 20, 16))
        self.eyeDw_L.setText("")
        self.eyeDw_L.setObjectName("eyeDw_L")
        self.eyeDw_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDw_R.setGeometry(QtCore.QRect(170, 170, 21, 16))
        self.eyeDw_R.setText("")
        self.eyeDw_R.setObjectName("eyeDw_R")
        self.mainLipsDw = QtWidgets.QPushButton(self.faceTab_layout)
        self.mainLipsDw.setGeometry(QtCore.QRect(220, 350, 41, 16))
        self.mainLipsDw.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.mainLipsDw.setText("")
        self.mainLipsDw.setObjectName("mainLipsDw")
        self.mainLipsUp = QtWidgets.QPushButton(self.faceTab_layout)
        self.mainLipsUp.setGeometry(QtCore.QRect(220, 330, 41, 16))
        self.mainLipsUp.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.mainLipsUp.setText("")
        self.mainLipsUp.setObjectName("mainLipsUp")
        self.browMain_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.browMain_L.setGeometry(QtCore.QRect(250, 110, 81, 20))
        self.browMain_L.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.browMain_L.setText("")
        self.browMain_L.setObjectName("browMain_L")

        self.browMain_L.clicked.connect(lambda: self.SelectControl(ControlName = 'browsMain_l_ctr'))       
        self.browMain_L.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.browMain_L.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='browsMain_l_ctr', addSelection = True))


        self.browMain_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.browMain_R.setGeometry(QtCore.QRect(120, 110, 81, 20))
        self.browMain_R.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.browMain_R.setText("")
        self.browMain_R.setObjectName("browMain_R")

        self.browMain_R.clicked.connect(lambda: self.SelectControl(ControlName = 'browsMain_r_ctr'))       
        self.browMain_R.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.browMain_R.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='browsMain_r_ctr', addSelection = True))



        self.brow01_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow01_L.setGeometry(QtCore.QRect(250, 90, 16, 16))
        self.brow01_L.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow01_L.setText("")
        self.brow01_L.setObjectName("brow01_L")
        self.brow02_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow02_L.setGeometry(QtCore.QRect(280, 90, 16, 16))
        self.brow02_L.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow02_L.setText("")
        self.brow02_L.setObjectName("brow02_L")
        self.brow03_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow03_L.setGeometry(QtCore.QRect(310, 90, 16, 16))
        self.brow03_L.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow03_L.setText("")
        self.brow03_L.setObjectName("brow03_L")
        self.brow01_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow01_R.setGeometry(QtCore.QRect(180, 90, 16, 16))
        self.brow01_R.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow01_R.setText("")
        self.brow01_R.setObjectName("brow01_R")
        self.brow02_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow02_R.setGeometry(QtCore.QRect(150, 90, 16, 16))
        self.brow02_R.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow02_R.setText("")
        self.brow02_R.setObjectName("brow02_R")
        self.brow03_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.brow03_R.setGeometry(QtCore.QRect(120, 90, 16, 16))
        self.brow03_R.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.brow03_R.setText("")
        self.brow03_R.setObjectName("brow03_R")
        self.ear_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.ear_L.setGeometry(QtCore.QRect(360, 260, 21, 21))
        self.ear_L.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.ear_L.setText("")
        self.ear_L.setObjectName("ear_L")
        self.ear_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.ear_R.setGeometry(QtCore.QRect(80, 270, 21, 21))
        self.ear_R.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.ear_R.setText("")
        self.ear_R.setObjectName("ear_R")
        self.eyeUpInt_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUpInt_L.setGeometry(QtCore.QRect(360, 60, 16, 16))
        self.eyeUpInt_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.eyeUpInt_L.setText("")
        self.eyeUpInt_L.setObjectName("eyeUpInt_L")
        self.eyeUpCen_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUpCen_L.setGeometry(QtCore.QRect(390, 40, 16, 16))
        self.eyeUpCen_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.eyeUpCen_L.setText("")
        self.eyeUpCen_L.setObjectName("eyeUpCen_L")
        self.eyeUpExt_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUpExt_L.setGeometry(QtCore.QRect(420, 60, 16, 16))
        self.eyeUpExt_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.eyeUpExt_L.setText("")
        self.eyeUpExt_L.setObjectName("eyeUpExt_L")
        self.eyeIntUp_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeIntUp_R.setGeometry(QtCore.QRect(70, 60, 16, 16))
        self.eyeIntUp_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeIntUp_R.setText("")
        self.eyeIntUp_R.setObjectName("eyeIntUp_R")
        self.eyeUpCen_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUpCen_R.setGeometry(QtCore.QRect(40, 40, 16, 16))
        self.eyeUpCen_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeUpCen_R.setText("")
        self.eyeUpCen_R.setObjectName("eyeUpCen_R")
        self.eyeUpExt_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeUpExt_R.setGeometry(QtCore.QRect(10, 60, 16, 16))
        self.eyeUpExt_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeUpExt_R.setText("")
        self.eyeUpExt_R.setObjectName("eyeUpExt_R")
        self.eyeDwInt_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwInt_L.setGeometry(QtCore.QRect(360, 80, 16, 16))
        self.eyeDwInt_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.eyeDwInt_L.setText("")
        self.eyeDwInt_L.setObjectName("eyeDwInt_L")
        self.eyeDwCen_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwCen_L.setGeometry(QtCore.QRect(390, 100, 16, 16))
        self.eyeDwCen_L.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(255, 0, 0);")
        self.eyeDwCen_L.setText("")
        self.eyeDwCen_L.setObjectName("eyeDwCen_L")
        self.eyeDwExt_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwExt_L.setGeometry(QtCore.QRect(420, 80, 16, 16))
        self.eyeDwExt_L.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.eyeDwExt_L.setText("")
        self.eyeDwExt_L.setObjectName("eyeDwExt_L")
        self.eyeDwInt_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwInt_R.setGeometry(QtCore.QRect(70, 80, 16, 16))
        self.eyeDwInt_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeDwInt_R.setText("")
        self.eyeDwInt_R.setObjectName("eyeDwInt_R")
        self.eyeDwCen_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwCen_R.setGeometry(QtCore.QRect(40, 100, 16, 16))
        self.eyeDwCen_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeDwCen_R.setText("")
        self.eyeDwCen_R.setObjectName("eyeDwCen_R")
        self.eyeDwExt_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeDwExt_R.setGeometry(QtCore.QRect(10, 80, 16, 16))
        self.eyeDwExt_R.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.eyeDwExt_R.setText("")
        self.eyeDwExt_R.setObjectName("eyeDwExt_R")
        self.nose = QtWidgets.QPushButton(self.faceTab_layout)
        self.nose.setGeometry(QtCore.QRect(220, 130, 16, 16))
        self.nose.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.nose.setText("")
        self.nose.setObjectName("nose")
        self.septum = QtWidgets.QPushButton(self.faceTab_layout)
        self.septum.setGeometry(QtCore.QRect(220, 190, 16, 16))
        self.septum.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.septum.setText("")
        self.septum.setObjectName("septum")
        self.noseTip = QtWidgets.QPushButton(self.faceTab_layout)
        self.noseTip.setGeometry(QtCore.QRect(220, 260, 16, 16))
        self.noseTip.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.noseTip.setText("")
        self.noseTip.setObjectName("noseTip")
        self.nostrol_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.nostrol_L.setGeometry(QtCore.QRect(250, 230, 16, 16))
        self.nostrol_L.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.nostrol_L.setText("")
        self.nostrol_L.setObjectName("nostrol_L")
        self.nostrol_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.nostrol_R.setGeometry(QtCore.QRect(190, 230, 16, 16))
        self.nostrol_R.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.nostrol_R.setText("")
        self.nostrol_R.setObjectName("nostrol_R")
        self.cheek_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.cheek_R.setGeometry(QtCore.QRect(320, 320, 16, 16))
        self.cheek_R.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.cheek_R.setText("")
        self.cheek_R.setObjectName("cheek_R")
        self.cheek_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.cheek_L.setGeometry(QtCore.QRect(130, 320, 16, 16))
        self.cheek_L.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.cheek_L.setText("")
        self.cheek_L.setObjectName("cheek_L")
        self.jaw = QtWidgets.QPushButton(self.faceTab_layout)
        self.jaw.setGeometry(QtCore.QRect(200, 450, 81, 20))
        self.jaw.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.jaw.setText("")
        self.jaw.setObjectName("jaw")



        self.squetchNose = QtWidgets.QPushButton(self.faceTab_layout)
        self.squetchNose.setGeometry(QtCore.QRect(220, 280, 16, 16))
        self.squetchNose.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.squetchNose.setText("")
        self.squetchNose.setObjectName("squetchNose")

        self.squetchNose.clicked.connect(lambda: self.SelectControl(ControlName = 'noseSquetch_c_ctr'))       
        self.squetchNose.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.squetchNose.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='noseSquetch_c_ctr', addSelection = True))


        self.lipDw_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipDw_R.setGeometry(QtCore.QRect(190, 360, 16, 16))
        self.lipDw_R.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(85, 170, 255);")
        self.lipDw_R.setText("")
        self.lipDw_R.setObjectName("lipDw_R")
        self.lipDw_C = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipDw_C.setGeometry(QtCore.QRect(230, 370, 16, 16))
        self.lipDw_C.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lipDw_C.setText("")
        self.lipDw_C.setObjectName("lipDw_C")
        self.lipDw_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipDw_L.setGeometry(QtCore.QRect(260, 360, 16, 16))
        self.lipDw_L.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(255, 0, 0);")
        self.lipDw_L.setText("")
        self.lipDw_L.setObjectName("lipDw_L")
        self.lipUp_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipUp_R.setGeometry(QtCore.QRect(190, 320, 16, 16))
        self.lipUp_R.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(85, 170, 255);")
        self.lipUp_R.setText("")
        self.lipUp_R.setObjectName("lipUp_R")
        self.lipUp_C = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipUp_C.setGeometry(QtCore.QRect(230, 310, 16, 16))
        self.lipUp_C.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.lipUp_C.setText("")
        self.lipUp_C.setObjectName("lipUp_C")
        self.lipUp_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipUp_L.setGeometry(QtCore.QRect(260, 320, 16, 16))
        self.lipUp_L.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(255, 0, 0);")
        self.lipUp_L.setText("")
        self.lipUp_L.setObjectName("lipUp_L")
        self.lipCorner_r = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipCorner_r.setGeometry(QtCore.QRect(280, 340, 16, 16))
        self.lipCorner_r.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(255, 0, 0);")
        self.lipCorner_r.setText("")
        self.lipCorner_r.setObjectName("lipCorner_r")
        self.lipCorner_l = QtWidgets.QPushButton(self.faceTab_layout)
        self.lipCorner_l.setGeometry(QtCore.QRect(170, 340, 16, 16))
        self.lipCorner_l.setStyleSheet("background-color: rgb(0, 255, 0);\n"
        "background-color: rgb(85, 170, 255);")
        self.lipCorner_l.setText("")
        self.lipCorner_l.setObjectName("lipCorner_l")

        self.lipCorner_l.clicked.connect(lambda: self.SelectControl(ControlName = 'lipMainCorner_r_ctr'))       
        self.lipCorner_l.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.lipCorner_l.customContextMenuRequested.connect(lambda: self.SelectControl(ControlName='lipMainCorner_r_ctr', addSelection = True))



        self.eyeCornerExt_l = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeCornerExt_l.setGeometry(QtCore.QRect(300, 160, 16, 16))
        self.eyeCornerExt_l.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.eyeCornerExt_l.setText("")
        self.eyeCornerExt_l.setObjectName("eyeCornerExt_l")
        self.eyeCornerInt_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeCornerInt_L.setGeometry(QtCore.QRect(240, 160, 16, 16))
        self.eyeCornerInt_L.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.eyeCornerInt_L.setText("")
        self.eyeCornerInt_L.setObjectName("eyeCornerInt_L")
        self.eyeCornerInt_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeCornerInt_R.setGeometry(QtCore.QRect(200, 160, 16, 16))
        self.eyeCornerInt_R.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.eyeCornerInt_R.setText("")
        self.eyeCornerInt_R.setObjectName("eyeCornerInt_R")
        self.eyeCornerExt_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eyeCornerExt_R.setGeometry(QtCore.QRect(140, 160, 16, 16))
        self.eyeCornerExt_R.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.eyeCornerExt_R.setText("")
        self.eyeCornerExt_R.setObjectName("eyeCornerExt_R")
        self.cheek_R_2 = QtWidgets.QPushButton(self.faceTab_layout)
        self.cheek_R_2.setGeometry(QtCore.QRect(310, 230, 16, 16))
        self.cheek_R_2.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.cheek_R_2.setText("")
        self.cheek_R_2.setObjectName("cheek_R_2")
        self.cheek_R_3 = QtWidgets.QPushButton(self.faceTab_layout)
        self.cheek_R_3.setGeometry(QtCore.QRect(140, 230, 16, 16))
        self.cheek_R_3.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.cheek_R_3.setText("")
        self.cheek_R_3.setObjectName("cheek_R_3")
        self.eye_L = QtWidgets.QPushButton(self.faceTab_layout)
        self.eye_L.setGeometry(QtCore.QRect(380, 60, 31, 31))
        self.eye_L.setStyleSheet("background-color: rgb(85, 85, 255);\n"
        "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.eye_L.setText("")
        self.eye_L.setObjectName("eye_L")
        self.eye_R = QtWidgets.QPushButton(self.faceTab_layout)
        self.eye_R.setGeometry(QtCore.QRect(30, 60, 31, 31))
        self.eye_R.setStyleSheet("background-color: rgb(85, 85, 255);\n"
        "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));")
        self.eye_R.setText("")
        self.eye_R.setObjectName("eye_R")



        self.tabWidget.addTab(self.faceTab_layout, "")
        self.verticalLayout_11.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout_11)
        self.gridLayout_botones = QtWidgets.QGridLayout()
        self.gridLayout_botones.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_botones.setObjectName("gridLayout_botones")
        

        #Reset Body
        self.pushButton_ResetBody = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ResetBody.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_ResetBody.setObjectName("pushButton_ResetBody")
        self.pushButton_ResetBody.clicked.connect(lambda: self.Reset(section='body'))
        self.gridLayout_botones.addWidget(self.pushButton_ResetBody, 3, 0, 1, 1)

        #Isolate Head
        self.pushButton_IsolateHead = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_IsolateHead.setStyleSheet("background-color: rgb(65, 140, 230);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_IsolateHead.setObjectName("pushButton_IsolateHead")
        self.gridLayout_botones.addWidget(self.pushButton_IsolateHead, 2, 1, 1, 1)


        #Mirror
        self.pushButton_Mirror = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Mirror.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Mirror.setObjectName("pushButton_DeformArm")
        self.pushButton_Mirror.clicked.connect(self.Mirror)
        self.gridLayout_botones.addWidget(self.pushButton_Mirror, 0, 1, 1, 1)

        #Select All
        self.pushButton_selectAll = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_selectAll.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_selectAll.setObjectName("pushButton_selectAll")
        self.pushButton_selectAll.clicked.connect(self.select_all)      
        self.gridLayout_botones.addWidget(self.pushButton_selectAll, 0, 0, 1, 1)



        self.pushButton_DeformArm_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_DeformArm_2.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_DeformArm_2.setObjectName("pushButton_DeformArm_2")
        self.gridLayout_botones.addWidget(self.pushButton_DeformArm_2, 2, 2, 1, 1)
        self.pushButton_DeformLeg = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_DeformLeg.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_DeformLeg.setObjectName("pushButton_DeformLeg")
        self.gridLayout_botones.addWidget(self.pushButton_DeformLeg, 3, 2, 1, 1)
        
        self.pushButton_IsoleteEyes = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_IsoleteEyes.setStyleSheet("background-color:  rgb(65, 140, 230);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_IsoleteEyes.setObjectName("pushButton_IsoleteEyes")
        self.gridLayout_botones.addWidget(self.pushButton_IsoleteEyes, 3, 1, 1, 1)
        
		#Inverse
        self.pushButton_Inverse = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Inverse.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_Inverse.setObjectName("pushButton_Inverse")
        self.gridLayout_botones.addWidget(self.pushButton_Inverse, 1, 1, 1, 1)
        self.pushButton_Inverse.clicked.connect(self.inverse)





        self.pushButton_ResetSel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ResetSel.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_ResetSel.setObjectName("pushButton_ResetSel")
        self.gridLayout_botones.addWidget(self.pushButton_ResetSel, 2, 0, 1, 1)
        self.pushButton_DisplayBodyControl = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_DisplayBodyControl.setStyleSheet("background-color: rgb(255, 85, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_DisplayBodyControl.setObjectName("pushButton_DisplayBodyControl")
        self.gridLayout_botones.addWidget(self.pushButton_DisplayBodyControl, 0, 2, 1, 1)
        self.pushButton_DisplayFacialControl = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_DisplayFacialControl.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 85, 255);")
        self.pushButton_DisplayFacialControl.setObjectName("pushButton_DisplayFacialControl")
        self.gridLayout_botones.addWidget(self.pushButton_DisplayFacialControl, 1, 2, 1, 1)
        

        #Key. Sel
        self.pushButton_KeySel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_KeySel.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_KeySel.setObjectName("pushButton_KeySel")
        self.gridLayout_botones.addWidget(self.pushButton_KeySel, 1, 0, 1, 1)
        self.pushButton_KeySel.clicked.connect(self.key_selected)
        

        #Reset. Face
        self.pushButton_ResetFacial = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ResetFacial.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_ResetFacial.setObjectName("pushButton_ResetFacial")
        self.gridLayout_botones.addWidget(self.pushButton_ResetFacial, 4, 0, 1, 1)
        self.pushButton_Menu = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_Menu.setObjectName("pushButton_Menu")
        self.gridLayout_botones.addWidget(self.pushButton_Menu, 4, 1, 1, 1)
        self.pushButton_DeformBody = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_DeformBody.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_DeformBody.setObjectName("pushButton_DeformBody")
        self.gridLayout_botones.addWidget(self.pushButton_DeformBody, 4, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_botones)
        self.centralwidget.addLayout(self.verticalLayout_2)

        #self.retranslateUi(Dialog)
        #self.tabWidget.setCurrentIndex(0)
        #QtCore.QMetaObject.connectSlotsByName(Dialog)

    #def retranslateUi(self, Dialog):
        self.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pushButton_48.setText(QtWidgets.QApplication.translate("Dialog", "SWITCH ARM R", None, -1))
        self.pushButton_49.setText(QtWidgets.QApplication.translate("Dialog", "SWITCH ARM L", None, -1))
        self.pushButton_50.setText(QtWidgets.QApplication.translate("Dialog", "SWITCH LEG L", None, -1))
        self.pushButton_51.setText(QtWidgets.QApplication.translate("Dialog", "SWITCH LEG R", None, -1))
        self.MATCHIK_FK_R.setText(QtWidgets.QApplication.translate("Dialog", "MATCH IK/FK", None, -1))
        self.matchIK_FK_L.setText(QtWidgets.QApplication.translate("Dialog", "MATCH IK/FK", None, -1))
        self.matchLegIK_FK_R.setText(QtWidgets.QApplication.translate("Dialog", "MATCH IK/FK", None, -1))
        self.matchLegIK_FK_L.setText(QtWidgets.QApplication.translate("Dialog", "MATCH IK/FK", None, -1))
        self.showHand_L.setText(QtWidgets.QApplication.translate("Dialog", "SHOW", None, -1))
        self.showHand_R.setText(QtWidgets.QApplication.translate("Dialog", "SHOW", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.bodyTab_layout), QtWidgets.QApplication.translate("Dialog", "Body", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.faceTab_layout), QtWidgets.QApplication.translate("Dialog", "Face", None, -1))
        self.pushButton_ResetBody.setText(QtWidgets.QApplication.translate("Dialog", "Reset Body", None, -1))
        self.pushButton_IsolateHead.setText(QtWidgets.QApplication.translate("Dialog", "Isolate Head", None, -1))
        self.pushButton_Mirror.setText(QtWidgets.QApplication.translate("Dialog", "Mirror", None, -1))

        self.pushButton_DeformArm_2.setText(QtWidgets.QApplication.translate("Dialog", "Deform Arm", None, -1))
        self.pushButton_DeformLeg.setText(QtWidgets.QApplication.translate("Dialog", "Deform Leg", None, -1))
        self.pushButton_IsoleteEyes.setText(QtWidgets.QApplication.translate("Dialog", "Isolate Eyes", None, -1))
        self.pushButton_selectAll.setText(QtWidgets.QApplication.translate("Dialog", "Sel. All", None, -1))
        self.pushButton_Inverse.setText(QtWidgets.QApplication.translate("Dialog", "Inverse", None, -1))
        self.pushButton_ResetSel.setText(QtWidgets.QApplication.translate("Dialog", "Reset. Sel", None, -1))
        self.pushButton_DisplayBodyControl.setText(QtWidgets.QApplication.translate("Dialog", "Display Body Control", None, -1))
        self.pushButton_DisplayFacialControl.setText(QtWidgets.QApplication.translate("Dialog", "Display Facial Control", None, -1))
        self.pushButton_KeySel.setText(QtWidgets.QApplication.translate("Dialog", "Key. Sel", None, -1))
        self.pushButton_ResetFacial.setText(QtWidgets.QApplication.translate("Dialog", "Reset Facial", None, -1))
        self.pushButton_Menu.setText(QtWidgets.QApplication.translate("Dialog", "...", None, -1))
        self.pushButton_DeformBody.setText(QtWidgets.QApplication.translate("Dialog", "Deform Body", None, -1))
        self.window()
        

#FUNCTIONS
    def hideSomething(self, n=None):
        if cmds.getAttr('{}.visibility'.format(n)) == True:
            cmds.setAttr('{}.visibility'.format(n), 0)    
        else:
            cmds.setAttr('{}.visibility'.format(n), 1) 

    def SelectControl(self, ControlName = None, addSelection=None):
		name_space = self.text_edit_name_space.text()
		if addSelection == None:
			if name_space:
				cmds.select('{}{}{}'.format(name_space, ':', ControlName))
			else: 	
				cmds.select(ControlName)  
		else:
			if name_space:
				cmds.select('{}{}{}'.format(name_space, ':', ControlName))
			else:
				cmds.select(ControlName)
			cmds.select(ControlName, add=True)	
    def SwitchIKFK(self, attr=None):
        if cmds.getAttr(attr) == 1:
            cmds.setAttr(attr, 0)
        else:
            cmds.setAttr(attr, 1)  
    def Reset(self, section='body'):
        list = cmds.listRelatives('general_c_ctr', ad=True, shapes=False, typ='transform')
        for element in list:
            if '_ctr' in element:
                for axis in 'xyz':
                    try:
                        cmds.setAttr('{}.t{}'.format(element, axis), 0)
                    except:
                        pass
                    try:    
                        cmds.setAttr('{}.r{}'.format(element, axis), 0)
                    except:
                        pass    
            else:
                pass    
    def Mirror(self):
        sel = cmds.ls(sl=True)

        def getRotation(obj):

            xRot = cmds.getAttr('{}.rotateX'.format(obj))
            yRot = cmds.getAttr('{}.rotateY'.format(obj))  
            zRot = cmds.getAttr('{}.rotateZ'.format(obj))    

            return [xRot, yRot, zRot]

        def getPosition(obj):

            xPos = cmds.getAttr('{}.translateX'.format(obj))
            yPos = cmds.getAttr('{}.translateY'.format(obj))  
            zPos = cmds.getAttr('{}.translateZ'.format(obj)) 

            return [xPos, yPos, zPos]                              

        def setRotation(obj, rotList):
            if obj in self.inverted_controls:
            	for axis in self.inverted_controls.get(obj)[1]:
            		rotList[axis] = rotList[axis] * (-1)

            xRot = cmds.setAttr('{}.rotateX'.format(obj), rotList[0])
            yRot = cmds.setAttr('{}.rotateY'.format(obj), rotList[1])  
            zRot = cmds.setAttr('{}.rotateZ'.format(obj), rotList[2]) 

        def setPosition(obj, posList):
            if obj in self.inverted_controls:
                for axis in self.inverted_controls.get(obj)[0]:
                	posList[axis] = posList[axis] * (-1)

            xPos = cmds.setAttr('{}.translateX'.format(obj), posList[0])
            yPos = cmds.setAttr('{}.translateY'.format(obj), posList[1])  
            zPos = cmds.setAttr('{}.translateZ'.format(obj), posList[2]) 
  

        def getOppositeObj(obj):

            oppObj = ''
            if '_l_' in obj:
                oppObj = obj.replace('_l_', '_r_')
            elif '_r_' in obj:
                oppObj = obj.replace('_r_', '_l_')    

            return oppObj

        def mirrorPosition(obj):

            pos = getPosition(obj)
            targetObj = getOppositeObj(obj)

            if targetObj:
                setPosition(targetObj, pos)    

        def mirrorRotation(obj):

            rot = getRotation(obj)
            targetObj = getOppositeObj(obj)

            if targetObj:
                setRotation(targetObj, rot)    
        for eachObj in sel:
            mirrorRotation(eachObj)
            mirrorPosition(eachObj)        
    
    def armMatch(self, s):   
        from maya import cmds
        from maya.api import OpenMaya
        def transfLocation(ctrl_list):
            for elm in ctrl_list:
                source = elm[1]
                destination=elm[0]
                pos = cmds.xform(source, q=1, ws=1, t=1)
                rot = cmds.xform(source, q=1, ws=1, ro=1)
                cmds.xform(destination, ws=1, t=pos)
                cmds.xform(destination, ws=1, ro=rot)
        
        def transfAttr(transf_dict):
            for elm in transf_dict:
                dest=elm
                source = transf_dict[elm]
                curr_value = cmds.getAttr(source)
                cmds.setAttr(dest, curr_value)
               
        def setAttrDict(attr_dict):
            for attr_name in attr_dict:
                value = attr_dict[attr_name]       
                cmds.setAttr(attr_name, value)

        #IK and pole 


        def transfLocIK(match_list):
            for elm in (match_list):
                source = elm[1]
                destination=elm[0]
                pos = cmds.xform(source, q=1, ws=1, t=1)
                rot = cmds.xform(source, q=1, ws=1, ro=1)
                cmds.xform(destination, ws=1, t=pos)
                cmds.xform(destination, ws=1, ro=rot)
                
        def transLocPole(start_jnt, mid_jnt, end_jnt, pole_vector):
            start_pos=cmds.xform(start_jnt, q=1, ws=1,t=1)
            end_pos=cmds.xform(end_jnt, q=1, ws=1,t=1)
            elbow_pos=cmds.xform(mid_jnt, q=1, ws=1,t=1)
            start_vector= OpenMaya.MVector(start_pos)
            end_vector=OpenMaya.MVector(end_pos)
            elbow_vector=OpenMaya.MVector(elbow_pos)
            mid_vector=((end_vector-start_vector)/2.0)+start_vector
            diff_vect=((mid_vector-elbow_vector)*-1)+elbow_vector
            cmds.xform(pole_vector, ws=1,t=list(diff_vect))

        #Match functions

        def FKmatch(side):
            ctrl_list = [['shoulderFK_'+side+'_ctr','shoulderFK_'+side+'_ctr_snap'],
            ['elbowFK_'+side+'_ctr','elbowFK_'+side+'_ctr_snap'],
            ['handFK_'+side+'_ctr','handFK_'+side+'_ctr_snap']]
            transf_dict = {'shoulderFK_'+side+'_ctr.Stretch':'shoulder_'+side+'_jnt.scaleX',
            'elbowFK_'+side+'_ctr.Stretch': 'elbow_'+side+'_jnt.scaleX'}
            attr_dict = {'armSettings_'+side+'_ctr.Arm_IK' : 0}  
            transfLocation(ctrl_list)
            transfAttr(transf_dict)
            setAttrDict(attr_dict)

        def IKmatch(side):
            match_list = [['handIK_'+side+'_ctr','handIK_'+side+'_ctr_snap']]
            pole_vector_dic = {'start':'shoulder_'+side+'_jnt',
                                'mid':'elbow_'+side+'_jnt',
                                'end':'hand_'+side+'_skn', 
                                'pole':'armPole_'+side+'_ctr'}
            attr_dict = {'armSettings_'+side+'_ctr.Arm_IK': 1}
            transfLocIK(match_list)
            setAttrDict(attr_dict)
            transLocPole(pole_vector_dic['start'], pole_vector_dic['mid'],pole_vector_dic['end'], pole_vector_dic['pole'])

        #Position reader

        def switchIKFK(side):
            attr_switch =cmds.getAttr('armSettings_'+side+'_ctr.Arm_IK')
            if attr_switch == 1:
                FKmatch(side)
            else:
                IKmatch(side)

        switchIKFK(s)

    def legMatch(self, s):   
        from maya import cmds
        from maya.api import OpenMaya
        def transfLocation(ctrl_list):
            for elm in ctrl_list:
                source = elm[1]
                destination=elm[0]
                pos = cmds.xform(source, q=1, ws=1, t=1)
                rot = cmds.xform(source, q=1, ws=1, ro=1)
                cmds.xform(destination, ws=1, t=pos)
                cmds.xform(destination, ws=1, ro=rot)
        
        def transfAttr(transf_dict):
            for elm in transf_dict:
                dest=elm
                source = transf_dict[elm]
                curr_value = cmds.getAttr(source)
                cmds.setAttr(dest, curr_value)
               
        def setAttrDict(attr_dict):
            for attr_name in attr_dict:
                value = attr_dict[attr_name]       
                cmds.setAttr(attr_name, value)

        #IK and pole 


        def transfLocIK(match_list):
            for elm in (match_list):
                source = elm[1]
                destination=elm[0]
                pos = cmds.xform(source, q=1, ws=1, t=1)
                rot = cmds.xform(source, q=1, ws=1, ro=1)
                cmds.xform(destination, ws=1, t=pos)
                cmds.xform(destination, ws=1, ro=rot)
                
        def transLocPole(start_jnt, mid_jnt, end_jnt, pole_vector):
            start_pos=cmds.xform(start_jnt, q=1, ws=1,t=1)
            end_pos=cmds.xform(end_jnt, q=1, ws=1,t=1)
            elbow_pos=cmds.xform(mid_jnt, q=1, ws=1,t=1)
            start_vector= OpenMaya.MVector(start_pos)
            end_vector=OpenMaya.MVector(end_pos)
            elbow_vector=OpenMaya.MVector(elbow_pos)
            mid_vector=((end_vector-start_vector)/2.0)+start_vector
            diff_vect=((mid_vector-elbow_vector)*-1)+elbow_vector
            cmds.xform(pole_vector, ws=1,t=list(diff_vect))

        #Match functions

        def FKmatch(side):
            ctrl_list = [['hipFK_'+side+'_ctr','hipFK_'+side+'_ctr_snap'],
            ['kneeFK_'+side+'_ctr','kneeFK_'+side+'_ctr_snap'],
            ['footFK_'+side+'_ctr','footFK_'+side+'_ctr_snap']]
            transf_dict = {'hipFK_'+side+'_ctr.Stretch':'hip_'+side+'_jnt.scaleX',
            'kneeFK_'+side+'_ctr.Stretch': 'knee_'+side+'_jnt.scaleX'}
            attr_dict = {'legSettings_'+side+'_ctr.Leg_IK' : 0}  
            transfLocation(ctrl_list)
            transfAttr(transf_dict)
            setAttrDict(attr_dict)

        def IKmatch(side):
            match_list = [['footIK_'+side+'_ctr','footIK_'+side+'_ctr_snap']]
            pole_vector_dic = {'start':'hip_'+side+'_jnt',
                                'mid':'knee_'+side+'_jnt',
                                'end':'foot_'+side+'_jnt', 
                                'pole':'legPole_'+side+'_ctr'}
            attr_dict = {'legSettings_'+side+'_ctr.Leg_IK': 1}
            transfLocIK(match_list)
            setAttrDict(attr_dict)
            transLocPole(pole_vector_dic['start'], pole_vector_dic['mid'],pole_vector_dic['end'], pole_vector_dic['pole'])

        #Position reader

        def switchIKFK(side):
            attr_switch =cmds.getAttr('legSettings_'+side+'_ctr.Leg_IK')
            if attr_switch == 1:
                FKmatch(side)
            else:
                IKmatch(side)

        switchIKFK(s)
   
    def key_selected(self):
        selection_list = cmds.ls(sl=True)
        for ctr in selection_list:
            cmds.setKeyframe(ctr)	


    def inverse(self):
		sel = cmds.ls(sl=True)

		def getRotation(obj):

			xRot = cmds.getAttr('{}.rotateX'.format(obj))
			yRot = cmds.getAttr('{}.rotateY'.format(obj))  
			zRot = cmds.getAttr('{}.rotateZ'.format(obj))    
			print 'got Rot'

			return [xRot, yRot, zRot]

		def getPosition(obj):

			xPos = cmds.getAttr('{}.translateX'.format(obj))
			yPos = cmds.getAttr('{}.translateY'.format(obj))  
			zPos = cmds.getAttr('{}.translateZ'.format(obj)) 
			print 'got Pos'
			return [xPos, yPos, zPos]                              

		def setRotation(obj, rotList):
			if obj in self.inverted_controls:
				for axis in self.inverted_controls.get(obj)[1]:
					rotList[axis] = rotList[axis] * (-1)
			try:
				xRot = cmds.setAttr('{}.rotateX'.format(obj), rotList[0])
				yRot = cmds.setAttr('{}.rotateY'.format(obj), rotList[1])  
				zRot = cmds.setAttr('{}.rotateZ'.format(obj), rotList[2]) 
			except:
				print 'set Rotation Failed'
				pass	
			print 'setted'
		def setPosition(obj, posList):
			if obj in self.inverted_controls:
				for axis in self.inverted_controls.get(obj)[0]:
					posList[axis] = posList[axis] * (-1)
			try:
				xPos = cmds.setAttr('{}.translateX'.format(obj), posList[0])
				yPos = cmds.setAttr('{}.translateY'.format(obj), posList[1])  
				zPos = cmds.setAttr('{}.translateZ'.format(obj), posList[2]) 
			except:
				print 'set Position Failed'
				pass	
			print 'setted'

		def getOppositeObj(obj):

			oppObj = ''
			if '_l_' in obj:
			    oppObj = obj.replace('_l_', '_r_')
			elif '_r_' in obj:
			    oppObj = obj.replace('_r_', '_l_')    
			print oppObj
			return oppObj

		def mirrorPosition(obj):

			pos = getPosition(obj)
			targetObj = getOppositeObj(obj)

			if targetObj:
			    setPosition(targetObj, pos)    
			print 'mirrorPos'
		def mirrorRotation(obj):

			rot = getRotation(obj)
			targetObj = getOppositeObj(obj)

			if targetObj:
			    setRotation(targetObj, rot)   
			print 'mirrorRot'    
		def inverseCtrl(ctrl):
			initPos = getPosition(ctrl)
			initRot = getRotation(ctrl)

			mirrorCtr = getOppositeObj(ctrl)
			mirrorPos = getPosition(mirrorCtr)
			mirrorRot = getRotation(mirrorCtr)

			setPosition(ctrl, mirrorPos)
			setPosition(mirrorCtr, initPos)
			setRotation(ctrl, mirrorRot)
			setRotation(mirrorCtr, initRot)         
		for eachObj in sel:
			inverseCtrl(eachObj)

    def select_all(self):
        control_list = []
        transform_list = cmds.ls(type='transform')
        for element in transform_list:
            if element.endswith(('_ctr')):
                control_list.append(element)
        cmds.select(cl=True)
        for element in control_list:
            cmds.select(element, add=True)

#import picmap_piero_rc
#import picmap_piero_rc
