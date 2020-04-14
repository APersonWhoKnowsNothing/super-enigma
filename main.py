###########################
# A Player of Audio Files # 
# Made With Pygame        #
###########################

# Imports
import pygame

# Set up
pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

# clock = pygame.time.Clock()

icon = pygame.image.load('icon.png')

pygame.display.set_caption("Music Player")
# pygame.display.set_icon(icon)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Meat
def program_exit():
    pygame.quit()
    quit()

def background():
    display.fill(white)



def run_program(): # Main display loop. The thing that renders other things.
    # Program Loop
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                print(event)
                program_exit()

    # Background
    background()

    # Updates Display
    pygame.display.update()
    #clock.tick(60)

# Run Program
if __name__ == "__main__":
    run_program()