#########################
# https://www.youtube.com/watch?v=zfvxp7PgQ6c&list=PLxqNHKW7AOjj0_o83dgWSkdxX7wGRtN1E&index=16&t=2447s
#########################
import pygame
import random

## creating the data structure for pieces
## setting up global vars
## functions:
##   - create grid
##   - draw_grid
##   - draw_window
##   - rotating shape in main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
pygame.init()
pygame.font.init()

# GLOBAL VARS
s_width, s_height = 800, 700
play_width, play_height = 300, 600
rows, cols = 20, 10
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

grid_middle_x, grid_middle_y = (top_left_x + play_width//2, top_left_y + play_height //2)

## Define some color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# SHAPE FORMATS

S = [['.....',
     '......',
     '..00..',
     '.00...',
     '.....'],
    ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]
 
Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
 
I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]
 
O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]
 
J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]
 
L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]
 
T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y< 1:
            return True
    return False

def get_shape():
    return random.choice(shapes)

def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (grid_middle_x - (label.get_width()//2), grid_middle_y - label.get_height()//2-30))

def draw_grid(surface, rows, cols):
    sx = top_left_x
    sy = top_left_y
    for i in range(rows):
        pygame.draw.line(surface, GRAY, (sx, sy + i*block_size), (sx + play_width, sy + i*block_size))
    
    for j in range(cols):
        pygame.draw.line(surface, GRAY, (sx + j * block_size, sy), (sx + j * block_size, sy + play_height))


def clear_rows(grid, locked):
    pass

def draw_next_shape(next_shape, surface):
    pass

def draw_window(surface, score):

    surface.fill(BLACK)
    
    ### draw title
    title_font = pygame.font.SysFont("comicsans", 60)
    title_label = title_font.render("Tetris", 1, WHITE)   
    surface.blit(title_label, (grid_middle_x - (title_label.get_width() // 2), 30))

    ### draw Score board
    score_font = pygame.font.SysFont("comicsans", 40)
    score_label = score_font.render(f"Score: {score}", 1, WHITE)   
    surface.blit(score_label, (top_left_x + play_width + 50, top_left_y))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i* block_size, block_size, block_size), 0)

    draw_grid(surface, rows, cols)
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height), 3)

    

def main():
    global grid

    locked_positions = {}
    grid = create_grid(locked_positions)

    change_peice = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    score = 0
    fall_time = 0
    level_time = 0
    fall_speed = 0.8



    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_peice, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_peice.x += 1
                    if not valid_space(current_peice, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    # ROTATE SHAPE
                    current_piece.rotation = (current_peice.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_peice, grid):
                        current_peice.rotation = (current_piece.rotation - 1) % len(current_peice.shape)

                elif event.key == pygame.K_DOWN:
                    # go to botton
                    while valid_space(current_piece,grid):
                        current_piece.y += 1
                    current_peice.y -= 1

        ## Whenever a peice get locked (settled down)
        if change_piece:

            current_piece = next_piece
            next_piece = get_shape()

            ### check filled-up rows
            if clear_row(grid, lock_positions):
                score += 10

        draw_window(WIN, score)
        # draw_next_shape(next_piece, WIN)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    draw_text_middle("You Lost", 40, WHITE, WIN)
    pygame.display.update()
    pygame.time.delay(3000)


def main_menu():

    run = True
    while run:

        WIN.fill(BLACK)
        draw_text_middle("Press any key to begin", 60, WHITE, WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                main()
    
    pygame.quit()
    
WIN = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")

main_menu() ## start game