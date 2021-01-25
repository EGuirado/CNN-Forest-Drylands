# CNN-Forest-Drylands
Convolutional Neural Network-based model for forest classification with very high resolution satellite imagery. 
## Getting Started

We address the problem of forest/non-forest classifying in large scale areas represented by a large number of images. To build these model, we need to build a training datasets.

### Convolutional Neural Networks with Tensorflow API
We used <a href="https://www.tensorflow.org">TensorFlow</a>, an open source library for numerical computation, specializing in machine learning applications.

This codelab was tested on TensorFlow 1.12

```
pip install --upgrade "tensorflow==1.12.*"
```

Step 1. Presence/absence with Tensorflow (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0)
Architecture: Inception v3
Transfer learning: ImageNet
Data-augmentation:flip left right, random crop, random scale, random brightness

```
  parser.add_argument(
      '--flip_left_right',
      default=True,
      help="""\
      Whether to randomly flip half of the training images horizontally.\
      """,
      action='store_true'
  )
  parser.add_argument(
      '--random_crop',
      type=int,
      default=1,
      help="""\
      A percentage determining how much of a margin to randomly crop off the
      training images.\
      """
  )
  parser.add_argument(
      '--random_scale',
      type=int,
      default=1,
      help="""\
      A percentage determining how much to randomly scale up the size of the
      training images by.\
      """
  )
  parser.add_argument(
      '--random_brightness',
      type=int,
      default=1,
      help="""\
      A percentage determining how much to randomly multiply the training image
      input pixels up or down by.\
      """
  )
```

### Training dataset
We built the first large training datasets for forest/non-forest classification, 30,781 images (Data S2).

### Testing dataset

We focused on global drylands in 4 aridity levels, 4 tree cover levels and 12 regions (16,739 images in total).

## Authors

Publication in progress
Corresponding author Emilio Guirado: e.guirado@ual.es

## Acknowledgments

* Cheng et al. for NWPU-RESISC45 database
* Tensorflow developers
* Google Earth developer team
