import pygame
from pygame import Color


class InventorySystem:

    def __init__(self, font, cols:int, rows:int, slot_size:int, padding:int, position_x:float, position_y:float, slot_base_color:Color, slot_hover_color:Color):
        self.font = font
        self.active = False

        # Inventory Data
        self.slots = [None] * (cols * rows)
        self.selected_index = 0

        # UI Config
        self.cols = cols
        self.rows = rows
        self.slot_size = slot_size
        self.padding = padding
        self.slot_base_color = slot_base_color
        self.slot_hover_color = slot_hover_color

        # Position
        self.start_x = position_x
        self.start_y = position_y

        # Dragging
        self.dragging_item = None
        self.dragging_index = None
        self.mouse_pos = (0, 0)

        # Hovered slot
        self.hovered_index = None

    # Function that is going to handle system event.
    def handle_event(self, event):
        # Case system not active ignore.
        if not self.active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 : # Left Click
                index = self.get_slot_at_pos(event.pos)

                if index is not None and self.slots[index] is not None:
                    # Drag activation
                    self.dragging_item = self.slots[index]
                    self.dragging_index = index
                    self.slots[index] = None  # remove from slot

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # left click

                # Only proceed if dragging something
                if self.dragging_item is not None:
                    index = self.get_slot_at_pos(event.pos)

                    if index is not None:
                        # Swap items
                        target_item = self.slots[index]

                        self.slots[index] = self.dragging_item

                        # If there was an item, return it to origin
                        if target_item is not None:
                            self.slots[self.dragging_index] = target_item

                    else:
                        # Dropped outside return to original slot
                        self.slots[self.dragging_index] = self.dragging_item

                    # Reset dragging
                    self.dragging_item = None
                    self.dragging_index = None

        # Updates mouse movement.
        elif event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos

    def draw(self, screen):
        # Case system not active ignore.
        if not self.active:
            return

        # Printing inventory grid.
        for i in range(len(self.slots)):
            rect = rect = self.get_slot_rect(i)

            # Draw white square
            square_line_width = 3

            # Setting default color.
            color = self.slot_base_color

            if i == self.hovered_index:
                # Case it's being hovered change color.
                color = self.slot_hover_color

            # Draw inventory slot.
            pygame.draw.rect(screen, color, rect, square_line_width)

            # Draw item if it exists
            item = self.slots[i]

            # Renders item
            if item is not None:
                text_surface = self.font.render(item, True, self.slot_base_color)

                # Center text in slot.
                text_rect = text_surface.get_rect(center=rect.center)

                screen.blit(text_surface, text_rect)

        # Renders dragging item
        if self.dragging_item is not None:
            text_surface = self.font.render(self.dragging_item, True, self.slot_base_color)
            text_rect = text_surface.get_rect(center=self.mouse_pos)
            screen.blit(text_surface, text_rect)

    def get_slot_at_pos(self, pos):
        for i in range(len(self.slots)):
            rect = self.get_slot_rect(i)

            if rect.collidepoint(pos):
                return i
        # Safe exit
        return None

    def get_slot_rect(self, i):
        col = i % self.cols
        row = i // self.cols

        x = self.start_x + col * (self.slot_size + self.padding)
        y = self.start_y + row * (self.slot_size + self.padding)

        return pygame.Rect(x, y, self.slot_size, self.slot_size)

    def update(self):
        # Only executes case inventory is active
        if not self.active:
            return

        # Update hovered index with update function.
        self.hovered_index = self.get_slot_at_pos(pygame.mouse.get_pos())

    # Function used to enable/disable system.
    def toggle(self):
        self.active = not self.active

    # Function to easy check if system is active.
    def is_active(self):
        return self.active