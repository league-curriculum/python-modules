class Button:
  
  def __init__(self, label, x_pos, y_pos, button_width, button_height):
    self.label = label
    self.x = x_pos
    self.y = y_pos
    self.w = button_width
    self.h = button_height

  def draw(self):
    push()
    
    if self.mouse_is_over():
      fill('#FCF000')
    else:
      fill(218)
    
    stroke(141)
    rect(self.x, self.y, self.w, self.h, 10)
    textAlign(CENTER, CENTER)
    textSize(32)
    fill(0)
    text(self.label, self.x + (self.w / 2), self.y + (self.h / 3))
    
    pop()
  
  def mouse_is_over(self):
    if( mouseX > self.x and mouseX < (self.x + self.w) and
        mouseY > self.y and mouseY < (self.y + self.h)):
        return True
    
    return False
