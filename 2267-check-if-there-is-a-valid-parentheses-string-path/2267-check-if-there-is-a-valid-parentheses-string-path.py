class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First must be '('
        if grid[0][0] == ')':
            return False

        # Last must be ')'
        if grid[m - 1][n - 1] == '(':
            return False

        memo = {}

        def dfs(i, j, balance):

            # Add current character
            if grid[i][j] == '(':
                balance += 1
            else:
                balance -= 1

            # Invalid balance
            if balance < 0:
                return False

            # Too much balance left to close
            remaining = (m - 1 - i) + (n - 1 - j)

            if balance > remaining:
                return False

            # Destination
            if i == m - 1 and j == n - 1:
                return balance == 0

            # Memoization
            state = (i, j, balance)

            if state in memo:
                return memo[state]

            # Move down
            if i + 1 < m:
                if dfs(i + 1, j, balance):
                    memo[state] = True
                    return True

            # Move right
            if j + 1 < n:
                if dfs(i, j + 1, balance):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0, 0)
        