import img_capture as i
from pynput import keyboard

def main():
    base_dir = "C:/Users/bened/OneDrive/Arbeit/Lernen/python-training/data_dual_inputs/"
    
    dino_capt = i.capturer(400, 150, 1500, 300)
    score_capt = i.capturer(300, 1530, 160, 50)
    
    score_nums = []
  
    def on_press(key):
        if key == keyboard.Key.up:
            dino_capt.play_picture(base_dir + "train/" + "up/")
            score_capt.play_picture(base_dir + "train/" + "score/")
            
        elif key == keyboard.Key.right:
            dino_capt.play_picture(base_dir + "train/" + "right/")
            score_capt.play_picture(base_dir + "train/" + "score/")
            
    def on_release(key):
        if key == keyboard.Key.esc:
            return False        
    
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
  
  
main()

#TODO:
#Check if taking pictures works, transform inputs for model

