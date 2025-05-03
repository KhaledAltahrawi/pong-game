import pygame
import sys
import random

# Initialize pygame
pygame.init()

# --- Game Setup ---
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game - Player vs Computer")

FPS = 60
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 12
BALL_WIDTH = 15
START_BALL_SPEED_X = 6
START_BALL_SPEED_Y = 6
MAX_BALL_SPEED = 25
WIN_SCORE = 10

# --- Intro Screen ---
def show_start_screen():
    waiting = True
    while waiting:
        WIN.fill(BLACK)
        title_text = large_font.render("PONG", True, WHITE)
        instruction_text = font.render("Press SPACE to Start", True, WHITE)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 60))
        WIN.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

# --- Game Loop Wrapper ---
def run_game():
    global ball_speed_x, ball_speed_y

    # Initialize paddles and ball
    left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_WIDTH // 2, HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)

    player_score = 0
    computer_score = 0

    ball_speed_x = START_BALL_SPEED_X
    ball_speed_y = START_BALL_SPEED_Y * random.choice([-1, 1])

    running = True
    paused = False

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused

        if paused:
            pause_text = font.render("PAUSED - Press 'P' to Resume", True, WHITE)
            WIN.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            continue

        # --- Player Input ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # --- AI Logic ---
        ai_speed = player_score * 0.2 + 3.8
        if abs(ball.centery - right_paddle.centery) > 10:
            if ball.centery < right_paddle.centery and right_paddle.top > 0:
                right_paddle.y -= ai_speed
            if ball.centery > right_paddle.centery and right_paddle.bottom < HEIGHT:
                right_paddle.y += ai_speed

        # --- Ball Movement ---
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Bounce off top/bottom
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Bounce off paddles
        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x *= -1.2
            ball_speed_x = max(min(ball_speed_x, MAX_BALL_SPEED), -MAX_BALL_SPEED)
        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x *= -1.2
            ball_speed_x = max(min(ball_speed_x, MAX_BALL_SPEED), -MAX_BALL_SPEED)

        # --- Scoring ---
        if ball.left <= 0:
            computer_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x = START_BALL_SPEED_X
            ball_speed_y = START_BALL_SPEED_Y * random.choice([-1, 1])
            pygame.time.delay(800)

        elif ball.right >= WIDTH:
            player_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x = START_BALL_SPEED_X * -1
            ball_speed_y = START_BALL_SPEED_Y * random.choice([-1, 1])
            pygame.time.delay(800)

        # --- Win Condition ---
        if player_score == WIN_SCORE or computer_score == WIN_SCORE:
            winner = "Player" if player_score == WIN_SCORE else "Computer"
            show_winner(winner, player_score, computer_score)
            return

        # --- Drawing ---
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, WHITE, left_paddle)
        pygame.draw.rect(WIN, WHITE, right_paddle)
        pygame.draw.ellipse(WIN, WHITE, ball)
        pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        player_text = font.render(f"Player: {player_score}", True, WHITE)
        computer_text = font.render(f"Computer: {computer_score}", True, WHITE)
        WIN.blit(player_text, (50, 20))
        WIN.blit(computer_text, (WIDTH - computer_text.get_width() - 50, 20))

        pygame.display.update()

# --- Show Winner and Ask Replay ---
def show_winner(winner, player_score, computer_score):
    while True:
        WIN.fill(BLACK)

        win_msg = f"{winner} Wins!"
        replay_msg = "Press Y to play again or N to quit."
        score_msg = f"Final Score - Player: {player_score}  Computer: {computer_score}"

        win_text = large_font.render(win_msg, True, WHITE)
        replay_text = font.render(replay_msg, True, WHITE)
        score_text = font.render(score_msg, True, WHITE)

        WIN.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - 100))
        WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 30))
        WIN.blit(replay_text, (WIDTH // 2 - replay_text.get_width() // 2, HEIGHT // 2 + 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    run_game()
                    return
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

# --- Start Everything ---
show_start_screen()
run_game()
