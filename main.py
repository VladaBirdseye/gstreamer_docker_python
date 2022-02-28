from threading import Thread

import gi
import cv2

gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib
from gstreamer import GstContext, GstPipeline, GstApp
from time import sleep

Gst.init(None)
Gst.debug_set_active(True)
Gst.debug_set_default_threshold(3)

main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()

image = cv2.imread("test.jpg")
# cv2.imshow("a", image)
pipeline = Gst.parse_launch("videotestsrc num-buffers=50 ! appsink")
#pipeline = Gst.parse_launch("rtspsrc location=rtsp://aiaccount:yhdSYq8qTS4HZSjb@66.225.150.88:8331/ISAPI/Streaming/Channels/101 !" +
               #             "decodebin ! videoconvert ! appsink")
pipeline.set_state(Gst.State.PLAYING)
appsink = pipeline.get_by_cls(GstApp.AppSink).pop(0)
appsink.connect("new-sample", on_buffer, None)

try:
    while True:
    #    print(cam.isOpened())
        sample = appsink.emit("pull-sample") 
        sleep(0.1)
        print("ing")
        cv2.imwrite("cool.png", image)
except KeyboardInterrupt:
    exit()

pipeline.set_state(Gst.State.NULL)
main_loop.quit()

