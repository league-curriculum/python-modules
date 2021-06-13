class Button {
  String label;
  float x;    // top left corner x position
  float y;    // top left corner y position
  float w;    // width of button
  float h;    // height of button
  
  Button(String labelB, float xpos, float ypos, float widthB, float heightB) {
    label = labelB;
    x = xpos;
    y = ypos;
    w = widthB;
    h = heightB;
  }
  
  void draw() {
    push();
    
    if( mouseIsOver() ){
      fill(#FCF000);
    } else {
      fill(218);
    }
    stroke(141);
    rect(x, y, w, h, 10);
    textAlign(CENTER, CENTER);
    textSize(32);
    fill(0);
    text(label, x + (w / 2), y + (h / 3));
    
    pop();
  }
  
  boolean mouseIsOver() {
    if (mouseX > x && mouseX < (x + w) && mouseY > y && mouseY < (y + h)) {
      return true;
    }
    return false;
  }
}
