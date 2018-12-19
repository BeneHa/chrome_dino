import img_capture as i
from pynput import keyboard
from pynput.keyboard import Key, Controller
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import time, sys
from skimage.transform import resize
from PIL import Image

def main():

    c = i.capturer(400, 150, 1500, 300)
    
    keyboard = Controller()
    model = load_model('C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/jump_nojump_v3.h5')
    
    def play():
        try:
            while True:
                c.play_picture("C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/")
                
                file = "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/" + str(c.counter_play - 1) + ".png"
                img = image.load_img(file, target_size = (250, 75))
                img_tensor = image.img_to_array(img)
                img_tensor = np.expand_dims(img_tensor, axis=0)
                img_tensor /= 255.
                
                res = model.predict(img_tensor)[0,0]
                
                if res < 0.5:
                    keyboard.press(Key.up)
                    time.sleep(0.01)
                    keyboard.release(Key.up)
                    
                    
                print(str(c.counter_play - 1) + ": " + str(res))
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            pass
        
        
    play()

main()


