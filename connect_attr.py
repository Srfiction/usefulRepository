selected = cmds.ls(sl=True)
orig = selected[0]
dest = selected[1]

for axis in 'xyz':
    for attr in 'trs':
        cmds.connectAttr('{}.{}{}'.format(orig, attr, axis), '{}.{}{}'.format(dest, attr, axis))