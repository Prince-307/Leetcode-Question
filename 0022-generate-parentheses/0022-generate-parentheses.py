class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def generate(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if open < n:
                generate(s + "(", open + 1, close)

            if close < open:
                generate(s + ")", open, close + 1)

        generate("", 0, 0)

        return ans
        