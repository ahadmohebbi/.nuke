#Define Variable for default knob
firstFrame=1001
lastFrame=1100
project_directory='[python {nuke.script_directory()}]'
resolution='HD_1080'
frameHold='FrameHold.firstFrame.setValue(nuke.frame())'
blurExp='[value size]\n[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
mergeExp='[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
filterErodeExp='[value size]\n[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
erodeExp='[value size]\n[if {[value blur]!=0} {return "blur:[value blur]"} else {return " "}]\n[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
dilateExp='[value size]\n[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
addMixExp='[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
keymixExp='[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
rotoPaintExp='[value output]\nLifetime:[value lifetime_type]'
gradeExp='[value channels]\n[if {[value mix] != 1} {return "mix:[value mix]"} else {return " "}]'
cropExp='[value preset]'
keylightExp='[value show]'
cameraTrackerExp='Error:[value solveRMSE]'
camera3Exp='focal:[value focal]\n [value haperture] x [value vaperture]'
camera4Exp='focal:[value focal]\n [value haperture] x [value vaperture]'

nuke.knobDefault('Root.format', resolution)
nuke.knobDefault('Root.project_directory', project_directory)
nuke.knobDefault('Root.first_frame', str(firstFrame))
nuke.knobDefault('Root.last_frame', str(lastFrame))
nuke.knobDefault(frameHold)
nuke.knobDefault('Blur.label', blurExp)
nuke.knobDefault('Merge2.label', mergeExp)
nuke.knobDefault('FilterErode.label', filterErodeExp)
nuke.knobDefault('Erode.label', erodeExp)
nuke.knobDefault('Dilate.label', dilateExp)
nuke.knobDefault('AddMix.label', addMixExp)
nuke.knobDefault('Keymix.label', keymixExp)
nuke.knobDefault('RotoPaint.label', rotoPaintExp)
nuke.knobDefault('Grade.label', gradeExp)
nuke.knobDefault('Crop.label', cropExp)
nuke.knobDefault('OFXuk.co.thefoundry.keylight.keylight_v201.label', keylightExp)
nuke.knobDefault('CameraTracker.label', cameraTrackerExp)
nuke.knobDefault('Camera3.label', camera3Exp)
nuke.knobDefault('Camera4.label', camera4Exp)


def Backdrop():
    import nuke
    nuke.thisNode().knob('appearance').setValue('Border')
    nuke.thisNode().knob('note_font_color').setValue(0xffffffff)
    nuke.thisNode().knob('note_font_size').setValue(55)

def StickyNote():
	import nuke
	nuke.thisNode().knob('note_font_size').setValue(25)
	nuke.thisNode().knob('note_font_color').setValue(0xffffffff)


def classicScanlineRender():
	import nuke
	#create Custom User Tab
	node=nuke.thisNode()
	tab=nuke.Tab_Knob('user', 'User Setting')
	node.addKnob(tab)

	#Define floating silders
	guiSamples=nuke.Double_Knob('gui_samples', 'GUI Samples')
	renerSamples=nuke.Double_Knob('render_samples', 'Render Samples')
	
	#Assign value to floating slider
	guiSamples.setValue(1) #Assign value to floating slider
	renerSamples.setValue(10) #Assign value to floating slider
	
	#Create floating silders
	node.addKnob(guiSamples)
	node.addKnob(renerSamples)

	#Add Expression to samples knob
	gui_cmd='$gui?gui_samples:\nrender_samples'
	nuke.thisNode().knob('samples').setExpression(gui_cmd)

	#Add Expression to label knob
	customExpressions="""GUI Samples:[value samples]
Render Samples:[value render_samples]
[if {[value antialiasing] != "none"} {return "Antialiasing:[value antialiasing]"} else {return " "}]
[if {[value overscan] != "0"} {return "Overscan:[value overscan]"} else {return " "}]
	"""
	nuke.thisNode().knob('label').setValue(customExpressions)
	

def newScanlineRender():
	import nuke
	#create Custom User Tab
	node=nuke.thisNode()
	tab=nuke.Tab_Knob('user', 'User Setting')
	node.addKnob(tab)

	#Define floating silders
	guiSamples=nuke.Double_Knob('gui_samples', 'GUI Samples')
	renerSamples=nuke.Double_Knob('render_samples', 'Render Samples')
	
	#Assign value to floating slider
	guiSamples.setValue(1) #Assign value to floating slider
	renerSamples.setValue(10) #Assign value to floating slider
	
	#Create floating silders
	node.addKnob(guiSamples)
	node.addKnob(renerSamples)

	#Add Expression to samples knob
	gui_cmd='$gui?gui_samples:\nrender_samples'
	nuke.thisNode().knob('samples').setExpression(gui_cmd)

	#Add Expression to label knob
	customExpressions="""Camera Samples:[value camera_sample_mode]
Render Samples:[value render_samples]
[if {[value antialiasing] != "none"} {return "Antialiasing:[value antialiasing]"} else {return " "}]
[if {[value Overscan] != "0"} {return "Overscan:[value Overscan]"} else {return " "}]
	"""
	nuke.thisNode().knob('label').setValue(customExpressions)



nuke.addOnCreate(classicScanlineRender, nodeClass="ScanlineRender")
#nuke.addOnCreate(newScanlineRender, nodeClass="ScanlineRender2")
nuke.addOnCreate(Backdrop, nodeClass="BackdropNode")
nuke.addOnCreate(StickyNote, nodeClass="StickyNote")



# dot
import Dots
m=nuke.menu('Nuke')
n=m.addMenu('Python/NodeGraph',icon='NodeGrapf.png')
n.addCommand ('Dots', 'Dots.Dots()', ',')

# KeepSome
import KeepSome
nuke.menu( 'Nuke' ).addCommand( 'Python/Close all but selected', 'KeepSome.KeepSome()', 'alt+r' )

# Aditive Keyer
nuke.menu( 'Nodes' ).addCommand( 'Keyer/AdditiveKeyer', "nuke.createNode( 'AdditiveKeyer2.gizmo' )")
nuke.menu( 'Nodes' ).addCommand( 'Keyer/DespillMadness', "nuke.createNode( 'DespillMadness.gizmo' )")
