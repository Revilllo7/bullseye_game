import pygame
import sys
from buttons import Button
# References buttons for main menu


pygame.init()

res = (1280, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Menu")

# ADD BACKGROUND HERE AFTER YOU MAKE IT
background = pygame.image.load("assets/background.png")


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


# Menu for play game
def play():
    pygame.display.set_caption("Play Game")

    while True:
        play_mouse_position = pygame.mouse.get_pos()
        # illusion of changing the screen
        screen.fill("black")

        play_text = get_font(45).render("This is the PLAY screen.", True, "White")
        play_rect = play_text.get_rect(center=(500, 250))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(500, 450), text_input="BACK",
                           font=get_font(75), base_color="White", hover_color="Red")
        play_back.color_change(play_mouse_position)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.input(play_mouse_position):
                    main_menu()

        pygame.display.update()

        
# Menu for settings
# def options():
