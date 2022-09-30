ffimport maya.cmds as mc

def myWindow():
        if mc.window('colorCurves', exists = True, q = True):
            mc.deleteUI('colorCurves')
        mc.window('colorCurves')
        mc.gridLayout(nc=3, cw=100)
        mc.button(label = 'blue', c = 'makeColor("blue")', bgc=[0,0,1])
        mc.button(label = 'red', c = 'makeColor("red")', bgc=[1,0,0])
        mc.button(label = 'yellow', c = 'makeColor("yellow")', bgc=[1,1,0])
        mc.showWindow('colorCurves')

def makeColor(myColor):
    sel = mc.ls(sl=True)
    for item in sel:
        shapeNode = mc.listRelatives(item)
        shapeNode = shapeNode[0]
        mc.setAttr(shapeNode + '.overrideEnabled', True)
        if myColor == 'yellow':
            mc.setAttr(shapeNode + '.overrideColor', 17)
        elif myColor == 'red':
            mc.setAttr(shapeNode + '.overrideColor', 13)
        elif myColor == 'blue':
            mc.setAttr(shapeNode + '.overrideColor', 6)
            
myWindow()