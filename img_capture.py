import mss
import mss.tools
import numpy as np
from PIL import Image

class capturer:
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        
    counter_jump = 1
    counter_nojump = 1
    counter_play = 1
        
    
    
    def take_picture(self, num, path):
        with mss.mss() as sct:
            monitor = {"top":self.top, "left":self.left, "width":self.width, "height": self.height}
            output = path + str(num) + ".png"

            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def up_arrow(self):
        self.take_picture(self.counter_jump, "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/train_pics/direction_up")
        self.counter_jump +=1
        
    def right_arrow(self):
        self.take_picture(self.counter_nojump, "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/train_pics/direction_right")
        self.counter_nojump += 1
    
    def play_picture(self):
        with mss.mss() as sct:
            monitor = {"top":self.top, "left":self.left, "width":self.width, "height": self.height}
            #img = np.array(sct.grab(monitor))
            #img = img[...,:3]
            #return img
        
            self.take_picture(self.counter_play, "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/")
            self.counter_play += 1




#img = numpy.array(sct.grab(monitor))









