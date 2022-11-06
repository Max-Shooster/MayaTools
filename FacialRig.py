import maya.cmds as mc
import os

def charFaceRigWin(win):
    if mc.window(win, exists=True, q=True):
        mc.deleteUI(win)
    mc.window(win)
    mc.columnLayout()
    mc.textFieldGrp('charName', label = 'Character Name: ', text = 'FaceRig')
    mc.floatFieldGrp('ctrl_pos', label = 'Control Position', nf=2, v1=15, v2=165)
    mc.button(label='Create Face Rig', c='createFaceRig()')
    mc.separator(h=40)
    mc.button(label = 'Clear Scene', c = 'clearScene()')
    mc.showWindow(win)

def clearScene():
    sel = mc.ls(sl=True)
    mc.delete(sel[0], ch=True)
    mc.select('*_Ctrl_Transformer')
    ctrl = mc.ls(sl=True)
    mc.delete(ctrl[0])
    mc.select('*_Blend')
    blendShapes = mc.ls(sl=True)
    for item in blendShapes:
        mc.delete(item)
    mc.select(sel[0])

def createFaceRig():
    sel = mc.ls(sl=True)
    x=mc.floatFieldGrp('ctrl_pos', v1=True, q=True)
    y=mc.floatFieldGrp('ctrl_pos', v2=True, q=True)
    charName = mc.textFieldGrp('charName', text=True, q=True)
    baseHead = sel[0]
    mc.delete(baseHead, ch=True)
    path = mc.workspace(rd=True, q=True)
    path = path + 'blendShapes/'
    allFiles = os.listdir(path)
    blendName = mc.blendShape(baseHead, name= 'FacialBlendShapes')
    blendName = blendName[0]
    index = 0
    faceController(charName, x,y)
    for item in allFiles:
        objCheck = item.split('.')
        objName = objCheck[0]
        if objCheck[1] == 'obj':
            mc.file(path + item, i=True)
            objName = mc.rename(objName, objName + '_Blend') #
            mc.setAttr(objName + '.visibility', 0)
            mc.blendShape('FacialBlendShapes', e=True, t=[baseHead, index, objName, 1])
            index = index + 1
            facePart = objName.split('_')
            if facePart[0] == 'Mouth':
                ctrlName = 'Mouth_ctrl'
                if objName == 'Mouth_Angry_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_Frown_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_Open_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_PressedClose_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_Pucker_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_ShiftLeft_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'tx', 1, 1)
                elif objName == 'Mouth_ShiftRight_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'tx', -1, 1)
                elif objName == 'Mouth_Smile_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                elif objName == 'Mouth_Surprised_Blend':
                    attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                else:
                    attachBlendToCTRL(blendName, objName, ctrlName, objName, 1, 1)
            elif facePart[0] == 'Brow':
                if facePart[-2] == 'R':
                    ctrlName = 'R_Brow_ctrl'
                    if objName == 'Brow_Angry_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Disgusted_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Sad_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Surprised_R_Blend':
                        print(ctrlName)
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    else:
                        attachBlendToCTRL(blendName, objName, ctrlName, objName, 1, 1)
                elif facePart[-2] == 'L':
                    ctrlName = 'L_Brow_ctrl'
                    if objName == 'Brow_Angry_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Disgusted_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Sad_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    elif objName == 'Brow_Surprised_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    else:
                        attachBlendToCTRL(blendName, objName, ctrlName, objName, 1, 1)
            elif facePart[0] == 'Eye':
                if facePart[-2] == 'R':
                    ctrlName = 'R_Eye_ctrl'
                    attachBlendToCTRL('Eye_Geo_R', 'rx', ctrlName, 'ty', -1, 30)
                    attachBlendToCTRL('Eye_Geo_R', 'rx', ctrlName, 'ty', 1, -30)

                    attachBlendToCTRL('Eye_Geo_R', 'ry', ctrlName, 'tx', 1, 30)
                    attachBlendToCTRL('Eye_Geo_R', 'ry', ctrlName, 'tx', -1, -30)

                    if objName == 'Eye_Look_Down_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', -1, 1)
                    elif objName == 'Eye_Look_Left_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'tx', 1, 1)
                    elif objName == 'Eye_Look_Right_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'tx', -1, 1)
                    elif objName == 'Eye_Look_Up_R_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    else:
                        attachBlendToCTRL(blendName, objName, ctrlName, objName, 1, 1)
                elif facePart[-2] == 'L':
                    ctrlName = 'L_Eye_ctrl'
                    attachBlendToCTRL('Eye_Geo_L', 'rx', ctrlName, 'ty', -1, 30)
                    attachBlendToCTRL('Eye_Geo_L', 'rx', ctrlName, 'ty', 1, -30)

                    attachBlendToCTRL('Eye_Geo_L', 'ry', ctrlName, 'tx', 1, 30)
                    attachBlendToCTRL('Eye_Geo_L', 'ry', ctrlName, 'tx', -1, -30)
                    if objName == 'Eye_Look_Down_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', -1, 1)
                    elif objName == 'Eye_Look_Left_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'tx', 1, 1)
                    elif objName == 'Eye_Look_Right_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'tx', -1, 1)
                    elif objName == 'Eye_Look_Up_L_Blend':
                        attachBlendToCTRL(blendName, objName, ctrlName, 'ty', 1, 1)
                    else:
                        attachBlendToCTRL(blendName, objName, ctrlName, objName, 1, 1)

