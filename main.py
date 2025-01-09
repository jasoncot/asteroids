import pygame
from constants import *
from player import Player

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	numpass, numfail = pygame.init()
	# print(numpass)
	# print(numfail)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	# group initialization
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	# group definitions
	Player.containers = (updatable, drawable)

	# player initialization
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player = Player(x, y)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		for item in updatable:
			item.update(dt)

		# paint the background
		screen.fill((0,0,0))

		# draw all the things
		for item in drawable:
			item.draw(screen)

		pygame.display.flip()
		dt = (clock.tick(60) / 1000)


if __name__ == "__main__":
	main()
