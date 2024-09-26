import nuke

def KeepSome():
    selNodes = nuke.selectedNodes()   
    alltheNodes = nuke.allNodes(recurseGroups = True)	
    for nodes in alltheNodes:
        if nodes not in selNodes:
            nodes.hideControlPanel()
        else:
            nodes.showControlPanel()
                