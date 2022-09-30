import maya.cmds as cmds
import sys

def genPrim():
    list = ['myCube', 'myCylinder', 'myCone', 'myTorus', 'myPlane']
    for i in range(len(list)):
        if list[i] == 'myCube':
            cmds.polyCube(name = 'myCube')
        elif list[i] == 'myCylinder':
            cmds.polyCylinder(name = 'myCylinder')
        elif list[i] == 'myCone':
            cmds.polyCone(name = 'myCone')
        elif list[i] == 'myTorus':
            cmds.polyTorus(name = 'myTorus')
        elif list[i] == 'myPlane':
            cmds.polyPlane(name = 'myPlane')
    spacing = 5
    for i in range(len(list)):
        translateX(list[i], spacing)
        spacing += 5

def translateX(prim, spacing):
    val = prim + '.translateX'
    cmds.setAttr(val, spacing)
   
def main():
    genPrim()

if __name__ == "__main__":
    main()
