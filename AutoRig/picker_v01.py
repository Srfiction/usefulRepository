def picker():
    ventanaNombre = 'quickPicker'
    Titulo = 'Picker'
    Alto = 300
    Ancho = 500
    if cmds.window(ventanaNombre, exists=True):
        cmds.deleteUI(ventanaNombre)
    VENTANA = cmds.window(ventanaNombre, title='quickPicker', width=Alto, height = Ancho)
    cmds.rowColumnLayout(numberOfColumns=3, columnOffset=[(1, 'right', 3) ] )    

    cmds.text(label='Head')
    cmds.separator(h=20, style=None)
    cmds.separator(h=20, style=None)


    cmds.text(label='Neck Follow:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=nFollow)
    cmds.separator(h=20, style=None)

    cmds.text(label='Neck Space:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=nSpace)
    cmds.separator(h=20, style=None)



    ###########
    cmds.text(label='Neck')
    cmds.separator(h=20, style=None)
    cmds.separator(h=20, style=None)


    cmds.text(label='Chest Space:')
    cmds.floatSlider(ann='test', min=0, max=1, v=1, dc=cSpace)
    cmds.separator(h=20, style=None)


    #########

    cmds.text(label='Arm')
    cmds.text(label='Left')
    cmds.text(label='Right')



    cmds.text(label='Pin Elbow:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=lPE)
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=rPE)



    cmds.text(label='Hand')
    cmds.text(label='Left')
    cmds.text(label='Right')

    cmds.text(label='Head Space:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=lPE)
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=rPE)

    cmds.text(label='Hip Space:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=lPE)
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=rPE)

    cmds.text(label='Chest Space:')
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=lPE)
    cmds.floatSlider(ann='test', min=0, max=1, v=0, dc=rPE)



    cmds.window(VENTANA, edit=True, width=Alto, height=Ancho)
    cmds.showWindow()         

    def nFollow(on = 1):
        cmds.setAttr('head_c_ctr.FollowHead', on) 

    def nSpace(on = 1):
        cmds.setAttr('head_c_ctr.neckSpace', on)

    def cSpace(on = 1):
        cmds.setAttr('neck_c_ctr.ChestSpace', on)    

    def rPE(on = 1):
        cmds.setAttr('armPole_l_ctr.PinElbow', on)  

    def lPE(on = 1):
        cmds.setAttr('armPole_r_ctr.PinElbow', on)   

    def lPE(on = 1):
        cmds.setAttr('.PinElbow', on)   

    def lPE(on = 1):
        cmds.setAttr('armPole_r_ctr.PinElbow', on)   

    def lPE(on = 1):
        cmds.setAttr('armPole_r_ctr.PinElbow', on)       
    
    
