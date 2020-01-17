import maya.cmds as cmds

def fg_get_center_position_of_objects(objects):
    # get the bounding box of selected list
    center_position = (0.0, 0.0, 0.0)

    if cmds.ls(objects):
        xmin, ymin, zmin, xmax, ymax, zmax = cmds.exactWorldBoundingBox(objects, ignoreInvisible=True)
        # look for center point
        center_position = (.5 * (xmax + xmin), .5 * (ymax + ymin), .5 * (zmax + zmin))

    return center_position

def create_default_point(point_pos = (0.0, 0.0, 0.0)):
    # create locator
    default_point = cmds.spaceLocator(position=(0.0, 0.0, 0.0), name='point_c_loc')[0]
    default_point_shape = cmds.listRelatives(default_point, shapes=True)[0]
    
    # lock scale and set shape size
    for axis in ['X', 'Y', 'Z']:
        cmds.setAttr('{0}.scale{1}'.format(default_point, axis), lock=True)
        cmds.setAttr('{0}.localScale{1}'.format(default_point_shape, axis), 0.1)
    cmds.setAttr('{0}.translate'.format(default_point), point_pos[0], point_pos[1], point_pos[2])
    
    return [default_point, default_point_shape]

def create_default_point_on_place():
    # look for the position that we wanna create the point (if nothing is selected the point will be created at origin)
    selected_list = cmds.ls(sl=True, flatten=True)
    center_selection_pos = fg_get_center_position_of_objects(selected_list)
    create_default_point(point_pos = center_selection_pos)


def create_multiple_default_point_on_place():
    # look for the position that we wanna create the point (if nothing is selected the point will be created at origin)
    selected_list = cmds.ls(sl=True, flatten=True)
    for selected in selected_list:
        center_selection_pos = fg_get_center_position_of_objects(selected)
        create_default_point(point_pos = center_selection_pos)

create_default_point_on_place()