import numpy as np

def pickup(board, basket, move, count):
    for idx, num in enumerate(board[move-1]):
        if num==0 : continue
        board[move-1][idx] = 0
        basket.append(num)
        if len(basket) > 1:
            if basket[-2] == basket[-1]:
                del basket[-2:]
                count += 2
        break
    return board, basket, count

def solution(board, moves):
    basket = []
    count = 0
    board = np.array(board).T.tolist()
    for move in moves:
        board, basket, count = pickup(board, basket, move, count)
    return count
