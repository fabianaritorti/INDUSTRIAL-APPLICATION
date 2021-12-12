import cv2
import os
import glob

import numpy as np

from PIL import Image
from IPython.display import clear_output, display
from imutils.video import VideoStream, FileVideoStream
from tqdm.notebook import tqdm
import time

class OneNNClassifier:
    
    def __init__(self, ids, descs):
      self.ids = ids
      self.descs = descs    


    def predict(self, queryF):
        #evaluate the dot products between descs and queryF
        #To sort the results create a zip between dot products and ids
        #then call the sorted function to sort them
        #return just the first result of the results list
        print("query:")
        print(queryF)
        print("descriptors")
        print(self.descs)
        scores = []
        for desc in self.descs:
            scores.append(np.dot(desc,queryF))
        zipped_lists = zip(scores, self.ids)
        sorted_zipped_lists = sorted(zipped_lists,reverse=True)
        if(sorted_zipped_lists[0][0]<0.80):
            return None
        else:
            return sorted_zipped_lists[0]
            #return res
