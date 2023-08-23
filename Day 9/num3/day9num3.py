import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Параметры окна
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Avoid the Balls Game")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
player_color = (0, 255, 0)

# Класс для представления шариков
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y, color):
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Отражение от стен
        if self.x <= self.radius or self.x >= window_size[0] - self.radius:
            self.speed_x = -self.speed_x
        if self.y <= self.radius or self.y >= window_size[1] - self.radius:
            self.speed_y = -self.speed_y

# Создание шара игрока
player_ball = Ball(window_size[0] // 2, window_size[1] // 2, 20, 0, 0, player_color)

# Создание списка для шариков-противников
enemy_balls = []

# Время начала игры и количество шаров
start_time = time.time()
start_time2 = time.time()
ball_count = 0

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_ball.x -= 5
    if keys[pygame.K_RIGHT]:
        player_ball.x += 5
    if keys[pygame.K_UP]:
        player_ball.y -= 5
    if keys[pygame.K_DOWN]:
        player_ball.y += 5

    # Создание нового шарика-противника каждые 10 секунд
    current_time = time.time()
    if current_time - start_time2 >= 10:
        enemy_balls.append(Ball(random.randint(0, window_size[0]), random.randint(0, window_size[1]),
                                random.randint(10, 30), random.choice([-1, 1]) * random.randint(1, 3),
                                random.choice([-1, 1]) * random.randint(1, 3),
                                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        start_time2 = current_time
        ball_count += 1

    # Проверка столкновения игрока с шариками-противниками
    for ball in enemy_balls:
        distance = ((player_ball.x - ball.x) ** 2 + (player_ball.y - ball.y) ** 2) ** 0.5
        if distance <= player_ball.radius + ball.radius:
            running = False  # Проигрыш

    # Перемещение и отрисовка шариков
    window.fill(black)
    for ball in enemy_balls:
        ball.move()
        pygame.draw.circle(window, ball.color, (ball.x, ball.y), ball.radius)

    # Перемещение и отрисовка игрока
    pygame.draw.circle(window, player_ball.color, (player_ball.x, player_ball.y), player_ball.radius)

    # Вывод времени и количества шаров на экран
    font = pygame.font.Font(None, 36)
    time_text = font.render("Time: {:.0f}".format(time.time() - start_time), True, white)
    ball_text = font.render("Balls: {}".format(ball_count), True, white)
    window.blit(time_text, (10, 10))
    window.blit(ball_text, (10, 40))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты обновления экрана
    pygame.time.delay(30)

# Завершение Pygame
pygame.quit()
