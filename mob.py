import random
import pygame
import math


class Mob:
    def __init__(self, name, center, radius, speed):
        self.name = name
        self.center = center  # (x_center, y_center)
        self.radius = radius
        self.speed = speed
        self.x = center[0]
        self.y = center[1]
        self.heading = 0
        self.target = None
        self.path = (random.uniform(self.center[0] - self.radius, self.center[0] + self.radius),
                     random.uniform(self.center[1] - self.radius, self.center[1] + self.radius))

    def move_randomly(self):
        if not self.target:
            px, py = self.path
            dx, dy = px - self.x, py - self.y
            distance = (dx**2 + dy**2)**0.5

            if distance < 5:  # If close to the current path target, pick a new one
                self.path = (
                    random.uniform(
                        self.center[0] - self.radius, self.center[0] + self.radius),
                    random.uniform(
                        self.center[1] - self.radius, self.center[1] + self.radius)
                )
            else:
                # Move towards the current path target
                dx, dy = dx / distance * self.speed, dy / distance * self.speed
                self.x += dx
                self.y += dy

    def move_towards_target(self):
        if self.target:
            tx, ty = self.target
            x, y = self.position
            dx, dy = tx - x, ty - y
            distance = (dx**2 + dy**2)**0.5
            if distance > self.speed:
                dx, dy = dx / distance * self.speed, dy / distance * self.speed
            new_x, new_y = x + dx, y + dy
            distance_from_center = (
                (new_x - self.center[0])**2 + (new_y - self.center[1])**2)**0.5
            if distance_from_center <= self.radius:
                self.position = (new_x, new_y)

    def update(self, ant_position=None):
        if ant_position:
            self.target = ant_position
            self.move_towards_target()
        else:
            self.target = None
            self.move_randomly()

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(
            self.x), int(self.y)), 5)

    def debug(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(
            self.center[0]), int(self.center[1])), self.radius, 1)
