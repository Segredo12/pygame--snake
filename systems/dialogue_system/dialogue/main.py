########################
# Main function to test DialogueSystem. #
########################
import pygame
from pygame import K_SPACE
from system import DialogueSystem

# Initialize pygame.
pygame.init()

# Game Variables.
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Configuration DialogueSystem variables.
font = pygame.font.Font(None, 32)
dialogue_box = pygame.Rect(50, 400, 700, 150)

# Initializing DialogueSystem
dialogue_system = DialogueSystem(font, dialogue_box)

# Simulating NPC.
# (DEBUG purposes)
circle_x = 100
circle_y = 300
speed = 3

# Game Loop Logic.
running = True
while running:
    for event in pygame.event.get():
        # Preparing Close Game Button.
        if event.type == pygame.QUIT:
            running = False

        # Trigger Chat using Btn E
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                dialogue_system.start([
                    "Bem vindo aventureiro.",
                    "Este é um sistema de diálogo feito pelo nosso criador.",
                    "Que corra tudo bem, e não desistas."
                ])

        if dialogue_system.is_active():
            # Handles dialogue.
            dialogue_system.handle_event(event, K_SPACE)
        else:
            # Player / Game input here.
            pass

    if not dialogue_system.is_active():
        # Moving circle
        circle_x += speed

        # Bouncing from screen edges.
        if circle_x > 800 or circle_x < 0:
            speed *= -1

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, (0, 200, 255), (circle_x, circle_y), 20)
    dialogue_system.draw(screen)

    # Updates game display
    pygame.display.flip()
    # 60 frames
    clock.tick(60)

# Quit game.
pygame.quit()