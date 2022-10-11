import maya.cmds as mc
sel = mc.ls(sl=True)
path = mc.workspace(rd=True, q = True)
for obj in sel:
  mc.setAttr(obj + '.v', 1)
  mc.select(obj)
  mc.file(path + '/blendShapes/' + obj + '.obj', es=True, typ = 'OBJexport')
  mc.setAttr(obj + '.v', 0)
