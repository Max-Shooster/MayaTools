import maya.cmds as cmds
import sys

spacing=0

def UiDupObj():
    if cmds.window('UiDupObj', exists = True, query=True):
        cmds.deleteUI('UiDupObj')
    cmds.window('UiDupObj')
    cmds.columnLayout()
    cmds.optionMenu('option', label = 'Primitives')
    cmds.menuItem(l = 'Cone')
    cmds.menuItem(l = 'Cube')
    cmds.menuItem(l = 'Cylinder')
    cmds.menuItem(l = 'Plane')
    cmds.menuItem(l = 'Sphere')
    cmds.menuItem(l = 'Torus')
    cmds.button(l = 'Create Primitive', c = 'spacing = dupObj(spacing)')
    cmds.showWindow()
    
def translateX(prim, spacing):
    val = prim + '.translateX'
    cmds.setAttr(val, spacing*5)
    
def dupObj(space):
    opt = cmds.optionMenu('option', v = True, q = True)
    if opt == 'Cube':
        myCube = cmds.polyCube(name = 'myCube')
        translateX(myCube[0], space)
    elif opt == 'Sphere':
        mySphere = cmds.polySphere(name = 'mySphere')
        translateX(mySphere[0], space)
    elif opt == 'Cylinder':
        myCylinder = cmds.polyCylinder(name = 'myCylinder')
        translateX(myCylinder[0], space)
    elif opt == 'Torus':
        myTorus = cmds.polyTorus(name = 'myTorus')
        translateX(myTorus[0], space)
    elif opt == 'Plane':
        myPlane = cmds.polyPlane(name = 'myPlane')
        translateX(myPlane[0], space)
    elif opt == 'Cone':
        myCone = cmds.polyCone(name = 'myCone')
        translateX(myCone[0], space)
    space += 1
    return(space)
   
def main():
    UiDupObj()

if __name__ == "__main__":
    main()
