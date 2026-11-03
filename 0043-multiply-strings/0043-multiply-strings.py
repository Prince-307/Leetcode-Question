class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])

                product = digit1 * digit2
                total = product + result[i + j + 1]

                result[i + j + 1] = total % 10
                result[i + j] += total // 10

        # Remove leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')

        return result_str if result_str else "0"
        
        
