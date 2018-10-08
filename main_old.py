from pygame.locals import *
import pygame
import time

pygame.init()

pygame.font.init()

WINDOW_WIDTH = 800
WINDOW_HEIGH = 600
SPEED = 32

class Player:
    x = []
    y = []
    step = 44
    direction = 0
    length = 3
    
    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.x.append(0),
            self.y.append(0)

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

             # update previous positions
            for i in range(self.length-1, 0, -1):
                print("self.x[" + (str(i) + "] = self.x[" + str(i-1) + "]"))
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
            
            # update position of head of snake
            if self.direction == 0:
                self.x[0] += self.step
            if self.direction == 1:
                self.x[0] -= self.step
            if self.direction == 2:
                self.y[0] -= self.step
            if self.direction == 3:
                self.y[0] += self.step
            
            self.updateCount = 0


    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
    
    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

class App:
    windowWidth = WINDOW_WIDTH
    windowHeigh = WINDOW_HEIGH
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player(10)
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeigh), pygame.HWSURFACE)

        pygame.display.set_caption('Клёвая игра, Питон')
        self._running = True
        self._image_surf = pygame.image.load("pygame.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        
    def on_loop(self):
        self.player.update()
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()
            elif (keys[K_LEFT]):
                self.player.moveLeft()
            elif (keys[K_UP]):
                self.player.moveUp()
            elif (keys[K_DOWN]):
                self.player.moveDown()

            if(keys[K_ESCAPE]):
                self._running = False
        
            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0)
        
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
            