def gaussianElimination(A, b):
  
    # 첨가 행렬 생성 (Deep Copy)
    # RREF 계산 시 원본 A, b는 유지되어야 하므로 복사본을 사용
    M = [row[:] + [bx] for row, bx in zip(A, b)]
    rows, cols = 3, 4
    pivot_row = 0

    # 1. 전진 소거 (Forward Elimination) - REF 만들기
    for j in range(3): # 열 순회 (변수 x1, x2, x3)
        if pivot_row >= rows: break

        # 피벗팅 (Pivoting): 현재 열에서 가장 큰 절댓값 원소를 피벗으로 선택
        max_val, max_row = 0, -1
        for i in range(pivot_row, rows):
            if abs(M[i][j]) > max_val:
                max_val = abs(M[i][j])
                max_row = i
        
        # 피벗이 0에 가까우면 다음 열로 이동
        if max_val < 1e-9: continue 

        # 행 교환
        M[pivot_row], M[max_row] = M[max_row], M[pivot_row]

        # 소거 (Elimination)
        pivot = M[pivot_row][j]
        for i in range(pivot_row + 1, rows):
            factor = M[i][j] / pivot
            for k in range(j, cols):
                M[i][k] -= factor * M[pivot_row][k]
                if abs(M[i][k]) < 1e-9: M[i][k] = 0.0 # 부동 소수점 오차 처리
        
        pivot_row += 1

    # 2. 후진 소거 (Backward Elimination) - RREF 만들기
    # 피벗을 1로 만들고 피벗 위의 원소들을 0으로 소거
    
    pivots = []
    for i in range(rows):
        for j in range(3):
            if abs(M[i][j]) > 1e-9:
                pivots.append((i, j))
                
                # 피벗을 1로 만들기
                pivot_val = M[i][j]
                for k in range(j, cols):
                    M[i][k] /= pivot_val
                
                break
    
    # 후진하며 피벗 위의 원소 소거
    for i, j in reversed(pivots):
        for row_idx in range(i):
            factor = M[row_idx][j]
            for k in range(j, cols):
                M[row_idx][k] -= factor * M[i][k]
                if abs(M[row_idx][k]) < 1e-9: M[row_idx][k] = 0.0

    return M