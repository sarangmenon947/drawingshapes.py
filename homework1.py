import pygame
import sys

# Initializing Pygame
pygame.init()

# Setting Pygame
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw Lines and Rectangles")

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Filling The Background Of The Screen
    screen.fill((0, 0, 0))

    # Drawing A Red Line
    pygame.draw.line(screen, (255, 0, 0), (50, 50), (200, 50), 5)

    # Drawing A Green Filled Rectangle
    pygame.draw.rect(screen, (0, 255, 0), (300, 100, 150, 75))

    # Drawing A Blue Rectangle
    pygame.draw.rect(screen, (0, 0, 255), (500, 100, 150, 75), 5)

    # Updating The Display
    pygame.display.flip()

# Quitting Pygame
pygame.quit()
sys.exit()