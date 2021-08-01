import pygame
import numpy as np
pygame.init()

#defining colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,165,255)
cyan = (224,255,255)
grey = (128,128,128)
turquiose = (64,224,208)
font = pygame.font.SysFont(None, 142, italic = True)

'''

#Creating the game display
display_height = 700
display_width = 700
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Connect Four')

'''

def boardDisplay():
	gameDisplay.fill(cyan)

	text = font.render(" 1 2  3  4  5  6  7", True, blue, turquiose)
	textRect = text.get_rect()
	textRect.center = (350, 650)
	gameDisplay.blit(text, textRect)
	
	for x in range(1,7):
		pygame.draw.line(gameDisplay, grey, (0, 100 * x), (display_width,100 * x), 5)
	for x in range (1,7):
		pygame.draw.line(gameDisplay, grey, (100 * x, 0), (100 * x, display_height), 5)

	pygame.display.flip()

def create_board_markers():
    markers = np.zeros((6,7))
    return markers

def place_board_markers(markers, row, selet_col, player_piece):
        markers[row][select_col-1] = player_piece

def valid_move(markers, select_col):
        if markers[5][select_col-1] == 0:
                return True
        else:
                False

def get_piece_position(markers, select_col):
        for row in range(6):
              if markers[row][select_col-1] == 0:
                      return row

def flip_markers(markers):
        return(np.flip(markers, 0))
        
def to_check_if_game_over(markers, player):
        
        #columns
        for col in range(7):
                for row in range(3):
                        if markers[row][col] == player and markers[row+1][col] == player and markers[row+2][col] == player and markers[row+3][col] == player:
                                return True
                               

        #rows
        for col in range(4):
                for row in range(6):
                        if markers[row][col] == player and markers[row][col+1] == player and markers[row][col+2] == player and markers[row][col+3] == player:
                                return True

        #diagonal type 1
        for col in range(4):
                for row in range(3):
                        if markers[row][col] == player and markers[row+1][col+1] == player and markers[row+2][col+2] == player and markers[row+3][col+3] == player:
                                return True

        #diagonal type 2
        for col in range(0,4):
                for row in range(3,6):
                        if markers[row][col] == player and markers[row-1][col+1] == player and markers[row-2][col+2] == player and markers[row-3][col+3] == player:
                                return True

        #Tie condition
        if player == 1 or player == 2:
                tie = True
                #condition where no marker has been placed yet and tie is false
                for row in markers:
                        for col in row:
                                if col == 0:
                                        tie = False
                #Tie
                if tie == True:
                        print("It's a tie!")
                        over = 1



               
#creating the markers array        
markers = create_board_markers()
print(flip_markers(markers))
over = False
player = 1

while not over:
        
    #boardDisplay()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    if player == 1:
        select_col = int(input("Player 1 enter key from 1 to 7 :"))
        if select_col<8 and select_col >0:
                if valid_move(markers, select_col):
                        row = get_piece_position(markers, select_col)
                        place_board_markers(markers, row, select_col, player)
                        if to_check_if_game_over(markers, player):
                                print("Player 1 wins")
                                over = True
                                
                                
                player+=1
        else:
                print("Enter valid input i.e. from 1 to 7")
                        
    elif player == 2:
        select_col = int(input("Player 2 enter key from 1 to 7 :"))
        if select_col<8 and select_col >0:
                if valid_move(markers, select_col):
                        row = get_piece_position(markers, select_col)
                        place_board_markers(markers, row, select_col, player)
                        if to_check_if_game_over(markers, player):
                                print("Player 2 wins")
                                over = True
                                
                player-=1
        else:
                print("Enter valid input i.e. from 1 to 7")

    print(flip_markers(markers))
        
    #pygame.display.update()

pygame.quit()
