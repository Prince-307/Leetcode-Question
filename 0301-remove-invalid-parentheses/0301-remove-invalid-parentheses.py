class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()

        # Count minimum removals needed
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        def backtrack(index, path, open_count, left_rem, right_rem):
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    result.add(path)
                return

            ch = s[index]

            # Option 1: Remove the parenthesis
            if ch == '(' and left_rem > 0:
                backtrack(index + 1, path, open_count,
                          left_rem - 1, right_rem)

            if ch == ')' and right_rem > 0:
                backtrack(index + 1, path, open_count,
                          left_rem, right_rem - 1)

            # Option 2: Keep the character
            if ch != '(' and ch != ')':
                backtrack(index + 1, path + ch, open_count,
                          left_rem, right_rem)
            elif ch == '(':
                backtrack(index + 1, path + ch, open_count + 1,
                          left_rem, right_rem)
            elif open_count > 0:
                backtrack(index + 1, path + ch, open_count - 1,
                          left_rem, right_rem)

        backtrack(0, "", 0, left, right)
        return list(result)