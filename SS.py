class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        return self.solver(board)
        
        
    def updatePos(self, b, p, c):
        for x in range(9):
            s_r = set(b[x])
            if "." not in s_r:
                continue
            s_r.remove(".")
            for y in range(9):
                if (x, y) not in c:
                    for e in s_r:
                        if e in p[(x, y)]:
                            p[(x, y)].remove(e)
        for y in range(9):
            s_c = set([e[y] for e in b])
            if "." not in s_c:
                continue
            s_c.remove(".")
            for x in range(9):
                if (x, y) not in c:
                    for e in s_c:
                        if e in p[(x, y)]:
                            p[(x, y)].remove(e)
        init_c = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        init_cell = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        for ct in init_c:
            l = []
            for ic in init_cell:
                l.append(b[ct[0]+ic[0]][ct[1]+ic[1]])
            s_s = set(l)
            if "." not in s_s:
                continue
            s_s.remove(".")
            for ic in init_cell:
                if (ct[0]+ic[0], ct[1]+ic[1]) not in c:
                    for e in s_s:
                        if e in p[(ct[0]+ic[0], ct[1]+ic[1])]:
                            p[(ct[0]+ic[0], ct[1]+ic[1])].remove(e)
        new_confirmed = dict()
        for p_e in p:
            if len(p[p_e])==0:
                return False
            if len(p[p_e])==1 and p_e not in c:
                new_confirmed[p_e] = p[p_e][0]
        for n_c in new_confirmed:
            c.add(n_c)
        return new_confirmed

    def updateBoa(self, b, nc):
        for n in nc:
            b[n[0]][n[1]] = nc[n]

    def solver(self, board):
        posibilities = dict()
        confirmed = set()
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    posibilities[(i, j)] = ["1","2","3","4","5","6","7","8","9"]
                else:
                    posibilities[(i, j)] = [board[i][j]]
                    confirmed.add((i, j))
        new_confirmed = self.updatePos(board, posibilities, confirmed)
        if new_confirmed == False:
            return False
        while new_confirmed != {}:
            self.updateBoa(board, new_confirmed)
            new_confirmed = self.updatePos(board, posibilities, confirmed)
            if new_confirmed == False:
                return False
        if len(confirmed)==81:
            if self.isValidSudoku(board):
                return board
            else :
                return False
        else:
            for guess_p in posibilities:
                if guess_p not in confirmed:
                    break
            guess = posibilities[guess_p]
            for g in guess:
                new_board = [[],[],[],[],[],[],[],[],[]]
                for m in range(9):
                    for n in range(9):
                        new_board[m].append(board[m][n])
                new_board[guess_p[0]][guess_p[1]] = g
                r = self.solver(new_board)
                if r:
                    return r
            return False
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for l in board:
            if not self.nineNumsValid(l):
                return False
        for i in range(9):
            l = [e[i] for e in board]
            if not self.nineNumsValid(l):
                return False
        init_c = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        init_cell = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        for c in init_c:
            l = []
            for ic in init_cell:
                l.append(board[c[0]+ic[0]][c[1]+ic[1]])
            if not self.nineNumsValid(l):
                return False
        return True
        
    def nineNumsValid(self, l):
        s = set()
        for i in range(9):
            if l[i] == '.':
                continue
            if l[i] in s:
                return False
            else:
                if '0'<l[i]<='9':
                    s.add(l[i])
                else:
                    return False
        return True
        