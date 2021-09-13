import pygame
from Paddle import Paddle
from Ball import Ball

pygame.init() 

# colors using RGB values
BLACK = (0,0,0)
WHITE = (255,255,255)


# setting up game client
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")


# properties of the paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200


# properties of the ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


# contains all the sprites used in the game
all_sprites_list = pygame.sprite.Group() 

# adding paddles and ball to list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)



### MAIN FUNCTION ###
# keeps on looping until user exits
carryOn = True

# used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialize player scores
scoreA = 0
scoreB = 0

while carryOn:
  for event in pygame.event.get(): # triggered when user does something
    if event.type == pygame.QUIT:
      carryOn = False # exits loop and stops
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q: # pressing q will quit the game
        carryOn = False

  # making the paddles move when buttons are pressed 
  keys = pygame.key.get_pressed() 
  if keys[pygame.K_w]:
    paddleA.moveUp(5) # moves up 5 pixels
  
  if keys[pygame.K_s]:
    paddleA.moveDown(5)

  if keys[pygame.K_UP]:
    paddleB.moveUp(5)
  
  if keys[pygame.K_DOWN]:
    paddleB.moveDown(5)

  # game logic section
  all_sprites_list.update()

  # implementing bounce algorithm, checking if the ball bounces against any of the 4 walls (on the screen)
  if ball.rect.x >= 690:
    scoreA += 1
    ball.velocity[0] = -ball.velocity[0]

  if ball.rect.x <= 0:
    scoreB += 1
    ball.velocity[0] = -ball.velocity[0]

  if ball.rect.y > 490:
    ball.velocity[1] = -ball.velocity[1]

  if ball.rect.y < 0:
    ball.velocity[1] = -ball.velocity[1]

  # detects collision between the ball and the paddles
  if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
    ball.bounce()

  # drawing section
  # clears screen to black
  screen.fill(BLACK)
  # draws the net
  pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5) 

  # drawing sprites onto screen
  all_sprites_list.draw(screen)
  
  # displaying scores
  font = pygame.font.Font(None, 74)
  text = font.render(str(scoreA), 1, WHITE)
  
  screen.blit(text, (250,10))
  text = font.render(str(scoreB), 1, WHITE)
  screen.blit(text, (420,10))

  # updates the screen
  pygame.display.flip()

  # limit to 60 frames per second
  clock.tick(60)

# Once the main progam stops, stop the game engine as well
pygame.quit()