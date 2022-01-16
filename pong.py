import pygame

pygame.init()

black =(0,0,0)
white =(255,255,255)
screen_size=(800, 600)
player_width = 15
player_height = 90

#coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

#coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

#coordenadas de pelota
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            
        if event.type == pygame.KEYDOWN:
            #jugador1
            if event.key == pygame.K_w:
                player1_y_speed = -3
            if event.key == pygame.K_s:
                player1_y_speed = 3
            #jugador2
            if event.key == pygame.K_UP:
                player2_y_speed = -3
            if event.key == pygame.K_DOWN:
                player2_y_speed = 3
                
        if event.type == pygame.KEYUP:
            #jugador1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #jugador2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0
      
    #evita que jugadores salgan de la pantalla
    if player1_y_coor > 500:
        player1_y_coor = 500
    if player1_y_coor < 10:
        player1_y_coor = 10
        
    if player2_y_coor > 500:
        player2_y_coor = 500
    if player2_y_coor < 10:
        player2_y_coor = 10
              
    #revota pelota si choca arriba o abajo
    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1
    
    #revisa si pelota sale por el lado derecho    
    if ball_x > 800 or ball_x < 10:
        ball_x = 400
        ball_y = 300
    #si sale de la pantalla, invierte direccion
        ball_speed_x *= -1
        ball_speed_y *= -1 
    #modifica coordenadas para dar movimiento a jugadores / pelota
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    ball_x += ball_speed_x
    ball_y += ball_speed_y
          
    screen.fill(black)
    #zona de dibujo
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor,player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor,player2_y_coor, player_width, player_height))
    pelota = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)
    
    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        ball_speed_x *= -1
    
    pygame.display.flip()
    clock.tick(60)          
pygame.quit()
