#########################
# Main function to test Tile-Map System.  #
#########################
import pygame

from system import TileMap

# Initialize pygame.
pygame.init()

# Window (what player sees)
screen = pygame.display.set_mode((720, 480))

# Internal resolution (Game world) (GBA Edition)
GAME_WIDTH = 240
GAME_HEIGHT = 160

# Game Surface with internal resolution
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))

clock = pygame.time.Clock()

# Tile-Map
map_data = [
    "222222222222222",
    "200000000000002",
    "201111000011112",
    "200000000000002",
    "201111000011112",
    "200000000000002",
    "201111000011112",
    "200000000000002",
    "201111000011112",
    "222222222222222",
]

# Tile-Size
tile_size = 16

# Tile-Set
tile_set = {
    0: pygame.image.load("exemplo_assets/grass_00.png").convert_alpha(),
    1:  pygame.image.load("exemplo_assets/grass_01.png").convert_alpha(),
    2:  pygame.image.load("exemplo_assets/stump_grass.png").convert_alpha()
}

# Tile-Map System:
tile_map = TileMap(map_data, tile_size, tile_set)

# Game Loop
running = True
while running:
    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # UPDATE
    tile_map.update()

    # DRAW → draw EVERYTHING to game_surface
    game_surface.fill((0, 0, 0))
    tile_map.draw(game_surface)

    # SCALE → stretch to screen
    scaled_surface = pygame.transform.scale(game_surface, (720, 480))
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()