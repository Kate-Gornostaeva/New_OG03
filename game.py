import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Собери 100!')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.Font(None, 36)

# Переменные игры
score = 0
target_score = 100
items = []
item_lifetime = 2000  # Время жизни предмета в миллисекундах
spawn_time = 1000  # Время между появлением предметов

# Таймеры
last_spawn_time = pygame.time.get_ticks()


# Функции
def spawn_item():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    number = random.randint(1, 20)
    items.append({'rect': pygame.Rect(x, y, 50, 50), 'number': number, 'spawn_time': pygame.time.get_ticks()})


def draw_items():
    for item in items:
        pygame.draw.rect(screen, RED, item['rect'])
        text = font.render(str(item['number']), True, WHITE)
        screen.blit(text, (item['rect'].x + 10, item['rect'].y + 10))


def check_item_click(pos):
    global score
    for item in items[:]:
        if item['rect'].collidepoint(pos):
            score += item['number']
            items.remove(item)


def update_items():
    current_time = pygame.time.get_ticks()
    for item in items[:]:
        if current_time - item['spawn_time'] > item_lifetime:
            items.remove(item)


# Основной цикл игры
running = True
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            check_item_click(event.pos)

    # Спавн новых предметов
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > spawn_time:
        spawn_item()
        last_spawn_time = current_time

    # Обновление и отрисовка предметов
    update_items()
    draw_items()

    # Отрисовка счета
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Проверка на выигрыш
    if score == target_score:
        win_text = font.render('Вы выиграли!', True, WHITE)
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()