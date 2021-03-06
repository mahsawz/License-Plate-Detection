# License-Plate-Detection

This repository contains my final project of [Compute Vision course](https://github.com/mahsawz/Computer-Vision-Course), which I done it with [@mohammadmahdiabdolahpour](https://github.com/mohammadmahdiabdollahpour).

First, We analyze the dataset and understood that it has 1876 images in class 0, 283 images in class 1 and, 568 images in class 2. Therefore, we decided to inspect the models that has less parameter and higher accuracy, so we decided to train and test "Xception", "MobilelNet", and "ResNet50" models.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/models.png" height=300 width=500>

As you see, this dataset is too small and has lacking images in classes 1 and 2, especially class 1, so we decided to create some images of these two classes, one of them is not license plate at all and another is not clear one.

Also, we should split dataset into Train, Validation, and Test to increase models' accuracy. We add that created images by ourselves in ratio 80-10-10 to the splited dataset.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/correct-dataset.png" height=200 width=100>

We change the brightness of images by using "V" of HSV color space, which related to brightness.

Finally, we reach to these result, which you can see in below.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/results.png" height=550 width=400>

Here is some of the incorrect predict by network:

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img1.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img2.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img3.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img4.png" height=200 width=200>
