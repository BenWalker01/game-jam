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
NUM_ANTS = 5

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Jam")  # TODO : Change lol


# Clock for controlling frame rate
clock = pygame.time.Clock()


def main():
    running = True

    bob = Ant(player_controlled=True)
    ants = [bob]
    for i in range(NUM_ANTS):
        ants.append(Ant(following=ants[i]))

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
        # bob.draw(screen)
        # alice.look_at_lead()
        # if bob.distance_to(alice) > 30:
        #     alice.move_forward()
        # alice.draw(screen)

        bob.draw(screen)
        for ant in ants[1:]:
            ant.look_at_lead()
            print(ant.distance_to_lead())
            if ant.distance_to_lead() > 30:
                ant.move_forward()
            ant.draw(screen)
            # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
