def restorePose():
    c=0
    for i in list:
        key = locatorsDict.keys()[c]
        pos = locatorsDict[key][0]
        cmds.setAttr('{}.t'.format(key), pos[0], pos[1], pos[2])
        c = c + 1
