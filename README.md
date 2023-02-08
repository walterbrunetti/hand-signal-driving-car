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



```
  # Saved model sanity check
  saved_model = tf.keras.models.load_model(saved_model_path)

  # check predictions are identical
  pred_inputs, _ = next(iter(train_dataset))
  pred = model(pred_inputs, training=False)
  pred2 = saved_model(pred_inputs, training=False)

  tf.debugging.assert_equal(pred, pred2)

```

Using the SavedModel format
```
To Save: tf.saved_model.save(model, path_to_dir)
To Load: model = tf.saved_model.load(path_to_dir)
```
https://www.tensorflow.org/guide/saved_model


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



# Capturing
Open questions:
- image or array capture?
- should I have a layer for resizing or just capture in the desired size?
- queston above is valid for traing and vision captures 

