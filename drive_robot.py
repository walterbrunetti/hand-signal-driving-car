
import time
import tensorflow as tf
import numpy as np

CLASS_NAMES = ("palm", "punch")  # hand gestures


def load_model():
    model = tf.keras.models.load_model("/content/op2") 
    return model
    

def classify_prediction(predictions):
    score = tf.nn.softmax(predictions[0])

    prediction_class = CLASS_NAMES[np.argmax(score)]


    # validate delta

    # validate percentage



def run_program():

    model = load_model()

    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration(display=None, main={"size": (640, 480)},)  # diplay None = No preview
    picam2.configure(capture_config)
    picam2.start()


    

    while True:

        time.sleep(2)
        print("capture")


        img = picam2.capture_array("main")
        img_array = tf.expand_dims(img, 0)

        predictions = model.predict(img_array)
        resp = classify_predictions(predictions)

        if resp == "punch":
            print("moving forward")
            time.sleep(2)
        elif resp == "palm":
            print("stop")
        else:
            print("its nothing")

        



if __name__ == "__main__":
    
    run_program()

        
