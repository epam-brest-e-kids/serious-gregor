from pygame.locals import *
import pygame

class Snake:
  def __init__(self):
    self.trail = [] # Хвост змеи
    self.length = 5 # Длина змеи
    self.xv = 0 # x velocity - скорость по х
    self.yv = 0 # y velocity - скорость по y
    self.x = 50
    self.y = 50
    self.speed = 20
  
  def update(self, scene):
    self.move(scene)
    
    for tail in self.trail:
      if (tail.get("x") == self.x and tail.get("y") == self.y):
        self.length = 5
    
    self.trail.append({
      "x": self.x,
      "y": self.y
      })
    
    cutLength = len(self.trail) - self.length
    while (cutLength>0):
      self.trail.pop()
      cutLength = cutLength -1
    
  def grow():
    self.length +=1

  def move(self, scene):
    self.x += self.xv*self.speed
    self.y += self.yv*self.speed
    print(self.x)
    print(self.y)
    if (self.x < 0):
      self.x = scene.tc -1
    if (self.x > scene.tc -1):
      self.x = 0
    if (self.y < 0):
      self.y = scene.tc -1
    if (self.y > scene.tc -1):
      self.y = 0

    keys = pygame.key.get_pressed()
    if (keys[K_UP]):
      self.xv = 0
      self.yv = -1
    if (keys[K_DOWN]):
      self.xv = 0
      self.yv = 1
    if (keys[K_LEFT]):
      self.xv = -1
      self.yv = 0
    if (keys[K_RIGHT]):
      self.xv = 1
      self.yv = 0

  def draw(self, surface, gs):
    for tail in self.trail:
      pygame.draw.rect(
        surface,
        pygame.Color("red"),
        pygame.Rect(tail.get("x")*gs, tail.get("y")*gs, gs-2, gs-2)
      )


class Apple:
  def __init__(self):
    self.x = 15
    self.y = 15
  
  def update(self):
    pass

  def draw(self, surface):
    pass

class Scene:
  gs = 20
  tc = 20
  def __init__(self):
    self.windowWidth = 800
    self.windowHeight = 600

    self._display_surface = pygame.display.set_mode(
      (self.windowWidth, self.windowHeight),
      pygame.HWSURFACE | pygame.RESIZABLE
      )
    pygame.display.set_caption('Питон')

    self.snake = Snake()
    self.apple = Apple()
  
  def on_loop(self):
    self.snake.update(self)
  
  def on_render(self):
    self._display_surface.fill((0,100,0))
    self.snake.draw(self._display_surface, self.gs)
    self.apple.draw(self._display_surface)
    pygame.display.flip()

  def update(self):
    self.on_loop()
    self.on_render()

class App:
  gs = 20 # grid size
  tc = 20 # tile count
  def __init__(self):
    self._running = False
    print("Вот мы и запустили нашу игру")

  def on_init(self):
    pygame.init()
    pygame.font.init()

    self.scene = Scene()

    self._running = True
  
  def on_execute(self):
    if self.on_init() == False:
      self._running = False
    
    while(self._running):
      pygame.event.pump()
      keys = pygame.key.get_pressed()

      if (keys[K_ESCAPE]):
        self._running = False
      
      self.scene.update()
      
    self.on_cleanup()

  def on_cleanup(self):
    pygame.quit()

if __name__ == "__main__":
  app = App()
  app.on_execute()