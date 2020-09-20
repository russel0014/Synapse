# SYNAPSE-Computer-vision

The AIM is to create a model a neural network to detect objects and recognise face.
- OBJECT DETECTION
  - well computer vision is how a computer views an image a image for a computer is a matrix of 3 channels of rgb.
    we can use supervisedlearning for image classfications a logistic algorithm can be used for this.Logistic regression is a classification algorithm, used when the value of the target variable is categorical in nature. Logistic regression is most commonly used when the data in question has binary output, so when it belongs to one class or another, or is either a 0 or 1.
    We can view a basic image classification with mnist data set at
    https://www.tensorflow.org/tutorials/keras/classification.
    Here a basic deep neural network is created.But this isnt feasible for object detection because here the input images are grayscale images and it wont be feasible because for the fully connected networks would 
    
    
    
    
    
    
    
    
    
    
   - So here we now use a CNN.Now if we have a nxn matrix instead of a node connecting each node we can have the image compared in pieces.\ A training set is trained by mutliplying with the  filter fxf.In the nxn image matrix it detects the features.Now when a image would be used for object detection these filters may be used to analyze these features detect the object.
    Now for a object detection we basically need to use  *CNN* which uses a **RELU** activation  also has **Max Pooling** the features the edges maybe detected more accurately
    and then is connected to **FULLY connected network**
  - A relu function is used to discard the negative values.
   - convolutions can also be padded be stridded each having their own benefits
    Now to implement a object detection code i may use a [yolo alogorithm](https://www.kaggle.com/aruchomu/yolo-v3-object-detection-in-tensorflow) 
    we need a dataset we can used so there are various data sets for training like cocodata set the darknet sets.these inputs have various cropped images of many things.As these database is large we may need a gpu.
    some of the dependcies which we may need:\
    tensorflow\
    numpy\
    opencv\
    tensorflow-gpu(we can use google collab for free gpu)\
    plt or sns for checking accuracy loss\
    keras\
    after these we need to think about the model,anchors,activation functions
    generally a relu activation function is used.
    Now we need to create a CNN layer and apply the convulsions then max pooling and we need to select a right network architecture for implementing this conv layer.
    detection layers are used after CNN layers these do the roles of object localization and anchor boxes we also may need to use Intersection over Union(IOU)\
    In cnn we may slide over the image that is we may use sliding window detection for detecting the features but it may not be the most efficient way to do it so  another way to do this is to turn the fc layers into convolutional layers.\
    NOW Many times while detecting object the grids may detect the same object mutiple times so we use someting as non max supression that doesnt allow the object to be detected multiple time.It discard some boxes.
    Now after defining all these layers we finally make the model
    After making the models we can use te testing data to check whether our model is accurate or not
 - face recogntion
    For face recognition we need to first detect a face 
    we can use open cv for this.We can conver the image into hog format.
    - HOG is based on the idea that local object appearance can be effectively described by the distribution ( histogram ) of edge directions ( oriented gradients ).
      we can also use harcade features for face detection
      but there is a problem that we can just detect a proper straight face. If face is some what rotated it may not be  able to identify the face and a photo of mutlipe faces too wont be detected because we are just encoding the places of landmark location of eyes ears mouth into something like Haarcascade. So Haarcascade has a con: it can not detect non-frontal face images and also boxes sometimes do not include full face, clipping chins or forehead.So we will prefer to train a Deep Convolutional Neural Network.
    - now we can use the object detection algorithm for face detection too .i.e the **YOLO V3**  
    For info on YOLO we Can refer this [pdf](https://pjreddie.com/media/files/papers/YOLOv3.pdf)
   - Though the important problem regarding face recogntion is one shot learning problems.We know that CNN doesnt work accurately on small data set.But in face recognition systems, we want to be able to recognize a person’s identity by just feeding one picture of that person’s face to the system. And, in case, it fails to recognize the picture, it means that this person’s image is not stored in the system’s database.
   - so now we need a similarity function and it is solved by siamese network.Notice that this network is not learning to classify an image directly to any of the output classes. Rather, it is learning a similarity function, which takes two images as input and expresses how similar they are.
   the Siamese Model performances are much better . However there is some gap between the results on training set and validation set which indicate that model is over fitting.
    
