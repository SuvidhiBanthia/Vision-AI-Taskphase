#importing pygame module
import pygame

#initializing the module
pygame.init()

#defining colors and font used
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,165,255)
cyan = (224,255,255)
grey = (128,128,128)

font = pygame.font.SysFont(None, 45, italic = True)

#Creating the game display
display_height = 300
display_width = 300
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tic-Tac-Toe')

#to track user mouse clicks
click = False

#to check which player's chance it is
player = 1

#to get the postion of the mouse click to detrmine the box
pos = [0,0]

#analysing the game state
over = 0

#vaiable for deciding the winner
winner = 0

#Representing the grid marks
marks = [[0,0,0],
           [0,0,0],
           [0,0,0]]


def boardDisplay():
	gameDisplay.fill(blue)
	for x in range(1,3):
		pygame.draw.line(gameDisplay, grey, (0, 100 * x), (display_width,100 * x), 5)
		pygame.draw.line(gameDisplay, grey, (100 * x, 0), (100 * x, display_height), 5)
		

def to_draw_marks():
	x_pos = 0
	for x in marks:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(gameDisplay, black, (x_pos * 100 + 10, y_pos * 100 + 10), (x_pos * 100 + 90, y_pos * 100 + 90), 7)
				pygame.draw.line(gameDisplay, black, (x_pos * 100 + 90, y_pos * 100 + 10), (x_pos * 100 + 10, y_pos * 100 + 90), 7)
			if y == -1:
				pygame.draw.circle(gameDisplay, white, (x_pos * 100 + 50, y_pos * 100 + 50), 45, 7)
			y_pos += 1
		x_pos += 1	


def to_check_if_game_over():

        #defining global variables for this loop
	global over
	global winner

	x_pos = 0

	#rows and columns
	for x in marks:
            
		#rows
		if sum(x) == 3:
			winner = 1
			over = 1
			
		if sum(x) == -3:
			winner = 2
			over = 1
			
		#columns
		if marks[0][x_pos] + marks [1][x_pos] + marks [2][x_pos] == 3:
			winner = 1
			over = 1
			
		if marks[0][x_pos] + marks [1][x_pos] + marks [2][x_pos] == -3:
			winner = 2
			over = 1
		x_pos += 1

	#diagonals
	if marks[0][0] + marks[1][1] + marks [2][2] == 3 or marks[2][0] + marks[1][1] + marks [0][2] == 3:
		winner = 1
		over = 1
		
	if marks[0][0] + marks[1][1] + marks [2][2] == -3 or marks[2][0] + marks[1][1] + marks [0][2] == -3:
		winner = 2
		over = 1

	#Tie condition
	if over == 0:
		tie = True
		
		#condition where no mark has been placed yet and tie is false
		for i in marks:
			for j in i:
				if j == 0:
					tie = False

		#Tie
		if tie == True:
			over = 1
			winner = 0



def decide_winner(winner):
    
    if winner != 0:
        if winner == 1:
            text = "    X wins!"
        elif winner == 2:
            text = "    O wins!"
    elif winner == 0:
        text = "    It's a tie!"

    endDisplay = font.render(text, True, black)

    #creating background rectangle and text for display
    pygame.draw.rect(gameDisplay, cyan, (display_width // 2 - 100, display_height // 2 - 60, 200, 57))
    gameDisplay.blit(endDisplay, (display_width // 2 - 100, display_height // 2 - 55))

    text2 = 'Start Again?'
    textPhoto = font.render(text2, True, black)
    pygame.draw.rect(gameDisplay, cyan, pygame.Rect(display_width // 2 - 90, display_height // 2, 200, 50))
    gameDisplay.blit(textPhoto, (display_width // 2 - 80, display_height // 2 + 12))


#MAIN LOOP
    
stop = False

while not stop:

	#creating board and enabling marks function
	boardDisplay()
	to_draw_marks()
	
        #Analysing the events
	for event in pygame.event.get():
            
		#for game exit
		if event.type == pygame.QUIT:
			stop = True
			
		#running the game
		if over == 0:
                    
			#check for mouseclick
			if event.type == pygame.MOUSEBUTTONDOWN and click == False:
				click = True
			if event.type == pygame.MOUSEBUTTONUP and click == True:
				click = False
				pos = pygame.mouse.get_pos()

				#flooring by 100 to get the box position in 1 simple integer
				box_x = pos[0] // 100
				box_y = pos[1] // 100

				# checking if the box clicked by mouse is empty
				if marks[box_x][box_y] == 0:
					marks[box_x][box_y] = player

					#passing the chance to next player
					player *= -1
					
					to_check_if_game_over()
					

	#To check if game over and not continue
	if over == 1:
		decide_winner(winner)
		
		#check for 'start again' option click
		if event.type == pygame.MOUSEBUTTONDOWN and click == False:
			click = True
		if event.type == pygame.MOUSEBUTTONUP and click == True:
			click = False
			pos = pygame.mouse.get_pos()

			#seeing if the mouse click is within the specified rectangle region
			if pygame.Rect(display_width // 2 - 90, display_height // 2, 200, 50).collidepoint(pos):
                            
				#resetting variables to initial values
				over = 0
				winner = 0
				player = 1
				pos = [0,0]
				marks = [[0,0,0],
                                         [0,0,0],
                                         [0,0,0]]

	#updating the display screen
	pygame.display.update()

#quitting the program
pygame.quit()

# confirmation message before exitting
quit()
