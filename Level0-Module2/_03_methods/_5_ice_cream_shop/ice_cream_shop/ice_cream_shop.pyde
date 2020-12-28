# When you are done, this program will draw an ice cream cone with 
#     scoops of ice cream, sprinkles, and a cherry on top.


def setup():

     size(500,500)
     
     # Call the makeIceCreamCone() method below to draw the cone for your ice cream
     makeIceCreamCone()
     # Use the addScoop method below to add as many scoops of ice cream as you want
     # Choose a different flavor for each scoop
     addScoop("chocolate")
     # Use the method provided to add some sprinkles to your ice cream
     addSprinkle(100)
     # Write code to add a cherry to the top of your ice cream. Hint: ellipse
     fill(255,0,0)
     ellipse(250,100,50,50)


#***********  These are methods for you to use. DON'T CHANGE CODE BELOW THIS LINE !!!   *****************/

# Icecream recipe
SCOOPSIZE = 150
scoops = 0
coneY = 320


def makeIceCreamCone():
     fill(188,126,49)
     triangle(190,320,310,300,255,500)


def addScoop(flavor):
     noStroke()
     if flavor.equalsIgnoreCase("chocolate"):
         fill(116,71,16)
     elif flavor.equalsIgnoreCase("Strawberry"):
         fill( 232 ,144,129)
     elif flavor.equalsIgnoreCase("Vanilla"):
         fill(245, 243, 227)
     else:
         println("ERROR: We don't have the flavor "+ flavor) 
         return

     ellipse(width/2,coneY - 50 - (SCOOPSIZE*scoops)/2,SCOOPSIZE,SCOOPSIZE)
     scoops+=1


def addSprinkle(numberOfSprinkles):
    for i in range(numberOfSprinkles):
         fill(random(256),random(256),random(256))
         minX = width/2-SCOOPSIZE/2 + 10
         maxX = SCOOPSIZE/3 +width/2 +10
         minY = coneY-((SCOOPSIZE)*scoops)/2-40
         maxY = coneY
         sprinkleAreaX = random(minX, maxX)
         sprinkleAreaY = random(minY, maxY)
         sprinkleWidth = random(2,9)
         sprinkleHeight = random(2,9)
         ellipse(sprinkleAreaX,sprinkleAreaY,sprinkleHeight,sprinkleWidth)
