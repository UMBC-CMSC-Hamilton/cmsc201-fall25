"""
DFS = Depth First Search

If you're searching around in a maze, here's the strategy.
    Pick a direction, go that way, leave breadcrumbs until you get stuck.
        When you get stuck, pick up the breadcrumbs until another path you haven't gone down is available.
"""

from random import random, randint

# create the grid
# either it's empty or there's a wall, walls are going to be *'s.

WALL = '* '
SPACE = '__'
GOAL = 'G '

def create_grid(height, width, p = 0.33):
    the_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            if random() < p:
                new_char = WALL
            else:
                new_char = SPACE
            new_row.append(new_char)
        the_grid.append(new_row)

    y = randint(0, height - 1)
    x = randint(0, width - 1)

    the_grid[y][x] = GOAL  # the goal where we want to go.
    return the_grid



main_grid = create_grid(10, 10, 0.3)
for i in range(len(main_grid)):
    print(' '.join(main_grid[i]))

def print_grid(grid, y, x):
    for i in range(len(grid)):
        if i != y:
            print(' '.join(grid[i]))
        else:
            copy_line = list(grid[i])  # copy_line is a 1-d array which a copy of the ith grid line
            copy_line[x] = 'X'
            print(' '.join(copy_line))


"""
    Range checking, wall checking
"""

def manual_movement():
    # we're going to start at 0, 0 every time.
    next_move = input('>> ').lower().strip()

    cur_y = 0
    cur_x = 0

    while next_move != 'quit':
        if next_move == 'w':
            if cur_y >= 1 and main_grid[cur_y - 1][cur_x] != WALL:
                cur_y -= 1
        elif next_move == 'a':
            if cur_x >= 1 and main_grid[cur_y][cur_x - 1] != WALL:
                cur_x -= 1
        elif next_move == 's':
            if cur_y + 1 < len(main_grid) and main_grid[cur_y + 1][cur_x] != WALL:
                cur_y += 1
        elif next_move == 'd': # width of the list at cur_y
            if cur_x + 1 < len(main_grid[cur_y]) and main_grid[cur_y][cur_x + 1] != WALL:
                cur_x += 1

        print_grid(main_grid, cur_y, cur_x)
        next_move = input('>> ').lower().strip()


"""
    Are we able to get to the G or not?  
"""

def find_the_path(the_grid, y_pos, x_pos, visited, count=0):

    if the_grid[y_pos][x_pos] == GOAL:
        return True

    if (y_pos, x_pos) in visited:
        return False
    print(y_pos, x_pos)

    visited.append((y_pos, x_pos))

    found_up = found_left = found_down = found_right = False
    if y_pos >= 1 and the_grid[y_pos - 1][x_pos] != WALL:
        found_up = find_the_path(the_grid, y_pos - 1, x_pos, visited, count + 1)
        if found_up or True:
            the_grid[y_pos][x_pos] = str(count).zfill(2)
    if x_pos >= 1 and the_grid[y_pos][x_pos - 1] != WALL:
        found_left = find_the_path(the_grid, y_pos, x_pos - 1, visited, count + 1)
        if found_left or True:
            the_grid[y_pos][x_pos] = str(count).zfill(2)
    if y_pos + 1 < len(the_grid) and the_grid[y_pos + 1][x_pos] != WALL:
        found_down = find_the_path(the_grid, y_pos + 1, x_pos, visited, count + 1)
        if found_down or True:
            the_grid[y_pos][x_pos] = str(count).zfill(2)
    if x_pos + 1 < len(the_grid[y_pos]) and the_grid[y_pos][x_pos + 1] != WALL:
        found_right = find_the_path(the_grid, y_pos, x_pos + 1, visited, count + 1)
        if found_right or True:
            the_grid[y_pos][x_pos] = str(count).zfill(2)
    return found_up or found_down or found_left or found_right

print(find_the_path(main_grid, 0,0, []))
for i in range(len(main_grid)):
    print(' '.join(main_grid[i]))

# Breadth First Search - shortest path from the source to the destination
# Depth First Search - Gives you the first path it finds.
"""
00 03 04 *  __ __ *  37 FG 35
01 02 05 __ *  __ __ 36 35 34
*  07 06 __ *  *  __ __ __ 33
*  08 09 10 11 12 __ *  *  32
__ *  *  __ *  13 *  *  30 31
__ __ __ *  __ 14 *  __ 29 * 
__ __ *  __ *  15 __ *  28 * 
__ RG __ __ 17 16 *  __ 27 * 
__ *  __ *  18 21 22 *  26 __
__ __ *  __ 19 20 23 24 25 __
"""

"""
00 03 04 *  __ __ *  37 G  35
01 02 05 __ *  __ __ 36 35 34
*  07 06 __ *  *  __ __ __ 33
*  08 09 10 11 12 __ *  *  32
__ *  *  __ *  13 *  *  30 31
__ __ __ *  __ 14 *  __ 29 * 
__ __ *  __ *  15 __ *  28 * 
__ __ __ __ 17 16 *  __ 27 * 
__ *  __ *  18 21 22 *  26 __
__ __ *  __ 19 20 23 24 25 __

At 34
	Go Up, At 35 (top one)
		Go Up -> Off Board
		Go Left -> Goal = True
		Go Down -> Visited
		Go Right -> Off Board
		return True
	Go Left At (left 35)
		Up -> Find Goal- True
		Go Left
		At 36
			Go Up At 37
				Go Up-> Off Board
				Go Left-> Goal = True
				Go Down-> We do this but don't find anything
				Go Right -> Visited
		Go Down, = don't find the answer
		Go right = don't find the answer
"""