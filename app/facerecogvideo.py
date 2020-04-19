from os import listdir
from os.path import isdir
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from matplotlib import pyplot
from numpy import savez_compressed
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from numpy import load
from numpy import expand_dims
from keras.models import load_model
from random import choice
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import datetime
from .filetanddvideo import filecreator
import os






def extract_face(filename, required_size=(160, 160)):
	# load image from file
	image = Image.open(filename)
	# convert to RGB, if needed
	image = image.convert('RGB')
	# convert to array
	pixels = asarray(image)
	# create the detector, using default weights
	detector = MTCNN()
	# detect faces in the image
	results = detector.detect_faces(pixels)
	# extract the bounding box from the first face
	x1, y1, width, height = results[0]['box']
	# bug fix
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	# extract the face
	face = pixels[y1:y2, x1:x2]
	# resize pixels to the model size
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array

def extract_facetest(directory, required_size=(160, 160)):



	# load image from file
    image = Image.open(directory)
        # convert to RGB, if needed
    image = image.convert('RGB')
        # convert to array
    pixels = asarray(image)
        # create the detector, using default weights
    detector = MTCNN()
        # detect faces in the image
    results = detector.detect_faces(pixels)
    X=list()
    for i in range (0,len(results)):
        count=0
        x1, y1, width, height = results[i]['box']
                # bug fix
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
                # extract the face
        face = pixels[y1:y2, x1:x2]
                #resize pixels to the model size
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array = asarray(image)
        X.append(face_array)
    print('Length is:')
    print(len(X))
    return X

def loadfacetest(directory):
    X=list()
    for filename in listdir(directory):
        path=directory+filename
        faces=extract_facetest(path)
        X.extend(faces)
    return asarray(X)

def load_faces(directory):
	faces = list()
	# enumerate files
	for filename in listdir(directory):
		# path
		path = directory + filename
		# get face
		face = extract_face(path)
		# store
		faces.append(face)
	return faces


# load a dataset that contains one subdir for each class that in turn contains images
def load_datasettrain(directory):
	X, y = list(), list()
	# enumerate folders, on per class
	for subdir in listdir(directory):
		# path
		path = directory + subdir + '/'
		# skip any files that might be in the dir
		if not isdir(path):
			continue
		# load all faces in the subdirectory
		faces = load_faces(path)
		# create labels
		labels = [subdir for _ in range(len(faces))]
		# summarize progress
		print('>loaded %d examples for class: %s' % (len(faces), subdir))
		# store
		X.extend(faces)
		y.extend(labels)
	return asarray(X), asarray(y)



def get_embedding(model, face_pixels):
	# scale pixel values
	face_pixels = face_pixels.astype('float32')
	# standardize pixel values across channels (global)
	mean, std = face_pixels.mean(), face_pixels.std()
	face_pixels = (face_pixels - mean) / std
	# transform face into one sample
	samples = expand_dims(face_pixels, axis=0)
	# make prediction to get embedding
	yhat = model.predict(samples)
	return yhat[0]


def facerecog(video):
    slot=filecreator(video)
    trainX, trainy = load_datasettrain(os.getcwd().replace('\\','/') +'/app/facenettest/train/')
    print(trainX.shape, trainy.shape)
    # load test dataset
    all=datetime.datetime.now()
    date=str(all.day)+'_'+str(all.month)+'_'+str(all.year)
    path_test=os.getcwd().replace('\\','/') +'/app/facenettest/storagevideo/'+date+'/'+slot+'/'
    testX= loadfacetest(path_test)
    print(testX.shape)
    # save arrays to one file in compressed format
    savez_compressed('facenettest.npz', trainX, trainy, testX)

    data = load('facenettest.npz')
    trainX, trainy, testX = data['arr_0'], data['arr_1'], data['arr_2']
    print('Loaded: ', trainX.shape, trainy.shape, testX.shape)

    model = load_model(os.getcwd()+'/app/facenet_keras.h5')
    print('Loaded Model')

    newTrainX = list()
    for face_pixels in trainX:
        embedding = get_embedding(model, face_pixels)
        newTrainX.append(embedding)
    newTrainX = asarray(newTrainX)
    print(newTrainX.shape)

    newTestX = list()
    for face_pixels in testX:
        embedding = get_embedding(model, face_pixels)
        newTestX.append(embedding)
    newTestX = asarray(newTestX)
    print(newTestX.shape)

    savez_compressed('facenettest.npz', newTrainX, trainy, newTestX)

    data = load('facenettest.npz')
    testX_faces = data['arr_2']

    data = load('facenettest.npz')
    trainX, trainy, testX = data['arr_0'], data['arr_1'], data['arr_2']

    in_encoder = Normalizer(norm='l2')
    trainX = in_encoder.transform(trainX)
    testX = in_encoder.transform(testX)

    out_encoder = LabelEncoder()
    out_encoder.fit(trainy)
    trainy = out_encoder.transform(trainy)


    model = SVC(kernel='linear', probability=True)
    model.fit(trainX, trainy)
    print(testX.shape[0])
    present=list()
    for i in range(testX.shape[0]):
        random_face_pixels = testX_faces[i]
        random_face_emb = testX[i]


        samples = expand_dims(random_face_emb, axis=0)
        yhat_class = model.predict(samples)
        yhat_prob = model.predict_proba(samples)

        class_index = yhat_class[0]
        class_probability = yhat_prob[0,class_index] * 100

        predict_names = out_encoder.inverse_transform(yhat_class)
        c=0
        if i!=0:
            for i in range(0,len(present)):
                if present[i] ==predict_names[0]:
                    c=1

        if c==0:
            present.append(predict_names[0])

    #print(present)
    return present,slot

#facerecog('slot1')
