from pynput.keyboard import Controller
import img_capture as i

c = i.capturer(300, 1500, 100, 100)

def main():
    
    keyboard = Controller()
    
    def play():
        try:
            while True:
                c.play_picture("C:/Users/bened/OneDrive/Arbeit/Lernen/python_training/score_pics/")
    
    
        except KeyboardInterrupt:
            pass
        
        
    play()
    
    
main()

#Bilder Score machen