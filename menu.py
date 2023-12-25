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


# REMEMBER TO CHANGE FONT LATER
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
        play_rect = play_text.get_rect(center=(640, 250))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(640, 450), text_input="BACK",
                           font=get_font(75), base_color="White", hover_color="Red")
        play_back.color_change(play_mouse_position)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.input(play_mouse_position):
                    pygame.display.set_caption("Menu")
                    main_menu()

        pygame.display.update()


# Menu for settings
def settings():
    pygame.display.set_caption("settings")

    while True:
        settings_mouse_position = pygame.mouse.get_pos()
        # illusion of changing the screen
        screen.fill("black")

        settings_text = get_font(45).render("this is the SETTINGS screen.", True, "White")
        settings_rect = settings_text.get_rect(center=(640, 250))
        screen.blit(settings_text, settings_rect)

        settings_back = Button(image=None, pos=(640, 450), text_input="BACK", font=get_font(75), base_color="White",
                               hover_color="Red")
        settings_back.color_change(settings_mouse_position)
        settings_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_back.input(settings_mouse_position):
                    pygame.display.set_caption("Menu")
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(background, (0, 0))
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("", True, "Red")
        # leftover code. Kept in case I go back or graphics fail and I add indexing
        menu_rect = menu_text.get_rect(center=(640, 150))
        play_button = Button(image=pygame.image.load("assets/Button_border.png"), pos=(640, 270), text_input="PLAY",
                             font=get_font(45), base_color="White", hover_color="#F51B14")
        settings_button = Button(image=pygame.image.load("assets/Button_border.png"), pos=(640, 400),
                                 text_input="SETTINGS",
                                 font=get_font(45), base_color="White", hover_color="#F51B14")
        quit_button = Button(image=pygame.image.load("assets/Button_border.png"), pos=(640, 540), text_input="QUIT",
                             font=get_font(45), base_color="White", hover_color="#F51B14")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, settings_button, quit_button]:
            button.color_change(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.input(menu_mouse_pos):
                    play()
                if settings_button.input(menu_mouse_pos):
                    settings()
                if quit_button.input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
