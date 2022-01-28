import os       #Module used to manage file paths
import pygame   #Module used for game development in python

pygame.init()             #initializes all pygame modules

#Set up game window
background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Image_files/background.jpg'))   #load game window background image and store it in a variable
screen = pygame.display.set_mode((background.get_width(), background.get_height()))   #create game window of the same size as background image
pygame.display.set_caption('Space Invaders')   #set game window name

#Create player class
class Player(pygame.sprite.Sprite):   #Define player class, that inherits from pygame's Sprite class
    #Class constructor, defines player attributes (in this case, position x,y of the player image origin in the game window, and the player image used)
    # Player image origin is its top left corner
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self) #initialize attributes from the parent class
        self.x = x  #pixel position of the player image origin in the x axis of the game window
        self.y = y  #pixel position of the player image origin in the y axis of the game window
        self.sprite = sprite    #Image used to represent the player in the game

    # Class methods
    # draw method places the player image on the game window, with its origin at the x,y pixel position
    def draw(self):
        screen.blit(self.sprite, (self.x, self.y))   #place the player image on the game window, with its origin at the (x,y) pixel

#Create player class object
playerImage = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Image_files/player_ship.png'))  # load player ship image and store it in a variable
xInitialPosition = background.get_width() / 2 - playerImage.get_width()/2   #Define in which initial pixel x coordinate we want the player sprite to spawn
yInitialPosition = background.get_height() - 70                             #Define in which initial pixel y coordinate we want the player sprite to spawn
player = Player(xInitialPosition, yInitialPosition, playerImage)            #create an object of the player class, initializing its x,y position, and setting its sprite

#Define pixel limits to ensure that the player sprite is always within the game window
leftLimit = -9999   # variable that stores the value of the x coordinate of the left pixel limit. It should be 0
rightLimit = 9999   # variable that stores the value of the x coordinate of the right pixel limit. It should be equal to (background image width - ship image width)

#Infinite execution loop
while True:
    screen.blit(background, (0, 0))     #place background image on the screen window
    player.draw()                       #place player image on the screen window. Do it after placing background, so player image is on top

    pressed = pygame.key.get_pressed()  #detect all pressed keys
    if pressed[pygame.K_LEFT]:          #if left arrow pressed
        if player.x > leftLimit:        #if player x position not yet in the left limit of the game screen
            player.x -= 0.5             #move it 0.5 pixels to the left
    elif pressed[pygame.K_RIGHT]:       #else, if right arrow pressed
        if player.x < rightLimit:       #if player x position not yet in the right limit of the game screen
            player.x += 0.5             #move it 0.5 pixels to the right

    for event in pygame.event.get():    #For each event (key pressed/mouse clicked, etc) into the game screen
        if event.type == pygame.QUIT:   #if detected click on game window "X" button
            pygame.quit()               #quit pygame
            exit()                      #end code

    pygame.display.update()             #refresh game window, showing the drawed images
