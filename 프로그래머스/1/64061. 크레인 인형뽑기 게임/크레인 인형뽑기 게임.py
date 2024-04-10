"""
-------------------------------------------
[접근]
격자판 -> 2차원 배열, 바구니 -> 스택으로 생각
moves를 다 돌면 게임이 끝남 -> moves를 순회하면서 격자판에 접근하기

[카테고리]
스택
-------------------------------------------
"""

def take_doll(brd, col):
    for i in range(len(brd)):
        print(i, col, brd[i][col])
        if brd[i][col]:
            doll = brd[i][col]
            brd[i][col] = 0
            # print(brd[i][col]) # 4 3 1 1 3 2 4
            if stack and stack[-1] == doll:
                stack.pop()
                return 2
            else:
                stack.append(doll)
                return 0
            
    return 0
            
            

def solution(board, moves):
    global stack

    stack = [] # 바구니 생성
    count = 0 # count
    
    for i in range(len(moves)):
        # print(moves[i])
        count += take_doll(board, moves[i] - 1)    
        
    return count