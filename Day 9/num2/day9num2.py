import pygame
import random
# Инициализация Pygame
pygame.init()
win = int(input('Введите число до скольки оставшихся клеток будет продолжаться игра: '))
# Настройки игры
width, height = 400, 450
cell_size = 50
num_cells = width // cell_size
target_cells = 5
# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
won = False
# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Number Matching Game")

# Генерация случайных чисел для каждой клетки
numbers = [[random.randint(1, 9) for _ in range(num_cells)] for _ in range(num_cells)]


# Функция для отрисовки игровых элементов
def draw_game(selected_cells):
    screen.fill(white)

    font = pygame.font.Font(None, 24)
    moves_text = font.render(f"Moves: {moves}", True, black)
    screen.blit(moves_text, (10, height - 30))
    if won:
        font = pygame.font.Font(None, 48)
        win_text = font.render("You Win!", True, red)
        win_text_rect = win_text.get_rect(center=(width // 2, height // 2))
        screen.blit(win_text, win_text_rect)
        pygame.display.flip()
        return
    for row in range(num_cells):
        for col in range(num_cells):
            pygame.draw.rect(screen, black, (col * cell_size, row * cell_size, cell_size, cell_size), 1)
            number = numbers[row][col]
            if number != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(number), True, black)
                text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                screen.blit(text, text_rect)
            if (row, col) in selected_cells:
                pygame.draw.rect(screen, blue, (col * cell_size, row * cell_size, cell_size, cell_size), 3)
    pygame.display.flip()


# Основной цикл игры
running = True
selected_cells = set()
moves = 0
curr_cells = (sum(len(_) for _ in numbers))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // cell_size
            row = y // cell_size
            selected_cells.add((row, col))

            def is_adjacent(pos1, pos2):
                return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1
            def can_be_selected(cell1, cell2):
                return cell1 + cell2 == 10


            if len(selected_cells) == 2:
                cell1_row, cell1_col = selected_cells.pop()
                cell2_row, cell2_col = selected_cells.pop()
                selected_cells.clear()

                if is_adjacent((cell1_row, cell1_col), (cell2_row, cell2_col)):
                    if can_be_selected(numbers[cell1_row][cell1_col], numbers[cell2_row][cell2_col]):
                        numbers[cell1_row][cell1_col] = 0
                        numbers[cell2_row][cell2_col] = 0
                        moves += 1
                        curr_cells -= 2
                        print(curr_cells)
                        if win >= curr_cells: won = True


    # Отрисовка игры
    draw_game(selected_cells)

# Завершение Pygame
pygame.quit()
