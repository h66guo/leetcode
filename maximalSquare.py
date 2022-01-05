class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        HEIGHT, WIDTH = len(matrix), len(matrix[0])
        dp = [0] * (WIDTH + 1)
        max_square = 0
        top_left = 0
        
        for row in range(1, HEIGHT + 1):
            for col in range(1, WIDTH + 1):
                print(dp)
                above = dp[col]
                left = dp[col - 1]
                if matrix[row - 1][col - 1] == '1':
                    dp[col] = min(above, top_left, left) + 1
                    max_square = max(max_square, dp[col])
                else:
                    dp[col] = 0
                top_left = above

        return max_square * max_square
