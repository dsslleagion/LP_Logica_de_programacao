import pygame
import time
import random

# Inicializa o pygame
pygame.init()

# Define cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Definições de tela
width = 800
height = 800

# Criando a tela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobrinha")

# Controle da cobra
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [x, y])

def gameLoop():
    game_over = False
    game_close = False
    
    x = width / 2
    y = height / 2
    
    dx = 0
    dy = 0
    
    snake_list = []
    length_snake = 1
    
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            screen.fill(black)
            message("Você perdeu! Pressione C para jogar novamente ou Q para sair", red, 50, height / 2)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += dx
        y += dy
        screen.fill(black)
        pygame.draw.rect(screen, green, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]
        
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
        
        for segment in snake_list:
            pygame.draw.rect(screen, blue, [segment[0], segment[1], snake_block, snake_block])
        
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_snake += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()
