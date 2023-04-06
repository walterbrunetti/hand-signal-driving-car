# hand-signal-driving-car
Computer vision project




## Camera 5MP OV5647 v1.3 - Brand: HobbyTronica
The camera module uses the OV5647 sensor capable of 5MP image capture at 2592 x 1944 resolution and 1080P video at 30 fps with H.264 (AVC) codec.



## Installation


## RaspberryPi

### Create env:
```
python3 -m venv <env-name> --system-site-packages
git clone git@github.com:walterbrunetti/hand-signal-driving-car.git

```

### Install requirements:
`sudo apt install libatlas-base-dev   # tensorflow dependency`

activate env

`pip install -r raspberry_requirements.txt`



### Mac
```
python3 -m venv <env-name> 
git clone git@github.com:walterbrunetti/hand-signal-driving-car.git
#activate env
pip install tensorflow==2.11.0
```




## Saving and loading the model

Namely, after training a Keras model, which is stored in a model variable, we like to save it as it is so that on next loading we can skip training and just make predictions. 


Difference between the 3 ways:
https://stackoverflow.com/questions/66827371/difference-between-tf-saved-model-savemodel-path-to-dir-and-tf-keras-model-sa


https://www.tensorflow.org/guide/saved_model
https://keras.io/guides/serialization_and_saving/

https://medium.com/mlearning-ai/why-loading-a-previously-saved-keras-model-gives-different-results-lessons-learned-aeea1014e0ba  --> reasons why loading a model might give different predictions


# Picamera2

Manual: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

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


# Useful links
- How to load images: https://www.tensorflow.org/tutorials/load_data/images
- Complement the link above by adding details on how to train and classify: https://www.tensorflow.org/tutorials/images/classification
- Processing and Augmentation layers: https://www.tensorflow.org/guide/keras/preprocessing_layers
- How to add aumentation: https://www.tensorflow.org/tutorials/images/data_augmentation



## Next steps
- Very NEXT STEP: use same model, remove crop, and improve dataset by generating 100 pics each class, all closer zoom. 

- How to predict or classify a No class/ unclassified image in tensorflow. I am working on a multi-class classification problem. I want the model to detect
- what is a good dataset? in terms of image quality, zoom, brightness, etc
- Model performance: is Relu the best act function? try others + play with hiperparams
- Augmentation: 
    - are these layers being applied inside the model to predict?
        - Note: when preprocessing layers are part of your model, data augmentation is inactive at test time so input images will only be augmented during calls to Model.fit (not Model.evaluate or Model.predict).
    - Try using a dataset only with gestures (white and full background). Ignore images where gestures are far. 
    - Crop images after capturing: https://blog.roboflow.com/why-and-how-to-implement-random-crop-data-augmentation/
    - should augmentation be appield within the model or in dataset directly?


## Augmentation on data (not part of the model)
```
# Option 1
trainAug = Sequential([
	preprocessing.Rescaling(scale=1.0 / 255),
	preprocessing.RandomFlip("horizontal_and_vertical"),
	preprocessing.RandomZoom(
		height_factor=(-0.05, -0.15),
		width_factor=(-0.05, -0.15)),
	preprocessing.RandomRotation(0.3)
])

trainDS = tf.data.Dataset.from_tensor_slices((trainX, trainLabels))
trainDS = (
	trainDS
	.shuffle(BATCH_SIZE * 100)
	.batch(BATCH_SIZE)
	.map(lambda x, y: (trainAug(x), y),
		 num_parallel_calls=tf.data.AUTOTUNE)
	.prefetch(tf.data.AUTOTUNE)
)

# Option 2
def augment_using_ops(images, labels):
	# randomly flip the images horizontally, randomly flip the images
	# vertically, and rotate the images by 90 degrees in the counter
	# clockwise direction
	images = tf.image.random_flip_left_right(images)
	images = tf.image.random_flip_up_down(images)
	images = tf.image.rot90(images)
	# return the image and the label
	return (images, labels)

ds = tf.data.Dataset.from_tensor_slices(imagePaths)
ds = (ds
	.shuffle(len(imagePaths), seed=42)
	.map(load_images, num_parallel_calls=AUTOTUNE)
	.cache()
	.batch(BATCH_SIZE)
	.map(augment_using_ops, num_parallel_calls=AUTOTUNE)
	.prefetch(tf.data.AUTOTUNE)
)



# 2 ways of applying aumentation to data. The model just recieves a dataset with this applied.
# Test/validation DS should not applied augmentation, just rescaling or/and resizing

```
