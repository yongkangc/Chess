import pygame
import os
import time

import piece
from Board import board

pygame.font.init()


board_img = pygame.transform.scale(pygame.image.load(os.path.join("img","board_alt.png")), (750, 750))


turn = "w"


def menu_screen(win):
    "This function sets the screen that user clicks and enters into the game"
    global bo
    run = True

    while run:
        win.fill((128,128,128))
        font = pygame.font.SysFont("comicsans", 80)
        title = font.render("CHESS!", 1, (0,200,0))
        join = font.render("Click To Play 2 Players", 1, (0, 128, 0))
        win.blit(title, (width/2 - title.get_width()/2, 200))
        win.blit(join, (width / 2 - join.get_width() / 2, 400))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
          
                run = False
    main()
                
def redraw_gameWindow(win, p1, p2, color):
        """ Displays up the Chess Board Window 
        includes time """
        
        win.blit(board_img, (0, 0))
        
    
    
        formatTime1 = str(int(p1//60)) + ":" + str(int(p1%60))
        formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
        if int(p1%60) < 10:
            formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
        if int(p2%60) < 10:
            formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]
    
        font = pygame.font.SysFont("comicsans", 30)
        txt = font.render("Player 2 Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render("Player 1 Time: " + str(formatTime1), 1, (255,255,255))
        win.blit(txt, (540,10))
        win.blit(txt2, (540, 700))
    
        txt = font.render("Press q to Quit", 1, (255, 255, 255))
        win.blit(txt, (10, 20))
    
    
    
        font = pygame.font.SysFont("comicsans", 30)
            
        if board.turn == color:
            txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
        else:
            txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
            win.blit(txt3, (width / 2 - txt3.get_width() / 2, 700))
    
    
        pygame.display.update()



def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text,1, (255,0,0))
    win.blit(txt, (width / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT+1, 3000)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False


def click(pos):
    """
    clicks on the board squares
    :return: mouse position in 2D board Array form
    """
    rect = (113,113,525,525)
    
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[1]
            i = int(divX / (rect[2]/8))
            j = int(divY / (rect[3]/8))
            return i, j

    return -1, -1





def main():

    clock = pygame.time.Clock()
    run = True
    p1Time = 900
    p2Time = 900
    
    
    piece_display = board(8,8)

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONUP: 
                    pos = pygame.mouse.get_pos()
                    i, j = click(pos)
                    piece_display.select(i,j,piece_display.turn)
                    piece_display.update_moves()
                    print(i,j,piece_display.turn)
                    
                   

        win.blit(board_img, (0, 0))
        
        #displaying the pieces
        piece_display.draw(win,piece_display.turn)
        
        pygame.display.update()
  
    menu_screen(win)


width = 750
height = 750
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
menu_screen(win)