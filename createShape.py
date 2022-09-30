import maya.cmds as mc

def myWindow():
        if mc.window('win', exists = True, q = True):
            mc.deleteUI('win')
        mc.window('win')
        mc.columnLayout()
        mc.textFieldGrp('objName', label = 'Object Name', tx='ball')
        mc.intFieldGrp('numObj', label = 'Number of Objects')
        mc.button(label = 'Create Sphere', c = 'createSpheres()')
        mc.showWindow('win')

def createSpheres():
    myObj = mc.textFieldGrp('objName', tx=True, q = True)
    numObj = mc.intFieldGrp('numObj', v=True, q=True)
    numObj = numObj[0]
    count = 0
    while count < numObj:
        ball = mc.polySphere(n=myObj)
        ball = ball[0]
        mc.setAttr(ball + '.tx', count * 5)
        count += 1
        
myWindow()
