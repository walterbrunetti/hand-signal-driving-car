#!/usr/bin/python3

from picamera2 import Picamera2 
import time



def capture():


    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration()
    picam2.start(show_preview=False)
    time.sleep(1)
    picam2.switch_mode_and_capture_file(capture_config, "image.jpg")



def record_video():

    picam2 = Picamera2()
    picam2.start_and_record_video("test.mp4", duration=15)



if __name__ == "__main__":
    capture()
    #record_video()

