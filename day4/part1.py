def sum_all_unpicked_numbers(board):
    unpicked_sum = 0
    for row in board:
        for item in row:
            if item['picked'] == False:
                unpicked_sum = unpicked_sum + item['num']
    
    return unpicked_sum

def mark_boards(boards, drawnum):
    for board in boards:
        for row in board:
            for item in row:
                if item['num'] == drawnum:
                    item['picked'] = True

def check_rows(board):
    for row in board:
            picked_items = [item['num'] for item in row if item['picked']]
            if len(picked_items) == len(row):
                return True
    return False

def check_bingo(boards):
    for board in boards:
        transposed_board = []
        transposed_board = transpose(board, transposed_board)
        if check_rows(board) or check_rows(transposed_board):
            return board
    return []   
        
def transpose(list1, list2):
    list2 =[[row[i] for row in list1] for i in range(len(list1[0]))]
    return list2

input_data = open("./bingo_input.txt").read().splitlines()

drawnumbers = []

drawnumbers = input_data[0].split(',')

input_line_num = 1

boards = []
total_boards = -1

while input_line_num < len(input_data):
    if input_data[input_line_num] == '':
        boards.append([])
        total_boards = total_boards + 1
    else:
        row_input = input_data[input_line_num].lstrip().replace('  ', ' ').split(' ')
        row = [{'num': int(item), 'picked': False} for item in row_input]
        boards[total_boards].append(row)
    input_line_num = input_line_num + 1

current_board_index = 0
final_score = 0

for num in drawnumbers:
    mark_boards(boards, int(num))
    winning_board = check_bingo(boards)
    if len(winning_board) > 0:
        final_score = sum_all_unpicked_numbers(winning_board) * int(num)
        break

print(final_score)