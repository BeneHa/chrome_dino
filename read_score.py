import img_capture as i
import time

c = i.capturer(300, 1530, 160, 50)

def main():
    
    def play():
        try:
            while True:
                c.play_picture("C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/score_pics/")
                time.sleep(1)
    
        except KeyboardInterrupt:
            pass
        
        
    play()
    
    
main()




#https://github.com/CJHMPower/digit-sequence-recognition/blob/master/digit_recognition.ipynb