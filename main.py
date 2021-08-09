import pygame
from snake import *
from food import Food

pygame.init()
bounds = (300, 300)  # size of the game screen
window = pygame.display.set_mode(bounds)  # creates game window
pygame.display.set_caption("Snake")  # title of the game

block_size = 20 # grid is 20 pixels tall and wide (20x20)
snake = Snake(block_size, bounds) # used to check when snake hits the edge of the screen
food = Food(block_size,bounds) # creates a new Food object
font = pygame.font.SysFont('comicsans', 60, True) # font for the game over screen

run = True
while run: # keeps repeating every 100ms until it becomes false, then game window closes
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT: # done by clicking the "Close Window" button at the top of the window
      run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)

  snake.move()
  snake.check_for_food(food)
  # if snake goes out of bound, render "game over", pause, and reset game
  if snake.check_bounds() == True or snake.check_tail_collision() == True:
    text = font.render('Game Over', True, (255,255,255))
    window.blit(text, (20,120)) # puts at center of screen
    pygame.display.update()
    pygame.time.delay(1000) # waits and resets game
    snake.respawn()
    food.respawn()

  window.fill((0,0,0)) # fills screen with black after every restart
  snake.draw(pygame, window) # allows the snake to move around
  food.draw(pygame, window)
  # adding the food
  pygame.display.update() # renders screen and takes all the updates and "flips" them from the window buffer to the screen

