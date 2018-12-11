import img_capture as i
from pynput import keyboard

def main():
  
    c = i.capturer(400, 150, 1500, 300)
  
    def on_press(key):
        if key == keyboard.Key.up:
            c.up_arrow()
        elif key == keyboard.Key.right:
            c.right_arrow()
    def on_release(key):
        if key == keyboard.Key.esc:
            return False        
    
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
  
  
main()




