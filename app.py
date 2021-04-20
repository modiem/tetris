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
top_left_y = s_height - play_height - 20

grid_middle_x, grid_middle_y = (top_left_x + play_width//2, top_left_y + play_height //2)

## Define some color
WHITE = (255, 243, 176) # Medium Champagne
BLACK = (51, 92, 103) # Deep Space Sparkle
GRAY = (27, 58, 75) # Charcoal
RED = (11, 82, 91) # Midnight Green Eagle Green
YELLOW = (224, 159, 62) # Indian Yellow


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
shape_colors = [(219, 180, 44), # Gold Metallic
                (142, 202, 230), # Light Cornflower Blue
                (255, 238, 50), # Yellow 
                (255, 239, 211),  # Papaya Whip
                (188, 138, 95),  # Antique Brass
                (144, 190, 109),  # olive
                (239, 189, 235)] # Pink Lavender

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape # list of rotatted tetriminoes
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

    def get_positions(self):
        '''
        Reutrn a list of coordinates of the tetrimino blocks.
        Each coordinate should be assign a color.
        '''
        positions = []

        ## get tetrimino
        # tetrimino =  ['.....',
                    #   '.0...',
                    #   '.000.',
                    #   '.....',
                    #   '.....']
        tetrimino = self.shape[self.rotation]

        for i, line in enumerate(tetrimino):
            line = list(line)
            for j, col in enumerate(line):
                if col == "0":
                    positions.append((self.x + j, self.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] -2, pos[1]-4)

        return positions

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]
    return grid


def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(len(grid[i])) if grid[i][j] == BLACK] for i in range(len(grid))]
    ## flatten accepted_positions:
    accepted_positions = [_ for sub in accepted_positions for _ in sub]


    positions = shape.get_positions()
    for pos in positions:
        if pos not in accepted_positions and pos[1] >= 0:
            return False

    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y< 1:
            return True
    return False

def get_shape():
    random_shape = random.choice(shapes)
    return Piece(5, 0, random_shape)

def draw_text_middle(text, size, color, surface):
    # pygame.draw.rect(surface, BLACK, (0, grid_middle_x - 80, s_width, 120), 0)
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (grid_middle_x - (label.get_width()//2), grid_middle_y - 50))

def draw_grid(surface, rows, cols):
    sx = top_left_x
    sy = top_left_y
    for i in range(rows):
        pygame.draw.line(surface, RED, (sx, sy + i*block_size), (sx + play_width, sy + i*block_size), 1)
    
    for j in range(cols):
        pygame.draw.line(surface, RED, (sx + j * block_size, sy), (sx + j * block_size, sy + play_height), 1)


def clear_rows(grid, locked_positions):
    cleared_rows = 0
    i = len(grid)
    while i > 0:
        i -= 1
        row = grid[i]
        if BLACK not in row:
            ## add positions to remove from locked_positions
            for j in range(len(row)):
                try:
                    del locked_positions[(j, i)]
                except:
                    continue
            cleared_rows += 1

            for key in sorted(list(locked_positions), key = lambda x: x[1])[::-1]:
                (x, y) = key
                if y < i:
                    newKey = (x, y + 1)
                    locked_positions[newKey] = locked_positions.pop(key) 

            grid = create_grid(locked_positions)
            i += 1

    return grid, cleared_rows
            

def draw_next_piece(next_piece, surface):

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2

    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape: ", 1, WHITE)
    surface.blit(label, (sx, sy - label.get_height() - 10))

    for i, row in enumerate(next_piece.shape[next_piece.rotation]):
        row = list(row)
        for j, col in enumerate(row):
            if col == "0":
                pygame.draw.rect(surface, next_piece.color, (sx + j * block_size, sy + i * block_size, block_size, block_size), 0)



def draw_window(surface, stats, next_piece):
    '''
    draw whole window:
        - background
        - grid, border, separation
        - score board
        - tetrominoes
    '''

    surface.fill(BLACK)
    
    ### draw title
    title_font = pygame.font.SysFont("comicsans", 60)
    title_label = title_font.render("Tetris", 1, WHITE)   
    surface.blit(title_label, (grid_middle_x - (title_label.get_width() // 2), 30))
    
    ### draw Score board and other statistics
    sx = top_left_x + play_width + 50
    sy = top_left_y

    stats_font = pygame.font.SysFont("comicsans", 40)
    score_label = stats_font.render(f"Score: {stats['score']}", 1, WHITE)   
    surface.blit(score_label, (sx, sy))
    line_height = score_label.get_height()

    level_label = stats_font.render(f"level: {stats['level']}", 1, WHITE)
    surface.blit(level_label, (sx, sy + line_height + 10))

    lines_label = stats_font.render(f"lines: {stats['lines']}", 1, WHITE)
    surface.blit(lines_label, (sx, sy + (line_height + 10) * 2))


    ### draw next tetriminoes
    draw_next_piece(next_piece, WIN)


    ### draw tetriminoes
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i* block_size, block_size, block_size), 0)

    # draw grid and border
    draw_grid(surface, rows, cols)
    pygame.draw.rect(surface, RED, (top_left_x, top_left_y, play_width, play_height), 4)


    

def main():
    global grid

    locked_positions = {}
    stats = {
        "level": 1,
        "score": 0,
        "lines": 0,
    }

    run = True
    change_piece = False
    current_piece = get_shape()
    next_piece = get_shape()

    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    fall_speed = 0.5
    level = 0



    while run:

        ## set the timer
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 4:
            level_time = 0      
            if fall_speed > 0.15:
                fall_speed -= 0.005
                level += 1
                if level >= 10:
                    stats["level"] += 1
                    level = 0
                


        # Piece Falling Code
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True


        # control tetrominoe through keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    # ROTATE SHAPE
                    current_piece.rotation = (current_piece.rotation + 1) % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = (current_piece.rotation - 1) % len(current_piece.shape)

                elif event.key == pygame.K_DOWN:
                    # go to botton
                    while valid_space(current_piece,grid):
                        current_piece.y += 1
                    current_piece.y -= 1
                    change_piece = True


        ## Add piece to the grid for drawing
        shape_pos = current_piece.get_positions()
        for i in range(len(shape_pos)):
            (x, y) = shape_pos[i]
            if y >= 0:
                grid[y][x] = current_piece.color


        ## Whenever a piece get locked (settled down)
        if change_piece:
            for pos in shape_pos:
                locked_positions[pos] = current_piece.color

            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            stats["score"] += 5
            fall_time = 0

            ## check complete rows
            grid, num = clear_rows(grid, locked_positions)
            stats["lines"] += num

        draw_window(WIN, stats, next_piece)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    draw_text_middle("Game Over!!", 40, WHITE, WIN)
    pygame.display.update()
    pygame.time.delay(5000)

    ## press space bar to start a new game

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