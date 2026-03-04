class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = []
        col = []

        for i in range(len(mat)):
            one_count =0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    one_count += 1
            row.append(one_count)

        for j in range(len(mat[0])):
            one_count = 0
            for i in range(len(mat)):
                if mat[i][j]==1:
                    one_count +=1
            col.append(one_count)
        
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    if row[i] == 1 and col[j] == 1:
                        count += 1
        return count






        