import pygame
import random
import time

# initialize pygame
pygame.init()

# set window size and title
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")

# create mine grid
grid_size = (10,10)
grid = [[0 for x in range(grid_size[0])] for y in range(grid_size[1])]
mines = 10

# randomly place mines in grid
for i in range(mines):
    x = random.randint(0, grid_size[0]-1)
    y = random.randint(0, grid_size[1]-1)
    grid[x][y] = 1

# variables to track game state
game_over = False

# create revealed grid to track which cells have been clicked
revealed = [[False for x in range(grid_size[0])] for y in range(grid_size[1])]

# create flag grid to track which cells have been flagged
flagged = [[False for x in range(grid_size[0])] for y in range(grid_size[1])]

# font for displaying text
font = pygame.font.Font(None, 30)

def reveal_empty_cells(x, y):
    # check if cell is out of bounds or already revealed
    if (x < 0 or x >= grid_size[0] or y < 0 or y >= grid_size[1] or revealed[x][y]):
       return
    
    revealed[x][y] = True
    # check if cell has mines around
    mines_around = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (0 <= x+i < grid_size[0]) and (0 <= y+j < grid_size[1]) and grid[x+i][y+j] == 1:
                mines_around += 1
    if mines_around == 0:
        # reveal empty cells around current cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                reveal_empty_cells(x+i, y+j)

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # get x and y of mouse click
            pos = pygame.mouse.get_pos()
            x = pos[0] // 50
            y = pos[1] // 50
            if event.button == 1:
                # check if clicked on mine
                if grid[x][y] == 1:
                    game_over = True
                elif not flagged[x][y]:
                    reveal_empty_cells(x, y)
            elif event.button == 3:
                flagged[x][y] = not flagged[x][y]

    # draw grid and mines on screen
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if game_over and grid[x][y] == 1:
                pygame.draw.rect(screen, (255,0,0), (x*50, y*50, 50, 50))
            elif not game_over and revealed[x][y]:
                # check number of mines around cell
                mines_around = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (0 <= x+i < grid_size[0]) and (0 <= y+j < grid_size[1]) and grid[x+i][y+j] == 1:
                            mines_around += 1
                # display number of mines around cell or empty cell
                if mines_around > 0:
                    text = font.render(str(mines_around), 1, (0, 0, 0))
                    screen.blit(text, (x*50+20, y*50+20))
                else:
                    pygame.draw.rect(screen, (255,255,255), (x*50, y*50, 50, 50))
            else:
                # draw shaded square for unrevealed cells
                pygame.draw.rect(screen, (50,50,50), (x*50, y*50, 50, 50))
                pygame.draw.rect(screen, (200,200,200), (x*50+5, y*50+5, 40, 40))
                if flagged[x][y]:
                    pygame.draw.polygon(screen, (255, 0, 0), [(x*50+20, y*50+5), (x*50+5, y*50+25), (x*50+35, y*50+25)])
    if game_over:
        text = font.render("Game Over", 1, (255, 0, 0))
        screen.blit(text, (300, 450))
    else:
        #chequear que todos los none-mines esten revelados 
        non_mine_cells = grid_size[0] * grid_size[1] - mines
        cells_revealed = 0
        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                if revealed[x][y]:
                    cells_revealed += 1
        if cells_revealed == non_mine_cells:
            pygame.display.flip()
            pygame.draw.rect(screen, (255,255,255), (0, 0, 500, 500))
            text = font.render("You Win!", 2000, (0, 255, 0))
            screen.blit(text, (230, 250))
            pygame.display.flip()
            time.sleep(2)
            running = False
    pygame.display.flip()

# clean up and quit pygame
pygame.quit()