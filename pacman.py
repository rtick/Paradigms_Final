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
		#lower right half of board start
		if x>636:
			return 0
		elif y>633:
			return 0
		elif x>536 and y>213 and y<453:
			return 0
		elif x>476 and x<532 and y>333 and y<453:
			return 0
		elif x> 416 and x<532 and y>453 and y<513:
			return 0
		elif (y>453 and y<513 and x>536 and x<636) or (y>481 and y<573 and x>536 and x<596):
			return 0
		elif (y>513 and y<573 and x>596):
			return 0
		elif (y>573 and y<633 and x>416 and x<636) or (x<532 and x>476 and y>513 and y<609):
			return 0
		elif (y<633 and y>537 and x<416 and x>352) or (y>513 and y<572 and x>296 and x<476):
			return 0
		elif (x<416 and x>356 and y<513 and y>421) or (y>393 and y<453 and x>296 and x<476):
			return 0
		#lower right half of board end
		#lower left half of board
		elif ((x<= 292 and x>= 237) and (y>= 332 and y <=449)):
			return 0
		elif ((x>=237 and x<=355) and (y>=454 and y<=512)):
			return 0
		elif ((x<=231) and (y>=214 and y<=452)):
			return 0
		elif ((x<=131) and (y>=452 and y<= 514)):
			return 0
		elif (( x>= 137 and x <=177) and (y>=454 and y<=512)):
			return 0
		elif ((x>=177 and x<=231) and (y>=454 and y<=572)):
			return 0
		elif ((x <= 171) and (y >= 516 and y<= 572)):
			return 0
		elif ((x<= 131) and (y >= 573)):
			return 0
		elif ((x >= 237 and x<= 291) and (y>= 516 and y<= 629)):
			return 0
		elif ((x>= 137 and x<=351) and (y<=632 and y>=578)):
			return 0
		#end lower left half of board
		else:
			return 1
		
				
	def move(self, keycode):
		if (keycode == K_RIGHT):
			if self.validMove(self.rect.x+4, self.rect.y):
				self.rect = self.rect.move(4, 0)
			
		if (keycode == K_LEFT):
			if self.validMove(self.rect.x-4, self.rect.y):
				self.rect = self.rect.move(-4,0)
			
		if (keycode == K_DOWN):
			if self.validMove(self.rect.x, self.rect.y+4):
				self.rect = self.rect.move(0,4)
			
		if (keycode == K_UP):
			if self.validMove(self.rect.x, self.rect.y-4):
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
		
		pygame.key.set_repeat(1, 50) #adjust this to make pacman move faster
		
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
