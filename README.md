# SYNAPSE-Computer-vision

The AIM is to create a model a neural network to detect objects and recognise face.
- OBJECT DETECTION
  - well computer vision is how a computer views an image a image for a computer is a matrix of 3 channels of rgb.
    we can use supervisedlearning for image classfications a logistic algorithm can be used for this.Logistic regression is a classification algorithm, used when the value of the target variable is categorical in nature. Logistic regression is most commonly used when the data in question has binary output, so when it belongs to one class or another, or is either a 0 or 1.
    We can view a basic image classification with mnist data set at
    https://www.tensorflow.org/tutorials/keras/classification.
    Here a basic deep neural network is created.But this isnt feasible for object detection because here the input images are grayscale images and it wont be feasible because for the fully connected networks would 
    
    
    
    
    
    
    
    
    
    
   - So here we now use a CNN.Now if we have a nxn matrix instead of a node connecting each node we can have the image compared in pieces.Now a training set is trained by mutliplying with the  filter fxf.In the nxn image matrix it detects the features.Now when a image would be used for object detection these filters may be used to analyze these features detect the object.
    Now for a object detection we basically need to use  *CNN* which uses a *RELU* activation  also has *Max Pooling* the features the edges are detected maybe more accurately
    and then is connected to *FULLY connected network*
  - A relu function is used to discard the neagtive values.
   - convolutions can also be padded be stridded each having their own benefits
    Now to implement a object detection code i may use a yolo alogorithm which is build by 
    we need a dataset we can used so there are various data sets for training like cocodata set the darknet sets.these inputs have various cropped images of many things.As these database is large we may need a gpu.
    some of the dependcies which we may need:
    -1.tensorflow
    -2.numpy
    -3.opencv
    -4.tensorflow-gpu(we can use google collab for free gpu)
    -5.plt or sns for checking accuracy loss
    after these we need to think about the model,anchors,activation functions
    generally a relu activation function is used.
    Now we need to create a CNN layer and apply the conv2d and then max pooling we need to select a right network for implementing this conv layer.
    detection layers are used after CNN layers these do the roles of object localization and anchor boxes we also may need to use intersection using union
    IN cnn we may slide over the image that is we may use sliding window detection but it may not be the most efficient way to do it another way to do this is to turn the fc layers into convolutional layers
    NOW Many times while detecting object the grids may detect the same object mutiple times so we use someting as non max supression that doesnt allow the object to be detected multiple time.It discard some boxes.
    Now after defining all these layers we finally make the mode
    After making the models we can use te testing data to check whether our model is accurate or not
    
    
    
