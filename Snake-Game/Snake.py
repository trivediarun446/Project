import pygame 
import random
# Pygame initialization 
pygame.init()


# Screen Configuration 
screen_x , screen_y = 800 , 600 
window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Snake Game")


# Score 
score = 0 
clock = pygame.time.Clock()

# Snake Configuration 
snake_size = 10 
snake_speed = 15    
snake_length = 1 
snake = [] 
snake_head = pygame.Rect( screen_x/2 , screen_y/2 , snake_size , snake_size )


# Food Configuration 
food = pygame.Rect(
    round(random.randrange(0,screen_x-snake_size) / 10 )*10.0 , 
    round(random.randrange(0 , screen_y - snake_size)/10)*10.0 , 
    snake_size , snake_size 
)

# Initial starting condition of loop 
runing = True 
x = 0 
y = 0 
direction = "stop" 


# Main Game Loop 
while runing :
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT :
               runing = False 
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP and direction != "down":
                    y -= snake_size 
                    x = 0 
                    direction = "Up"
               elif event.key == pygame.K_DOWN and direction != "Up":
                    y += snake_size 
                    x = 0 
                    direction = "down"
               elif event.key == pygame.K_LEFT and direction != "Right":
                    x-= snake_size 
                    y = 0 
                    direction = "Left"
               elif event.key == pygame.K_RIGHT and direction != "Left":
                    x+= snake_size 
                    y = 0 
                    direction = "Right"
     
     
     # Collision detection 
     # if snake_head.x >= screen_x or snake_head.y <= screen_y or snake_head.x < 0 or snake_head.y < 0: 
     #      runing = False 
     
     snake_head.x += x 
     snake_head.y += y 

     window.fill((0,0,0))

     pygame.draw.rect(window ,(255,0,0) , food) 

     pygame.display.flip()


     # clock.tick(snake_speed)

pygame.quit()

