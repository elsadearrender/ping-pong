# Import library
import pygame
import random as rd
from pygame import mixer

# Initialize pygame

pygame.init()

# window size
screen_width = 800
screen_height = 600

# Colors
background_color = (0, 0, 0)
player_color = (255, 255, 255)
ball_color = (255, 255, 255)
line_color = (255, 255, 255)


# Player size
players_width = 15
players_height = 150

# Player 1 coordinates
player_1_x = 55
player_1_y = 210
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 735
player_2_y = 210
player_2_y_speed = 0

# Ball coordinates
ball_x = 400
ball_y = 300
ball_radius = 20

ball_speed_x = 0.3
ball_speed_y = 0.3

# Icon
icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption("Tenis de Mesa")

# Score variables
player_1_score = 0
player_2_score = 0

# Score font 
score_font = pygame.font.Font("minecraft1.otf", 32)

# Win font
win_font = pygame.font.Font("minecraft1.otf", 64)

# Score position in the screen - Player 1
player_1_score_x = 10
player_1_score_y = 10

# Score position in the screen - Player 2
player_2_score_x = screen_width - 185
player_2_score_y = 10

# Win text position
win_x = 80
win_y = 250

# Player 1 score function
def show_score_1(x, y):
    score1 = score_font.render("El Niño: " + str(player_1_score), True, (255, 255, 255))
    screen.blit( score1, (x, y) )

# Player 2 score function
def show_score_2(x, y):
    score2 = score_font.render("La Niña: " + str(player_2_score), True, (255, 255, 255))
    screen.blit( score2, (x, y) )






# size variable
size = ( screen_width, screen_height )

# Display the window
screen = pygame.display.set_mode( size )

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player key controls

        # Cheks for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Player 1
            if event.key == pygame.K_a:
                player_1_y_speed = -0.5

            if event.key == pygame.K_s:
                player_1_y_speed = 0.5

            # Player 2
            if event.key == pygame.K_k:
                player_2_y_speed = -0.5

            if event.key == pygame.K_l:
                player_2_y_speed = 0.5
 
        if event.type == pygame.KEYUP:

            # Player 1
            if event.key == pygame.K_a:
                player_1_y_speed = -0

            if event.key == pygame.K_s:
                player_1_y_speed = 0

            # Player 2
            if event.key == pygame.K_l:
                player_2_y_speed = -0

            if event.key == pygame.K_k:
                player_2_y_speed = 0




    # Player movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed

    # Players boundaries

    # Player 1
    if player_1_y <= 0:
        player_1_y = 0

    if player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0

    if player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball boundaries: top or buttom
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1

    # Ball boudaries (right or left) and score update
    if ball_x > screen_width:

        player_1_score += 1
        
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice((-1, 1))

    elif ball_x < 0:

        player_2_score += 1
          
        ball_x = screen_width/2
        ball_y = screen_height/2
        ball_speed_x *= rd.choice((-1, 1))
        
   


    # Fill the screen with color
    screen.fill( background_color )

    # Drawing area

    # Define the player 1 - left: rectangle
    player_1 = pygame.draw.rect( screen, player_color, (player_1_x, player_1_y, players_width, players_height ))

    # Define the player 2 - left: rectangle
    player_2 = pygame.draw.rect( screen, player_color, (player_2_x, player_2_y, players_width, players_height ))

    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2,0),( screen_width/2, screen_height) )

    # Draw the ball
    ball = pygame.draw.circle( screen, ball_color, (ball_x, ball_y), ball_radius)

    # collitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball_sound = mixer.Sound("sonido de pato.wav")
        ball_sound.play()

    # Player win
    if player_1_score == 3:

        ball_y = 2000

        ball_speed_x = 0
        ball_speed_y = 0
        
        player_1_y_speed = 0
        player_2_y_speed = 0

        win_text = win_font.render("FELICITACIONES", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y))

    elif player_2_score == 3:

        ball_y = 2000

        ball_speed_x = 0
        ball_speed_y = 0

        player_1_y_speed = 0
        player_2_y_speed = 0

        win_text = win_font.render("FELICIDADES", True, (255, 255, 255))
        screen.blit(win_text, (win_x, win_y))




    # Call the show_score_1 function
    show_score_1(player_1_score_x, player_1_score_y)

    # Call the show_score_2 function
    show_score_2(player_2_score_x, player_2_score_y)


    # Refresh the window
    pygame.display.flip()


    