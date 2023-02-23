# hand-signal-driving-car
Computer vision project




## Camera 5MP OV5647 v1.3 - Brand: HobbyTronica
The camera module uses the OV5647 sensor capable of 5MP image capture at 2592 x 1944 resolution and 1080P video at 30 fps with H.264 (AVC) codec.



## Installation


###RaspberryPi

### Create env:
`python3 -m venv <env-name> --system-site-packages`
`git clone git@github.com:walterbrunetti/hand-signal-driving-car.git`

### Install requirements:
sudo apt install libatlas-base-dev   # tensorflow dependency
activate env
`pip install -r raspberry_requirements.txt`



### Mac
`python3 -m venv <env-name> `
`git clone git@github.com:walterbrunetti/hand-signal-driving-car.git`
activate env
`pip install tensorflow==2.11.0`




## Saving and loading the model

Namely, after training a Keras model, which is stored in a model variable, we like to save it as it is so that on next loading we can skip training and just make predictions. 


Difference between the 3 ways:
https://stackoverflow.com/questions/66827371/difference-between-tf-saved-model-savemodel-path-to-dir-and-tf-keras-model-sa


https://www.tensorflow.org/guide/saved_model
https://keras.io/guides/serialization_and_saving/

https://medium.com/mlearning-ai/why-loading-a-previously-saved-keras-model-gives-different-results-lessons-learned-aeea1014e0ba  --> reasons why loading a model might give different predictions


# Picamera2

The Pi has an Image Signal Processor (ISP) which reads this image from memory. It performs all these cleaning
and processing steps on the pixels that were received from the camera.

The ISP can produce up to two output images for every input frame from the camera:
- Main image: it can be in either RGB or YUV formats.
- Lores image: lower resolution stream, it must be in a YUV format. It must also be no larger than the main image.


Image formats:

For the main stream:
• XBGR8888 - every pixel is packed into 32-bits, with a dummy 255 value at the end, so a pixel would look like [R, G, B,
255] when captured in Python. (These format descriptions can seem counter-intuitive, but the underlying
infrastructure tends to take machine endianness into account, which can mix things up!)
• XRGB8888 - as above, with a pixel looking like [B, G, R, 255].
• RGB888 - 24 bits per pixel, ordered [B, G, R].
• BGR888 - as above, but ordered [R, G, B].
• YUV420 - YUV images with a plane of Y values followed by a quarter plane of U values and then a quarter plane of V
values.
For the lores stream, only 'YUV420' is really used.




## Progress

```
Epoch 5/5
4/4 [==============================] - 2s 503ms/step - loss: 0.6930 - accuracy: 0.5000 - val_loss: 0.6842 - val_accuracy: 0.5000


Epoch 15/15
4/4 [==============================] - 2s 496ms/step - loss: 0.2813 - accuracy: 0.8958 - val_loss: 0.2313 - val_accuracy: 0.8333

Epoch 15/15
6/6 [==============================] - 3s 452ms/step - loss: 0.4502 - accuracy: 0.8421 - val_loss: 0.2383 - val_accuracy: 0.9500

```


## Next steps

- How to predict or classify a No class/ unclassified image in tensorflow. I am working on a multi-class classification problem. I want the model to detect


