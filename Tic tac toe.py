#import modules
import pygame
from pygame.locals import *

pygame.init()

screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


font = pygame.font.SysFont(None, 40)

clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0

#setup a rectangle for "Play Again" Option
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

#create empty 3 x 3 list to represent the grid
for x in range (3):
	row = [0] * 3
	markers.append(row)

def draw_board():
	bg = (255, 255, 210)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0, 100 * x), (screen_width,100 * x), line_width)
		pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)


#main loop
run = True
while run:

	
	draw_board()
	for event in pygame.event.get():
		#handle game exit
		if event.type == pygame.QUIT:
			run = False
		#run new game
		
	

	#update display
	pygame.display.update()

pygame.quit()