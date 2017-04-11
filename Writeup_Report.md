# **Behavioral Cloning** 

### By Simon Mijares
---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
-  Use the simulator to collect data of good driving behavior
-  Build, a convolution neural network in Keras that predicts steering angles from images
-  Train and validate the model with a training and validation set
- Test that the model successfully drives around track one without leaving the road
- Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
- model.py containing the script to create and train the model
- drive.py for driving the car in autonomous mode
- model.h5 containing a trained convolution neural network 
- writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

To begin with, the data is normalized and set to a zero centered. Then the top and the bottom is cropped as the examples suggest (model.py lines 47-48).

My model consists of a net of four convolution neural network with 5x5, 5x5, 3x3 & 3x3 filter sizes and depths of 36, 48, 64 & 64 respectively (model.py lines 49-53). The model includes RELU layers to introduce nonlinearity (code line 20), and a tanh at tha last convolutional layer to obtain a positive and negative output assuming that the steering might be positive or negative at any given moment.

Then the network is flatten (line 54) to a full connected layers of 100, 50, 10 and finally one output for the steering.

#### 2. Attempts to reduce overfitting in the model

The model was trained and validated on different data sets to ensure that the model was not overfitting, since the train data consist on three different laps on the regular direction and two laps on reverse direction. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track. During testing, the system could be interrupted to get it close to the lane line and it will try to correct its driving.

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 63).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, some recovering from the left and right sides of the road and recording the track on reverse direction.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to mimic the nvidia model replacing some activation functions.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set (70-30). I found that my first model had not a good performance, so I try recording the tracks with the mouse movement, this doesn't showed mayor improvement. So I returned to the keyboard driven data.
Next I try replacing the activation functions, obtaining the best performance replacing the relu on the last convolutional network with a tanh to obtain positive and negative responses.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture  (model.py lines 46-58) consisted of a net of four convolution neural network with 5x5, 5x5, 3x3 & 3x3 filter sizes and depths of 36, 48, 64 & 64 (model.py lines 49-53). The model includes RELU layers to introduce nonlinearity (code line 20), and a tanh at tha last convolutional layer to obtain a positive and negative output assuming that the steering might be positive or negative. This is connected to a faltten layer (line 54) and to a full connected layers of 100, 50, 10 and finally one output for the steering.

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one driving in the regular direction, a lap in reverse direction, another lap in regular direction and a final lap in reverse. Here is the video of the training & validation data:

**Training Data:**
[![Training Data](https://img.youtube.com/vi/nl1mGM4GZwM/2.jpg)](https://youtu.be/nl1mGM4GZwM)

After the collection process and including the three camera angles I finished with 12161 data points. I then preprocessed this data by centered the range to zero and compressing it between -0.5 and +0.5

I finally randomly shuffled the data set and put 30% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The number of epochs used were 30 as evidenced of a low trainning loss less than 1e-3 and a validation loss around 0.01. I used an adam optimizer so that manually training the learning rate wasn't necessary.

The final performance can be wached in the following video:

**Network Result:**
[![Training Data](https://img.youtube.com/vi/I5HHvozsGI0/0.jpg)](https://youtu.be/I5HHvozsGI0)