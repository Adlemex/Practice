import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров экрана
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, ножницы, бумага")

# Загрузка изображений
rock_image = pygame.image.load("rock.png")
paper_image = pygame.image.load("paper.png")
scissors_image = pygame.image.load("scissors.png")

# Определение начальных координат кнопок
button_y = 300
rock_x = 100
paper_x = 250
scissors_x = 400

# Определение размеров кнопок
button_width = 100
button_height = 100

# Определение счетчиков
player_score = 0
comp_score = 0
games_played = 0

# Определение шрифта
font = pygame.font.Font(None, 36)


def determine_winner(player_choice, comp_choice) -> str:
    if player_choice == comp_choice:
        return "ничья"
    elif (player_choice == "камень" and comp_choice == "ножницы") or \
            (player_choice == "бумага" and comp_choice == "камень") or \
            (player_choice == "ножницы" and comp_choice == "бумага"):
        return "игрок"
    else:
        return "компьютер"


def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))


# Основной игровой цикл
running = True
clock = pygame.time.Clock()
result = ""

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if button_y < mouse_y < button_y + button_width:
                if rock_x < mouse_x < rock_x + button_height:
                    player_choice = "камень"
                elif paper_x < mouse_x < paper_x + button_height:
                    player_choice = "бумага"
                elif scissors_x < mouse_x < scissors_x + button_height:
                    player_choice = "ножницы"

                if player_choice:
                    choices = ["камень", "бумага", "ножницы"]
                    comp_choice = random.choice(choices)

                    result = determine_winner(player_choice, comp_choice)
                    games_played += 1

                    if result == "игрок":
                        player_score += 1
                    elif result == "компьютер":
                        comp_score += 1

    # Отрисовка
    screen.fill(WHITE)
    screen.blit(rock_image, (rock_x, button_y))
    screen.blit(paper_image, (paper_x, button_y))
    screen.blit(scissors_image, (scissors_x, button_y))

    display_text(f"Игрок: {player_score}", 20, 20)
    display_text(f"Компьютер: {comp_score}", 20, 60)
    display_text(f"Ничья: {games_played}", 20, 100)

    if "player_choice" in locals():
        display_text(f"Ваш выбор: {player_choice}", 300, 20)
        display_text(f"Выбор компьютера: {comp_choice}", 300, 60)
        display_text(f"Результат: {result.capitalize()}", 300, 100)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
