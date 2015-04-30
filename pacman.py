import sys, os, math, time, pygame
from pygame.locals import *

class Background(pygame.sprite.Sprite):
	def __init__(self, gs=None):
		self.gs = gs
		FILE = "images/board.png"
		self.image = pygame.image.load(FILE)
		self.rect = self.image.get_rect()

		
class Player(pygame.sprite.Sprite):
		
	def __init__(self, gs=None):
		self.gs = gs
		FILE = "images/pacman.png"
		self.image = pygame.image.load(FILE)
		self.image = pygame.transform.scale(self.image, (int(30),int(30)))
		
		self.rect = self.image.get_rect()
		self.rect.x = 396
		self.rect.y = 393

	def validMove(self, x, y):
		return 1
		
				
	def move(self, keycode):
		if (keycode == K_RIGHT):
			if self.validMove(self.rect.x+4, self.rect.y):
				self.rect = self.rect.move(4, 0)
			
		if (keycode == K_LEFT):
			self.rect = self.rect.move(-4,0)
			
		if (keycode == K_DOWN):
			self.rect = self.rect.move(0,4)
			
		if (keycode == K_UP):
			self.rect = self.rect.move(0,-4)
		return
		
	def tick(self):

		print self.rect.x, self.rect.y

		return
		
class GameSpace:
	def main(self):
		pygame.init()

		pygame.mixer.pre_init(44100, -16, 2, 2048) #initializing sound
		
		winTitle = pygame.display.set_caption("Paradigms Final Project: Multiplayer Pacman")
		
		self.size = self.width, self.height = 800, 800
		
		self.black = 0, 0, 0
		
		self.screen = pygame.display.set_mode(self.size)
		
		pygame.key.set_repeat(1, 50)
		
		self.clock = pygame.time.Clock()
		
		self.player = Player(self)
		self.background = Background(self)
		
		while 1:
			self.clock.tick(60)
			
			for event in pygame.event.get():
				if (event.type == KEYDOWN):
					self.player.move(event.key)
			
				if (event.type == pygame.QUIT):
					sys.exit()
				self.player.tick()
				
				self.screen.fill(self.black)	
				self.screen.blit(self.background.image, self.background.rect)
				self.screen.blit(self.player.image, self.player.rect)
			
				pygame.display.flip()
			
if __name__ == '__main__':
	gs = GameSpace()
	gs.main()
