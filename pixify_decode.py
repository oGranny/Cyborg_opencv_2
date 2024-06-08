import numpy as np
import cv2
import os
import sys
import time
import random

'''
Guidelines :- 1) You are not allowed to import libraries other than those already mentioned
              2) You are allowed to code only in the function given below . Code present anywhere else would be ignored by the code verifying exec.
              3) You must code in such a way that the code inside the function is robust for all test cases.
              4) The code verifying exectubale would iterate over the test cases and call this function with one test image at a time. 
'''

def decode(image):
    '''
    Description:- This function takes in image as the input (a numpy array) and returns the character embedded in the image
    For example : if yellow squares = 4 , red squares = 3 , number of shapes containing shapes = 5 . Then the correct character to be returned would be (4*2 + 3*1 + 5) which is p. 
    Note :- if the value comes out to be 32 then the function should return an empty single space " ".
    '''


    ############ Enter your Code Here #################
    character = " "
    red = 0
    yellow = 0
    square = 0

    for i in range(100,700,100):
        for j in range(100, 700, 100):
            if list(image[j,i]) == [0,0,255]:
                red += 1
            elif list(image[j,i]) == [0,255,255]:
                yellow += 1

            if i == 600 or j == 600:
                continue

            img = image[i+10:i+90, j+10:j+90]
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, threshold = cv2.threshold(gray, 179, 255, cv2.THRESH_BINARY_INV)
            compare = np.full([80,80], 0, dtype = np.uint8)
            if not (compare == threshold).all():
                square +=1

    char_int = red + 2*yellow + square
    if char_int >0 and char_int <= 26: character = chr(char_int + 96)
    else: character = " "

    ###################################################
    return character

    

# if __name__ == "__main__":
#     for i in range(1,20):
#         img = cv2.imread(f'./test_cases/test_image_{14}.png')
#         print(decode(img))
