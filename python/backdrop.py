
def createModifiedBackdrop():
    
    import nukescripts
    import colorsys

    # create backdrop
    node = nukescripts.autoBackdrop()

    # convert TileColor to HSV
    originalTileColor = node.knob('tile_color').value()
    originalRGB = [(0xFF & originalTileColor >>  i) / 255.0 for i in [24,16,8]]
    originalHSV = colorsys.rgb_to_hsv(originalRGB[0],originalRGB[1],originalRGB[2])
    
    # modify HSV
    
    hue = originalHSV[0]
    saturation = originalHSV[1] /2
    value = originalHSV[2] /2
    
    # convert HSV to TileColor
    newHSV =  [hue,saturation,value]
    newRGB = colorsys.hsv_to_rgb(newHSV[0],newHSV[1],newHSV[2])
    newTileColor = int('%02x%02x%02x%02x' % (newRGB[0]*255,newRGB[1]*255,newRGB[2]*255,255),16)
    
    # set new Tile Color
    node.knob('tile_color').setValue(newTileColor)

#replace the original menu item
nuke.menu('Nodes').addCommand('Other/Backdrop', modifiedBackdrop, icon = 'Backdrop.png')