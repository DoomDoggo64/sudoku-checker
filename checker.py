
def range_in_list(range_obj, lst):
    return all(item in lst for item in range_obj)
    rows = input()


def sudoku(rowss):
    rows = rowss
    rows = list(rows)
    board = []
    for i in range(9):
        pos1 = 1 * i
        pos2 = pos1 + 9
        board.insert(-1, rows[pos1:pos2])
        my_range = range(1, 10)
        for row in board:
            for i in range(0, 9):
                row[i] = int(row[i])
            for row in board:
                if range_in_list(my_range, row) == False:
                    return False


if sudoku(rows):
    print 'yes'
else:
    print 'no'
