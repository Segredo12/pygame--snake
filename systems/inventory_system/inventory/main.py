#########################
# Main function to test Inventory System. #
#########################
import pygame
from pygame import Color

import systems
from system import InventorySystem
from systems.item_system.item.system import Item

# Use path lib to import sprites.
from pathlib import Path

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
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = BASE_DIR / "item_system/item/example_assets"

inventory.slots[0] = Item(1, "Sword", ASSETS_DIR / "sword.png")
inventory.slots[1] = Item(2, "Healing Potion", ASSETS_DIR / "red_potion.png")
inventory.slots[2] = Item(3, "Strange Key", ASSETS_DIR / "key.png")


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