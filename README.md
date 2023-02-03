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
`pip install -r raspberry_requirements.txt`



### Mac
`python3 -m venv <env-name> `
`git clone git@github.com:walterbrunetti/hand-signal-driving-car.git`

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



