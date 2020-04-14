###########################
# A Player of Audio Files # 
# Made With Pygame        #
###########################

# Imports
import pygame 

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set Up
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

# clock = pygame.time.Clock()

# Meat
def exit_program():
    pygame.quit()
    quit()

def image():
    display.fill(white)

def program_run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program()
            
        # Graphics
        image()

        pygame.display.update()

# Execute
program_run()

# Quit
pygame.quit()
quit()