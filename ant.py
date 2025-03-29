import pygame
import math


class Ant:
    def __init__(self, x=400, y=400, player_controlled=False):
        """Initialize the ant's position."""
        self.x = x
        self.y = y
        self.heading = 0
        self.speed = 1
        self.next_ant: Ant = None
        self.player_controlled = player_controlled

    def move_forward(self):
        """Move the ant forward based on its heading."""
        radians = math.radians(-self.heading)
        self.x += self.speed * math.cos(radians)
        self.y -= self.speed * math.sin(radians)

    def turn_left(self):
        """Turn left"""
        self.heading -= 5

    def turn_right(self):
        """Turn Right"""
        self.heading += 5

    def get_position(self):
        """Return the current position of the ant."""
        return self.x, self.y

    def draw(self, screen):
        """Draw the ant's current position using pygame."""
        ant_color = (255, 0, 0)  # Red color for the ant
        rotated_surface = pygame.Surface((20, 10), pygame.SRCALPHA)
        pygame.draw.ellipse(rotated_surface, ant_color, (0, 0, 20, 10))
        rotated_surface = pygame.transform.rotate(
            rotated_surface, -self.heading)
        rect = rotated_surface.get_rect(center=(self.x, self.y))
        screen.blit(rotated_surface, rect.topleft)

        # Draw a line facing forward
        forward_length = 20
        radians = math.radians(-self.heading)
        end_x = self.x + forward_length * math.cos(radians)
        end_y = self.y - forward_length * math.sin(radians)
        pygame.draw.line(screen, (0, 255, 0),
                         (self.x, self.y), (end_x, end_y), 2)

        self.update_follower()

    def update_follower(self):
        """Update the position of the next ant in the sequence"""
        if self.next_ant:
            dx = self.next_ant.x - self.x
            dy = self.next_ant.y - self.y
            angle_to_next = math.degrees(math.atan2(-dy, dx))
            self.next_ant.heading = 180 - angle_to_next

    def distance_to(self, ant2):
        """Calculate the distance between two ants."""
        return math.sqrt((ant2.x - self.x) ** 2 + (ant2.y - self.y) ** 2)
