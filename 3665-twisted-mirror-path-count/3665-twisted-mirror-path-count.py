class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][0]: ways entering (i, j) while moving right
        # dp[i][j][1]: ways entering (i, j) while moving down
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        # Start at (0, 0)
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                right = dp[i][j][0]
                down = dp[i][j][1]

                if grid[i][j] == 0:
                    # Empty cell: move right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + right + down
                        ) % MOD

                    # Empty cell: move down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + right + down
                        ) % MOD

                else:
                    # Mirror: entering while moving right -> down
                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + right
                        ) % MOD

                    # Mirror: entering while moving down -> right
                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + down
                        ) % MOD

        return sum(dp[m - 1][n - 1]) % MOD