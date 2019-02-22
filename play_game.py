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
    c_score = i.capturer(300, 1530, 160, 50)
    
    keyboard = Controller()
    #model = load_model('C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/jump_nojump_v3.h5')
    model = load_model('C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/models/model_dual_input.h5')
    model_score = load_model('C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/models/score_v2.h5')
    
    def get_result(result):
        resultstr = ''
        for i in range(5):
            resultstr += str(np.argmax(result[i]))
        return resultstr

    def play_dual():
        try:
            while True:
                c.play_picture("C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/dual/pics/")
                c_score.play_picture("C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/dual/score/")
                
                file_pic = "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/dual/pics/" + str(c.counter_play - 1) + ".png"
                score_pic = "C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/play_pics/dual/score/" + str(c_score.counter_play - 1) + ".png"
    
                img_pic = image.load_img(file_pic, target_size = (75,250))
                img_pic_tensor = image.img_to_array(img_pic)
                img_pic_tensor = np.expand_dims(img_pic_tensor, axis = 0)
                img_pic_tensor /= 255
                
                score_pic = image.load_img(score_pic, target_size = (50, 160))
                img_score_tensor = image.img_to_array(score_pic)
                img_score_tensor = (img_score_tensor - 128) / 128
                img_score_tensor = img_score_tensor[:,:,0]
                img_score_tensor = np.expand_dims(img_score_tensor, axis = 0)
                img_score_tensor = np.expand_dims(img_score_tensor, axis = 3)
                score = model_score.predict(img_score_tensor)
                score = get_result(score)
                score = int(score)
                score = np.expand_dims(score, axis = 0)
                
                res = model.predict([img_pic_tensor, score])
                
                if res > 0.5:
                    keyboard.press(Key.up)
                    time.sleep(0.015)
                    keyboard.release(Key.up)
                    
                    
                print(str(c.counter_play - 1) + ": " + str(res))
                sys.stdout.flush()
                
        except KeyboardInterrupt:
            pass
    
    
    def play_old():
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
        
        
    #play_old()
    play_dual()

        

main()


