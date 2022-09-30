import maya.cmds as cmds
import sys
import math

def UiDupObj():
    if cmds.window('UiDupObj', exists = True, query=True):
        cmds.deleteUI('UiDupObj')
    cmds.window('UiDupObj')
    cmds.columnLayout()
    cmds.text(l ='Spacing')
    cmds.intField('spacing', v = 5)
    cmds.text(l = 'Row/Col Value') # Note: Requires same row value and column value
    cmds.intField('RowColValue', v=5)
    cmds.button(l = 'Run', c = 'dupObj()')
    cmds.showWindow()

"""
def shift(sel, num, num_y, counter):
    num = 0
    size = 5
    for i in range(size):
        newName = "DupObj" + str(counter)
        cmds.duplicate(name = newName)
        cmds.setAttr(newName + '.tx', (num+1) * 5)
        cmds.setAttr(newName + '.tz', (num_y) * 5)
        num += 1
        counter += 1
    return counter
"""

def dupObj():
    RowColValue = cmds.intField('RowColValue', value = True, q=True)
    numCopies = int(math.pow(RowColValue, 2))
    spacing = cmds.intField('spacing', value = True, q=True)
    sel = cmds.ls(sl = True)
    counter = 1
    count = 0
    num = 0
    grpObjs = []
    for i in range(RowColValue):
        num += 1
        size = RowColValue
        for i in range(size):
            dup = cmds.duplicate(name = "DupObj1")
            grpObjs.append(dup[0])
            cmds.setAttr(dup[0] + '.tx', (num+1) * 5)
            cmds.setAttr(dup[0] + '.tz', (i) * 5)
            counter += 1
        
    cmds.select(grpObjs)
    cmds.group(n='DuppedObjs')
    sel_all = cmds.ls(sl = True)
    
       
def main():
    sel = cmds.ls(sl = True)
    UiDupObj()
    dupObj()

if __name__ == "__main__":
    main()
    
    