def attachBlendToCTRL(blendName, objName, ctrlName, attrName, dir, bsRange):
    if objName == attrName:
        mc.select(ctrlName)
        mc.addAttr(ln=objName, min=0, max=1, defaultValue=0, k=True)
    bsAttr = blendName + '.' + objName
    print(bsAttr + " BSATTR")
    ctrlAttr = ctrlName + '.' + attrName
    print(ctrlAttr + " CTRLATT")
    mc.setDrivenKeyframe(bsAttr, cd=ctrlAttr)
    mc.setAttr(ctrlAttr, dir*1)
    mc.setAttr(bsAttr, bsRange)
    mc.setDrivenKeyframe(bsAttr, cd=ctrlAttr)
    mc.setAttr(ctrlAttr, 0)

def createCtrl(ctrlName, X,Y):
    square = mc.curve(d=1,p=[(1.25,1.25,0), (1.25,-1.25,0), (-1.25,-1.25,0),(-1.25,1.25,0),(1.25,1.25,0)], n='frame_' + ctrlName)
    circleCtrl = mc.circle(nr=(0,0,1), r=0.25, n=ctrlName + '_ctrl')
    mc.transformLimits(circleCtrl[0], tx=(-1,1), etx=(True,True), ty = (-1,1), ety=(True,True), tz=(0,0), etz=(True,True))
    shape = mc.listRelatives(circleCtrl)
    shape = shape[0]
    mc.setAttr(shape + '.overrideEnabled', 1)
    mc.setAttr(shape + '.overrideColor', 17)
    nameTag = mc.textCurves(t=ctrlName, n=ctrlName + '_tag_')
    mc.setAttr(nameTag[0] + '.ty', 1.25)
    mc.setAttr(nameTag[0] + '.ty', 1.25)
    mc.setAttr(nameTag[0] + '.tx', -1.25)
    mc.setAttr(nameTag[0] + '.sx', 0.5)
    mc.setAttr(nameTag[0] + '.sy', 0.5)
    mc.setAttr(nameTag[0] + '.sz', 0.5)
    mc.setAttr(square + '.template', 1)
    mc.parent(nameTag[0], square)
    grp = mc.group(circleCtrl, name=ctrlName + 'zeroGRP')
    mc.parentConstraint(square, grp)
    grp = mc.group(square, grp, n=ctrlName + '_mainGRP')
    mc.setAttr(grp + '.tx', X)
    mc.setAttr(grp + '.ty', Y)
    return(grp)

def faceController(charName, x,y):
    lBrow = createCtrl('L_Brow', -1.5, 1.5)
    rBrow = createCtrl('R_Brow', 1.5, 1.5)
    lEye = createCtrl('L_Eye', -1.5, -1.5)
    rEye = createCtrl('R_Eye', 1.5, -1.5)
    lNose = createCtrl('L_Nose', -1.5, -4.5)
    rNose = createCtrl('R_Nose', 1.5, -4.5)
    mouth = createCtrl('Mouth', 0, -7.5)
    square = mc.curve(d=1, p=[(3,3.3,0), (3,-9,0), (-3,-9,0), (-3,3.3,0), (3,3.3,0)], n = charName + '_Ctrl_Transformer')
    nameTag = mc.textCurves(t=charName, n=charName + '_tag_')
    mc.setAttr(nameTag[0] + '.ty', 3.5)
    mc.setAttr(nameTag[0] + '.tx', -3)
    mc.setAttr(nameTag[0] + '.template', 1)
    mc.parent(nameTag[0], lBrow, rBrow, lEye, rEye, lNose, rNose, mouth, square)
    mc.setAttr(square + '.tx', x)
    mc.setAttr(square + '.ty', y)
    mc.select(cl=True)
    mc.setAttr('FaceRig_Ctrl_Transformer' + '.tx', 15)
    mc.setAttr('FaceRig_Ctrl_Transformer' + '.ty', 10)
    mc.setAttr('FaceRig_Ctrl_Transformer' + '.tz', 0)

charFaceRigWin('FaceRigWindow')
