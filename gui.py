# --- SUDOKU-SOLVER GUI ---
import pygame
from solver import board, solve

pygame.init()

# Define constants
SCREEN_WIDTH = 540
SCREEN_HEIGHT = 540
CELL_SIZE = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")

font = pygame.font.Font(None, 40)

def render_board(screen, board):
    screen.fill(WHITE)

    # Draw grid
    for i in range(10):
        line_color = BLACK if i % 3 == 0 else GRAY
        pygame.draw.line(screen, line_color, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), 2)
        pygame.draw.line(screen, line_color, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT), 2)

    # Adds values to board
    for row in range(len(board)):
        for col in range(len(board[row])):
            value = board[row][col]
            if value != 0:
                number = font.render(str(value), True, BLACK)
                x = (col * CELL_SIZE) + (CELL_SIZE // 2)
                y = (row * CELL_SIZE) + (CELL_SIZE // 2)
                screen.blit(number, (x-number.get_width() // 2, y-number.get_height() // 2))

    pygame.display.update()

run = True
solved = True 

while run:

    render_board(screen, board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                solve(board)

pygame.quit()