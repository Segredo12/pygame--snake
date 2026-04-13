#########################
# Main function to test Inventory System. #
#########################
import pygame
from pygame import Color
from system import InventorySystem


# Initialize pygame.
pygame.init()

# Game Variables.
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Configuration DialogueSystem variables.
font = pygame.font.Font(None, 24)

# Initializing InventorySystem.
inventory = InventorySystem(
    font=font,
    cols=4,
    rows=3,
    slot_size=100,
    padding=5,
    position_x=0,
    position_y=0,
    slot_base_color=Color(255, 255, 255),
    slot_hover_color=Color(255, 255, 0)
)

# Add test items.
inventory.slots[0] = "Sword"
inventory.slots[1] = "Potion"
inventory.slots[2] = "Key"


# Game Loop Logic
running = True
while running:
    for event in pygame.event.get():
        # Preparing Close Game Button
        if event.type == pygame.QUIT:
            running = False

        # Trigger open inventory Btn i
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                inventory.toggle()

        # Updating inventory logic
        if inventory.is_active():
            inventory.handle_event(event)

    # Update systems
    inventory.update()

    # Draw everything
    screen.fill((30, 30, 30))  # clear screen
    inventory.draw(screen)

    # Updates game display
    pygame.display.flip()
    # 60 frames
    clock.tick(60)

# Quit game.
pygame.quit()