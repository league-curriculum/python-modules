class Cell {
  int i, j, x, y;
  boolean mine, revealed, pinned;
  int minesAround;
  
  Cell(int i, int j) {
    this.i = i;              // cell row #
    this.j = j;              // cell col #
    this.x = i * cellWidth;  // cell x in pixels
    this.y = j * cellWidth;  // cell y in pixels
    this.y += headerHeight;  // cell y adjustment
    this.mine = false;
    this.revealed = false;
    this.pinned = false;
  }
  
  void draw() {    
    if( this.revealed ) {
      if( this.mine ) {
        image(mineImg, this.x, this.y);
      } else {
        image(images[this.minesAround], this.x, this.y);
      }
    } else {
      fill(cellColor);
      rect(this.x, this.y, cellWidth, cellWidth);
      
      // Draw pin after cell background
      if (this.pinned) {
        image(pinImg, this.x, this.y);
      }
    }
    
    // Draw cell border at the end on top of the images
    // for clearer cell seperation
    stroke(0);
    strokeWeight(1);
    noFill();
    rect(this.x, this.y, cellWidth, cellWidth);
  }
}
