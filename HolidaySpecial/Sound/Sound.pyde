 def setup():
    size(200,200)
 
def draw():
    pass
 
def mouseClicked():
    play_sound('arcade_bomb2.mp3')
    
    
add_library("minim")
global minim
minim = None
                
def play_sound(file_name):
    global minim
    if minim is not None:
        minim.stop()
    minim=Minim(this)
    s=minim.loadFile(file_name)
    s.play()
    
