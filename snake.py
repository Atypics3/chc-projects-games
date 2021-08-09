# used to define the direction (and other stuff) that the snake can travel
from enum import Enum

class Direction(Enum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

# define the snake class
class Snake:
  length = None
  direction = None
  body = None
  block_size = None
  color = (0,0,255)
  bounds = None


  # the initializer method
  def __init__(self, block_size, bounds):
    # size of each block that makes up the game's grid
    self.block_size = block_size

    # boundary of the game (same as the size of the game screen)
    self.bounds = bounds
    
    # default setup for snake's length, initial body, and intial direction,
    # will also reset the game when the player goes out of bounds (dies)
    self.respawn()


  def respawn(self):
    # default length at spawn
    self.length = 3 
    # describes where the snake's body (or blocks) are in (x,y) form
    self.body = [(20,20),(20,40),(20,60)] 
    # faces down when player first spawns in
    self.direction = Direction.DOWN 
  

    # the method for showing the window
  def draw(self, game, window):
    for segment in self.body:
      # draw.rect draws a rectangle for each block, or segments of the snake in the body list
      # block_size sets the width and height of each rectangle drawn
      game.draw.rect(window, self.color, (segment[0],segment[1],self.block_size, self.block_size))


  def move(self):
    curr_head = self.body[-1] # gets last element in indice
    #If it is going up or down, we append a new block by copying the x co-ordinate of the current head, and adding or subtracting (depending on if the snake is going up or down) one grid block_size to the y co-ordinate.
    if self.direction == Direction.DOWN:
      next_head = (curr_head[0], curr_head[1] + self.block_size)
      self.body.append(next_head)
    
    elif self.direction == Direction.UP:
      next_head = (curr_head[0], curr_head[1] - self.block_size)
      self.body.append(next_head)
    
    # if the snake is heading left or right, we append a new block to the body list, using the y co-ordinate of the current head, but modifying the x co-ordinate by one block_size.
    elif self.direction == Direction.RIGHT:
      next_head = (curr_head[0] + self.block_size, curr_head[1])
      self.body.append(next_head)
    
    elif self.direction == Direction.LEFT:
      next_head = (curr_head[0] - self.block_size, curr_head[1])
      self.body.append(next_head)
    
    # removes a block from tail end of snake
    if self.length < len(self.body): # determines whether or not the tail end should be removed
      self.body.pop(0)
    

    # The method accepting the direction. If the direction is different from the current direction, the direction is updated.
  def steer(self, direction):
    if self.direction == Direction.DOWN and direction != Direction.UP:
      self.direction = direction

    elif self.direction == Direction.UP and direction != Direction.DOWN:
      self.direction = direction

    elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
      self.direction = direction
      
    elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
      self.direction = direction
  

  def eat(self): # increases length of snake
    self.length += 1


  # sees if the head of the snake is over the food
  def check_for_food(self, food):
    head = self.body[-1]
    if head[0] == food.x and head[1] == food.y: # if so, then food is eaten and respawns elsewhere
      self.eat()
      food.respawn()

  # this method checks if the snake has crossed over, or bitten itself
  def check_tail_collision(self):
    head = self.body[-1]
    has_eaten_tail = False
    
    for i in range(len(self.body) - 1):
      segment = self.body[i]
      if head[0] == segment[0] and head[1] == segment[1]:
        has_eaten_tail = True
    
    return has_eaten_tail
  
  
  def check_bounds(self):
    head = self.body[-1]
    # checks each dimensions against the bounds of the WindowsError
    # if snake's head is outside the boundary, return true and game ends
    if head[0] >= self.bounds[0]:
      return True
    if head[1] >= self.bounds[1]:
      return True

    if head[0] < 0:
      return True
    if head[1] < 0:
      return True 
    # if not, return false and game continues
    return False