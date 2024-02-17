#######################################################################
#
#   GENERATED CODE !!!  TheBloke * phi 2 3B Q4_K_S gguf
#
#######################################################################

import pygame 
import random

# Set up the screen 
width = 800
height = 600
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Snake") 
 
# Create colors 
white = (255, 255, 255) 
black = (0, 0, 0) 
 
# Set up snake body 
snake = pygame.image.load("snake.png") 
body = [pygame.transform.scale(snake, (50, 50))] 
snake_head = pygame.image.load("snake-head.png") 
 
# Set up food 
food = pygame.image.load("food.png") 
food_pos = [random.randint(0, width - snake.get_width()), 
            random.randint(0, height - snake.get_height())] 
 
# Set up score and game state variables 
score = 0 
game_over = False 
 
while True: 
 
    # Handle events 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 

    # Move snake head 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: 
        snake_head.rect.move_ip(-10, 0) 
    elif keys[pygame.K_RIGHT]: 
        snake_head.rect.move_ip(10, 0) 

    # Check if snake has eaten food and increase score 
    if snake_head.rect.colliderect(food): 
        score += 10 
        food_pos = [random.randint(0, width - snake.get_width()), 
                    random.randint(0, height - snake.get_height())] 
        snake.appendleft(snake.pop()) 

    # Check if game is over 
    if len(snake) > 20 or (not food_pos): 
        game_over = True 
    else: 
        for part in snake[1:-1]: 
            part.rect.x = snake_head.rect.x - 10 * (len(snake) - 1) 

    # Draw game screen 
    screen.fill(white) 
    screen.blit(snake_head, snake_head.get_rect()) 
    for part in snake: 
        screen.blit(part, part.get_rect()) 
    if food_pos != [0, 0]: 
        screen.blit(food, food_pos) 

    # Check for collisions and remove dead parts of the snake 
    if snake_head.colliderect(snake[-1].rect): 
        game_over = True 
        score = 0 
    for part in reversed(snake)[1:]: 
        if part.rect.x < 0 or part.rect.x > width - snake.get_width() or \
                part.rect.y < 0 or part.rect.y > height - snake.get_height(): 
            game_over = True 
            score = 0 

    pygame.display.flip() 
    pygame.time.wait(100) 

print("Score:", score)
