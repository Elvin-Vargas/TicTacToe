# Import Modules
import pygame
from pygame.locals import *

pygame.init()


# Game Window
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Defining the variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False

# Define Colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Define Font
font = pygame.font.SysFont(None, 40)

# Define Restart Rectangle
restartRect = Rect(SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2, 160, 50)

# This function defines the screen and draws the grid on screen
def drawGrid():

	# Defining the colors
	bg = 255,255,255
	gridColor = 0,0,0

	# Declaring the Screen
	screen.fill(bg)

	# Defining the Grid
	for x in range(1,3):
		pygame.draw.line(screen, gridColor, (0, x * 100), (SCREEN_WIDTH, x * 100), line_width)
		pygame.draw.line(screen, gridColor, (x * 100, 0), (x * 100, SCREEN_HEIGHT), line_width)

for x in range(3):
	row = [0] * 3
	markers.append(row)


def drawMarkers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, green, (x_pos*100 + 15, y_pos*100 + 15), (x_pos*100 + 85, y_pos*100 + 85), line_width)
				pygame.draw.line(screen, green, (x_pos*100 + 15, y_pos*100 + 85), (x_pos*100 + 85, y_pos*100 + 15), line_width)
			if y == -1:
				pygame.draw.circle(screen, red, (x_pos*100 + 50, y_pos*100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1

def checkWinner():

	global winner
	global game_over

	y_pos = 0

	for x in markers:
		# Check Columns
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True

		# Check Rows
		if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
			winner = 2
			game_over = True

		y_pos += 1

	# Check Cross
	if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
		winner = 2
		game_over = True

def drawWinner(winner):
	winText = 'Player ' + str(winner) + ' wins!'
	winImg = font.render(winText, True, blue)
	pygame.draw.rect(screen, green, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60, 200, 50))
	screen.blit(winImg, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))

	restartText = 'Play Again?'
	restartImg = font.render(restartText, True, blue)
	pygame.draw.rect(screen, green, restartRect)
	screen.blit(restartImg, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))

# Game Loop
run = True
while run:

	drawGrid()
	drawMarkers()

	# Game Event Handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if game_over == 0:
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0]
				cell_y = pos[1]
				if markers[cell_x // 100][cell_y // 100] == 0:
					markers[cell_x // 100][cell_y // 100] = player
					player *= -1
					checkWinner()

	if game_over == True:
		drawWinner(winner)
		# Check for mouseClick to see if restart plate was clicked
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if restartRect.collidepoint(pos):
				# Reset All Variables
				markers = []
				pos = []
				player = 1
				winner = 0
				game_over = False
				for x in range(3):
					row = [0] * 3
					markers.append(row)


	pygame.display.update()

pygame.quit()