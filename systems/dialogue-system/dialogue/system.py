import pygame

class DialogueSystem:
    # Constructor
    def __init__(self, font, box_rect):
        self.font = font
        self.box_rect = box_rect

        self.dialogue:list[str] = []
        self.current_index:int = 0
        self.active:bool = False

    # Function used to start dialogue
    def start(self, dialogue_lines:list[str]):
        self.dialogue = dialogue_lines
        self.current_index = 0
        self.active = True

    # Function used to handle skip dialogue
    def handle_event(self, event, key_pressed):
        # If dialogue is deactivate does nothing.
        if not self.active:
            return

        # if event key was pressed handles the event.
        if event.type == pygame.KEYDOWN:
            if event.key == key_pressed:
                self.current_index += 1

                if self.current_index >= len(self.dialogue):
                    self.active = False

    # Function used to draw chat box.
    def draw(self, screen):
        # if dialogue is deactivate does nothing.
        if not self.active:
            return

        # Draw Box
        pygame.draw.rect(screen, (0, 0, 0), self.box_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.box_rect, 2)

        # Draw Text
        text = self.dialogue[self.current_index]
        text_surface = self.font.render(text, True, (255, 255, 255))

        screen.blit(text_surface, (self.box_rect.x + 10, self.box_rect.y + 10))

    # Easy access to know if dialogue is being used.
    def is_active(self):
        return self.active