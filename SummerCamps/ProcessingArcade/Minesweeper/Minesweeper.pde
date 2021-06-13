import java.util.List;
import java.util.ArrayList;

// Game settings
int rows = 10;                 // same number of columns as rows
int cellWidth = 40;            // in pixels
int headerHeight = cellWidth;  // height of game info header
int numOfMines = 20;           // number of mines in the game
int minesFlagged = 0;          // number of mines flagged
color cellColor = #C0C0C0;     // color of unrevealed cell

// Game images
PImage empty, one, two, three, four, five, six, seven, eight;
PImage mineImg, pinImg, wonImg, lostImg;
PImage[] images;

Button startButton;
List<Cell> cells = new ArrayList<Cell>();
boolean gameReady = false;
boolean gameInProgress = false;
int nowMs, gameTimeSec;

void setup() {
  //size( cellWidth * rows, (cellWidth * rows) + headerHeight )
  size(400, 440);
  
  initializeGame();
}

void draw() {
  if( gameReady ){
    background(255);
    updateGameTime();
    drawGameHeader();
    drawCells();
  }
}

void updateGameTime(){
  if( gameInProgress ){
    if(millis() > nowMs + 1000) {
      gameTimeSec++;
      nowMs = millis();
    }
  }
}

void drawGameHeader(){
  textSize(48);
  fill(0);
  if( numOfMines - minesFlagged > 0 ){ 
    text( (numOfMines - minesFlagged), 5, cellWidth - 5);
  } else {
    text( "0", 5, cellWidth - 5);
  }
  text( gameTimeSec, width - 100, cellWidth - 5 );
  startButton.draw();
}

void drawCells(){
  for( Cell c : cells ) {
    c.draw();
  }
}

void initializeGame(){
  initializeImages();
  gameTimeSec = 0;
  
  if( startButton == null ){
    startButton = new Button("start", width/2 - 50, 0, 100, cellWidth);
  }
  
  cells.clear();
  for( int i = 0; i < rows; i++ ) {
    for (int j = 0; j < rows; j++) {
      Cell c = new Cell(i, j);
      cells.add(c);
    }
  }
  
  initializeMines();
  nowMs = millis();
}

void initializeImages(){
  empty = loadImage("empty.png");
  one = loadImage("1.png");
  two = loadImage("2.png");
  three = loadImage("3.png");
  four = loadImage("4.png");
  five = loadImage("5.png");
  six = loadImage("6.png");
  seven = loadImage("7.png");
  eight = loadImage("8.png");
  mineImg = loadImage("bomb.png");
  pinImg = loadImage("flag.png");
  wonImg = loadImage("sunglasses.png");
  lostImg = loadImage("cry.png");
  
  // Only add new images to the end of the array. The array index
  // is used to display the corresponding image for surrounding mines.
  images = new PImage[] {empty, one, two, three, four, five, six,
                         seven, eight, mineImg, pinImg, wonImg, lostImg};
                         
  for( PImage img : images ){
    img.resize(cellWidth, cellWidth);
  }
}

void initializeMines(){
  // Don't place any mines if more than the number of cells--invalid starting state
  if( numOfMines < (rows * rows) ){
    minesFlagged = 0;
    int minesPlaced = 0;
    
    while( minesPlaced != numOfMines ){
      Cell randCell = cells.get( (int)random(0, (rows * rows)) );
      
      if( !randCell.mine ){
        randCell.mine = true;
        minesPlaced++;
      }
    }
    
    gameReady = true;
  }

  // Set number of mines around each cell, empty to eight
  for( Cell c : cells ) {
    List<Cell> neighbors = getNeighbors(c);
    int mines = 0;

    for(Cell neighbor : neighbors) {
      if( neighbor.mine ) {
        mines++;
      }

      c.minesAround = mines;
    }
  }
}

List<Cell> getNeighbors(Cell cell) {
  List<Cell> neighbors = new ArrayList<Cell>();

  for( Cell c : cells ) {
    if( (c.i >= cell.i - 1) && (c.i <= cell.i + 1) && (c.j >= cell.j - 1) && (c.j <= cell.j + 1) ) {
      neighbors.add(c);
    }
  }

  return neighbors;
}

void revealCell(Cell cell) {
  cell.revealed = true;

  // Hit mine, reveal all cells, game is over!
  if( cell.mine ) {
    for( Cell c : cells ) {
      c.revealed = true;
    }
    return;
  }

  // No mines around this cell, reveal all neighboring cells.
  // Do this until all neighboring cells with 0 surrounding mines are revealed
  if ( cell.minesAround == 0 ) {
    List<Cell> neighbors = getNeighbors(cell);
    
    for( Cell c : neighbors ) {
      if( !c.revealed ) {
        revealCell(c);
      }
    }
  }
}

void gameEnd(String state) {
  gameInProgress = false;
  
  if( state.toLowerCase().equals( "won" ) ){
    mineImg = wonImg;
  }
  
  for ( Cell c : cells ) {
    c.revealed = true;
  }
}

Cell checkCellPressed() {
  Cell cell = null;
  
  for( Cell c : cells ) {
    if( (c.x < mouseX) && (c.x + cellWidth > mouseX) && (c.y < mouseY) && (c.y + cellWidth > mouseY) ) {
      cell = c;
      break;
    }
  }
  
  return cell;
}

void mousePressed() {
  if( startButton.mouseIsOver() ){
    initializeGame();
    gameInProgress = true;
    return;
  }
  
  Cell cell = checkCellPressed();

  if( cell != null ){
    if( mouseButton == RIGHT ){
      cell.pinned = !cell.pinned;
      minesFlagged++;
    } else if( mouseButton == LEFT ){
      
      // Don't reveal pinned/marked cells. User must unpin to reveal.
      if( cell.pinned ){ 
        return;
      }
    
      revealCell(cell);

      if( cell.mine ){
        gameEnd("Lost");
      } else {
        // Check if game is won
      
        int cellsLeft = 0;
        for( Cell c : cells ){
          if( !c.mine && !c.revealed ){
            cellsLeft++;
          }
        }
      
        if( cellsLeft == 0 ){
          gameEnd("Won");
        }
      }
    }
  }
}
