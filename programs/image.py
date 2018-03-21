import cv2
import pyzed.camera as zcam
import pyzed.types as tp
import pyzed.core as core
import pyzed.defines as sl

camera_settings = sl.PyCAMERA_SETTINGS.PyCAMERA_SETTINGS_BRIGHTNESS
str_camera_settings = "BRIGHTNESS"
step_camera_settings = 1

def main():
    print("Running...")
    init = zcam.PyInitParameters()
    cam = zcam.PyZEDCamera()
    if not cam.is_opened():
        print("Opening ZED Camera...")
    status = cam.open(init)
    if status != tp.PyERROR_CODE.PySUCCESS:
        print(repr(status))
        exit()

    runtime = zcam.PyRuntimeParameters()
    mat = core.PyMat()

    err = cam.grab(runtime)
    if err == tp.PyERROR_CODE.PySUCCESS:
        cam.retrieve_image(mat, sl.PyVIEW.PyVIEW_LEFT)
        cv2.imwrite(r"/home/nvidia/ZED.jpg", mat.get_data())

    cam.close()
    print("\nFINISH")

main()
