import numpy as np
import cv2
import os

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)