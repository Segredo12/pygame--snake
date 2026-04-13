import pygame

class Player:

    def __init__(self, x, y, speed, sprite_frames):
        self.x = x
        self.y = y
        self.speed = speed

        # Animation frames (list of images)
        self.frames = sprite_frames
        self.current_frame = 0
        self.animation_timer = 0
        self.animation_speed = 10  # Lower equals Faster animation
        self.state = "IDLE"

        # Movement state
        self.direction = pygame.Vector2(0, 0)

    def update(self):
        # Read what key is pressed.
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        self.direction.y = 0

        # Movement (WASD)
        if keys[pygame.K_w]:
            self.direction.y = -1
        if keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_d]:
            self.direction.x = 1

        # Normalize diagonal movement
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        # Apply movement
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed

        previous_state = self.state

        # Animation Update
        if self.direction.length() > 0:
            self.state = "WALK"
        else:
            self.state = "IDLE"

        # Reset animation if state changed
        if self.state != previous_state:
            self.current_frame = 0
            self.animation_timer = 0

        # Animation update
        animation = self.frames[self.state]

        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(animation)

    def handle_event(self):
        pass  # we will use key state instead

    def draw(self, screen):
        animation = self.frames[self.state]
        frame = animation[self.current_frame]
        rect = frame.get_rect(center=(self.x, self.y))
        screen.blit(frame, rect)