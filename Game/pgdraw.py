import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 810, 810
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('White Rectangle with Black Outline')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Rectangle properties
rect_width, rect_height = 270, 270
rect_x, rect_y = 270,0
outline_thickness = 3

# Main loop
running = True
while running:
    screen.fill(white)  # Fill the screen with white color

    # Draw the outline (black border)
    pygame.draw.rect(screen, black, (rect_x - outline_thickness, rect_y - outline_thickness,
                                     rect_width + outline_thickness * 2, rect_height + outline_thickness * 2))

    # Draw the white rectangle
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame properly
pygame.quit()
sys.exit()