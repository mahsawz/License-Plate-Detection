# License-Plate-Detection

This repository contains my final project for [Computer Vision course](https://github.com/mahsawz/Computer-Vision-Course), which I did with [@mohammadmahdiabdolahpour](https://github.com/mohammadmahdiabdollahpour).

First, we analyzed the dataset and found that it had 1876 images in class 0, 283 images in class 1, and 568 images in class 2. Therefore, we decided to inspect models that have fewer parameters and higher accuracy, so we decided to train and test the "Xception," "MobileNet," and "ResNet50" models.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/models.png" height=300 width=500>

Since this dataset is too small and lacks images in classes 1, 2, and especially class 1, we had to create some images for these two classes, one of which does not contain a license plate at all and another does not show any details.

Also, we should split the dataset into Train, Validation, and Test to increase the models' accuracy. To the splited dataset, we added the images created by ourselves in the ratio 80-10-10.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/correct-dataset.png" height=200 width=100>

We change the brightness of images by using "V" in HSV color space, which is related to brightness.

Finally, we reached these results, which you can see below.

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/results.png" height=550 width=400>

Here are some of the incorrect predictions made by network:

<img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img1.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img2.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img3.png" height=200 width=200><img src="https://github.com/mahsawz/License-Plate-Detection/blob/main/images/img4.png" height=200 width=200>
