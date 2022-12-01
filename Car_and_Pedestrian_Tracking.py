'''
import cv2

# Our image
img_file = 'many-cars-on-road-B9RXX5.jpg'

# Our pre trained classifier
classifier_file = 'cars.xml'

# create opencv image
img=cv2.imread(img_file)

# convert to grayscale (needed for haarcascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create car classifier
car_tracker=cv2.CascadeClassifier(classifier_file)

# detect car
cars = car_tracker.detectMultiScale(black_n_white)

# draw rectangles around the cars
for(x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

print(cars)

#display the image with faces spotted
cv2.imshow('Apoorva car detector:',img)

# Dont autoclose (wait here for the code and listen for the key press)
cv2.waitKey()

print("code completed")
'''

import cv2

# get the video
video = cv2.VideoCapture('videoplayback (2).mp4')

# Our pre trained classifier
classifier_file = 'cars.xml'
classifier_file2 = 'pedestrian.xml'

# create car classifier
car_tracker=cv2.CascadeClassifier(classifier_file)
pedestrian_tracker=cv2.CascadeClassifier(classifier_file2)

# iterate forever over frames
while True:

    # read the current frame 
    read_successful , frame = video.read()  # this function read a single frame at a time (frame is basically the image only in the video)

    #safe coding
    if read_successful:
        #must convert to grayscale
        gray_scaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    # detect car
    cars = car_tracker.detectMultiScale(gray_scaled_frame)
    pedestrians=pedestrian_tracker.detectMultiScale(gray_scaled_frame)

    # draw rectangles around the cars
    for(x,y,w,h) in cars:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

    for(x,y,w,h) in pedestrians:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),3)

    # display the frame 
    cv2.imshow('Apoorva car detector:',frame)
    
    # Dont autoclose (wait here for the code and listen for the key press)
    key=cv2.waitKey(1)
    
    # Stop if Q is pressed 
    if key==81 or key==113:
        break
#Release the video captures object
video.release()

print("code completed")