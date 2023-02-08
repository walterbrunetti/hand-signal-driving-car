#!/usr/bin/python3

from picamera2 import Picamera2 
import time
import numpy
import pygame
"""
tar -zcvf hand-palm.tar.gz hand-palm

tar -zxvf hand-palm.tar.gz



Default size:
    2592 × 1944
    width x height of the image
"""

def capture():

    pygame.mixer.init()
    pygame.mixer.music.load("bip.wav")


    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration(display=None, main={"size": (640, 480)},)  # diplay None = No preview
    picam2.configure(capture_config)
    picam2.start()


    print("Prepare")
    time.sleep(5)

    all_images = []

    for i in range(2):

        #print("3 seconds")
        #time.sleep(3)

        
        #print("1 second")
        #time.sleep(1)
        

        pygame.mixer.music.play()
        print(f"take {i}")
        #picam2.capture_file(f"hand-palm/palm_{i}.jpg")

        array = picam2.capture_array("main")   # <class 'numpy.ndarray'>  (height, width, 3) 3 channel RGB type formats

        all_images.append(array)

    #print(all_images)
    #print(type(all_images[0]))

    all_images = numpy.array(all_images)  #Test with this commented out
    numpy.save('my_data', all_images)


def capture_video():
    picam2 = Picamera2()
    picam2.start_and_record_video("test.mp4", duration=15)



if __name__ == "__main__":
    capture()
    #capture_video()

