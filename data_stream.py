
'''\
This Simple program Demonstrates how to use G-Streamer and capture RTSP Frames in Opencv using Python
- Sahil Parekh

@Motifications: Vlad

'''

import multiprocessing as mp
from threading import Thread
import time
import vid_streamv3 as vs
import cv2
import sys

'''
Main class
'''
class mainStreamClass(mp.Process):
    def __init__(self, sources, cam_name, results):
        super().__init__()
        self.camProcess = []
        self.cam_queue = []
        self.stopbit = []
        self.camlink = sources
        self.cam_name = cam_name
        self.framerate = 15
        self.last_image = results
    
    def run(self):

        for source in self.camlink:
            self.cam_queue.append(mp.Queue(maxsize=100))
            self.stopbit.append(mp.Event())
            self.camProcess.append(vs.StreamCapture(source,
                                self.stopbit[-1],
                                self.cam_queue[-1],
                                self.framerate))
            print(source)
            self.camProcess[-1].start()

        # calculate FPS
        lastFTime = time.time()

        while True:
            for i, queue in enumerate(self.cam_queue):                  
                if not queue.empty():
                    cmd, val = queue.get()

                    if cmd == vs.StreamCommands.FRAME:
                        self.last_image[i] = val
                        if val is not None:
                            cv2.imwrite('DATA_STREAM_{}.png'.format(self.cam_name + str(i)), val)


    def stopCamStream(self):
        print('in stopCamStream')

        if self.stopbit is not None:
            self.stopbit.set()
            while not self.cam_queue.empty():
                try:
                    _ = self.cam_queue.get()
                except:
                    break
                self.cam_queue.close()

            self.camProcess.join()


    def get_last_image(self):
        return self.last_image


def print_results(results):
    while True:
        time.sleep(1/15)
        print("aaa---aaa")
        print(results.get_last_image())


if __name__ == "__main__":
    results = {}
    mc = mainStreamClass(["rtsp://aiaccount:Developer123!@10.110.20.12:8801/streaming/channels/3001", "rtsp://aiaccount:Developer123!@10.110.20.12:8801/streaming/channels/3001",
    "rtsp://aiaccount:Developer123!@10.110.20.12:8801/streaming/channels/3001", "rtsp://aiaccount:yhdSYq8qTS4HZSjb@10.91.20.106:8011/Streaming/Channels/101",
    "rtsp://aiaccount:yhdSYq8qTS4HZSjb@10.91.20.106:8011/Streaming/Channels/101",  "rtsp://aiaccount:yhdSYq8qTS4HZSjb@10.6.20.83:554/Streaming/Channels/101"], "c123132", results)
    
    print_cameras = Thread(target=print_results, args=[mc])
    print_cameras.start()
    mc.start()
    
    print_cameras.join()
    mc.join()
    
    