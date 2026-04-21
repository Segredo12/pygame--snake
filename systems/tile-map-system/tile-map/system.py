import pygame

class TileMap:

    def __init__(self, map_data, tile_size, tile_set):
        # Converting map into numbers.
        self.map_data = [[int(tile) for tile in row] for row in map_data]
        self.tile_size = tile_size
        self.tile_set = tile_set

        # --Hardcoded-- (Adapt later)
        self.solid_tiles = {2}

    def is_solid(self, x, y):
        col = x // self.tile_size
        row = y // self.tile_size

        if 0 <= row < len(self.map_data) and 0 <= col < len(self.map_data[0]):
            return self.map_data[row][col] in self.solid_tiles

        return False

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        for row_index, row in enumerate(self.map_data):
            for col_index, tile in enumerate(row):

                x = col_index * self.tile_size
                y = row_index * self.tile_size

                tile_image = self.tile_set.get(tile)

                if tile_image:
                    screen.blit(tile_image, (x, y))