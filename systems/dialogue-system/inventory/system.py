import pygame


class InventorySystem:

    def __init__(self, font, cols:int, rows:int, slot_size:int, padding:int, position_x:float, position_y:float):
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

        # Position
        self.start_x = position_x
        self.start_y = position_y

        # Dragging
        self.dragging_item = None
        self.dragging_index = None
        self.mouse_pos = (0, 0)

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

        elif event.type == pygame.MOUSEMOTION:
            self.mouse_pos = event.pos

    def draw(self, screen):
        # Case system not active ignore.
        if not self.active:
            return

        # Printing inventory grid.
        for i in range(len(self.slots)):
            col = i % self.cols
            row = i // self.cols

            x = self.start_x + col * (self.slot_size + self.padding)
            y = self.start_y + row * (self.slot_size + self.padding)

            rect = pygame.Rect(x, y, self.slot_size, self.slot_size)

            # Draw white square
            square_line_width = 3
            pygame.draw.rect(screen, (255, 255, 255), rect, square_line_width)

            # Draw item if it exists
            item = self.slots[i]

            # Renders item
            if item is not None:
                text_surface = self.font.render(item, True, (255, 255, 255))

                # Center text in slot.
                text_rect = text_surface.get_rect(center=rect.center)

                screen.blit(text_surface, text_rect)

        # Renders dragging item
        if self.dragging_item is not None:
            text_surface = self.font.render(self.dragging_item, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.mouse_pos)
            screen.blit(text_surface, text_rect)

    def get_slot_at_pos(self, pos):
        for i in range(len(self.slots)):
            col = i % self.cols
            row = i // self.cols

            x = self.start_x + col * (self.slot_size + self.padding)
            y = self.start_y + row * (self.slot_size + self.padding)

            rect = pygame.Rect(x, y, self.slot_size, self.slot_size)

            if rect.collidepoint(pos):
                return i
        # Safe exit
        return None

    def update(self):
        pass

    # Function used to enable/disable system.
    def toggle(self):
        self.active = not self.active

    # Function to easy check if system is active.
    def is_active(self):
        return self.active