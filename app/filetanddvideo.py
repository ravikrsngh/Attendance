import os
import datetime
import cv2
import tensorflow as tf
from tensorflow import keras
# Function to extract frames
def FrameCapture(pathd,paths):

    # Path to video file
    vidObj = cv2.VideoCapture(paths)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        if  count%100==0:
          print(count)
          path=pathd+'frame%d.jpg' % count
          #print('here  '+path)
          cv2.imwrite(path, image)

        count += 1
    print(count)



def filecreator(video):



    all=datetime.datetime.now()
    date=str(all.day)+'_'+str(all.month)+'_'+str(all.year)
    #time=str(all.hour)+"_"+str(all.minute)
    h=all.hour
    m=all.minute
    if(h==8 and m>30)or(h==9 and m<=30):
        slot='slot1'
        fn=os.getcwd().replace('\\','/') +'/app/facenettest/storagevideo/'+date
        os.makedirs(fn)
    elif(h==9 and m>30)or(h==10 and m<=30):
        slot='slot2'
    elif(h==10 and m>50)or(h==11 and m<=50):
        slot='slot3'
    elif(h==11 and m>50)or(h==12 and m<=50):
        slot='slot4'
    elif(h==13 and m>45)or(h==14 and m<=45):
        slot='slot5'
    elif(h==14 and  m>45)or(h==15 and m<=45):
        slot='slot6'
    else:
        slot='slot7'
    fn=os.getcwd().replace('\\','/')+'/app/facenettest/storagevideo/'+date+'/'+slot+'/'
    os.makedirs(fn)
    FrameCapture(fn,video)
    return slot

#print(filecreator('./test video.mp4'))
