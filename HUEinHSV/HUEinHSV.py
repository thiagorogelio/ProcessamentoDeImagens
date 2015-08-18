# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 01:33:49 2015

@author: maxx

Cód para gerar HUE em HSV

"""

import cv2
import numpy as np

SIZE = 255

HSV = np.uint8(np.zeros((512, 512, 3)))

ll, cc = np.indices((512,512))

HSV[:,:,0] = (np.degrees(np.arctan2(cc-SIZE,ll-SIZE))+270)/2
HSV[:,:,1] = np.clip(np.int16(np.sqrt((ll-SIZE)**2+(cc-SIZE)**2)), 0, SIZE)
HSV[(HSV[:,:,1] < 255),2] = 255;

RGB = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

cv2.imshow("HUE",RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()