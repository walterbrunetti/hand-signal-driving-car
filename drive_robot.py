
import time
import tensorflow as tf
import numpy as np
from picamera2 import Picamera2 


CLASS_NAMES = ("palm", "punch")  # hand gestures


def load_model():
    model = tf.keras.models.load_model("hand-v1-saved") 
    return model
    

def classify_prediction(predictions):
        

    # validate delta
    prediction_a, prediction_b = predictions[0]
    #[[ 1.2791113  -0.16450806]]  # real palm
    #[[1.701399  1.6643939]] strawberries
    delta = abs(prediction_a - prediction_b)


    # validate percentage
    score = tf.nn.softmax(predictions[0])
    percentage = 100 * np.max(score)


    print(f"delta: {delta} - prediction: {predictions[0]} - percentage: {percentage}%")

    if percentage >= 72 and delta >= 1.01 and (prediction_a >= 0.9 or prediction_b >=0.9):
        prediction_class = CLASS_NAMES[np.argmax(score)]
        return prediction_class


def run_program():

    model = load_model()

    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration(display=None, main={"size": (640, 480)},)  # diplay None = No preview
    picam2.configure(capture_config)
    picam2.start()

    all_images = []
    predictions_result = []

    for i in range(30):
    #while True:

        time.sleep(2)
        print("capture")

        img = picam2.capture_array("main")
        img_array = tf.expand_dims(img, 0)

        predictions = model.predict(img_array)
        resp = classify_prediction(predictions)


        
        all_images.append(img)
        predictions_result.append((resp, predictions[0][0], predictions[0][1]))



        if resp == "punch":
            print("MOVE FORWARD")
            time.sleep(2)
        elif resp == "palm":
            print("STOP")
        else:
            print("its nothing")

    all_images = np.array(all_images)
    np.save(f'live_data_1', all_images)
    all_predictions_result = np.array(predictions_result)
    np.save(f'live_result_1', all_predictions_result)




if __name__ == "__main__":    
    run_program()

