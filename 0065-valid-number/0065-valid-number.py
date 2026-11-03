class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if '0' <= ch <= '9':
                seen_digit = True

            elif ch == '.':
                # Decimal point cannot appear twice
                # or after the exponent
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            elif ch in 'eE':
                # Exponent requires a number before it
                # and cannot appear twice
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                seen_digit = False

            elif ch in '+-':
                # Sign is allowed only at the beginning
                # or immediately after e/E
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            else:
                return False

        return seen_digit
            