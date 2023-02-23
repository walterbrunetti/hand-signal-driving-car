#!/usr/bin/python3

from picamera2 import Picamera2 
import time
import numpy
import pygame

import argparse

"""
tar -zcvf gestures.tar.gz gestures-photos

tar -zxvf gestures.tar.gz



Default size:
    2592 × 1944
    width x height of the image
"""

def capture(class_name, number_of_captures):

    pygame.mixer.init()
    pygame.mixer.music.load("sound1.mp3")


    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration(display=None, main={"size": (640, 480)},)  # diplay None = No preview
    picam2.configure(capture_config)
    picam2.start()


    print("Prepare yourself...")
    time.sleep(5)

    all_images = []

    for i in range(number_of_captures):

        print("3 seconds")
        pygame.mixer.music.play()
        time.sleep(4)
        
        timestamp = int(time.time())

        print(f"take {i}")
        #picam2.capture_file(f"gestures-photos/{class_name}/{class_name}_{timestamp}.jpg")

        array = picam2.capture_array("main")   # <class 'numpy.ndarray'>  (height, width, 3) 3 channel RGB type formats
        all_images.append(array)


    all_images = numpy.array(all_images)  #Test with this commented out
    numpy.save(f'{class_name}_data_zoom_1', all_images)


def capture_video():
    picam2 = Picamera2()
    picam2.start_and_record_video("test.mp4", duration=15)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(
            description="Capture frames",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument("class_name", help="Classification of the captures", choices=["palm", "punch"])
    parser.add_argument("number_of_captures", help="Number of captures")

    args = parser.parse_args()
    capture(args.class_name, int(args.number_of_captures))
    #capture_video()

