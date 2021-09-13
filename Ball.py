import pygame
from random import randint
BLACK = (0,0,0)

# represents a ball, it's derived from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):
  # calling Sprite (the parent class) constructor
  def __init__(self, color, width, height):
    super().__init__()

    # passes in color of ball and its width and height.
    # setting background color to transparent
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    # draw the ball's shape (rectangle)
    pygame.draw.rect(self.image, color, [0,0,width,height])

    # setting velocity vector, which moves the ball
    self.velocity = [randint(4,8), randint(-8,8)]

    # fetch the rectangle object that has the dimensions of the image
    self.rect = self.image.get_rect()

  # updates the ball when its moving
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
  
  # if ball collides with paddle, then make the ball bounce
  def bounce(self):
    self.velocity[0] = -self.velocity[0]
    self.velocity[1] = randint(-8,8)
	