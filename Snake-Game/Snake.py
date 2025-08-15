import pygame 
import random

# Initializing the pygame 
pygame.init() 

# set the length and breath of the pygame window 
window = pygame.display.set_mode((800 , 600))

# set the Window name 
pygame.display.set_caption("Snake Game")

# For continuous running of the window
runing = True 


#  Here some important varible 
Player_Name = ""
score = 0 
Diffculty_level = ""  




while runing :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False 

    for row in range(1 , 791 , 1 ):
        for col in range( 1 , 591 , 1):
            if row == 1 or row == 790 or col== 1 or col == 590:
                    #  b_rect = pygame.Rect()
                     pygame.draw.rect(window , (0 , 255 , 0 ) , (row , col ,10,10))

    # snake_head = pygame.Rect() 
    pygame.draw.rect(window,(255,255,255), (800/2 , 600/2 , 10 , 10))
    pos_x = random.randint(2 , 789)
    pos_y = random.randint(2 , 589)
    if pos_x == 800/2 and pos_y == 600/2:
        pygame.draw.circle(window,(0,0,255) ,( pos_x % 790 , pos_y % 590 ) , 10)
    else:
        pygame.draw.circle(window,(0,0,255) ,( 500 , 400 ) , 10)
         
    pygame.display.flip()

pygame.quit()