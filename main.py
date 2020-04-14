###########################
# A Player of Audio Files # 
# Made With Pygame        #
###########################

# Imports
import pygame
import time
from pathlib import Path
import os

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
def button(msg, x, y, w, h, ic, ac):
    mouse = pygame.mouse.get_pos()
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
    else:
        pygame.draw.rect(display, ic, (x, y, w, h))

    text_display(msg, 15)

def audio_folder():
    path = "Audio_Files"
    isdir = os.path.isdir(path)
    if isdir == True:
        return True
        # audio_files = True
    elif isdir == False:
        print("`Audio_Files` Directory Does Not Exist")
        print("Creating New Directory")
        os.mkdir("Audio_Files")
        print("Directory Created Successfully")
        # audio_files = True
    else:
        print("fuck")

def program_exit():
    pygame.quit()
    quit()

def background():
    display.fill(black)

    pygame.draw.line(display, white, (1,75), (800, 75), 5)

def text_object(msg, font, color):
    text_surface = font.render(msg, True, color)
    return text_surface, text_surface.get_rect()

def text_display(msg, font_size):
    text = pygame.font.Font('freesansbold.ttf', font_size)
    text_surf, text_rect = text_object(msg, text, white)
    text_rect.center = ((display_width / 2), (35))
    display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(1)
    program_run()

def program_run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                program_exit()
        
        audio_folder()

        #button('test', 155, 155, 100, 50, red, green)

        # GUI
        background()
        text_display("Audio Files", 60) # Main Header

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