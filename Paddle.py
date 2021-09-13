import pygame
BLACK = (0,0,0)

#This class represents a paddle. It derives from the "Sprite" class in Pygame
class Paddle(pygame.sprite.Sprite):
  
  def __init__(self, color, width, height):
    # Call the parent class (Sprite) constructor
    super().__init__()

    #Pass the color, x-position, y-position, width, and height.
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)


    # drawing the paddle, with the paddle being a rectangle, having the color white, and a specified width and height
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    # get rectangle object that has the dimensions of the image
    self.rect = self.image.get_rect()

  #move up
  def moveUp(self, pixels):
    self.rect.y -= pixels
    # check for out of bounds
    if self.rect.y < 0:
      self.rect.y = 0 # prevents it from going out of bounds (doesn't go past y = 0)

    
  #move down
  def moveDown(self, pixels):
    self.rect.y += pixels
  #Check that you are not going too far (off the screen)
    if self.rect.y > 400:
      self.rect.y = 400
