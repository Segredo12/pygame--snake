#######################
# Main function to test Player System. #
#######################
import pygame

from system import Player

# Initialize pygame.
pygame.init()

# Game Variables.
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def load_frames(path_list):
    return [pygame.image.load(p).convert_alpha() for p in path_list]

# Player System:
player_frames = {
    "IDLE": load_frames([
        "example_assets/idle_0.png",
        "example_assets/idle_1.png",
    ]),
    "WALK": load_frames([
        "example_assets/walk_0.png",
        "example_assets/walk_1.png",
    ]),
}


player = Player(
    x=400,
    y=300,
    speed=3,
    sprite_frames=player_frames
)

# Game Loop Logic
running = True
while running:
    for event in pygame.event.get():
        # Preparing Close Game Button
        if event.type == pygame.QUIT:
            running = False

    # Update systems
    player.update()

    # Draw everything
    screen.fill((30, 30, 30))  # clear screen
    player.draw(screen)

    # Updates game display
    pygame.display.flip()
    # 60 frames
    clock.tick(60)

# Quit game.
pygame.quit()