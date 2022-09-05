import asrtoolkit
from asrtoolkit import wer, cer
import cv2
import io
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np
from PIL import Image
import pytesseract
import sys
from skimage import io as ioski
from skimage.color import rgb2gray
from skimage.transform import rotate, resize
import os 
from google.cloud import vision
from google.cloud.vision_v1 import types
from dotenv import load_dotenv, find_dotenv
load_dotenv()

# with open("/tmp/google.json", "wt") as fp:
#     fp.write(str(os.getenv("GOOGLE_CREDS")))

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ="/tmp/google.json"
# client = vision.ImageAnnotatorClient() 

dirpath = os.getcwd()
print("This Directory", dirpath)
parentDirectory = os.path.dirname(dirpath)
print(parentDirectory)
GrandparentDirectory = os.path.dirname(parentDirectory)
print(GrandparentDirectory)
print(os.path.abspath(os.path.join(os.getcwd(),  '..')))
out_path_myhand = os.getenv("LOCAL_PATH")
print("My_hand_Trained_data",out_path_myhand)
out_path_StorySquad = os.path.abspath(os.path.join(os.getenv("LOCAL_PATH","NOt found"), "..",".."))
print(out_path_StorySquad)

sys.path.insert(0, out_path_StorySquad+'/deskew')
from deskew import determine_skew
sample_img ="Sample.jpg"

outputimage = Image.open(sample_img)
print(outputimage)
outputimage