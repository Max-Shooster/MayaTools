import maya.cmds as mc
import os
path = mc.workspace(rd = True, q = True)
path = path + 'blendShapes/'
allFiles = os.listdir(path)
print(allFiles)
mc.blendShape('CC_Base_Body', name='FacialBlendShapes')
index = 0
for item in allFiles:
    objCheck = item.split('.')
    objName = objCheck[0]
    if objCheck[1] == 'obj':
        mc.file(path + item, i = True)
        mc.setAttr(objName + '.visibility', 0)
        mc.blendShape('FacialBlendShapes', e = True, t = ['CC_Base_Body', index, objName, 1])
        index += 1