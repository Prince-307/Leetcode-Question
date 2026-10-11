class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(st):
            count = 0
            for ch in st:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        level = {s}

        while level:
            valid = [st for st in level if is_valid(st)]
            if valid:
                return valid

            next_level = set()
            for st in level:
                for i, ch in enumerate(st):
                    if ch not in '()':
                        continue
                    next_level.add(st[:i] + st[i + 1:])

            level = next_level

        return [""]