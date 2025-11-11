"""

    What is a two dimensional (or higher dimensional list)?

        In python there are lists within lists.

"""

my_list = [
    [1, 2, 3],
    [2, 3, 4, 5, 5, 6, 7],
    [4, 5],
    [],
    [1, 2, 3, 4, 5, 6]
]

print(my_list)

"""
If you wanted to print each number individually how would you do it?
    You need to use a first index to get into the list and choose a sublist
"""

for i in range(len(my_list)):
    print(i, my_list[i])

"""
How do I access a specific element within that list?
"""
for i in range(len(my_list)):
    # if you accidentally or somewhat intentionally use the inner index with len(my_list)
    # we want the length of the current sublist, not the total list.
    for j in range(len(my_list[i])):
        print(my_list[i][j])


GAP = '  '

def display_board(the_board):
    for i in range(len(the_board)):
        print(GAP.join(the_board[i]))
"""
  01234567
0 X_X_X_X_
1 _X_X_X_X
2 X_X_X_X_
3 _X_X_X_X


We can move onto the lines but not the dots
"""

SPACE = '__'
UNMOVABLE = '..'
RED_PIECE = 'RR'
BLACK_PIECE = 'BB'

def populate_board(the_board):
    # 3 == number of rows of pieces we will get
    for i in range(3):
        for j in range(len(the_board[i])):
            if the_board[i][j] == SPACE:
                the_board[i][j] = BLACK_PIECE

    for i in range(len(the_board) - 3, len(the_board)):
        for j in range(len(the_board[i])):
            if the_board[i][j] == SPACE:
                the_board[i][j] = RED_PIECE


checkerboard_size = 8
the_board = []
for i in range(checkerboard_size):
    new_row = []
    for j in range(checkerboard_size):
        if (i + j) % 2 == 0:
            new_row.append(SPACE)
        else:
            new_row.append(UNMOVABLE)
    the_board.append(new_row)

print(the_board)
display_board(the_board)
populate_board(the_board)
print('New Board:')
display_board(the_board)


def move_piece(the_board, start_x, start_y, offset_x, offset_y):
    """
        It moves the piece if it can but if not it will return False

    :param the_board:
    :param start_x:
    :param start_y:
    :param offset_x:
    :param offset_y:
    :return:
    """
    # want to check that we start at a position where there's a piece
    if the_board[start_x][start_y] not in [RED_PIECE, BLACK_PIECE]:
        return False
    # we want to make sure that we're moving diagonally AND we're only jumping one or two places
    if abs(offset_x) not in [1, 2] or abs(offset_x) != abs(offset_y):
        return False
    # can't move off the board
    if not(0 <= start_x + offset_x < len(the_board)) or not(0 <= start_y + offset_y < len(the_board[start_x + offset_x])):
        return False
    # collisions are not allowed in checkers.
    if the_board[start_x + offset_x][start_y + offset_y] != SPACE:
        return False

    the_board[start_x + offset_x][start_y + offset_y] = the_board[start_x][start_y]
    the_board[start_x][start_y] = SPACE
    return True

move_piece(the_board, 2, 2, 1, 1)
print()
display_board(the_board)


"""
    
"""

crazy_list = [
    ['a', 'b', 'c', 'd'],
    ['t', 's', 'u', 'e', 'v'],
    ['q', 'r', 's', 'p', 'z']
]

# the index variable inside a for each loop IF the underlying data type is mutable, you can modify the list, dictionary, or class
# this works the same way as pass by references vs pass by value
# works by using a reference for the list rather than a copy.
# copy when immutable
# reference when mutable
for sublist in crazy_list:
    sublist.append('f')
    sublist = [1, 2, 3, 4]
    print(sublist)

print(crazy_list)


"""
Why stop at 2d?
    No reason, it's just the most common higher dimensional list
"""
three_dee_list = [
    [[1, 2, 3], [2, 3, 4], [3, 4, 5]],  # 0
    [[5, 6, 7], [8, 9, 1], [2, 3, 6]],  # 1
    [[5, 5, 5], [9, 9, 9], [2, 2, 2]],  # 2
]

print(three_dee_list[1][0][1])
print(three_dee_list[2][2][1])
print(three_dee_list[0][2][1])

three_dim_map = {
    'eric8': {
        'Name': 'Eric',
        'Grades': {
            'Exam 1': 97,
            'HW2': 24,
            'HW1': 17,
            'HW3': 25
        }
    },
    'robert7': {},
    'jill9': {}
}


# 1st level -> usernames => Name or grades => if grades, it's assignment name

print(three_dim_map['eric8']['Grades']['HW3'])

