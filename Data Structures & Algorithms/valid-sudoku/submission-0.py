class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. Vérification des lignes
        for i in range(len(board)):
            verif_row = []  # On vide la liste pour chaque nouvelle ligne
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in verif_row:
                    verif_row.append(board[i][j])
                else: 
                    return False
                    
        # 2. Vérification des colonnes
        for j in range(len(board)):
            verif_colum = []  # On vide la liste pour chaque nouvelle colonne
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in verif_colum:
                    verif_colum.append(board[i][j])
                else: 
                    return False
        
        # 3. Vérification des carrés 3x3 (ton code, nickel !)
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                verif_box = []
                for i in range(3):
                    for j in range(3):
                        row = r + i
                        col = c + j
                        val = board[row][col]
                        
                        if val == ".":
                            continue
                        if val in verif_box:
                            return False
                        verif_box.append(val)
                        
        return True