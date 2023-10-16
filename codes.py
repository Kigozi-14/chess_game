# these are my chess game codes
board = [['bc', 'bk', 'br', 'bm', 'bq', 'br', 'bk', 'bc'],
         ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
         ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
         ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
         ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
         ['nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl', 'nl'],
         ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
         ['wc', 'wk', 'wr', 'wm', 'wq', 'wr', 'wk', 'wc']]

occupied_positions = set()
board_positions = set()

# OCCUPIED POSITIONS
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] != 'nl':
            occupied_positions.add((i, j))

# BOARD POSITIONS
for i in range(len(board)):
    for j in range(len(board[i])):
        board_positions.add((i, j))

# KNIGHT MOVEMENT
def knight_movement(knight_position):
    res = []
    k_row, k_col = knight_position
    knight_go = [(k_row-2, k_col-1), (k_row-1, k_col-2), (k_row+1, k_col-2), (k_row+2, k_col-1), (k_row-2, k_col+1), (k_row-1, k_col+2), (k_row+1, k_col+2), (k_row+2, k_col+1)]
    for dr, dc in knight_go:
        if (dr, dc) in board_positions:
            res.append((dr, dc))
    return res
knight_position = (0,6)
# print(knight_movement(knight_position))

# CASTLE MOVEMENT
def castle_movement(castle_position):   
    c_row, c_col = castle_position
    castle_go = []
    for i in range(c_row, -1, -1):
        if (i, c_col) in occupied_positions:
            break
        else:
            castle_go.append((i, c_col))
    for i in range(c_row, 8):
        if (i, c_col) in occupied_positions:
            break
        else:
            castle_go.append((i, c_col))
    for i in range(c_col, -1, -1):
        if (c_row, i) in occupied_positions:
            break
        else:
            castle_go.append((c_row, i))
    for i in range(c_col, 8):
        if (c_row, i) in occupied_positions:
            break
        else:
            castle_go.append((c_row, i))
    return castle_go 
# print(castle_movement((4, 2)))

# BISHOP MOVEMENT
def bishop_movement(bishop_position):
    b_row, b_col = bishop_position
    bishop_go = set()
    k = b_col+1
    l = b_col-1
    m = b_row-1
    n = b_col-1
    # DOWN RIGHT MOVEMENT
    for i in range(b_row+1, 8):
        if (i, k) not in occupied_positions and (i, k) in board_positions:
            bishop_go.add((i, k))
            k += 1
        else:
            break
    # DOWN LEFT MOVEMENT
    for i in range(b_row+1, 8):
        if (i, l) not in occupied_positions and (i, l) in board_positions:
            bishop_go.add((i, l))
            l -= 1
        else:
            break
    # UPPER RIGHT MOVEMENT
    for i in range(b_col+1, 8):
        if (m, i) not in occupied_positions and (m, i) in board_positions:
            bishop_go.add((m, i))
            m -= 1
        else:
            break
    # UPPER LEFT MOVEMENT
    for i in range(b_row-1, -1, -1):
        if (i, n) not in occupied_positions and (i, n) in board_positions:
            bishop_go.add((i, n))
            n -= 1
        else:
            break
    return bishop_go
# print(bishop_movement((4, 1)))

def queen_movement(queen_position):
    queen_row, queen_col = queen_position
    queen_go = set()
    a = castle_movement((queen_row, queen_col))
    b = bishop_movement((queen_row, queen_col))
    return a, b
# print(queen_movement((3, 4)))

def king_movement(king_position):
    pass
