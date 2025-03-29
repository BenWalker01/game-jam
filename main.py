import pygame
import random
import sys
from ant import Ant
# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CIRCLE_COLOR = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Jam")  # TODO : Change lol


# Clock for controlling frame rate
clock = pygame.time.Clock()


def main():
    running = True

    bob = Ant()
    alice = Ant(500, 400)
    bob.next_ant = alice

    while running:
        # Clear screen
        screen.fill(BLACK)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #     bob.move_left()
        # if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #     bob.move_right()
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     bob.move_up()
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     bob.move_down()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            bob.move_forward()

        if keys[pygame.K_q]:
            bob.turn_left()
        if keys[pygame.K_e]:
            bob.turn_right()

        # Draw the Ant
        bob.draw(screen)
        alice.draw(screen)
        if bob.distance_to(alice) > 30:
            alice.move_forward()
        # Create and draw other ants that follow Bob
        num_ants = 5

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
