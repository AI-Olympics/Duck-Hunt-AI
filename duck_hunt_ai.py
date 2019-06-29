import numpy as np 
import cv2
import pyscreenshot as ImageGrab
import pyautogui as pg
import time 

#location of the game screen
x1, y1 = (0, 150)
x2, y2 = (620, 550)
screen = ImageGrab.grab(bbox = (x1, y1, x2, y2))  

i = 0
killed = 0

while i < 1000:  
    #grab the screen
    screen = ImageGrab.grab(bbox = (x1, y1, x2, y2))  
    img_np = np.array(screen)

    #change color
    game_window = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    #detect white points in the image
    lower, upper = np.array([240,240,240]), np.array([255,255,255])
    mask = cv2.inRange(game_window, lower, upper)
    
    #extract the locations
    birds = np.where(mask > 0)
    x_birds = birds[1]
    y_birds = birds[0]


    try: 
        hit_pos = (x_birds[0] + x1, y_birds[1] + y1)
        #click the mouse
        pg.click(hit_pos)
        print('BIRD HIT at', hit_pos)
        #wait for a second for bird to fall
        time.sleep(1)
    except:
        pass
    
    i += 1
