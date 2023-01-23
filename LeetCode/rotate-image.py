class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        lenn = len(matrix)
        #reverse matrix on diagonal
        for i in range(lenn):
            for j in range(i+1,lenn):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        #reverse matrix on column
        for i in range(lenn):
            for j in range(lenn//2):
                matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]

        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
S1 = Solution()
print(S1.rotate(matrix))
        