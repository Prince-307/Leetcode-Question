class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        n = len(s)

        if n < word_len * word_count:
            return []

        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        for offset in range(word_len):
            left = offset
            seen = {}
            count = 0

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in word_freq:
                    seen = {}
                    count = 0
                    left = right + word_len
                    continue

                seen[word] = seen.get(word, 0) + 1
                count += 1

                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                if count == word_count:
                    result.append(left)

        return result