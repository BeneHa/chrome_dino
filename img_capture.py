import mss
import mss.tools

class capturer:
    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        
    counter_jump = 600
    counter_nojump = 600
    counter_play = 600
        
    
    
    def take_picture(self, num, path):
        with mss.mss() as sct:
            monitor = {"top":self.top, "left":self.left, "width":self.width, "height": self.height}
            output = path + str(num) + ".png"

            sct_img = sct.grab(monitor)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

    def up_arrow(self, path):
        self.take_picture(self.counter_jump, path)
        self.counter_jump += 1
        
    def right_arrow(self, path):
        self.take_picture(self.counter_nojump, path)
        self.counter_nojump += 1
    
    def play_picture(self, path):
        #with mss.mss() as sct:
            #monitor = {"top":self.top, "left":self.left, "width":self.width, "height": self.height}
        self.take_picture(self.counter_play, path)
        self.counter_play += 1
            












