import pygame


class Item:

    # Constructor
    def __init__(self, identifier, name, image_path):
        # Base variables
        self.identifier = identifier
        self.name = name
        self.image_path: image_path

        # Image loader.
        self. image = None
        if image_path:
            try:
                self.image = pygame.image.load(str(image_path)).convert_alpha()
            except:
                self.image = None