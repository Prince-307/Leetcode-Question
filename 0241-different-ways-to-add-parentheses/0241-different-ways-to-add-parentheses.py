class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        if expression.isdigit():
            return [int(expression)]

        results = []

        # Try every operator as a splitting point
        for i in range(len(expression)):

            if expression[i] in "+-*":

                # Divide expression into left and right parts
                left = expression[:i]
                right = expression[i + 1:]

                # Recursively calculate both sides
                left_results = self.diffWaysToCompute(left)
                right_results = self.diffWaysToCompute(right)

                # Combine all possible results
                for a in left_results:
                    for b in right_results:

                        if expression[i] == "+":
                            results.append(a + b)

                        elif expression[i] == "-":
                            results.append(a - b)

                        elif expression[i] == "*":
                            results.append(a * b)

        return results
            