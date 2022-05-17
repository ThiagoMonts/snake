import pygame
from random import randint
from pygame.locals import *

def on_grid_random(): #Função que determina a posição aleatória da maçã
    x = randint(0,59)
    y = randint(0,59)
    return (x * 10, y * 10)

def collision(c1, c2): #Função de colisão
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Definição macro para movimentação da cobra
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600)) #Criando uma janela vazia
pygame.display.set_caption('Snake')

snake = [(290, 300), (300, 300), (310, 300)] #Criando a cobra, inicia com 3 segmentos
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) #Cor da cobra

apple_pos = on_grid_random() #Criando a maçã
apple = pygame.Surface((10,10))
apple.fill((255,0,0)) #Cor da maçã

my_direction = LEFT

clock = pygame.time.Clock() #Ajustando a velocidade da cobra

font = pygame.font.Font('freesansbold.ttf', 24)
score = 0

game_over = False
while not game_over: #Criando um loop principal
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT: #Implementando a função de sair do jogo
            pygame.quit()
            exit()
        if event.type == KEYDOWN: #Definindo a movimentação
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_RIGHT:
                    my_direction = RIGHT

    if collision(snake[0], apple_pos): #Se a cobra comer a maçã
        apple_pos = on_grid_random() #Uma nova posição da maçã é gerada
        snake.append((0,0)) #A cobra aumenta de tamanho
        score += 10

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0: #Checa se a cobra bate nas bordas
        game_over = True
        break

    for i in range(1, len(snake) - 1): #Checa se a cobra bate nela mesma
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake [i-1][1])

#Movimentação da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    screen.fill((0,0,0)) #Limpando a tela
    screen.blit(apple,apple_pos)

    for x in range(0, 600, 10): #Desenha as linhas verticais
        pygame.draw.line(screen, (50,50,50), (x,0), (x,600))
    for y in range(0, 600, 10): #Desenha as linhas horizontais
        pygame.draw.line(screen, (50,50,50), (0,y), (600,y))

    score_font = font.render(f'Placar: {score}', True, (255,255,255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 180, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 90)
    game_over_screen = game_over_font.render('Game Over', True, (255,0,0))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 50)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
