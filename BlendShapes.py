import maya.cmds as mc

def mirrorBSWin():
    if mc.window('mirrorBS', exists = True, q = True):
        mc.deleteUI('mirrorBS')
    mc.window('mirrorBS')
    mc.columnLayout()
    mc.textFieldGrp('find', label = 'Find for:', text = 'L_')
    mc.textFieldGrp('replace', label = 'Replace with:', text = 'R_')
    mc.button(label = 'MirrorBlendShape', c = 'mirrorBS()')
    mc.showWindow('mirrorBS')
    
def mirrorBS():
    find = mc.textFieldGrp('find', text = True, q = True)
    replace = mc.textFieldGrp('replace', text = True, q = True)
    sel = mc.ls(sl=True)
    counter = 0
    baseShape = len(sel)
    for item in sel:
        counter += 1
        if counter == baseShape:
            pass
        else:
            newName = item.replace(find, replace)
            newShape = mc.duplicate(sel[-1], n = newName)
            newName = newShape[0]
            mc.setAttr(newName + '.sz', -1)
            mc.select(newName, sel[-1])
            myWrap = mc.CreateWrap()
            tempBlend = mc.blendShape(item, sel[-1], n = 'tempBlendShape')
            tempBlend = tempBlend[0]
            mc.setAttr(tempBlend + '.' + item, 1)
            dupShape = mc.duplicate(newName)
            mc.delete(newName)
            newName = mc.rename(dupShape[0], newName)
            mc.setAttr(newName + '.sz', 1)
            mc.setAttr(tempBlend + '.' + item, 0)
            mc.delete(sel[-1], ch=True)
mirrorBSWin()