import nuke
def extend_plugin_path():
    paths = ["Python","Gizmos","Utilities/pixelfudger3","Utilities/stamps"]
    for path in paths:
        nuke.pluginAddPath(path)

extend_plugin_path()
