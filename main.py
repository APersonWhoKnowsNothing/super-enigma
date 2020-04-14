###########################
# A Player of Audio Files # 
# Made With Pygame        #
###########################

# Imports
import pygame
import time

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set Up
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

pygame.display.set_caption("Audio Player")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Meat
def program_exit():
    pygame.quit()
    quit()

def background():
    display.fill(black)

    pygame.draw.line(display, white, (1,75), (800, 75), 5)

def text_object(msg, font, color):
    text_surface = font.render(msg, True, color)
    return text_surface, text_surface.get_rect()

def text_display(msg):
    text = pygame.font.Font('freesansbold.ttf', 60)
    text_surf, text_rect = text_object(msg, text, white)
    text_rect.center = ((display_width / 2), (35))
    display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)
    program_run()

def program_run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                program_exit()
            
        # GUI
        background()
        text_display("Audio Files") # Main Header

        # Update Display
        pygame.display.update()
        clock.tick(60)

# Execute
if __name__ == "__main__":
    print("Program Start")
    print("-------------")
    program_run()
else:
    print("Program Terminated Due to an Error")
    print("-------------")
    program_exit()