import pyyolo
import numpy as np
import sys
import cv2
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl

help(sl)

camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
str_camera_settings = "BRIGHTNESS"
step_camera_settings = 1

darknet_path = '/home/nvidia/pyyolo/darknet'
datacfg = 'cfg/coco.data'
cfgfile = 'cfg/tiny-yolo.cfg'
weightfile = '../darknet/tiny-yolo.weights'
filename = "/home/nvidia/ZED.jpg"
thresh = 0.24
hier_thresh = 0.5

pyyolo.init(darknet_path, datacfg, cfgfile, weightfile)

print("Running...")
init = zcam.PyInitParameters()
init.camera_resolution = sl.PyRESOLUTION.PyRESOLUTION_VGA  # Lowest possible value is VGA
init.camera_fps = 15  # Lowest possible value is 15
init.depth_mode = sl.PyDEPTH_MODE.PyDEPTH_MODE_NONE
cam = zcam.PyZEDCamera()
if not cam.is_opened():
	print("Opening ZED Camera...")
status = cam.open(init)

for i in range(20):
	"""
	if status != tp.PyERROR_CODE.PySUCCESS:
		print(repr(status))
		exit()

	runtime = zcam.PyRuntimeParameters()
	mat = core.PyMat()

	err = cam.grab(runtime)
	if err == tp.PyERROR_CODE.PySUCCESS:
		cam.retrieve_image(mat, sl.PyVIEW.PyVIEW_LEFT)
		cv2.imwrite(r"/home/nvidia/ZED.jpg", mat.get_data())
	"""
	
	# from file
	print('----- test original C using a file')
	outputs = pyyolo.test(filename, thresh, hier_thresh, 0)
	for output in outputs:
		print(output)

cam.close()

