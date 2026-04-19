import pygame
import random
import sys

pygame.init() #Initialize pygame library

WIDTH = 400 #Game window
HEIGHT = 600 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

BLACK = (0, 0, 0)

# LOAD IMAGES
bird_img = pygame.image.load("bird.png").convert_alpha()
pipe_img = pygame.image.load("pipe.png").convert_alpha()
bg_img = pygame.image.load("bg.jpg").convert()

# Resize images
bird_width = 50
bird_height = 40

pipe_width = 80
pipe_height = 600

bird_img = pygame.transform.scale(bird_img, (bird_width, bird_height)) #To fit the game window and for better aesthetics
pipe_img = pygame.transform.scale(pipe_img, (pipe_width, pipe_height))
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))

#BIRD
bird_x = 80
bird_y = 250

bird_velocity = 0
gravity = 0.5
jump_power = -8 #Go up when SPACE is pressed

#PIPES
pipe_gap = 160
pipe_speed = 3

pipes = []
score = 0 # Initial score
game_over = False #Game state
game_started = False
start_button = pygame.Rect(125, 260, 150, 60)


def create_pipe():
    height = random.randint(100, 350)
    return {
        "x": WIDTH,
        "top_height": height
    }

pipes.append(create_pipe())

def reset_game():
    global bird_y, bird_velocity, pipes, score, game_over

    bird_y = 250
    bird_velocity = 0
    pipes = [create_pipe()]
    score = 0
    game_over = False


#MAIN LOOP
while True:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if not game_started:
                if start_button.collidepoint(event.pos):
                    game_started = True

        # Keyboard
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                if game_started:
                    if game_over:
                        reset_game()
                    else:
                        bird_velocity = jump_power

    if game_started and not game_over: #Prevents movement before start

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Moving pipes for bird movement illusion
        for pipe in pipes:
            pipe["x"] -= pipe_speed

        # New pipe
        if pipes[-1]["x"] < 220:
            pipes.append(create_pipe())

        # Remove old pipe
        if pipes[0]["x"] < -pipe_width:
            pipes.pop(0)
            score += 1

        # Bird collision box
        bird_rect = pygame.Rect(
        bird_x + 10,      # move right
        bird_y + 8,      # move down
        bird_width - 20, # narrower
        bird_height - 16 # shorter
    )

        # Check collision
        for pipe in pipes:

            top_rect = pygame.Rect(
            pipe["x"] + 8,
            0,
            pipe_width - 16,
            pipe["top_height"]
        )

            bottom_rect = pygame.Rect(
            pipe["x"] + 8,
            pipe["top_height"] + pipe_gap,
            pipe_width - 16,
            HEIGHT - pipe["top_height"] - pipe_gap
        )

            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
                game_over = True

        # Ground / ceiling
        if bird_y < 0 or bird_y + bird_height > HEIGHT:
            game_over = True

    # Background
    screen.blit(bg_img, (0, 0))
    screen.blit(bird_img, (bird_x, bird_y))
    if not game_started:
        title = font.render("Flappy Bird", True, BLACK)
        screen.blit(title, (115, 180))

        pygame.draw.rect(screen, (0, 200, 0), start_button)

        start_text = font.render("START", True, BLACK)
        screen.blit(start_text, (145, 278))

        pygame.display.update() #Udates the screen with menu and sprites
        continue

    # Pipes
    for pipe in pipes:

        # Top pipe flipped
        top_pipe = pygame.transform.flip(pipe_img, False, True)

        screen.blit(
            top_pipe,
            (pipe["x"], pipe["top_height"] - pipe_height)
        )

        # Bottom pipe
        screen.blit(
            pipe_img,
            (pipe["x"], pipe["top_height"] + pipe_gap)
        )

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        BLACK
    )

    screen.blit(score_text, (10, 10))

    # Game Over
    if game_over:

        over_text = font.render("Game Over!", True, BLACK)
        restart_text = font.render("Press SPACE", True, BLACK)

        screen.blit(over_text, (110, 260))
        screen.blit(restart_text, (95, 310))

    pygame.display.update()